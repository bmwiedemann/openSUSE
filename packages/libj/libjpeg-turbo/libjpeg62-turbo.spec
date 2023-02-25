#
# spec file for package libjpeg62-turbo
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


%define major   62
%define minor   3
%define micro   0
%define libver  %{major}.%{minor}.%{micro}
%define srcver  2.1.5.1
Name:           libjpeg62-turbo
Version:        %{srcver}
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
# needed for tests as we remove the lib here
BuildRequires:  libturbojpeg0 >= 8.2.2
BuildRequires:  nasm
BuildRequires:  pkgconfig
Conflicts:      jpeg%{major}

%description
The libjpeg-turbo package contains a library of functions for manipulating
JPEG images. It supports architecture-specific SIMD instructions,
such as SSE/SSE2/AVX2, AltiVec, NEON, MIPS DSPR2, and Loongson MMI.

%package -n libjpeg%{major}
Version:        %{libver}
Release:        0
Summary:        A SIMD-accelerated JPEG compression/decompression library
Obsoletes:      libjpeg = 6.2.0

%description -n libjpeg%{major}
A library for manipulating JPEG images. It supports
architecture-specific SIMD instructions, such as SSE/SSE2/AVX2,
AltiVec, NEON, MIPS DSPR2, and Loongson MMI.

%package -n libjpeg%{major}-devel
Version:        %{libver}
Release:        0
Summary:        Development Tools for applications which will use the Libjpeg Library
Requires:       libjpeg%{major} = %{version}
Conflicts:      libjpeg-devel
Provides:       libjpeg-devel = %{version}
Obsoletes:      libjpeg-devel < %{version}

%description -n libjpeg%{major}-devel
The libjpeg-devel package includes the header files and libraries
necessary for compiling and linking programs which will manipulate JPEG
files using the libjpeg library.

%prep
%setup -q -n libjpeg-turbo-%{srcver}
%patch1

%build
export LDFLAGS="-Wl,-z,relro,-z,now"
%cmake \
    -DENABLE_STATIC=OFF \
%ifarch s390x riscv64
    -DFLOATTEST=fp-contract \
%endif
    %{nil}
%make_build

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%ctest

%install
%cmake_install
# Remove unwanted files
rm %{buildroot}%{_bindir}/*
rm %{buildroot}%{_mandir}/man1/*
# libjpegturbo is provided with libjpeg-turbo.spec yet
rm %{buildroot}%{_includedir}/turbojpeg.h
rm %{buildroot}%{_libdir}/libturbojpeg.so*
rm %{buildroot}%{_libdir}/pkgconfig/libturbojpeg.pc
rm -r %{buildroot}%{_libdir}/cmake
# Remove docs, we'll select docs manually
rm -rf %{buildroot}%{_datadir}/doc/

%post -n libjpeg%{major} -p /sbin/ldconfig
%postun -n libjpeg%{major} -p /sbin/ldconfig

%files -n libjpeg%{major}
%license LICENSE.md
%{_libdir}/libjpeg.so.%{major}
%{_libdir}/libjpeg.so.%{libver}

%files -n libjpeg%{major}-devel
%{_includedir}/*.h
%{_libdir}/libjpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%doc coderules.txt jconfig.txt libjpeg.txt structure.txt tjexample.c

%changelog
