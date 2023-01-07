#
# spec file for package elisa
#
# Copyright (c) 2022 SUSE LLC
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


%define qt5_version 5.15.0
%define kf5_version 5.98.0
%bcond_without released
Name:           elisa
Version:        22.12.1
Release:        0
Summary:        Music player and collection organizer
License:        LGPL-3.0-or-later
URL:            https://apps.kde.org/elisa
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Baloo) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5FileMetaData) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{kf5_version}
BuildRequires:  cmake(KF5Package) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Multimedia) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickControls2) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
Requires:       kdeclarative-components >= %{kf5_version}
Requires:       kirigami2 >= %{kf5_version}
Requires:       libqt5-qtquickcontrols >= %{qt5_version}
Requires:       libqt5-qtquickcontrols2 >= %{qt5_version}

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
  %cmake_kf5 -d build
  %cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.elisa Qt KDE AudioVideo Audio Player

%files
%license COPYING*
%doc README*
%doc %lang(en) %{_kf5_htmldir}/en/elisa/
%{_kf5_applicationsdir}/org.kde.elisa.desktop
%{_kf5_appstreamdir}/org.kde.elisa.appdata.xml
%{_kf5_bindir}/elisa
%{_kf5_debugdir}/elisa.categories
%{_kf5_iconsdir}/hicolor/*/apps/elisa.*
%{_kf5_libdir}/elisa/
%{_kf5_qmldir}/org/kde/elisa/
%{_kf5_sharedir}/dbus-1/services/org.kde.elisa.service

%files lang -f %{name}.lang

%changelog
