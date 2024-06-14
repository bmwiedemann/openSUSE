#
# spec file for package elisa
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
Name:           elisa
Version:        24.05.1
Release:        0
Summary:        Music player and collection organizer
License:        LGPL-3.0-or-later
URL:            https://apps.kde.org/elisa
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTest) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
Elisa is a music player with a library where music can be browsed by
album, artist or all tracks. It is indexed using either a private
indexer or an indexer using Baloo. The private one can be configured
to scan music on chosen paths. The Baloo one is faster because Baloo
is providing all needed data from its own database. Playlists can be
built and played.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name


%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/elisa/
%{_kf6_applicationsdir}/org.kde.elisa.desktop
%{_kf6_appstreamdir}/org.kde.elisa.appdata.xml
%{_kf6_bindir}/elisa
%{_kf6_debugdir}/elisa.categories
%{_kf6_iconsdir}/hicolor/*/apps/elisa.*
%{_kf6_libdir}/elisa/
%{_kf6_sharedir}/dbus-1/services/org.kde.elisa.service

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/elisa/

%changelog
