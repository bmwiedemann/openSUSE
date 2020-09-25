#
# spec file for package xcfun
#
# Copyright (c) 2020 SUSE LLC
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


%define major 2
%define libname lib%{name}%{major}
Name:           xcfun
Version:        %{major}.0.2
Release:        0
Summary:        Exchange-correlation functionals with arbitrary-order derivatives
License:        MPL-2.0
URL:            https://github.com/dftlibs/xcfun
Source:         https://github.com/dftlibs/xcfun/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.11
BuildRequires:  gcc-c++

%description
XCFun is a library of exchange-correlation (XC) functionals to be used in
density-functional theory (DFT) codes.

%package -n    %{libname}
Summary:        Exchange-correlation functionals with arbitrary-order derivatives

%description -n    %{libname}
XCFun is a library of exchange-correlation (XC) functionals to be used in 
density-functional theory (DFT) codes.

%package        devel
Summary:        Development files for lib%{name}
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.md
%{_libdir}/libxcfun.so.%{major}

%files devel
%doc README.md
%{_includedir}/XCFun
%{_libdir}/libxcfun.so
%{_datadir}/cmake/XCFun

%changelog
