#
# spec file for package coin-or-Cgl
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

%define soversion 1

Name:           coin-or-Cgl
Version:        0.60.6
Release:        0
Summary:        COIN-OR Cut Generator Library
License:        EPL-2.0
URL:            https://www.coin-or.org/
Source:         https://github.com/coin-or/Cgl/archive/refs/tags/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(osi-clp)

%description
The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators
that can be used with other COIN-OR packages that make use of cuts, such as,
among others, the linear solver Clp or the mixed integer linear programming
solvers Cbc or BCP

%package -n libCgl%{soversion}
Summary:        Shared Libraries for coin-or-Cgl
Group:          System/Libraries

%description -n libCgl%{soversion}
The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators
that can be used with other COIN-OR packages that make use of cuts, such as,
among others, the linear solver Clp or the mixed integer linear programming
solvers Cbc or BCP

%package devel
Summary:        Development headers for coin-or-Cgl
Requires:       libCgl%{soversion} = %{version}
Requires:       pkgconfig(coinutils)
Requires:       pkgconfig(osi)
Requires:       pkgconfig(osi-clp)

%description devel
The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators.

This package contains the development headers for coin-or-Cgl.

%prep
%setup -n Cgl-releases-%{version}

%build
%configure
%make_build

%install
%make_install DocInstallDir=%{_docdir}/%{name}

find %{buildroot}%{_libdir} -iname \*.la -print -delete
rm %{buildroot}/%{_datadir}/coin/doc/Cgl/cgl_addlibs.txt

# Obsolete/duplicate
rm %{buildroot}/%{_docdir}/%{name}/{AUTHORS,LICENSE}

%post -n libCgl%{soversion} -p /sbin/ldconfig
%postun -n libCgl%{soversion} -p /sbin/ldconfig

%files -n libCgl%{soversion}
%license LICENSE
%{_libdir}/libCgl.so.%{soversion}*

%files devel
%{_libdir}/libCgl.so
%{_includedir}/coin/
%{_libdir}/pkgconfig/cgl.pc

%changelog

