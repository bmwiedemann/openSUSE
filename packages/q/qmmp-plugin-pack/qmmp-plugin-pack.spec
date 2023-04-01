#
# spec file for package qmmp-plugin-pack
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014 Dmitry Misharov <quarckster@gmail.com>
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


%define qmmp_ver_min 2.1.0
%define qmmp_ver_max 2.1.99
%define mver    2.1
Name:           qmmp-plugin-pack
Version:        2.1.1
Release:        0
Summary:        Extra plugins for Qmmp
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://qmmp.ylsoftware.com/plugins.php
Source:         https://qmmp.ylsoftware.com/files/%{name}/%{mver}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libqmmp-plugins <= %{qmmp_ver_max}
BuildRequires:  libqmmp-plugins >= %{qmmp_ver_min}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(qmmp) <= %{qmmp_ver_max}
BuildRequires:  pkgconfig(qmmp) >= %{qmmp_ver_min}
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(taglib) >= 1.10
Requires:       qmmp <= %{qmmp_ver_max}
Requires:       qmmp >= %{qmmp_ver_min}
Obsoletes:      %{name}-history < %{version}
Obsoletes:      %{name}-mpg123 < %{version}
ExclusiveArch:  %ix86 x86_64

%description
This package contains extra plugins for Qmmp.

%package ffap
Summary:        Enhanced Monkey's Audio (APE) decoder for Qmmp
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description ffap
Enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded
CUE support).

%package ffvideo
Summary:        Video Playback Qmmp plugin
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description ffvideo
Qmmp plugin to play videos.

%package goom
Summary:        Goom visualisation Qmmp plugin
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description goom
Qmmp plugin which provides goom visualisation.

%package samplerate
Summary:        Qmmp plugin which uses libsamplerate for decoding
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description samplerate
Qmmp plugin which uses libsamplerate resampling library.

%package modplug
Summary:        Qmmp plugin which uses the libmodplug module library
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description modplug
Qmmp plugin which uses libmodplug to play module and tracker files.

%package youtube
Summary:        Qmmp plugin which uses the yt-dlp tool
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}
Requires:       yt-dlp

%description youtube
Qmmp plugin which uses yt-dlp to stream videos.

%prep
%setup -q

%build
%cmake_qt6 \
  -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
  -DLIB_DIR=%{_lib}
%qt6_build

%install
%qt6_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%dir %{_libdir}/qmmp-%{mver}/
%{_datadir}/metainfo/%{name}.appdata.xml

%files ffap
%dir %{_libdir}/qmmp-%{mver}/Input/
%{_libdir}/qmmp-%{mver}/Input/libffap.so

%files ffvideo
%dir %{_libdir}/qmmp-%{mver}/Engines/
%{_libdir}/qmmp-%{mver}/Engines/libffvideo.so

%files goom
%dir %{_libdir}/qmmp-%{mver}/Visual/
%{_libdir}/qmmp-%{mver}/Visual/libgoom.so

%files samplerate
%dir %{_libdir}/qmmp-%{mver}/Effect/
%{_libdir}/qmmp-%{mver}/Effect/libsrconverter.so

%files modplug
%dir %{_libdir}/qmmp-%{mver}/Input/
%{_libdir}/qmmp-%{mver}/Input/libmodplug.so

%files youtube
%dir %{_libdir}/qmmp-%{mver}/Transports
%{_libdir}/qmmp-%{mver}/Transports/libytb.so

%changelog
