#
# spec file for package qore
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define module_dir %{_libdir}/qore-modules
Name:           qore
Version:        0.8.13
Release:        0
Summary:        Multithreaded Programming Language
License:        LGPL-2.1-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
Url:            http://qore.org
Source:         https://github.com/qorelanguage/qore/releases/download/release-%{version}/qore-%{version}.tar.bz2
Source99:       qore-module.prov
Patch:          qore-libtool-2.4.6.patch
# PATCH-FIX-OPENSUSE bmwiedemann boo#1084909
Patch1:         reproducible.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.31
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
Requires:       %{_bindir}/env
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

%package -n libqore5
Summary:        The libraries for the qore runtime and qore clients
License:        LGPL-2.0-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
Provides:       qore-module(abi)%{?_isa} = 0.18
Provides:       qore-module(abi)%{?_isa} = 0.19
Provides:       qore-module(abi)%{?_isa} = 0.20
# provided for backwards-compatibility with unversioned capabilities and will be removed when the ABI drops backwards-compatibility
%(cat %{SOURCE99})

%description -n libqore5
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

This package provides the qore library required for all clients using qore
functionality.

%files -n libqore5
%defattr(-,root,root,-)
%{_libdir}/libqore.so.5.14.0
%{_libdir}/libqore.so.5
%doc COPYING.LGPL COPYING.GPL COPYING.MIT README-LICENSE

%post -n libqore5 -p /sbin/ldconfig
%postun -n libqore5 -p /sbin/ldconfig

%package doc
Summary:        API documentation, programming language reference, and Qore example programs
License:        LGPL-2.0-or-later OR GPL-2.0-or-later OR MIT
Group:          Documentation/HTML

%description doc
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

This package provides the HTML documentation for the Qore programming language
and also for user modules delivered with Qore and also example programs.

%files doc
%defattr(-,root,root,-)
%doc docs/lang docs/modules/* examples/ README.md README-MODULES RELEASE-NOTES AUTHORS ABOUT

%package devel
Summary:        The header files needed to compile programs using the qore library
License:        LGPL-2.0-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Languages/C and C++
Requires:       libqore5 = %{version}-%{release}

%description devel
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

This package provides header files needed to compile client programs using the
Qore library.

%files devel
%defattr(-,root,root,-)
%{_bindir}/qpp
%{_bindir}/qdx
%{_libdir}/libqore.so
%{_libdir}/pkgconfig/qore.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/Qore
%{_includedir}/*
%{_datadir}/qore

%package devel-doc
Summary:        C++ API documentation for the qore library
License:        LGPL-2.0-or-later OR GPL-2.0-or-later OR MIT
Group:          Documentation/HTML
Requires:       libqore5 = %{version}-%{release}

%description devel-doc
Qore is a scripting language supporting threading and embedded logic, designed
for applying a flexible scripting-based approach to enterprise interface
development but is also useful as a general purpose language.

%files devel-doc
%defattr(-,root,root,-)
%doc docs/library/html/*

%package misc-tools
Summary:        Miscellaneous user tools writen in Qore Programming Language
License:        LGPL-2.0-or-later OR GPL-2.0-or-later OR MIT
Group:          Development/Tools/Other
Requires:       qore = %{version}-%{release}

%description misc-tools
This package contains tool for working with:
 - REST APIs
 - SQL Databases

%files misc-tools
%defattr(-,root,root,-)
%{_bindir}/qget
%{_bindir}/rest
%{_bindir}/sfrest
%{_bindir}/sqlutil
%{_bindir}/schema-reverse

%prep
%setup -q
%patch -p1
%patch1 -p1
# silence the executable warning for examples
find examples -type f|xargs chmod 644

%build
aclocal
autoreconf -fi
%if "%_lib" == "lib64"
c64=--enable-64bit
%endif
%configure --disable-debug --disable-static $c64
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}/%{module_dir}/%{version}
mkdir -p %{buildroot}%{_prefix}/man/man1
make install prefix=%{_prefix} DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/libqore.la
%fdupes -s docs

# Check if we have all the provides for libqore - to ensure we provide all the qore-module-api-* the code supports
./qore --module-apis | awk -F',[[:blank:]]' '{i = 1; while (i < NF) { print "Provides: qore-module-api-"$i; i++  } }' > /tmp/qore-modules.prov
diff -ur %{SOURCE99} /tmp/qore-modules.prov

%files
%defattr(-,root,root,-)
%{_bindir}/qore
%{_bindir}/qdbg*
%{module_dir}
%dir %{_datadir}/qore-modules
%{_datadir}/qore-modules/0.8.13
%{_mandir}/man1/qore.1.*

%changelog
