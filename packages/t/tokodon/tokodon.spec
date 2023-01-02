#
# spec file for package tokodon
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


%bcond_without released
Name:           tokodon
Version:        23.01.0
Release:        0
Summary:        Mastodon client by KDE
License:        GPL-3.0-only
URL:            https://apps.kde.org/tokodon/
Source0:        https://download.kde.org/stable/tokodon/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/tokodon/%{name}-%{version}.tar.xz.sig
# https://carlschwan.eu/gpg-02325448204e452a/
Source2:        tokodon.keyring
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5WindowSystem) >= 5.91
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kirigami2
Requires:       kitemmodels-imports
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Requires:       sonnet-imports

%description
Tokodon is a Mastodon client. It allows you to interact with the Fediverse
community.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang tokodon tokodon.lang

%files
%license LICENSES/*
%doc README.md
%{_kf5_applicationsdir}/org.kde.tokodon.desktop
%{_kf5_appstreamdir}/org.kde.tokodon.appdata.xml
%{_kf5_bindir}/tokodon
%{_kf5_debugdir}/tokodon.categories
%{_kf5_iconsdir}/hicolor/scalable/actions/tokodon-chat-reply.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.tokodon.svg
%{_kf5_notifydir}/tokodon.notifyrc

%files lang -f tokodon.lang

%changelog
