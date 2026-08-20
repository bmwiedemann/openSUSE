#
# spec file for package zstd
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# This flavour packages nothing -- it exists only to run the test suite --
# so do not leave a zstd-test-debugsource behind either.
%global debug_package %{nil}
%else
%define psuffix %{nil}
%bcond_with test
%endif
# %%{name} carries the flavour suffix, so everything naming the upstream
# project -- sources, subpackages, requires -- has to go through %%{origname}.
%define origname zstd

%bcond_without cmake

%define libname libzstd1
%if 0%{?suse_version} <= 1500
%define with_gzip 0
%else
%define with_gzip 1
%endif
Name:           %{origname}%{psuffix}
Version:        1.5.7
Release:        0
Summary:        Zstandard compression tools
License:        BSD-3-Clause AND GPL-2.0-only
Group:          Productivity/Archiving/Compression
URL:            https://github.com/facebook/zstd
Source0:        https://github.com/facebook/zstd/releases/download/v%{version}/%{origname}-%{version}.tar.gz
Source1:        https://github.com/facebook/zstd/releases/download/v%{version}/%{origname}-%{version}.tar.gz.sig
Source2:        %{origname}.keyring
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE -- 0001-Don-t-export-libzstd_static-CMake-target.patch
Patch0:         0001-Don-t-export-libzstd_static-CMake-target.patch
# PATCH-FIX-OPENSUSE -- Backport https://github.com/facebook/zstd/commit/6af3842118ea5325480b403213b2a9fbed3d3d74.patch, relevant only for v1.5.7
Patch1:         0002-fix-1.5.7-documentation.patch
%if %{with cmake}
BuildRequires:  cmake
%endif
BuildRequires:  gcc
# C++ is needed for pzstd only
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# for .gz support
BuildRequires:  pkgconfig(zlib)
%if %{without test}
%{?suse_build_hwcaps_libs}
%endif
# The rings build every flavour unless told otherwise; the test suite has no
# business in the bootstrap ring.
%if %{with test} && 0%{?_with_ringdisabled}
ExclusiveArch:  do_not_build
%endif

%description
Zstd, short for Zstandard, is a lossless compression algorithm. Speed
vs. compression trade-off is configurable in small increments.
Decompression speed is preserved and remains roughly the same at all
settings, a property shared by most LZ compression algorithms, such
as zlib or lzma.

At roughly the same ratio, zstd (v1.4.0) achieves ~870%% faster
compression than gzip. For roughly the same time, zstd achieves a
~12%% better ratio than gzip. LZMA outperforms zstd by ~10%% faster
compression for same ratio, or ~1–4%% size reduction for same time.

%if %{without test}
%package -n %{libname}
Summary:        Zstd compression library
Group:          System/Libraries

%description -n %{libname}
Zstd, short for Zstandard, is a lossless compression algorithm,
targeting faster compression than zlib at comparable ratios.

This subpackage contains the implementation as a shared library.

%package -n lib%{origname}-devel
Summary:        Development files for the Zstd compression library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel

%description -n lib%{origname}-devel
Zstd, short for Zstandard, is a lossless compression algorithm,
targeting faster compression than zlib at comparable ratios.

Needed for compiling programs that link with the library.

%package -n lib%{origname}-devel-static
Summary:        Development files for the Zstd compression library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel-static
Requires:       lib%{origname}-devel = %{version}

%description -n lib%{origname}-devel-static
Zstd, short for Zstandard, is a lossless compression algorithm,
targeting faster compression than zlib at comparable ratios.

Needed for compiling programs that link with the library.

%if %{with_gzip}
%package gzip
Summary:        zstd and zlib based gzip drop-in
Group:          Productivity/Archiving/Compression
Requires:       %{origname} >= %{version}
Conflicts:      busybox-gzip
Conflicts:      gzip
Conflicts:      alternative(gzip)
Provides:       gzip
Provides:       alternative(gzip)

%description gzip
Zstd, short for Zstandard, is a lossless compression algorithm,
targeting faster compression than zlib at comparable ratios.

This subpackage provides a compatible alternative to gzip(1) using
an optimized deflate/zlib handling.
%endif
%endif

%prep
%autosetup -p1 -n %{origname}-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -std=c++11"
%if %{with test}
# Nothing to do: "make -C tests test-zstd" rebuilds the library and the CLI it
# tests through upstream's plain Makefile, so a cmake build here is wasted work.
%else
%if %{with cmake}
# %%cmake chdirs into ./build, so ./cmake resolves to the build/cmake sources
%cmake ./cmake -DZSTD_BUILD_CONTRIB:BOOL=ON -DZSTD_ZLIB_SUPPORT:BOOL=ON
%cmake_build
%else
# lib-mt is alias for multi-threaded library support
%make_build HAVE_ZLIB=1 prefix=%{_prefix} libdir=%{_libdir} -C lib lib-mt
for dir in programs contrib/pzstd; do
  %make_build -C "$dir"
done
%endif
%endif

%check
%if %{with test}
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -std=c++11"
# The full suite, including the large-data round trips gated behind
# --test-large-data, which is what test-zstd (unlike "check") turns on.
%make_build -C tests test-zstd
#make_build -C contrib/pzstd test-pzstd
%endif

%install
%if %{without test}
%if %{with cmake}
%cmake_install
rm %{buildroot}%{_datadir}/doc/packages/zstd/zstd_manual.html
%else
%make_install V=1 VERBOSE=1 prefix=%{_prefix} libdir=%{_libdir}
install -D -m755 contrib/pzstd/pzstd %{buildroot}%{_bindir}/pzstd
install -D -m644 programs/zstd.1 %{buildroot}%{_mandir}/man1/pzstd.1
%endif
%if %{with_gzip}
ln -s zstd %{buildroot}/%{_bindir}/gzip
ln -s zstd %{buildroot}/%{_bindir}/gunzip
ln -s zstdcat %{buildroot}/%{_bindir}/zcat
%endif
%endif

%if %{without test}
%ldconfig_scriptlets -n %{libname}

%files
%license COPYING LICENSE
%doc README.md CHANGELOG
%{_bindir}/pzstd
%{_bindir}/unzstd
%{_bindir}/zstd
%{_bindir}/zstdcat
%{_bindir}/zstdgrep
%{_bindir}/zstdless
%{_bindir}/zstdmt
%{_mandir}/man1/*.1%{?ext_man}

%files -n %{libname}
%license COPYING LICENSE
%{_libdir}/libzstd.so.1*

%files -n lib%{origname}-devel
%license COPYING LICENSE
%{_includedir}/*.h
%{_libdir}/pkgconfig/libzstd.pc
%{_libdir}/libzstd.so
%if %{with cmake}
%{_libdir}/cmake/zstd/
%endif

%files -n lib%{origname}-devel-static
%license COPYING LICENSE
%{_libdir}/libzstd.a

%if %{with_gzip}
%files gzip
%license COPYING LICENSE
%{_bindir}/gzip
%{_bindir}/gunzip
%{_bindir}/zcat
%endif
%endif

%changelog
