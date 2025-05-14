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
Summary:        A modern and fast cryptographic hash function
License:        Apache-2.0
URL:            https://github.com/BLAKE3-team/BLAKE3
Source0:        https://github.com/BLAKE3-team/BLAKE3/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  tbb-devel
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}
%if 0%{?with_b3sum}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
%endif
%if 0%{?with_clib}
BuildRequires:  cmake
BuildRequires:  gcc-c++
%endif

%description
BLAKE3 is a modern cryptographic hash function designed for
high performance, strong security, and parallelism. It builds
upon earlier BLAKE and BLAKE2 designs but introduces a Merkle
tree structure that enables efficient parallel computation
across multiple cores, making it significantly faster than many
traditional hash functions like SHA-2 or SHA-3. BLAKE3 offers
a fixed 256-bit output and is designed to be simple, compact,
and memory-efficient, making it suitable for a wide range of
platforms—from embedded devices to high-performance servers. In
addition to being a cr yptographic hash, BLAKE3 can also serve as
a keyed hash (MAC) or extendable output function (XOF), making it
versatile for various cryptographic applications.

%if 0%{?with_b3sum}
%package -n b3sum
Summary:        A command line utility for calculating BLAKE3 hashes

%description -n b3sum
A command line utility for calculating BLAKE3 hashes, similar to Coreutils tools
like b2sum or md5sum.

%endif # with_b3sum

%if 0%{?with_clib}
%package -n libblake3-%{soname}
Summary:        The official C implementation of BLAKE3

%description -n libblake3-%{soname}
The official C implementation of BLAKE3.

%package -n libblake3-devel
Summary:        Development files for libblake3
Requires:       libblake3-%{soname} = %{version}

%description -n libblake3-devel
This package contains the development files (mainly C header files) for libblake3.

%endif # with_clib

%prep
%autosetup -p1 -a1 -n BLAKE3-%{version}

%build

%if 0%{?with_b3sum}
pushd b3sum
%{cargo_build}
popd
%endif # with_b3sum

%if 0%{?with_clib}
pushd c
%cmake -DBLAKE3_USE_TBB=1
%cmake_build
popd
%endif # with_clib

%install

%if 0%{?with_b3sum}
pushd b3sum
%{cargo_install}
popd
%endif

%if 0%{?with_clib}
pushd c
%cmake_install
popd
%endif # with_clib

%if 0%{?with_b3sum}
%check
pushd b3sum
%{cargo_test}
popd
%endif

%if 0%{?with_clib}
%ldconfig_scriptlets -n libblake3-%{soname}
%endif

%if 0%{?with_b3sum}
%files -n b3sum
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0
%{_bindir}/b3sum

%endif # with_b3sum

%if 0%{?with_clib}
%files -n libblake3-%{soname}
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0
%{_libdir}/libblake3.so.*

%files -n libblake3-devel
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0
%{_includedir}/blake3.h
%{_libdir}/cmake/blake3
%{_libdir}/libblake3.so
%{_libdir}/pkgconfig/libblake3.pc

%endif # with_clib

%changelog
