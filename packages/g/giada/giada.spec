#
# spec file for package giada
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2015 Packman Team <packman@links2linux.de>
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           giada
Version:        1.1.0
Release:        0
Summary:        Sampler Audio Tool
License:        (AGPL-3.0-only OR GPL-2.0-or-later) AND GPL-3.0-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND OFL-1.1 AND Zlib
URL:            https://giadamusic.com
Source0:        %{name}-%{version}.tar.xz
Patch0:         giada-fmt.patch
Patch3:         003-cmake-exclude-juce_and_fltk-from-all.patch
%if 0%{?suse_version} <= 1560
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  cmake
BuildRequires:  fltk-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jansson) >= 2.7
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoxft)
BuildRequires:  pkgconfig(rtmidi) >= 2.1.0
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)

%description
Giada is an audio tool for DJs and live performers. Up to 32 samples
may be loaded or recorded, and may be played in single mode (drum
machine) or loop mode (sequencer). The keyboard can be used to
control this.

%prep
%autosetup -p1

%build
test -x "$(type -p g++-12)" && export CXX=g++-12 OBJCXX=g++-12
%cmake -DVSTGUI_USE_SYSTEM_EXPAT=ON -DCMAKE_BUILD_TYPE=Release -DWITH_VST3=ON -DCMAKE_CXX_FLAGS="-std=c++17 "
%cmake_build

%install
%cmake_install

%suse_update_desktop_file -c %{name} %{name} "Sampler Audio Tool" %{name} %{name} AudioVideo Audio Sequencer

%files
%doc ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/metainfo/*

%changelog
