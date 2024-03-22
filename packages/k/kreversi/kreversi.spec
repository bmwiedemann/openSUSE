#
# spec file for package kreversi
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


# Internal QML import
%global __requires_exclude qt6qmlimport\\(ColorScheme.*

%define kf6_version 5.246.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kreversi
Version:        24.02.1
Release:        0
Summary:        Reversi board game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kreversi
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kreversi5 < %{version}
Provides:       kreversi5 = %{version}

%description
KReversi is a board game game where two players have to gain the
majority of pieces on the board. This is done by tactically placing
ones pieces to turn over the opponents pieces.

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
%doc %lang(en) %{_kf6_htmldir}/en/kreversi/
%{_kf6_applicationsdir}/org.kde.kreversi.desktop
%{_kf6_appstreamdir}/org.kde.kreversi.appdata.xml
%{_kf6_bindir}/kreversi
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_notificationsdir}/kreversi.notifyrc
%{_kf6_sharedir}/kreversi/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kreversi/

%changelog
