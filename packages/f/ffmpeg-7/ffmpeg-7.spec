#
# spec file for package ffmpeg-7
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


%define flavor @BUILD_FLAVOR@%nil
#
# preamble is present twice, watch out
#
%if "%flavor" != "ffmpeg-7-mini"

# Create proper conflicts to make sure we require all from one version
# p:   Conflict string, eg if you need them all for requires instead
#      Default value Conflicts:
# c:   copmare string ie "<" or ">=", must be defined
# v:   version string ie. "< 42.3.4" or ">= 15.0.2.1", must be defined
%define devel_conflicts(p:c:v:) \
%define preamble_string %{-p:%{-p*}}%{!-p:Conflicts:} \
%define comparator %{-c:%{-c*}}%{!-c:%{error:Comparator not defined}} \
%define conflicts_version %{-v:%{-v*}}%{!-v:%{error:Version not defined}} \
\
%preamble_string libavcodec-devel %comparator %conflicts_version \
%preamble_string libavdevice-devel %comparator %conflicts_version \
%preamble_string libavfilter-devel %comparator %conflicts_version \
%preamble_string libavformat-devel %comparator %conflicts_version \
%preamble_string libavutil-devel %comparator %conflicts_version \
%preamble_string libpostproc-devel %comparator %conflicts_version \
%preamble_string libswresample-devel %comparator %conflicts_version \
%preamble_string libswscale-devel %comparator %conflicts_version \
%nil

%if 0%{?BUILD_ORIG}
%bcond_without amf_sdk
%bcond_without cuda_sdk
%else
# If software H264 is disabled, the hw driver must be as well:
# HW drivers can fail to initialize, namely when the hardware is absent.
# Browsers choose video formats on sites like youtube based on `ffmpeg
# -codecs` rather than the success/failure status of libav* initialization.
# This becomes a problem when a format only has a HW driver;
# the browser thinks it can do H264 but never succeeds.
%bcond_with    amf_sdk
%bcond_with    cuda_sdk
%endif

%bcond_with    amrwb
%bcond_with    fdk_aac_dlopen
%bcond_with    opencore
%bcond_with    smbclient
%bcond_with    x264
%bcond_with    x265
%bcond_with    xvid

%if 0%{?suse_version} > 1500
%bcond_without mysofa
%bcond_without vidstab
%bcond_without codec2
%bcond_without rubberband
%bcond_without vulkan
%bcond_without amrwb
%bcond_without opencore
%bcond_without xvid
%else
%bcond_with mysofa
%bcond_with vidstab
%bcond_with codec2
%bcond_with rubberband
%bcond_with vulkan
%endif

%define _name ffmpeg
%define _major_version 7
%define _major_expected 8

Name:           ffmpeg-7
Version:        7.0
Release:        0
Summary:        Set of libraries for working with various multimedia formats
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://ffmpeg.org/

#Freshcode-URL:    http://freshcode.club/projects/ffmpeg
#Git-Clone:     git://source.ffmpeg.org/ffmpeg
Source:         https://www.ffmpeg.org/releases/%_name-%version.tar.xz
Source2:        https://www.ffmpeg.org/releases/%_name-%version.tar.xz.asc
Source3:        ffmpeg-7-rpmlintrc
Source4:        enable_decoders
Source5:        enable_encoders
Source6:        ffmpeg-dlopen-headers.tar.xz
Source92:       ffmpeg_get_dlopen_headers.sh
Source98:       http://ffmpeg.org/ffmpeg-devel.asc#/ffmpeg-7.keyring
Source99:       baselibs.conf
Patch1:         ffmpeg-arm6l.diff
Patch2:         ffmpeg-new-coder-errors.diff
Patch3:         ffmpeg-codec-choice.diff
Patch4:         ffmpeg-4.2-dlopen-fdk_aac.patch
Patch5:         work-around-abi-break.patch
Patch10:        ffmpeg-chromium.patch
Patch91:        ffmpeg-dlopen-openh264.patch
Patch92:        ffmpeg-7-CVE-2024-32228.patch
Patch93:        ffmpeg-7-CVE-2024-32230.patch
BuildRequires:  ladspa-devel
BuildRequires:  libgsm-devel
BuildRequires:  libmp3lame-devel >= 3.98.3
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom) >= 1.0.0
BuildRequires:  pkgconfig(dav1d) >= 0.5.0
BuildRequires:  pkgconfig(ffnvcodec) >= 8.1.24.15
BuildRequires:  pkgconfig(fontconfig) >= 2.4.2
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi) >= 0.19.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass) >= 0.11.0
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libopenmpt) >= 0.2.6557
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libraw1394)
BuildRequires:  pkgconfig(libssh) >= 0.6.0
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libvmaf) >= 2.0.0
BuildRequires:  pkgconfig(libwebp) >= 0.4
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzmq) >= 4.2.1
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2) >= 2.0.1
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(theora) >= 1.1
BuildRequires:  pkgconfig(twolame) >= 0.3.10
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zimg) >= 2.7.0
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28

%if %{with amf_sdk}
BuildRequires:  AMF-devel
%endif
%if %{with mysofa}
BuildRequires:  libmysofa-devel
%endif
%if %{with codec2}
BuildRequires:  pkgconfig(codec2)
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
BuildRequires:  pkgconfig(libjxl) >= 0.7.0
BuildRequires:  pkgconfig(libjxl_threads) >= 0.7.0
BuildRequires:  pkgconfig(librist) >= 0.2.7
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(rav1e) >= 0.5.0
%endif
%if %{with rubberband}
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
%endif
%if %{with smbclient}
BuildRequires:  pkgconfig(smbclient)
%endif
%if %{with vidstab}
BuildRequires:  pkgconfig(vidstab) >= 0.98
%endif
%if %{with fdk_aac_dlopen}
BuildRequires:  pkgconfig(fdk-aac)
%endif
%if %{with xvid}
BuildRequires:  libxvidcore-devel
%endif
%if %{with opencore}
BuildRequires:  pkgconfig(opencore-amrnb)
%endif
%if %{with amrwb}
BuildRequires:  pkgconfig(vo-amrwbenc)
%endif
%if %{with x264}
BuildRequires:  pkgconfig(x264)
%endif
%if %{with x265}
BuildRequires:  pkgconfig(x265)
%endif

%ifarch x86_64 %x86_64 aarch64
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
BuildRequires:  pkgconfig(SvtAv1Enc) >= 0.9.0
%endif
%endif

%if %{with vulkan}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
BuildRequires:  pkgconfig(libplacebo) >= 6.292.0
%else
BuildRequires:  (pkgconfig(libplacebo) >= 4.192.0 with pkgconfig (libplacebo) < 6.292.0)
%endif
BuildRequires:  pkgconfig(shaderc) >= 2019.1
BuildRequires:  pkgconfig(vulkan) >= 1.3.255
%endif

%if 0%{?suse_version} < 1550 && 0%{?sle_version} >= 150200 && 0%{?sle_version} < 150600
%ifarch x86_64 %x86_64
BuildRequires:  pkgconfig(libmfx)
%endif
%else
%ifarch x86_64 %x86_64
BuildRequires:  pkgconfig(vpl) >= 2.6
%endif
%endif

Provides:       ffmpeg-tools = %version
Conflicts:      ffmpeg-tools
Provides:       ffmpeg = %version
Obsoletes:      ffmpeg < %version
Requires:       (libavcodec61 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavdevice61 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavfilter10 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavformat61 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavutil59 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libpostproc58 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libswresample5 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libswscale8 = %version-%release or ffmpeg-7-mini-libs = %version-%release)

%description
FFmpeg is a multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play several formats
that humans and machines have created.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package -n libavcodec61
Summary:        FFmpeg codec library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release
Requires:       libswresample5 = %version-%release
%if 0%{?BUILD_ORIG}
Provides:       libavcodec-full = %version-%release
# This can be (and is) required by packages like vlc-codecs -
# do follow the shlib name to not get random lib providers
Provides:       libavcodec61(unrestricted)
%endif
# For mozillas
Provides:       libavcodec = %version-%release

%description -n libavcodec61
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package libavcodec-devel
Summary:        Development files for FFmpeg's codec library
Group:          Development/Libraries/C and C++
Provides:       libavcodec-devel = %version-%release
Obsoletes:      libavcodec-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libavcodec61 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavcodec-devel
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavdevice61
Summary:        FFmpeg device library
Group:          System/Libraries
Requires:       libavcodec61 = %version-%release
Requires:       libavfilter10 = %version-%release
Requires:       libavformat61 = %version-%release
Requires:       libavutil59 = %version-%release

%description -n libavdevice61
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

%package libavdevice-devel
Summary:        Development files for FFmpeg's device library
Group:          Development/Libraries/C and C++
Provides:       ffmpeg-devel = %version-%release
Conflicts:      ffmpeg-devel
Provides:       libavdevice-devel = %version-%release
Obsoletes:      libavdevice-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavfilter-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavdevice61 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavdevice-devel
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavfilter10
Summary:        FFmpeg audio and video filtering library
Group:          System/Libraries
Requires:       libavcodec61 = %version-%release
Requires:       libavformat61 = %version-%release
Requires:       libavutil59 = %version-%release
Requires:       libpostproc58 = %version-%release
Requires:       libswresample5 = %version-%release
Requires:       libswscale8 = %version-%release

%description -n libavfilter10
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

%package libavfilter-devel
Summary:        Development files for FFmpeg's audio/video filter library
Group:          Development/Libraries/C and C++
Provides:       libavfilter-devel = %version-%release
Obsoletes:      libavfilter-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavfilter10 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavfilter-devel
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

This subpackage contains the headers for FFmpeg libavfilter.

%package -n libavformat61
Summary:        FFmpeg's stream format library
Group:          System/Libraries
Requires:       libavcodec61 = %version-%release
Requires:       libavutil59 = %version-%release

%description -n libavformat61
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package libavformat-devel
Summary:        Development files for FFmpeg's stream format library
Group:          Development/Libraries/C and C++
Provides:       libavformat-devel = %version-%release
Obsoletes:      libavformat-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       libavformat61 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavformat-devel
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.

This subpackage contains the headers for FFmpeg libavformat.

%package -n libavutil59
Summary:        FFmpeg's utility library
Group:          System/Libraries

%description -n libavutil59
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

%package libavutil-devel
Summary:        Development files for FFmpeg's utility library
Group:          Development/Libraries/C and C++
Provides:       libavutil-devel = %version-%release
Obsoletes:      libavutil-devel < %version-%release
Requires:       libavutil59 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavutil-devel
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

This subpackage contains the headers for FFmpeg libavutil.

%package -n libpostproc58
Summary:        FFmpeg post-processing library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release

%description -n libpostproc58
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

%package libpostproc-devel
Summary:        Development files for the FFmpeg post-processing library
Group:          Development/Libraries/C and C++
Provides:       libpostproc-devel = %version-%release
Obsoletes:      libpostproc-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libpostproc58 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libpostproc-devel
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

This subpackage contains the headers for FFmpeg libpostproc.

%package -n libswresample5
Summary:        FFmpeg software resampling library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release

%description -n libswresample5
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

%package libswresample-devel
Summary:        Development files for the FFmpeg software resampling library
Group:          Development/Libraries/C and C++
Provides:       libswresample-devel = %version-%release
Obsoletes:      libswresample-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswresample5 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswresample-devel
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

This subpackage contains the headers for FFmpeg libswresample.

%package -n libswscale8
Summary:        FFmpeg image scaling and colorspace/pixel conversion library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release

%description -n libswscale8
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

%package libswscale-devel
Summary:        Development files for FFmpeg's image scaling and colorspace library
Group:          Development/Libraries/C and C++
Conflicts:      libswscale-devel
Provides:       libswscale-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswscale8 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswscale-devel
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

This subpackage contains the headers for FFmpeg libswscale.

%prep
%autosetup -p1 -a6 -n %_name-%version

%build
%ifarch %ix86 %arm
%define _lto_cflags %nil
%endif
%if "%_lto_cflags" != ""
%global _lto_cflags %_lto_cflags -ffat-lto-objects
%endif
CFLAGS="%optflags" \
%if 0%{?suse_version} > 1500
%ifarch %ix86
%else
LDFLAGS="%_lto_cflags" \
%endif
%endif
./configure \
	--prefix="%_prefix" \
	--libdir="%_libdir" \
	--shlibdir="%_libdir" \
	--incdir="%_includedir/ffmpeg" \
	--extra-cflags="%optflags" \
	--optflags="%optflags" \
	--disable-htmlpages \
	--enable-pic \
	--disable-stripping \
	--enable-shared \
	--disable-static \
	--enable-gpl \
	--enable-version3 \
%if %{with smbclient}
	--enable-libsmbclient \
%endif
	--disable-openssl \
	--enable-gnutls \
	--enable-ladspa \
%if %{with vulkan}
	--enable-libshaderc \
	--enable-vulkan \
	--enable-libplacebo \
%endif
%if %{with amf}
        --enable-amf \
%endif
%if !%{with cuda_sdk}
	--disable-cuda-sdk \
%endif
	--enable-libaom \
	--enable-libass \
	--enable-libbluray \
	--enable-libbs2b \
	--enable-libcdio \
%if %{with codec2}
	--enable-libcodec2 \
%endif
	--enable-libdav1d \
	--enable-libdc1394 \
	--enable-libdrm \
	--enable-libfontconfig \
	--enable-libfreetype \
	--enable-libfribidi \
	--enable-libgsm \
	--enable-libjack \
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
	--enable-libjxl \
	--enable-librist \
%endif
	--enable-libmp3lame \
%if %{with mysofa}
	--enable-libmysofa \
%endif
	--enable-libopenjpeg \
	--enable-libopenmpt \
	--enable-libopenh264-dlopen \
	--enable-libopus \
	--enable-libpulse \
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
	--enable-librav1e \
%endif
%if %{with rubberband}
	--enable-librubberband \
%endif
%ifarch x86_64 %x86_64 aarch64
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
	--enable-libsvtav1 \
%endif
%endif
	--enable-libsoxr \
	--enable-libspeex \
	--enable-libssh \
	--enable-libsrt \
	--enable-libtheora \
	--enable-libtwolame \
%if %{with vidstab}
	--enable-libvidstab \
%endif
	--enable-libvmaf \
	--enable-libvorbis \
	--enable-libvpx \
	--enable-libwebp \
	--enable-libxml2 \
	--enable-libzimg \
	--enable-libzmq \
	--enable-libzvbi \
%if 0%{?suse_version} > 1500
%ifarch %ix86
%else
	--enable-lto \
%endif
%endif
	--enable-lv2 \
%if 0%{?suse_version} < 1550 && 0%{?sle_version} >= 150200 && 0%{?sle_version} < 150600
%ifarch x86_64 %x86_64
	--enable-libmfx \
%endif
%else
%ifarch x86_64 %x86_64
	--enable-libvpl \
%endif
%endif
	--enable-vaapi \
	--enable-vdpau \
	--enable-version3 \
%if %{with fdk_aac_dlopen}
	--enable-libfdk-aac-dlopen \
	--enable-nonfree \
%endif
%if %{with opencore}
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
%endif
%if %{with amrwb}
	--enable-libvo-amrwbenc \
%endif
%if %{with x264}
	--enable-libx264 \
%endif
%if %{with x265}
	--enable-libx265 \
%endif
%if %{with xvid}
	--enable-libxvid \
%endif
%if !0%{?BUILD_ORIG}
	--enable-muxers \
	--enable-demuxers \
	--disable-encoders \
	--disable-decoders \
	--disable-decoder=h264,hevc,vc1 \
	--enable-encoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_encoders)" \
	--enable-decoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_decoders)" \

for i in H264 HEVC VC1; do
	grep -q "#define CONFIG_${i}_DECODER 0" config_components.h
done
%endif

cat config.h
%make_build

%global extratools aviocat cws2fws ffescape ffeval ffhash fourcc2pixfmt graph2dot ismindex pktdumper probetest qt-faststart seek_print sidxindex trasher

for i in %extratools; do
	%make_build "tools/$i"
done

%install
b="%buildroot"
%make_install install-man
rm -Rf "$b/%_datadir/ffmpeg/examples"
for i in %extratools; do
	cp -a "tools/$i" "$b/%_bindir/"
done

%post   -n libavcodec61 -p /sbin/ldconfig
%postun -n libavcodec61 -p /sbin/ldconfig
%post   -n libavdevice61 -p /sbin/ldconfig
%postun -n libavdevice61 -p /sbin/ldconfig
%post   -n libavfilter10 -p /sbin/ldconfig
%postun -n libavfilter10 -p /sbin/ldconfig
%post   -n libavformat61 -p /sbin/ldconfig
%postun -n libavformat61 -p /sbin/ldconfig
%post   -n libavutil59 -p /sbin/ldconfig
%postun -n libavutil59 -p /sbin/ldconfig
%post   -n libpostproc58 -p /sbin/ldconfig
%postun -n libpostproc58 -p /sbin/ldconfig
%post   -n libswresample5 -p /sbin/ldconfig
%postun -n libswresample5 -p /sbin/ldconfig
%post   -n libswscale8 -p /sbin/ldconfig
%postun -n libswscale8 -p /sbin/ldconfig

%files
%doc Changelog CREDITS README.md
%_bindir/*
%_mandir/man1/ff*.1*
%_datadir/ffmpeg/

%files -n libavcodec61
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavcodec.so.*

%files -n libavdevice61
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavdevice.so.*

%files -n libavfilter10
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavfilter.so.*

%files -n libavformat61
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavformat.so.*

%files -n libavutil59
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavutil.so.*

%files -n libpostproc58
%license COPYING.GPLv2 LICENSE.md
%_libdir/libpostproc.so.*

%files -n libswresample5
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswresample.so.*

%files -n libswscale8
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswscale.so.*

%files libavcodec-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavcodec/
%_libdir/libavcodec.so
%_libdir/pkgconfig/libavcodec.pc
%_mandir/man3/libavcodec.3*

%files libavdevice-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavdevice/
%_libdir/libavdevice.so
%_libdir/pkgconfig/libavdevice.pc
%_mandir/man3/libavdevice.3*

%files libavfilter-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavfilter/
%_libdir/libavfilter.so
%_libdir/pkgconfig/libavfilter.pc
%_mandir/man3/libavfilter.3*

%files libavformat-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavformat/
%_libdir/libavformat.so
%_libdir/pkgconfig/libavformat.pc
%_mandir/man3/libavformat.3*

%files libavutil-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavutil/
%_libdir/libavutil.so
%_libdir/pkgconfig/libavutil.pc
%_mandir/man3/libavutil.3*

%files libpostproc-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libpostproc/
%_libdir/libpostproc.so
%_libdir/pkgconfig/libpostproc.pc

%files libswresample-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libswresample/
%_libdir/libswresample.so
%_libdir/pkgconfig/libswresample.pc
%_mandir/man3/libswresample.3*

%files libswscale-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libswscale/
%_libdir/libswscale.so
%_libdir/pkgconfig/libswscale.pc
%_mandir/man3/libswscale.3*

%else
%define _name ffmpeg
Name:           ffmpeg-7-mini
Version:        7.0
Release:        0
Summary:        Set of libraries for working with various multimedia formats
License:        GPL-3.0-or-later
URL:            https://ffmpeg.org/
#Git-Clone:     git://source.ffmpeg.org/ffmpeg
Source:         https://www.ffmpeg.org/releases/%_name-%version.tar.xz
Source2:        https://www.ffmpeg.org/releases/%_name-%version.tar.xz.asc
Source3:        ffmpeg-7-rpmlintrc
Source98:       http://ffmpeg.org/ffmpeg-devel.asc#/ffmpeg-7.keyring
Patch1:         ffmpeg-arm6l.diff
Patch3:         ffmpeg-codec-choice.diff
Patch4:         ffmpeg-4.2-dlopen-fdk_aac.patch
Patch5:         work-around-abi-break.patch
Patch10:        ffmpeg-chromium.patch
Patch91:        ffmpeg-dlopen-openh264.patch
BuildRequires:  c_compiler
Requires:       this-is-only-for-build-envs

%description
FFmpeg is a multimedia framework.
This package merely builds the API for the sake of other packages.

%package libs
# Even with mini, we want ff5 libs to be coinstallable to ff4-devel(!),
# hence mini-libs and mini-devel are still separated.
Summary:        Feature-reduced build of FFmpeg, a multimedia framework
Conflicts:      libavcodec61
Conflicts:      libavdevice61
Conflicts:      libavfilter10
Conflicts:      libavformat61
Conflicts:      libavutil59
Conflicts:      libpostproc58
Conflicts:      libswresample5
Conflicts:      libswscale8
Requires:       this-is-only-for-build-envs

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
Requires:       this-is-only-for-build-envs

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
for i in H264 HEVC VC1; do
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

%endif

%changelog
