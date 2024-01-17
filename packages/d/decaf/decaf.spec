#
# spec file for package decaf
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

%define sover 0

Name:           decaf
Version:        1.0.2
Release:        0
Summary:        Ed448-Goldilocks-based elliptic curve cryptography library
License:        MIT
URL:            https://ed448goldilocks.sourceforge.io/
Source:         %{name}-%{version}.tar.xz
Patch0:         remove_unsafe_methods.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3

%description
Ed448-Goldilocks is an Edwards-form elliptic curve proposed by
Michael Hamburg in 2015 and is suitable for cryptographic
operation with small keysizes.

%package -n lib%{name}%{sover}
Summary:        Ed448-Goldilocks-based elliptic curve cryptography library
Group:          System/Libraries

%description -n lib%{name}%{sover}
Ed448-Goldilocks is an Edwards-form elliptic curve proposed by
Michael Hamburg in 2015 and is suitable for cryptographic
operation with small keysizes.

%package devel
Summary:        Development files for libdecaf
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
Development files for Ed448-Goldilocks, an Edwards-form elliptic
curve proposed suitable for cryptographic operation with small
keysizes.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_C_FLAGS="-Wno-sizeof-array-div -Wno-array-parameter" \
  -DENABLE_STATIC=OFF \
  -DENABLE_STRICT=OFF \
  -Wno-dev
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc HISTORY.txt README.md

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}

%files devel
%{_libdir}/libdecaf.so
%dir %{_datadir}/decaf
%dir %{_datadir}/decaf/cmake
%{_datadir}/decaf/cmake/*

%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%changelog
