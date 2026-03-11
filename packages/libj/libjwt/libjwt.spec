#
# spec file for package libjwt
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

%define lib_name libjwt2

Name:           libjwt
Version:        1.18.3
Release:        0
Summary:        JWT C Library
License:        MPL-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/benmcollins/libjwt
Source:         libjwt-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libjansson-devel
BuildRequires:  libtool

%description
Javascript Object Signing and Encryption (JOSE) library

%package -n %{lib_name}
Summary:        LibJWT C Library
Group:          Development/Libraries/C and C++

%description -n %{lib_name}
LibJWT C Library - shared library

%package devel
Summary:        LibJWT C Library
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}
Requires:       cmake

%description devel
LibJWT C Library - devel headers and tools

%prep
%autosetup -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

# create cmake files
%cmake

mkdir -p %{buildroot}%{_libdir}/cmake/%{name}
cp libjwtConfig*.cmake %{buildroot}%{_libdir}/cmake/%{name}

rm %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f -name "*.la" -delete -print

%check
make check V=1

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%license LICENSE
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/jwt.h
%{_libdir}/lib*.so
%{_libdir}/cmake/%{name}/*.cmake
%{_bindir}/jwt*
%dir /usr/lib64/cmake
%dir /usr/lib64/cmake/%{name}

%changelog
