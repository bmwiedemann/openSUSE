#
# spec file for package qd
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


%define libname libqd0
Name:           qd
Version:        2.3.23
Release:        0
Summary:        Quad Double computation package
License:        BSD-3-Clause-LBNL
Group:          Development/Libraries/C and C++
URL:            https://www.davidhbailey.com/dhbsoftware/
Source0:        https://www.davidhbailey.com/dhbsoftware/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkg-config

%description
qd provides numeric types of twice the precision of IEEE double
(106 mantissa bits, or approximately 32 decimal digits) and four
times the precision of IEEE double (212 mantissa bits, or approximately
64 decimal digits).  Due to features such as operator and function
overloading, these facilities can be utilized with only minor modifications
to conventional C++ and Fortran-90 programs.

%package -n %{libname}
Summary:        A library for nonlinear optimization
Group:          System/Libraries

%description -n %{libname}
qd provides numeric types of twice the precision of IEEE double
(106 mantissa bits, or approximately 32 decimal digits) and four
times the precision of IEEE double (212 mantissa bits, or approximately
64 decimal digits).  Due to features such as operator and function
overloading, these facilities can be utilized with only minor modifications
to conventional C++ and Fortran-90 programs.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --enable-shared --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

rm -rf %{buildroot}%{_datadir}/doc/qd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/*.so.*

%files devel
%license COPYING
%doc AUTHORS docs/qd.pdf NEWS README
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/qd.pc

%changelog
