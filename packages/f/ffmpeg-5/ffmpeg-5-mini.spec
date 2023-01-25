#
# spec file for package ffmpeg-5-mini
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


%define _name ffmpeg

Name:           ffmpeg-5-mini
Version:        5.1.2
Release:        0
Summary:        Set of libraries for working with various multimedia formats
License:        GPL-3.0-or-later
URL:            https://ffmpeg.org/
#Git-Clone:     git://source.ffmpeg.org/ffmpeg
Source:         https://www.ffmpeg.org/releases/%_name-%version.tar.xz
Source2:        https://www.ffmpeg.org/releases/%_name-%version.tar.xz.asc
Source3:        %name-rpmlintrc
Source98:       http://ffmpeg.org/ffmpeg-devel.asc#/ffmpeg-5.keyring
Patch1:         ffmpeg-arm6l.diff
Patch2:         ffmpeg-new-coder-errors.diff
Patch3:         ffmpeg-codec-choice.diff
Patch4:         ffmpeg-4.2-dlopen-fdk_aac.patch
Patch5:         work-around-abi-break.patch
Patch9:         ffmpeg-4.4-CVE-2020-22046.patch
Patch10:        ffmpeg-chromium.patch
Patch11:        ffmpeg-CVE-2022-3964.patch
Patch91:        ffmpeg-dlopen-openh264.patch
BuildRequires:  c_compiler

%description
FFmpeg is a multimedia framework.
This package merely builds the API for the sake of other packages.

%package libs
# Even with mini, we want ff5 libs to be coinstallable to ff4-devel(!),
# hence mini-libs and mini-devel are still separated.
Summary:        Feature-reduced build of FFmpeg, a multimedia framework
Conflicts:      libavcodec59
Conflicts:      libavdevice59
Conflicts:      libavfilter8
Conflicts:      libavformat59
Conflicts:      libavutil57
Conflicts:      libpostproc56
Conflicts:      libswresample4
Conflicts:      libswscale6

%description libs
FFmpeg is a multimedia framework.
This package contains a cut-down version for building other packages.

%package devel
Summary:        Header files for feature-reduced FFmpeg build
Provides:       libavcodec-devel = %version-%release
Conflicts:      libavcodec-devel
Provides:       libavdevice-devel = %version-%release
Conflicts:      libavdevice-devel
Provides:       libavfilter-devel = %version-%release
Conflicts:      libavfilter-devel
Provides:       libavformat-devel = %version-%release
Conflicts:      libavformat-devel
Provides:       libavutil-devel = %version-%release
Conflicts:      libavutil-devel
Provides:       libpostproc-devel = %version-%release
Conflicts:      libpostproc-devel
Provides:       libswresample-devel = %version-%release
Conflicts:      libswresample-devel
Provides:       libswscale-devel = %version-%release
Conflicts:      libswscale-devel
Requires:       %name-libs = %version-%release

%description devel
FFmpeg is a multimedia framework.
This package contains the headers accompanying %name.

%prep
%autosetup -p1 -n %_name-%version

%build
%define _lto_cflags %nil
CFLAGS="%optflags" \
./configure \
	--prefix="%_prefix" \
	--libdir="%_libdir" \
	--shlibdir="%_libdir" \
	--incdir="%_includedir/ffmpeg" \
	--extra-cflags="%optflags" \
	--optflags="%optflags" \
	--disable-htmlpages --disable-stripping --disable-x86asm \
	--disable-static --enable-shared --enable-pic \
	--enable-gpl --enable-version3 \
	--disable-muxers --disable-demuxers \
	--disable-encoders --disable-decoders \
	--disable-programs --disable-doc
for i in MPEG4 H263 H264 HEVC VC1; do
	grep -q "#define CONFIG_${i}_DECODER 0" config_components.h
done
cat config.h
%make_build

%install
b="%buildroot"
%make_install
rm -Rf "$b/%_datadir/ffmpeg/examples"

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%_libdir/libavcodec.so.*
%_libdir/libavdevice.so.*
%_libdir/libavfilter.so.*
%_libdir/libavformat.so.*
%_libdir/libavutil.so.*
%_libdir/libpostproc.so.*
%_libdir/libswresample.so.*
%_libdir/libswscale.so.*

%files devel
%license COPYING.GPLv2 LICENSE.md
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/ffmpeg/

%changelog
