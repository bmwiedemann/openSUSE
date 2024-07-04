#
# spec file for package libvpx
#
# Copyright (c) 2024 SUSE LLC
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


%define         sover 9
%define use_gcc13 0%{?suse_version} < 1600
Name:           libvpx
Version:        1.14.1
Release:        0
Summary:        VP8/VP9 codec library
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.webmproject.org/
Source0:        %{name}-%{version}.tar.xz
Source1000:     baselibs.conf
Patch2:         libvpx-configure-add-arch.patch
%if %use_gcc13
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
# only needed for test suite
# Needed to be able to create pkgconfig() provides.
BuildRequires:  pkgconfig
BuildRequires:  yasm
# add curl and do not copy it in to get an updated test-data.sha1 file
#BuildRequires:  curl

%description
WebM is an open, royalty-free, media file format designed for the web.

WebM defines the file container structure, video and audio formats.
WebM files consist of video streams compressed with the VP8 video codec
and audio streams compressed with the Vorbis audio codec.
The WebM file structure is based on the Matroska container.

%package -n vpx-tools
Summary:        Utilies from the VP8/VP9 codec library
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Multimedia/Other

%description -n vpx-tools
This package contains utilities around the vp8 codec sdk.

WebM is an open, royalty-free, media file format designed for the web.

WebM defines the file container structure, video and audio formats.
WebM files consist of video streams compressed with the VP8 video codec
and audio streams compressed with the Vorbis audio codec.
The WebM file structure is based on the Matroska container.

%package -n %{name}%{sover}
Summary:        VP8/VP9 codec library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %{name}%{sover}
WebM is an open, royalty-free, media file format designed for the web.

WebM defines the file container structure, video and audio formats.
WebM files consist of video streams compressed with the VP8 video codec
and audio streams compressed with the Vorbis audio codec.
The WebM file structure is based on the Matroska container.

%package devel
Summary:        Development files for libvpx, a VP8/VP9 codec library
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Languages/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Development headers and library

WebM is an open, royalty-free, media file format designed for the web.

WebM defines the file container structure, video and audio formats.
WebM files consist of video streams compressed with the VP8 video codec
and audio streams compressed with the Vorbis audio codec.
The WebM file structure is based on the Matroska container.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%if 0%{?suse_version} < 1310
sed -i~ /ssse3/d configure
sed -i~ 's@ssse3@@' build/make/rtcd.pl
%endif
cd build
%if %use_gcc13
export CXX=g++-13
export CC=gcc-13
%endif
# It is only an emulation of autotools configure; the macro does not work
export CFLAGS="%{optflags} -O3"
export CXXFLAGS="%{optflags} -O3"
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-unit-tests \
    --enable-shared \
    --enable-pic \
    --disable-static \
    --enable-vp8 \
    --enable-vp9 \
    --enable-vp9-highbitdepth \
    --enable-postproc \
    --enable-multithread \
    --enable-pic \
%ifarch ppc64le
    --disable-vsx \
%endif
%ifarch armv5tel armv5el
    --target=armv5te-linux-gcc \
%endif
%ifarch armv7l armv7hl
    --target=armv7-linux-gcc \
    --enable-runtime-cpu-detect \
%endif
    --extra-cflags="-std=gnu99 -U_FORTIFY_SOURCE %{optflags}" \
    --extra-cxxflags="-U_FORTIFY_SOURCE %{optflags}" \
# size-limit to avoid CVE-2017-0641 DoS attacks. The limit is the
# 8K Fulldome resolution and should be enough for all current use cases
# bso#1056539
# the --size-limit switch is broken atm ...
echo '#define DECODE_WIDTH_LIMIT 8192'  >> vpx_config.h
echo '#define DECODE_HEIGHT_LIMIT 8192' >> vpx_config.h

%make_build verbose=yes GEN_EXAMPLES=

%install
cd build
make %{?_smp_mflags} verbose=yes GEN_EXAMPLES= DESTDIR=%{buildroot} install

%check
# needs network to download >400MB data
# make test

%ldconfig_scriptlets -n %{name}%{sover}

%files -n vpx-tools
%{_bindir}/*

%files -n %{name}%{sover}
%license LICENSE
%doc AUTHORS README CHANGELOG
%{_libdir}/libvpx.so.*

%files devel
%{_includedir}/vpx/
%{_libdir}/pkgconfig/vpx.pc
%{_libdir}/libvpx.so

%changelog
