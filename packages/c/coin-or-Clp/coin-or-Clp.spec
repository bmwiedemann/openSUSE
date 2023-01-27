#
# spec file for package coin-or-Clp
#
# Copyright (c) 2022 SUSE LLC
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

Name:           coin-or-Clp
Version:        1.17.7
Release:        0
Summary:        COIN-OR Linear Programming Solver
License:        EPL-2.0
URL:            https://www.coin-or.org/
Source:         https://github.com/coin-or/Clp/archive/refs/tags/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)

%description
Clp (Coin-or linear programming) is an open-source linear programming
solver. It is primarily meant to be used as a callable library, but a
basic, stand-alone executable version is also available.

%package -n libClp%{soversion}
Summary:        Shared Libraries for coin-or-Clp
Group:          System/Libraries

%description -n libClp%{soversion}
Clp (Coin-or linear programming) is an open-source linear programming
solver. It is primarily meant to be used as a callable library, but a
basic, stand-alone executable version is also available.

%package -n libOsiClp%{soversion}
Summary:        COIN-OR Open Solver Interface for CLP
Group:          System/Libraries

%description -n libOsiClp%{soversion}
Clp (Coin-or linear programming) is an open-source linear programming
solver. It is primarily meant to be used as a callable library, but a
basic, stand-alone executable version is also available.

%package devel
Summary:        Development headers for coin-or-Clp
Requires:       libClp%{soversion} = %{version}
Requires:       libOsiClp%{soversion} = %{version}

%description devel
Clp (Coin-or linear programming) is an open-source linear programming solver.

This package contains the development headers for coin-or-Clp.

%prep
%setup -n Clp-releases-%{version}

%build
%configure
%make_build

%install
%make_install DocInstallDir=%{_docdir}/%{name}

find %{buildroot}%{_libdir} -iname \*.la -print -delete
rm %{buildroot}/%{_datadir}/coin/doc/Clp/clp_addlibs.txt

# Obsolete/duplicate
rm %{buildroot}/%{_docdir}/%{name}/{AUTHORS,LICENSE}

%post -n libClp%{soversion} -p /sbin/ldconfig
%postun -n libClp%{soversion} -p /sbin/ldconfig

%post -n libOsiClp%{soversion} -p /sbin/ldconfig
%postun -n libOsiClp%{soversion} -p /sbin/ldconfig

%files
%{_bindir}/clp

%files -n libClp%{soversion}
%license LICENSE
%{_libdir}/libClp.so.%{soversion}*
%{_libdir}/libClpSolver.so.%{soversion}*

%files -n libOsiClp%{soversion}
%license LICENSE
%{_libdir}/libOsiClp.so.%{soversion}*

%files devel
%{_libdir}/libClp.so
%{_libdir}/libClpSolver.so
%{_libdir}/libOsiClp.so
%{_includedir}/coin/
%{_libdir}/pkgconfig/clp.pc
%{_libdir}/pkgconfig/osi-clp.pc

%changelog

