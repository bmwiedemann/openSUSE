#
# spec file for package qore
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014 David Nichols <david@qore.org>
# Copyright (c) 2014 Petr Vanek <petr@yarpen.cz>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?_datarootdir: %global mydatarootdir %_datarootdir}
%{!?_datarootdir: %global mydatarootdir /usr/share}

%if 0%{?sles_version}
%global dist .sles%{?sles_version}
%else
%if 0%{?suse_version}
# get *suse release major version
%global os_maj %(echo %suse_version|rev|cut -b3-|rev)
# get *suse release minor version without trailing zeros
%global os_min %(echo %suse_version|rev|cut -b-2|rev|sed s/0*$//)
%if %suse_version > 1010
%global dist .opensuse%{os_maj}_%{os_min}
%else
%global dist .suse%{os_maj}_%{os_min}
%endif
%endif
%endif

%define so_ver 12
%define module_dir %{_libdir}/qore-modules
%global user_module_dir %{mydatarootdir}/qore-modules/
%global libname libqore12
Name:           qore
Version:        1.18.1
Release:        1%{dist}
Summary:        Multithreaded Programming Language
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Other
URL:            https://qore.org
Source0:        https://github.com/qorelanguage/qore/releases/download/release-%{version}/%{name}-%{version}.tar.bz2#/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE bmwiedemann boo#1084909
Patch0:         reproducible.patch
BuildRequires:  bison
BuildRequires:  bzip2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.31
BuildRequires:  gcc-c++ >= 4.8.1
BuildRequires:  gmp-devel
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
Requires:       %{_bindir}/env
Requires(post): shared-mime-info
Requires(postun):shared-mime-info
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

%if 0%{?suse_version}
%endif

%package -n %{libname}
Summary:        Libraries for the qore runtime and qore clients
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
Provides:       qore-module(abi)%{?_isa} = 1.3
Provides:       qore-module(abi)%{?_isa} = 1.4
%if "%{libname}" == "libqore"
Provides:       libqore12 = %{version}
Obsoletes:      libqore12 < %{version}
%endif

%description -n %{libname}
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

This package provides the qore library required for all clients using qore
functionality.

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libqore.so.12.4.0
%{_libdir}/libqore.so.12
%doc README.md README-MODULES RELEASE-NOTES AUTHORS ABOUT
%license COPYING.LGPL COPYING.GPL COPYING.MIT README-LICENSE

%post -n %{libname}
ldconfig %{_libdir}

%postun -n %{libname}
ldconfig %{_libdir}

%package stdlib
Summary:        Standard library modules
Group:          System Environment/Libraries
Requires:       %{libname} = %{version}-%{release}

%description stdlib
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

This package provides the Qore language standard library user and binary
modules.

%files stdlib
%defattr(-,root,root,-)
%{user_module_dir}
%{module_dir}
%license COPYING.MIT README-LICENSE

%package doc
Summary:        API documentation, programming language reference, and Qore example programs
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

This package provides the HTML documentation for the Qore programming language
and also for user modules delivered with Qore and also example programs.

%files doc
%defattr(-,root,root,-)
%doc docs/lang docs/modules/* examples/
%license COPYING.LGPL COPYING.GPL COPYING.MIT README-LICENSE

%package devel
Summary:        Header files needed to compile programs using the qore library
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description devel
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

This package provides header files needed to compile client programs using the
Qore library.

%files devel
%defattr(-,root,root,-)
/usr/bin/qpp
/usr/bin/qdx
/usr/bin/qjar
%{_libdir}/libqore.so
%{_libdir}/pkgconfig/qore.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/Qore
%{_prefix}/include/*
%{mydatarootdir}/qore
%{mydatarootdir}/qore/*

%package devel-doc
Summary:        C++ API documentation for the qore library
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Documentation
BuildArch:      noarch

%description devel-doc
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

This package provides HTML documentation for the C++ API for the Qore library.

%files devel-doc
%defattr(-,root,root,-)
%doc docs/library/html/*

%package misc-tools
Summary:        Miscellaneous user tools writen in Qore Programming Language
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Tools/Other
Requires:       qore = %{version}-%{release}
BuildArch:      noarch

%description misc-tools
This package contains tool for working with:
 - REST APIs
 - SQL Databases

%files misc-tools
%defattr(-,root,root,-)
%{_bindir}/qdp
%{_bindir}/qget
%{_bindir}/rest
%{_bindir}/sfrest
%{_bindir}/saprest
%{_bindir}/sqlutil
%{_bindir}/schema-reverse

%prep
%setup -q
%patch0 -p1
# silence the executable warning for examples
find examples -type f -exec chmod -x {} \;

%build
export CXXFLAGS="%{?optflags}"
%configure --disable-debug --disable-dependency-tracking
%{__make} %{?_smp_mflags}
sed -i '1s,#!/usr/bin/env qore,#!/usr/bin/qore,' bin/* doxygen/qdx doxygen/qjar

%install
make install prefix=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/libqore.la
mkdir -p $RPM_BUILD_ROOT/%{module_dir}
%if 0%{?suse_version}
%fdupes -s docs/library/html
%endif

%check
export QORE_MODULE_DIR=qlib
./qore examples/test/qore/threads/background.qtest
./qore examples/test/qore/threads/deadlock.qtest
./qore examples/test/qore/threads/max-threads-count.qtest
./qore examples/test/qore/threads/set_thread_init.qtest
./qore examples/test/qore/threads/thread-object.qtest
./qore examples/test/qore/threads/thread-resources.qtest
./qore examples/test/qore/threads/tld.qtest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/qore
/usr/bin/qdbg
/usr/bin/qdbg-server
/usr/bin/qdbg-remote
/usr/bin/qdbg-vsc-adapter*
%if 0%{?_mandir:1}
%{_mandir}/man1/qore.1.*
%endif

%changelog
