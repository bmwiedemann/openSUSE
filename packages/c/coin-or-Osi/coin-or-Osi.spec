#
# spec file for package coin-or-Osi
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

Name:           coin-or-Osi
Version:        0.108.7
Release:        0
Summary:        COIN-OR Open Solver Interface
License:        EPL-2.0
URL:            https://www.coin-or.org/
Source:         https://github.com/coin-or/Osi/archive/refs/tags/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(coinutils)

%description
Osi (Open Solver Interface) provides an abstract base class to a generic
linear programming (LP) solver, along with derived classes for specific
solvers.

%package -n libOsi%{soversion}
Summary:        Shared Libraries for coin-or-Osi
Group:          System/Libraries

%description -n libOsi%{soversion}
Osi (Open Solver Interface) provides an abstract base class to a generic
linear programming (LP) solver, along with derived classes for specific
solvers.

%package devel
Summary:        Development headers for coin-or-Osi
Requires:       libOsi%{soversion} = %{version}

%description devel
Osi (Open Solver Interface) provides an abstract base class to a generic
linear programming (LP) solver.

This package contains the development headers for coin-or-Osi.

%prep
%setup -n Osi-releases-%{version}

%build
%configure
%make_build

%install
%make_install DocInstallDir=%{_docdir}/%{name}

find %{buildroot}%{_libdir} -iname \*.la -print -delete
rm %{buildroot}/%{_datadir}/coin/doc/Osi/osi_addlibs.txt

find %{buildroot}%{_libdir} -iname libOsiCommonTests.so\* -print -delete
rm %{buildroot}/%{_libdir}/pkgconfig/osi-unittests.pc

# Obsolete/duplicate
rm %{buildroot}/%{_docdir}/%{name}/{AUTHORS,LICENSE}

%post -n libOsi%{soversion} -p /sbin/ldconfig
%postun -n libOsi%{soversion} -p /sbin/ldconfig

%files -n libOsi%{soversion}
%license LICENSE
%{_libdir}/libOsi.so.%{soversion}*

%files devel
%{_libdir}/libOsi.so
%{_includedir}/coin/
%{_libdir}/pkgconfig/osi.pc

%changelog

