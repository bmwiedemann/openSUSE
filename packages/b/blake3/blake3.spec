#
# spec file for package blake3
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


%global soname 0

%if 0%{?suse_version} == 1500
# (open)SUSE 15.x does not have C++20 support
%bcond_with     clib
%else
%bcond_without  clib
%endif

# Disable b3sum cli tool by default, can be enabled with --with b3sum
# This is to avoid conflicts with the b3sum package in openSUSE Factory
%bcond_with     b3sum

Name:           blake3
Version:        1.8.2
Release:        0
Summary:        A cryptographic hash function
License:        Apache-2.0
URL:            https://github.com/BLAKE3-team/BLAKE3
Source0:        https://github.com/BLAKE3-team/BLAKE3/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  tbb-devel
BuildRequires:  zstd
%if 0%{?with_b3sum}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
%endif
%if 0%{?with_clib}
BuildRequires:  cmake
BuildRequires:  gcc-c++
%endif

%description
BLAKE3 is a cryptographic hash function with features like Extendable
Output Function (XOF), Key Derivation Functions (KDF), Pseudorandom
Functions (PRF) and Keyed Hashes (MAC). It introduces a Merkle tree
structure that enables parallel computation across multiple cores.
BLAKE3 offers a fixed 256-bit output and targets memory efficiency.

%package -n b3sum
Summary:        A command line utility for calculating BLAKE3 hashes

%description -n b3sum
A command line utility for calculating BLAKE3 hashes, similar to
Coreutils tools like b2sum or md5sum.

%package -n libblake3-%{soname}
Summary:        A cryptographic hash function

%description -n libblake3-%{soname}
BLAKE3 is a cryptographic hash function with features like Extendable
Output Function (XOF), Key Derivation Functions (KDF), Pseudorandom
Functions (PRF) and Keyed Hashes (MAC). It introduces a Merkle tree
structure that enables parallel computation across multiple cores.
BLAKE3 offers a fixed 256-bit output and targets memory efficiency.

The official C implementation of BLAKE3.

%package devel
Summary:        Development files for libblake3
Requires:       libblake3-%{soname} = %{version}
Obsoletes:      libblake3-devel < %{version}-%{release}
Provides:       libblake3-devel = %{version}-%{release}

%description devel
This package contains the development files (mainly C header files) for libblake3.

%prep
%autosetup -p1 -a1 -n BLAKE3-%{version}

%build
b="$PWD"

%if 0%{?with_b3sum}
cd b3sum
%{cargo_build}
cd "$b"
%endif # with_b3sum

%if 0%{?with_clib}
cd c
%cmake -DBLAKE3_USE_TBB=1
%cmake_build
cd "$b"
%endif # with_clib

%install
b="$PWD"

%if 0%{?with_b3sum}
cd b3sum
%{cargo_install}
cd "$b"
%endif

%if 0%{?with_clib}
cd c
%cmake_install
cd "$b"
%endif # with_clib

%if 0%{?with_b3sum}
%check
b="$PWD"
cd b3sum
%{cargo_test}
cd "$b"
%endif

%ldconfig_scriptlets -n libblake3-%{soname}

%if 0%{?with_b3sum}
%files -n b3sum
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0
%{_bindir}/b3sum

%endif # with_b3sum

%if 0%{?with_clib}
%files -n libblake3-%{soname}
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0
%{_libdir}/libblake3.so.*

%files devel
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0
%{_includedir}/blake3.h
%{_libdir}/cmake/blake3
%{_libdir}/libblake3.so
%{_libdir}/pkgconfig/libblake3.pc

%endif # with_clib

%changelog
