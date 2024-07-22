#
# spec file for package audiotube
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           audiotube
Version:        24.05.2
Release:        0
Summary:        YT Music player and playlists manager
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/audiotube/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Temporary: SR#1188363
BuildRequires:  python3-devel
BuildRequires:  python3-ytmusicapi
# ffmpeg and ffmpeg-mini-libs can be out of sync, leading to unresolvable conflicts
#!BuildIgnore: ffmpeg
BuildRequires:  python3-yt-dlp
BuildRequires:  cmake(FutureSQL6)
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core) >= 0.10.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(pybind11)
# audio/mpeg decoder is needed
Requires:       gstreamer-plugins-bad
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-purpose >= %{kf6_version}
Requires:       kirigami-addons6 >= 0.11
Requires:       python3-ytmusicapi
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}
Requires:       yt-dlp

%description
AudioTube can search YouTube Music, list albums and artists, play automatically
generated playlists, albums and allows to put your own playlist together. It is
adapted to mobile phones and desktop computers.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.audiotube.desktop
%{_kf6_appstreamdir}/org.kde.audiotube.appdata.xml
%{_kf6_bindir}/audiotube
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.audiotube.svg

%files lang -f %{name}.lang

%changelog
