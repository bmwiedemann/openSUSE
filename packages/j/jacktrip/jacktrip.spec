#
# spec file for package jacktrip
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.6.8
Release:        0
Summary:        Multi-machine network music performance over the Internet
License:        MIT
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/jcacerec/jacktrip
Source:         https://github.com/jcacerec/jacktrip/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libqt5-linguist
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PyYAML
BuildRequires:  rtaudio-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5NetworkAuth)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)

%description
JackTrip is a system used for multi-machine network performance over the
Internet. It supports any number of channels (as many as the
computer/network can handle) of bidirectional, high quality, uncompressed
audio signal streaming.

%prep
%setup -q

%build
mv build .build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE.md
%{_bindir}/jacktrip
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/icons/hicolor/symbolic
%dir %{_datadir}/icons/hicolor/symbolic/apps
%{_datadir}/icons/hicolor/*/apps/*

%changelog
