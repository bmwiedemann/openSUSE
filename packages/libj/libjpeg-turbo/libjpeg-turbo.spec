#
# spec file for package libjpeg-turbo
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


%define asan_build 0
%define debug_build 0
%define major    8
%define minor    2
%define micro    2
%define libver   %{major}.%{minor}.%{micro}
%define tmajor   0
%define tminor   2
%define tmicro   0
%define tlibver  %{tmajor}.%{tminor}.%{tmicro}
Name:           libjpeg-turbo
Version:        2.1.4
Release:        0
Summary:        A SIMD-accelerated library for manipulating JPEG image files
License:        BSD-3-Clause
URL:            https://sourceforge.net/projects/libjpeg-turbo
Source0:        https://downloads.sf.net/libjpeg-turbo/libjpeg-turbo-%{version}.tar.gz
Source1:        https://downloads.sf.net/libjpeg-turbo/libjpeg-turbo-%{version}.tar.gz.sig
Source2:        libjpeg-turbo.keyring
Source3:        baselibs.conf
Patch1:         libjpeg-turbo-1.3.0-tiff-ojpeg.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  pkgconfig
Conflicts:      jpeg%{major}
Obsoletes:      jpeg = 6b
Obsoletes:      jpeg = 8.0.1
Obsoletes:      jpeg = 8.0.2
Provides:       jpeg = %{version}
Obsoletes:      jpeg < %{version}
Provides:       jpegtran = %{version}

%description
The libjpeg-turbo package contains a library of functions for manipulating
JPEG images. It supports architecture-specific SIMD instructions,
such as SSE/SSE2/AVX2, AltiVec, NEON, MIPS DSPR2, and Loongson MMI.

It also includes the following command line utilities:
  djpeg - decompress a JPEG file to an image file
  jpegtran - lossless transformation of JPEG files
  rdjpgcom - display text comments from a JPEG file
  wrjpgcom - insert text comments into a JPEG file
  tjbench - a JPEG decompression/compression benchmark

%package -n libjpeg%{major}
Version:        %{libver}
Release:        0
Summary:        A SIMD-accelerated JPEG compression/decompression library

%description -n libjpeg%{major}
A library for manipulating JPEG images. It supports
architecture-specific SIMD instructions, such as SSE/SSE2/AVX2,
AltiVec, NEON, MIPS DSPR2, and Loongson MMI.

%package -n libturbojpeg%{tmajor}
Version:        %{version}
Release:        0
Summary:        A SIMD-accelerated JPEG compression/decompression library

%description -n libturbojpeg%{tmajor}
A library for manipulating JPEG images. It supports
architecture-specific SIMD instructions, such as SSE/SSE2/AVX2,
AltiVec, NEON, MIPS DSPR2, and Loongson MMI.

%package -n libjpeg%{major}-devel
Version:        %{libver}
Release:        0
Summary:        Development Tools for applications which will use the Libjpeg Library
Requires:       libjpeg%{major} = %{version}
Requires:       libturbojpeg%{tmajor} = %{version}
Conflicts:      libjpeg-devel
Provides:       libjpeg-devel = %{version}
Obsoletes:      libjpeg-devel < %{version}

%description -n libjpeg%{major}-devel
The libjpeg-devel package includes the header files and libraries
necessary for compiling and linking programs which will manipulate JPEG
files using the libjpeg library.

%prep
%setup -q
%patch1

%build
MYLDFLAGS="-Wl,-z,relro,-z,now"
MYCFLAGS="%{optflags}"
%if %{asan_build}
MYLDFLAGS="$MYLDFLAGS -lasan"
MYCFLAGS="$MYCFLAGS -fsanitize=address"
%endif
%if %{debug_build}
MYCFLAGS="$MYCFLAGS -O0 -g"
%endif
%cmake \
%if %{debug_build} || %{asan_build}
    -DCMAKE_BUILD_TYPE=DEBUG \
    -DCMAKE_C_FLAGS_DEBUG="$MYCFLAGS" \
%endif
%ifarch armv6l armv6hl
    -DWITH_SIMD=FALSE \
%endif
    -DCMAKE_SHARED_LINKER_FLAGS="$MYLDFLAGS" \
    -DENABLE_STATIC=OFF \
    -DWITH_JPEG8=ON \
%ifarch s390x riscv64
    -DFLOATTEST=fp-contract \
%endif
    %{nil}
%make_build

%check
%if %{asan_build}
# ASAN needs /proc to be mounted
exit 0
%endif
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%if 0%{?fedora_version} || 0%{?centos_version}
  ctest --output-on-failure --force-new-ctest-process
%else
  %ctest
%endif

%install
%if 0%{?fedora_version} || 0%{?centos_version}
  make DESTDIR=%{buildroot} install/fast
%else
  %cmake_install
%endif
# Remove docs, we'll select docs manually
rm -rf %{buildroot}%{_datadir}/doc/

%post -n libjpeg%{major} -p /sbin/ldconfig
%postun -n libjpeg%{major} -p /sbin/ldconfig
%post -n libturbojpeg%{tmajor} -p /sbin/ldconfig
%postun -n libturbojpeg%{tmajor} -p /sbin/ldconfig

%files
%doc README.md change.log ChangeLog.md
%doc usage.txt wizard.txt
%{_bindir}/*
%{_mandir}/man1/*

%files -n libjpeg%{major}
%license LICENSE.md
%{_libdir}/libjpeg.so.%{libver}
%{_libdir}/libjpeg.so.%{major}

%files -n libturbojpeg%{tmajor}
%license LICENSE.md
%{_libdir}/libturbojpeg.so.%{tmajor}
%{_libdir}/libturbojpeg.so.%{tlibver}

%files -n libjpeg%{major}-devel
%{_includedir}/*.h
%{_libdir}/libjpeg.so
%{_libdir}/libturbojpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%{_libdir}/pkgconfig/libturbojpeg.pc
%dir %{_libdir}/cmake/libjpeg-turbo
%{_libdir}/cmake/libjpeg-turbo/*
%doc coderules.txt jconfig.txt libjpeg.txt structure.txt tjexample.c

%changelog
