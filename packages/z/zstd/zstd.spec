#
# spec file for package zstd
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


%define major 1
%define libname lib%{name}%{major}
Name:           zstd
Version:        %{major}.4.5
Release:        0
Summary:        Zstandard compression tools
License:        BSD-3-Clause AND GPL-2.0-only
Group:          Productivity/Archiving/Compression
URL:            https://github.com/facebook/zstd
Source0:        https://github.com/facebook/zstd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
Patch1:         pzstd.1.patch
BuildRequires:  gcc
# C++ is needed for pzstd only
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Zstd, short for Zstandard, is a lossless compression algorithm. Speed
vs. compression trade-off is configurable in small increments.
Decompression speed is preserved and remains roughly the same at all
settings, a property shared by most LZ compression algorithms, such
as zlib or lzma.

At roughly the same ratio, zstd (v1.4.0) achieves ~870%% faster
compression than gzip. For roughly the same time, zstd achives a
~12%% better ratio than gzip. LZMA outperforms zstd by ~10%% faster
compression for same ratio, or ~1–4%% size reduction for same time.

# This compression summary is based on https://lists.opensuse.org/opensuse-factory/2019-05/msg00344.html

%package -n %{libname}
Summary:        Zstd compression library
Group:          System/Libraries

%description -n %{libname}
Zstd, short for Zstandard, is a lossless compression algorithm,
targeting faster compression than zlib at comparable ratios.

This subpackage contains the implementation as a shared library.

%package -n lib%{name}-devel
Summary:        Development files for the Zstd compression library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel

%description -n lib%{name}-devel
Zstd, short for Zstandard, is a lossless compression algorithm,
targeting faster compression than zlib at comparable ratios.

Needed for compiling programs that link with the library.

%package -n lib%{name}-devel-static
Summary:        Development files for the Zstd compression library
Group:          Development/Libraries/C and C++
BuildRequires:  glibc-devel-static
Requires:       lib%{name}-devel = %{version}

%description -n lib%{name}-devel-static
Zstd, short for Zstandard, is a lossless compression algorithm,
targeting faster compression than zlib at comparable ratios.

Needed for compiling programs that link with the library.

%prep
%setup -q
%patch1 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -std=c++11"
for dir in lib programs contrib/pzstd; do
  make %{?_smp_mflags} -C "$dir"
done

%check
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -std=c++11"
make %{?_smp_mflags} -C tests test-zstd
#make %{?_smp_mflags} -C contrib/pzstd test-pzstd

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
install -D -m755 contrib/pzstd/pzstd %{buildroot}%{_bindir}/pzstd
install -D -m644 programs/zstd.1 %{buildroot}%{_mandir}/man1/pzstd.1

%files
%license COPYING LICENSE
%doc README.md CHANGELOG
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files -n %{libname}
%license COPYING LICENSE
%{_libdir}/libzstd.so.*

%files -n lib%{name}-devel
%license COPYING LICENSE
%{_includedir}/*.h
%{_libdir}/pkgconfig/libzstd.pc
%{_libdir}/libzstd.so

%files -n lib%{name}-devel-static
%license COPYING LICENSE
%{_libdir}/libzstd.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%changelog
