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

%define so_ver 12
%define module_dir %{_libdir}/qore-modules
%global user_module_dir %{mydatarootdir}/qore-modules/
Name:           qore
Version:        1.13.0
Release:        0
Summary:        Multithreaded Programming Language
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Other
URL:            https://qore.org
Source0:        https://github.com/qorelanguage/qore/releases/download/release-%{version}/%{name}-%{version}.tar.bz2#/%{name}-release-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE bmwiedemann boo#1084909
Patch0:         reproducible.patch
BuildRequires:  automake
BuildRequires:  bison >= 1.8.5
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.31
BuildRequires:  gcc-c++ >= 4.8.1
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  libbz2-devel
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

%package -n libqore%{so_ver}
Summary:        Libraries for the qore runtime and qore clients
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
Provides:       qore-module(abi)%{?_isa} = 1.3

%description -n libqore%{so_ver}
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

This package provides the qore library required for all clients using qore
functionality.

%files -n libqore12
%defattr(-,root,root,-)
%{_libdir}/libqore.so.12.2.0
%{_libdir}/libqore.so.12
%doc README.md README-MODULES RELEASE-NOTES AUTHORS ABOUT
%license COPYING.LGPL COPYING.GPL COPYING.MIT README-LICENSE

%post -n libqore12 -p /sbin/ldconfig
%postun -n libqore12 -p /sbin/ldconfig

%package stdlib
Summary:        Standard library modules
Group:          System Environment/Libraries
Requires:       libqore12 = %{version}-%{release}

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
%doc docs/lang docs/modules/* examples/ COPYING.LGPL COPYING.GPL COPYING.MIT README-LICENSE

%package devel
Summary:        Header files needed to compile programs using the qore library
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/C and C++
Requires:       libqore%{so_ver} = %{version}-%{release}

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
Group:          Documentation/HTML
Requires:       libqore12 = %{version}-%{release}
BuildArch:      noarch

%description devel-doc
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

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
%setup -q -n %{name}-%{version}
%patch0 -p1
# silence the executable warning for examples
find examples -type f -exec chmod -x {} \;

%build
aclocal
autoreconf -fi
%if "%_lib" == "lib64"
c64=--enable-64bit
%endif
%configure --disable-debug --disable-static $c64
make %{?_smp_mflags}
sed -i '1s,#!/usr/bin/env qore,#!/usr/bin/qore,' bin/* doxygen/qdx doxygen/qjar

%install
make install prefix=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/libqore.la
mkdir -p $RPM_BUILD_ROOT/%{module_dir}
%fdupes -s docs

%check
export QORE_MODULE_DIR=qlib
./qore examples/test/qore/threads/background.qtest
./qore examples/test/qore/threads/deadlock.qtest
./qore examples/test/qore/threads/max-threads-count.qtest
./qore examples/test/qore/threads/set_thread_init.qtest
./qore examples/test/qore/threads/thread-object.qtest
./qore examples/test/qore/threads/thread-resources.qtest
./qore examples/test/qore/threads/tld.qtest

%files
%defattr(-,root,root,-)
%{_bindir}/qore
%{_bindir}/qdbg
%{_bindir}/qdbg-server
%{_bindir}/qdbg-remote
%{_bindir}/qdbg-vsc-adapter
%{_mandir}/man1/qore.1.*

%changelog
