#
# spec file for package qore
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.9.15
Release:        0
Summary:        Multithreaded Programming Language
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Other
URL:            https://qore.org
Source0:        https://github.com/qorelanguage/qore/archive/refs/tags/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
# All supported ABIs, remember to update after each update (see %%install section)
Source99:       qore-module.prov
# PATCH-FIX-OPENSUSE bmwiedemann boo#1084909
Patch0:         reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.31
BuildRequires:  gcc-c++ >= 4.8.1
BuildRequires:  gmp-devel
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
Requires:       %{_bindir}/env

%description
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

%package -n libqore6
Summary:        Libraries for the qore runtime and qore clients
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
%(awk 'NF { gsub(/ /,""); print "Provides: qore-module(abi)%{?_isa} = "$abi  }' %{SOURCE99})

%description -n libqore6
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

This package provides the qore library required for all clients using qore
functionality.

%files -n libqore6
%license COPYING.LGPL COPYING.GPL COPYING.MIT README-LICENSE
%{_libdir}/libqore.so.6*

%post -n libqore6 -p /sbin/ldconfig
%postun -n libqore6 -p /sbin/ldconfig

%package devel
Summary:        Header files needed to compile programs using the qore library
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/C and C++
Requires:       libqore6 = %{version}-%{release}

%description devel
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

This package provides header files needed to compile client programs using the
Qore library.

%files devel
%{_bindir}/qpp
%{_bindir}/qdx
%{_libdir}/libqore.so
%{_libdir}/pkgconfig/qore.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/Qore
%{_includedir}/*
%{_datadir}/qore

%package misc-tools
Summary:        Miscellaneous user tools writen in Qore Programming Language
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Tools/Other
Requires:       qore = %{version}-%{release}

%description misc-tools
This package contains tool for working with:
 - REST APIs
 - SQL Databases

%files misc-tools
%{_bindir}/qdp
%{_bindir}/qget
%{_bindir}/rest
%{_bindir}/sfrest
%{_bindir}/saprest
%{_bindir}/sqlutil
%{_bindir}/schema-reverse

%prep
%autosetup -p1 -n %{name}-release-%{version}
# silence the executable warning for examples
find examples -type f|xargs chmod 644

%build
autoreconf -fi
%configure --disable-debug --disable-dependency-tracking
%make_build

%install
%make_install
rm %{buildroot}/%{_libdir}/libqore.la

# Check if we have all the provides for libqore - to ensure we provide all the qore-module ABI's the code supports
./qore --module-apis | awk -F',[[:blank:]]' '{i = 1; while (i < NF) { print $i; i++  } }' > /tmp/qore-modules.prov
diff -ur %{SOURCE99} /tmp/qore-modules.prov

%check
make test

%files
%{_bindir}/qore
%{_bindir}/qdbg*
%{module_dir}
%dir %{_datadir}/qore-modules
%{_datadir}/qore-modules/%{version}
%{_mandir}/man1/qore.1%{?ext_man}

%changelog
