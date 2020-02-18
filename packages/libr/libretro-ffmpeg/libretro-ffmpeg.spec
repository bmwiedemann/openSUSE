#
# spec file for package libretro-ffmpeg
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


Name:           libretro-ffmpeg
Version:        0~git20191123
Release:        0
Summary:        FFmpeg libretro core
License:        GPL-3.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)

%description
FFmpeg is a collection of libraries and tools to process multimedia content such
as audio, video, subtitles and related metadata.

This package is for RetroArch/Libretro front-end.

%prep
%setup -q
sed -i "s/UPSTREAM_VERSION GIT_VERSION/\"%{version}\"/g" libretro/ffmpeg_core.c

%build
cd libretro
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp libretro/ffmpeg_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/ffmpeg_libretro.so

%changelog
