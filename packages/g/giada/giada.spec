#
# spec file for package giada
#
# Copyright (c) 2022 SUSE LLC
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
Version:        0.23.2
Release:        0
Summary:        Sampler Audio Tool
License:        GPL-3.0-or-later
URL:            https://giadamusic.com
Source0:        %{name}-%{version}.tar.xz
Patch0:         003-cmake-exclude-juce-from-all.patch
BuildRequires:  cmake
BuildRequires:  fltk-devel
%if 0%{?suse_version} < 1550
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jansson) >= 2.7
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(rtmidi) >= 2.1.0
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
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
test -x "$(type -p g++-10)" && export CXX=g++-10 OBJCXX=g++-10
%cmake -DCMAKE_BUILD_TYPE=Release -DWITH_VST3=ON
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
