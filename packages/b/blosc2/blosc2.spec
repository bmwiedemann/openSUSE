#
# spec file for package blosc2
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


%define major 2
%define libname lib%{name}-%{major}
Name:           blosc2
Version:        2.7.1
Release:        0
Summary:        A fast, compressed, persistent binary data store library for C
License:        MIT AND BSD-3-Clause AND BSD-2-Clause
URL:            https://www.blosc.org/c-blosc2/c-blosc2.html
Source:         https://github.com/Blosc/c-blosc2/archive/refs/tags/v%{version}.tar.gz#/c-blosc2-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  x86_64 %{ix86} aarch64

%description
Blosc is a high performance compressor optimized for binary data
(i.e. floating point numbers, integers and booleans). It has been
designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a
memcpy() OS call. Blosc main goal is not just to reduce the size
of large datasets on-disk or in-memory, but also to accelerate
memory-bound computations.

C-Blosc2 is the new major version of C-Blosc, and tries hard to
be backward compatible with both the C-Blosc1 API and its in-memory
format. However, the reverse thing is generally not true for the
format; buffers generated with C-Blosc2 are not format-compatible
with C-Blosc1 (i.e. forward compatibility is not supported). In
case you want to ensure full API compatibility with C-Blosc1 API,
define the BLOSC1_COMPAT symbol.

%package -n %{libname}
Summary:        A fast, compressed, persistent binary data store library for C
Group:          System/Libraries

%description -n %{libname}
Blosc is a high performance compressor optimized for binary data
(i.e. floating point numbers, integers and booleans).

%package devel
Summary:        Development libraries for %{libname}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package provides development libraries and headers
for %{libname}.

%prep
%autosetup -p1 -n c-blosc2-%{version}

%build
%cmake \
  -DDEACTIVATE_AVX2:BOOL=ON \
  -DPREFER_EXTERNAL_ZLIB:BOOL=ON \
  -DPREFER_EXTERNAL_ZSTD:BOOL=ON \
  -DPREFER_EXTERNAL_LZ4:BOOL=ON \
  -DBUILD_STATIC:BOOL=OFF \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_FUZZERS:BOOL=OFF \
  -DBUILD_BENCHMARKS:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
export LD_PRELOAD="$LD_PRELOAD  %{buildroot}%{_libdir}/libblosc2.so  %{buildroot}%{_libdir}/libblosc2.so.%{major}"
# https://github.com/Blosc/c-blosc2/issues/432
%ctest --exclude-regex 'test_sframe|test_schunk_frame|test_fill_special'
pushd build
ctest --tests-regex 'test_sframe|test_schunk_frame|test_fill_special'
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.txt LICENSES/*.txt
%doc ANNOUNCE.md README*.rst RELEASE_NOTES.md THANKS.rst
%{_libdir}/libblosc2.so.%{major}
%{_libdir}/libblosc2.so.%{version}

%files devel
%doc examples/
%{_includedir}/blosc2
%{_includedir}/blosc2.h
%{_includedir}/b2nd.h
%{_libdir}/libblosc2.so
%{_libdir}/pkgconfig/blosc2.pc

%changelog
