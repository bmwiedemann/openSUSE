#
# spec file for package ffmpeg-4
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
%preamble_string libavresample-devel %comparator %conflicts_version \
%preamble_string libavutil-devel %comparator %conflicts_version \
%preamble_string libpostproc-devel %comparator %conflicts_version \
%preamble_string libswresample-devel %comparator %conflicts_version \
%preamble_string libswscale-devel %comparator %conflicts_version \
%preamble_string ffmpeg-private-devel %comparator %conflicts_version \
%nil

# nvcodec headers only present after leap15
%bcond_with nvcodec
%if 0%{?suse_version} >= 1500
%bcond_without nvcodec
%endif
%if 0%{?BUILD_ORIG}
%bcond_with    amrwb
%bcond_without cuda_sdk
%else
%bcond_with    cuda_sdk
%endif
%bcond_with    fdk_aac_dlopen
%bcond_with    librtmp
%bcond_with    opencore
%bcond_with    smbclient
%bcond_with    x264
%bcond_with    x265
%bcond_with    xvid

%if 0%{?suse_version} > 1500
%bcond_without libaom
%bcond_without mysofa
%bcond_without vidstab
%bcond_without srt
%bcond_without codec2
%bcond_without lv2
%bcond_without librav1e
%bcond_without rubberband
%bcond_without soxr
%bcond_without zmq
%bcond_without vulkan
%else
%bcond_with libaom
%bcond_with mysofa
%bcond_with vidstab
%bcond_with srt
%bcond_with codec2
%bcond_with lv2
%bcond_with librav1e
%bcond_with rubberband
%bcond_with soxr
%bcond_with zmq
%bcond_with vulkan
%endif

%if 0%{?suse_version} >= 1500
%bcond_without zimg
%bcond_without openmpt
%else
%bcond_with zimg
%bcond_with openmpt
%endif

%define _name ffmpeg
%define _major_version 4
%define _major_expected 5
Name:           ffmpeg-4
Version:        4.4.3
Release:        0
Summary:        Set of libraries for working with various multimedia formats
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://ffmpeg.org/

#Freshcode-URL:    http://freshcode.club/projects/ffmpeg
#Git-Clone:     git://source.ffmpeg.org/ffmpeg
Source:         https://www.ffmpeg.org/releases/%_name-%version.tar.xz
Source2:        https://www.ffmpeg.org/releases/%_name-%version.tar.xz.asc
Source3:        ffmpeg-4-rpmlintrc
Source4:        enable_decoders
Source5:        enable_encoders
Source98:       http://ffmpeg.org/ffmpeg-devel.asc#/ffmpeg-4.keyring
Source99:       baselibs.conf
Patch1:         ffmpeg-arm6l.diff
Patch2:         ffmpeg-new-coder-errors.diff
Patch3:         ffmpeg-codec-choice.diff
Patch4:         ffmpeg-4.2-dlopen-fdk_aac.patch
Patch5:         soversion.patch
Patch8:         vmaf-trim-usr-local.patch
Patch9:         ffmpeg-4.4-CVE-2020-22046.patch
Patch10:        ffmpeg-chromium.patch
Patch11:        ffmpeg-libglslang-detection.patch
Patch12:        ffmpeg-CVE-2022-3964.patch
BuildRequires:  ladspa-devel
BuildRequires:  libgsm-devel
BuildRequires:  libmp3lame-devel
%if %{with mysofa}
BuildRequires:  libmysofa-devel
%endif
BuildRequires:  nasm
BuildRequires:  pkg-config
%ifarch x86_64
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(SvtAv1Enc) >= 0.8.4
%endif
%endif
BuildRequires:  pkgconfig(alsa)
%if %{with libaom}
BuildRequires:  pkgconfig(aom)
%endif
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(celt) >= 0.11.0
%if %{with codec2}
BuildRequires:  pkgconfig(codec2)
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  pkgconfig(dav1d)
%endif
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(fontconfig) >= 2.4.2
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi) >= 0.19.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
%if %{with openmpt}
BuildRequires:  pkgconfig(libopenmpt)
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libraw1394)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libvmaf) >= 1.3.9
BuildRequires:  pkgconfig(libwebp) >= 0.4
BuildRequires:  pkgconfig(libxml-2.0)
%if %{with zmq}
BuildRequires:  pkgconfig(libzmq)
%endif
%if %{with lv2}
BuildRequires:  pkgconfig(lilv-0)
%endif
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
%if %{with librav1e}
BuildRequires:  pkgconfig(rav1e)
%endif
%if %{with rubberband}
BuildRequires:  pkgconfig(rubberband)
%endif
BuildRequires:  pkgconfig(sdl2)
%if %{with smbclient}
BuildRequires:  pkgconfig(smbclient)
%endif
%if %{with soxr}
BuildRequires:  pkgconfig(soxr)
%endif
BuildRequires:  pkgconfig(speex)
%if %{with srt}
BuildRequires:  pkgconfig(srt)
%endif
BuildRequires:  pkgconfig(theora) >= 1.1
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vdpau)
%if %{with vidstab}
BuildRequires:  pkgconfig(vidstab) >= 0.98
%endif
%if %{with vulkan}
BuildRequires:  c++_compiler
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(vulkan)
%endif
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
%ifarch x86_64
BuildRequires:  pkgconfig(libmfx)
%endif
%endif
%if %{with zimg}
BuildRequires:  pkgconfig(zimg)
%endif
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28
%if %{with fdk_aac_dlopen}
BuildRequires:  pkgconfig(fdk-aac)
%endif
%if %{with librtmp}
BuildRequires:  pkgconfig(librtmp)
%endif
%if %{with nvcodec}
BuildRequires:  pkgconfig(ffnvcodec)
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
Provides:       ffmpeg-tools = %version
Obsoletes:      ffmpeg-tools < %version
Provides:       ffmpeg = %version
Obsoletes:      ffmpeg < %version
Conflicts:      ffmpeg-5
Requires:       libavcodec58_134 = %version-%release
Requires:       libavdevice58_13 = %version-%release
Requires:       libavfilter7_110 = %version-%release
Requires:       libavformat58_76 = %version-%release
Requires:       libavresample4_0 = %version-%release
Requires:       libavutil56_70 = %version-%release
Requires:       libpostproc55_9 = %version-%release
Requires:       libswresample3_9 = %version-%release
Requires:       libswscale5_9 = %version-%release

%description
FFmpeg is a multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play several formats
that humans and machines have created.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package -n libavcodec58_134
Summary:        FFmpeg codec library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release
Requires:       libswresample3_9 = %version-%release
%if 0%{?BUILD_ORIG}
Provides:       libavcodec-full = %version-%release
# This can be (and is) required by packages like vlc-codecs -
# do follow the shlib name to not get random lib providers
Provides:       libavcodec58_134(unrestricted)
%endif
# For mozillas
Provides:       libavcodec = %version-%release

%description -n libavcodec58_134
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
Requires:       %name-libavresample-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libavcodec58_134 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavcodec-devel
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavdevice58_13
Summary:        FFmpeg device library
Group:          System/Libraries
Requires:       libavcodec58_134 = %version-%release
Requires:       libavfilter7_110 = %version-%release
Requires:       libavformat58_76 = %version-%release
Requires:       libavutil56_70 = %version-%release

%description -n libavdevice58_13
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
Requires:       %name-libavresample-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavdevice58_13 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavdevice-devel
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavfilter7_110
Summary:        FFmpeg audio and video filtering library
Group:          System/Libraries
Requires:       libavcodec58_134 = %version-%release
Requires:       libavformat58_76 = %version-%release
Requires:       libavresample4_0 = %version-%release
Requires:       libavutil56_70 = %version-%release
Requires:       libpostproc55_9 = %version-%release
Requires:       libswresample3_9 = %version-%release
Requires:       libswscale5_9 = %version-%release

%description -n libavfilter7_110
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

%package libavfilter-devel
Summary:        Development files for FFmpeg's audio/video filter library
Group:          Development/Libraries/C and C++
Provides:       libavfilter-devel = %version-%release
Obsoletes:      libavfilter-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavresample-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavfilter7_110 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavfilter-devel
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

This subpackage contains the headers for FFmpeg libavfilter.

%package -n libavformat58_76
Summary:        FFmpeg's stream format library
Group:          System/Libraries
Requires:       libavcodec58_134 = %version-%release
Requires:       libavutil56_70 = %version-%release

%description -n libavformat58_76
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
Requires:       libavformat58_76 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavformat-devel
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.

This subpackage contains the headers for FFmpeg libavformat.

%package -n libavresample4_0
Summary:        FFmpeg alternate audio resampling library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release
Obsoletes:      libavresample4 < %version-%release
Provides:       libavresample4 = %version-%release

%description -n libavresample4_0
An audio resampling library that is being provided for drop-in
compatibility with libav.

It is advised to use libswresample for new code.

%package libavresample-devel
Summary:        Development files for libavresample as present in FFmpeg
Group:          Development/Libraries/C and C++
Provides:       libavresample-devel = %version-%release
Obsoletes:      libavresample-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libavresample4_0 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavresample-devel
An audio resampling library that is being provided for drop-in
compatibility with libav.

It is advised to use libswresample for new code.

This subpackage contains the headers for FFmpeg's copy of libavresample.

%package -n libavutil56_70
Summary:        FFmpeg's utility library
Group:          System/Libraries

%description -n libavutil56_70
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
Requires:       libavutil56_70 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavutil-devel
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

This subpackage contains the headers for FFmpeg libavutil.

%package -n libpostproc55_9
Summary:        FFmpeg post-processing library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release

%description -n libpostproc55_9
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

%package libpostproc-devel
Summary:        Development files for the FFmpeg post-processing library
Group:          Development/Libraries/C and C++
Provides:       libpostproc-devel = %version-%release
Obsoletes:      libpostproc-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libpostproc55_9 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libpostproc-devel
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

This subpackage contains the headers for FFmpeg libpostproc.

%package -n libswresample3_9
Summary:        FFmpeg software resampling library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release

%description -n libswresample3_9
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

%package libswresample-devel
Summary:        Development files for the FFmpeg software resampling library
Group:          Development/Libraries/C and C++
Provides:       libswresample-devel = %version-%release
Obsoletes:      libswresample-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswresample3_9 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswresample-devel
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

This subpackage contains the headers for FFmpeg libswresample.

%package -n libswscale5_9
Summary:        FFmpeg image scaling and colorspace/pixel conversion library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release

%description -n libswscale5_9
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

%package libswscale-devel
Summary:        Development files for FFmpeg's image scaling and colorspace library
Group:          Development/Libraries/C and C++
Provides:       libswscale-devel = %version-%release
Conflicts:      libswscale-devel
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswscale5_9 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswscale-devel
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

This subpackage contains the headers for FFmpeg libswscale.

%package private-devel
Summary:        Some FFmpeg private headers
Group:          Development/Libraries/C and C++
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Provides:       ffmpeg-private-devel = %version
Obsoletes:      ffmpeg-private-devel < %version
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description private-devel
FFmpeg is a multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play several formats
that humans and machines have created.

This package contains some private headers for libavformat, libavcodec and
libavutil which are needed by libav-tools to build. No other package apart
from libav should depend on these private headers which are expected to
break compatibility without any notice.

%prep
%autosetup -p1 -n %_name-%version

%build
%ifarch %ix86 %arm
%define _lto_cflags %nil
%endif
%if "%_lto_cflags" != ""
%global _lto_cflags %_lto_cflags -ffat-lto-objects
%endif
CFLAGS="%optflags" \
%if %suse_version > 1500
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
	--enable-avresample \
	--enable-gnutls \
	--enable-ladspa \
%if %{with vulkan}
	--enable-vulkan \
	--enable-libglslang \
%endif
%if ! %{with cuda_sdk}
	--disable-cuda-sdk \
%endif
%if %{with libaom}
	--enable-libaom \
%endif
	--enable-libass \
	--enable-libbluray \
	--enable-libbs2b \
	--enable-libcelt \
	--enable-libcdio \
%if %{with codec2}
	--enable-libcodec2 \
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
	--enable-libdav1d \
%endif
	--enable-libdc1394 \
	--enable-libdrm \
	--enable-libfontconfig \
	--enable-libfreetype \
	--enable-libfribidi \
	--enable-libgsm \
	--enable-libjack \
	--enable-libmp3lame \
%if %{with mysofa}
	--enable-libmysofa \
%endif
	--enable-libopenjpeg \
%if %{with openmpt}
	--enable-libopenmpt \
%endif
	--enable-libopus \
	--enable-libpulse \
%if %{with librav1e}
	--enable-librav1e \
%endif
%if %{with rubberband}
	--enable-librubberband \
%endif
%ifarch x86_64
%if 0%{?suse_version} >= 1550
	--enable-libsvtav1 \
%endif
%endif
%if %{with soxr}
	--enable-libsoxr \
%endif
	--enable-libspeex \
	--enable-libssh \
%if %{with srt}
	--enable-libsrt \
%endif
	--enable-libtheora \
	--enable-libtwolame \
%if %{with vidstab}
	--enable-libvidstab \
%endif
	--enable-libvmaf \
	--enable-libvorbis \
	--enable-libv4l2 \
	--enable-libvpx \
	--enable-libwebp \
	--enable-libxml2 \
%if %{with zimg}
	--enable-libzimg \
%endif
%if %{with zmq}
	--enable-libzmq \
%endif
	--enable-libzvbi \
%if 0%{?suse_version} > 1500
%ifarch %ix86
%else
  --enable-lto \
%endif
%endif
%if %{with lv2}
	--enable-lv2 \
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
%ifarch x86_64
	--enable-libmfx \
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
%if %{with librtmp}
	--enable-librtmp \
%endif
%if %{with xvid}
	--enable-libxvid \
%endif
%if !0%{?BUILD_ORIG}
	--enable-muxers \
	--enable-demuxers \
	--disable-encoders \
	--disable-decoders \
	--disable-decoder=mpeg4,h263,h264,hevc,vc1 \
	--enable-encoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_encoders)" \
	--enable-decoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_decoders)" \

for i in MPEG4 H263 H264 HEVC VC1; do
	grep -q "#define CONFIG_${i}_DECODER 0" config.h
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

# Install private headers required by libav-tools
for i in libavformat/options_table.h libavformat/os_support.h \
  libavformat/internal.h libavcodec/options_table.h libavutil/libm.h \
  libavutil/internal.h libavutil/colorspace.h libavutil/timer.h \
  libavutil/x86/emms.h libavutil/aarch64/timer.h libavutil/arm/timer.h \
  libavutil/bfin/timer.h libavutil/ppc/timer.h libavutil/x86/timer.h; do
	mkdir -p "$b/%_includedir/ffmpeg/private/"`dirname $i`
	cp -a $i "$b/%_includedir/ffmpeg/private/$i"
done

%post   -n libavcodec58_134 -p /sbin/ldconfig
%postun -n libavcodec58_134 -p /sbin/ldconfig
%post   -n libavdevice58_13 -p /sbin/ldconfig
%postun -n libavdevice58_13 -p /sbin/ldconfig
%post   -n libavfilter7_110 -p /sbin/ldconfig
%postun -n libavfilter7_110 -p /sbin/ldconfig
%post   -n libavformat58_76 -p /sbin/ldconfig
%postun -n libavformat58_76 -p /sbin/ldconfig
%post   -n libavresample4_0 -p /sbin/ldconfig
%postun -n libavresample4_0 -p /sbin/ldconfig
%post   -n libavutil56_70 -p /sbin/ldconfig
%postun -n libavutil56_70 -p /sbin/ldconfig
%post   -n libpostproc55_9 -p /sbin/ldconfig
%postun -n libpostproc55_9 -p /sbin/ldconfig
%post   -n libswresample3_9 -p /sbin/ldconfig
%postun -n libswresample3_9 -p /sbin/ldconfig
%post   -n libswscale5_9 -p /sbin/ldconfig
%postun -n libswscale5_9 -p /sbin/ldconfig

%files
%doc Changelog CREDITS README.md
%_bindir/aviocat
%_bindir/cws2fws
%_bindir/ffescape
%_bindir/ffeval
%_bindir/ffhash
%_bindir/ffmpeg
%_bindir/ffplay
%_bindir/ffprobe
%_bindir/fourcc2pixfmt
%_bindir/graph2dot
%_bindir/ismindex
%_bindir/pktdumper
%_bindir/probetest
%_bindir/qt-faststart
%_bindir/seek_print
%_bindir/sidxindex
%_bindir/trasher
%_mandir/man1/ff*.1*
%_datadir/ffmpeg/
%_libdir/libavcodec.so.58
%_libdir/libavdevice.so.58
%_libdir/libavfilter.so.7
%_libdir/libavformat.so.58
%_libdir/libavresample.so.4
%_libdir/libavutil.so.56
%_libdir/libpostproc.so.55
%_libdir/libswresample.so.3
%_libdir/libswscale.so.5

%files -n libavcodec58_134
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavcodec.so.58.134*

%files -n libavdevice58_13
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavdevice.so.58.13*

%files -n libavfilter7_110
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavfilter.so.7.110*

%files -n libavformat58_76
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavformat.so.58.76*

%files -n libavresample4_0
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavresample.so.4.0*

%files -n libavutil56_70
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavutil.so.56.70*

%files -n libpostproc55_9
%license COPYING.GPLv2 LICENSE.md
%_libdir/libpostproc.so.55.9*

%files -n libswresample3_9
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswresample.so.3.9*

%files -n libswscale5_9
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswscale.so.5.9*

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

%files libavresample-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavresample/
%_libdir/libavresample.so
%_libdir/pkgconfig/libavresample.pc

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

%files private-devel
%_includedir/ffmpeg/private/

%changelog
