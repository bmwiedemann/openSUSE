#
# spec file for package jacktrip
#
# Copyright (c) 2025 SUSE LLC
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


Name:           jacktrip
Version:        2.5.1
Release:        0
Summary:        Multi-machine network music performance over the Internet
License:        GPL-3.0-only AND MIT AND LGPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/jcacerec/jacktrip
Source0:        https://github.com/jcacerec/jacktrip/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PyYAML
BuildRequires:  qt6-tools-linguist
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6NetworkAuth)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6ShaderTools)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6WebEngineQuick)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(rtaudio)
BuildRequires:  pkgconfig(samplerate)

%description
JackTrip is a system used for multi-machine network performance over the
Internet. It supports any number of channels (as many as the
computer/network can handle) of bidirectional, high quality, uncompressed
audio signal streaming.

%prep
%autosetup

%build
mv build .build
%meson -Dlibsamplerate=disabled # https://github.com/jacktrip/jacktrip/issues/1380
%meson_build

%install
%meson_install

%files
%doc README.md
%{_mandir}/man*/*
%license LICENSE.md
%{_bindir}/jacktrip
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/icons/hicolor/symbolic
%dir %{_datadir}/icons/hicolor/symbolic/apps
%{_datadir}/icons/hicolor/*/apps/*

%changelog
