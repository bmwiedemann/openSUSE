#
# spec file for package qmmp-plugin-pack
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define qmmp_ver_min 1.3.0
%define qmmp_ver_max 1.3.99
%define mver    1.3
Name:           qmmp-plugin-pack
Version:        1.3.0
Release:        0
Summary:        Extra plugins for Qmmp
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://qmmp.ylsoftware.com/plugins.php
Source:         http://qmmp.ylsoftware.com/files/plugins/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  libqmmp-plugins <= %{qmmp_ver_max}
BuildRequires:  libqmmp-plugins >= %{qmmp_ver_min}
BuildRequires:  libqt5-qttools-devel >= 5.4
BuildRequires:  pkgconfig
BuildRequires:  yasm
BuildRequires:  pkgconfig(Qt5Core) >= 5.4
BuildRequires:  pkgconfig(Qt5Sql) >= 5.4
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(libavcodec) >= 57.48.101
BuildRequires:  pkgconfig(libavformat) >= 57.40.101
BuildRequires:  pkgconfig(libavutil) >= 55.27.100
BuildRequires:  pkgconfig(libmpg123) >= 1.13.0
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale) >= 4.1.100
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(qmmp) <= %{qmmp_ver_max}
BuildRequires:  pkgconfig(qmmp) >= %{qmmp_ver_min}
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(taglib) >= 1.10
Requires:       qmmp <= %{qmmp_ver_max}
Requires:       qmmp >= %{qmmp_ver_min}
Obsoletes:      %{name}-history < %{version}
Obsoletes:      %{name}-mpg123 < %{version}
ExclusiveArch:  %{ix86} x86_64

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

%package xmp
Summary:        Qmmp plugin which uses the libxmp module library
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}-%{release}

%description xmp
Qmmp plugin which uses libxmp to play module and tracker files.

%prep
%setup -q

%build
%cmake \
  -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
  -DLIB_DIR=%{_lib}
%make_jobs

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%dir %{_libdir}/qmmp-%{mver}/

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

%files xmp
%dir %{_libdir}/qmmp-%{mver}/Input/
%{_libdir}/qmmp-%{mver}/Input/libxmp.so

%changelog
