#
# spec file for package coin-or-Cbc
#
# Copyright (c) 2023 SUSE LLC
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

%define soversion 3

Name:           coin-or-Cbc
Version:        2.10.8
Release:        0
Summary:        COIN-OR Branch-and-Cut solver
License:        EPL-2.0
URL:            https://www.coin-or.org/
Source:         https://github.com/coin-or/Cbc/archive/refs/tags/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cgl)
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)

%description
Cbc (Coin-or branch and cut) is an open-source mixed integer linear
programming solver written in C++. It can be used as a callable
library or using a stand-alone executable. It can be used in a wide
variety of ways through various modeling systems, packages, etc.

%package -n libCbc%{soversion}
Summary:        Shared Libraries for coin-or-Cbc
Group:          System/Libraries

%description -n libCbc%{soversion}
Cbc (Coin-or branch and cut) is an open-source mixed integer linear
programming solver written in C++. It can be used as a callable
library or using a stand-alone executable. It can be used in a wide
variety of ways through various modeling systems, packages, etc.

%package -n libOsiCbc%{soversion}
Summary:        COIN-OR Open Solver Interface for Cbc
Group:          System/Libraries

%description -n libOsiCbc%{soversion}
Cbc (Coin-or branch and cut) is an open-source mixed integer linear
programming solver written in C++. It can be used as a callable
library or using a stand-alone executable. It can be used in a wide
variety of ways through various modeling systems, packages, etc.

%package devel
Summary:        Development headers for coin-or-Cbc
Requires:       libCbc%{soversion} = %{version}
Requires:       libOsiCbc%{soversion} = %{version}
Requires:       pkgconfig(coinutils)
Requires:       pkgconfig(osi)

%description devel
Cbc (Coin-or branch and cut) is an open-source mixed integer linear
programming solver written in C++.

This package contains the development headers for coin-or-Cbc.

%prep
%setup -n Cbc-releases-%{version}

%build
%configure
%make_build

%install
%make_install DocInstallDir=%{_docdir}/%{name}
find %{buildroot}%{_libdir} -iname \*.la -print -delete
rm %{buildroot}/%{_datadir}/coin/doc/Cbc/cbc_addlibs.txt

# Obsolete/duplicate
rm %{buildroot}/%{_docdir}/%{name}/{AUTHORS,LICENSE}

%post -n libCbc%{soversion} -p /sbin/ldconfig
%postun -n libCbc%{soversion} -p /sbin/ldconfig

%post -n libOsiCbc%{soversion} -p /sbin/ldconfig
%postun -n libOsiCbc%{soversion} -p /sbin/ldconfig

%files
%{_bindir}/cbc

%files -n libCbc%{soversion}
%license LICENSE
%{_libdir}/libCbc.so.%{soversion}*
%{_libdir}/libCbcSolver.so.%{soversion}*

%files -n libOsiCbc%{soversion}
%license LICENSE
%{_libdir}/libOsiCbc.so.%{soversion}*

%files devel
%{_libdir}/libCbc.so
%{_libdir}/libCbcSolver.so
%{_libdir}/libOsiCbc.so
%{_includedir}/coin/
%{_libdir}/pkgconfig/cbc.pc
%{_libdir}/pkgconfig/osi-cbc.pc

%changelog

