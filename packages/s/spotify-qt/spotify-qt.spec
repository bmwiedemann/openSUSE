#
# spec file for package spotify-qt
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


Name:           spotify-qt
Version:        3.12
Release:        0
Summary:        Lightweight Spotify client using Qt
License:        GPL-3.0-only
URL:            https://github.com/kraxarn/spotify-qt
Source:         https://github.com/kraxarn/spotify-qt/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Group:          Productivity/Multimedia/Sound/Players
BuildRequires:  gcc-c++
BuildRequires:  libsecret
BuildRequires:  make
%if 0%{?suse_version} >= 1600 && 0%{?is_opensuse}
BuildRequires:  kf6-kcrash-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
%endif
Suggests:       libsecret
%if 0%{?suse_version} >= 1600 && 0%{?is_opensuse}
Suggests:       librespot
%endif

%description
An unofficial Spotify client using Qt as a simpler, lighter alternative to the official client, inspired by spotify-tui. Much like spotify-tui, you need an actual Spotify client running, for example spotifyd, which can be configured from within the app. Also like other clients, controlling music playback requires Spotify Premium.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license license
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/scalable/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
