#
# spec file for package libff
#
# Copyright (c) 2025 SUSE LLC
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


%define lname libff-1_0_0
Name:           libff
Version:        1.0.0
Release:        0
Summary:        C++ library for Finite Fields and Elliptic Curves
License:        MIT
URL:            https://github.com/scipr-lab/libff
Source0:        https://github.com/scipr-lab/libff/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
Patch0:         00_no_bn128.patch
Patch1:         01_shared_lib.patch
Patch2:         02_config_hpp.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libopenssl-devel
%{?suse_build_hwcaps_libs}

%description
libff is a C++ library for finite fields and elliptic curves.

%package -n %{lname}
Summary:        C++ library for finite fields and elliptic curves

%description -n %{lname}
libff is a C++ library for finite fields and elliptic curves.

%package devel
Summary:        Development files for libff
Requires:       %{lname} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing applications that use libff.

%prep
%autosetup -p1
chmod 0644 LICENSE AUTHORS README.md
# see 00_no_bn128.patch
rm -r depends
rm -r libff/algebra/curves/bn128
rm libff/algebra/scalar_multiplication/multiexp_profile.cpp

%build
%cmake \
  -DWITH_PROCPS=OFF \
  -DPACKAGE_VERSION:STRING="%{version}"
%cmake_build

%check
pushd build
make check

%install
%cmake_install

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%doc README.md
%license LICENSE AUTHORS
%{_libdir}/libff-%{version}.so

%files devel
%{_includedir}/libff/

%changelog
