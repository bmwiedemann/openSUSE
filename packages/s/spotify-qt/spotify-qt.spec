#
# spec file for package spotify-qt
#
# Copyright (c) 2021 SUSE LLC
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


Name:           spotify-qt
Version:        3.7
Release:        0
Summary:	Lightweight Spotify client using Qt 
License:	GPL-3.0-or-later     
URL:           	https://github.com/kraxarn/spotify-qt 
Source:         https://github.com/kraxarn/spotify-qt/archive/refs/tags/v%{version}.tar.gz
Group:          Productivity/Multimedia/Sound/Players
BuildRequires:  cmake(Qt5Core)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	gcc-c++
BuildRequires:	make
Requires:       hicolor-icon-theme
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
BuildRequires:  update-desktop-files

%description
An unofficial Spotify client using Qt as a simpler, lighter alternative to the official client, inspired by spotify-tui. Much like spotify-tui, you need an actual Spotify client running, for example spotifyd, which can be configured from within the app. Also like other clients, controlling music playback requires Spotify Premium.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%post
%postun

%check
%ctest

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/scalable/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%changelog

