#
# spec file for package konversation
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
Name:           konversation
Version:        24.05.1
Release:        0
Summary:        A graphical IRC client by KDE
License:        GPL-2.0-or-later
URL:            https://konversation.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# To get the path to qdbus
BuildRequires:  qt6-tools-qdbus
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qca-qt6) >= 2.2.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Tools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# Only used by some very old scripts, no need to recommend it
Suggests:       qt6-tools-qdbus

%description
Konversation is an Internet Relay Chat (IRC) client built on the
KDE Platform.

Features:
* SSL server support
* Bookmarking support
* Multiple servers and channels in one single window
* DCC file transfer
* Multiple identities for different servers
* Text decorations and colors
* OnScreen Display for notifications
* Automatic UTF-8 detection
* Per channel encoding support
* Theme support for nick icons

%lang_package

%prep
%autosetup -p1

# search&replace not covered by %%patch0
sed -i 's#qdbus#qdbus6#' {doc,po/*/docs/konversation}/index.docbook

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html

%files
%license LICENSES/*
%doc AUTHORS ChangeLog NEWS README
%doc %{_kf6_htmldir}/en/konversation/
%{_kf6_applicationsdir}/org.kde.konversation.desktop
%{_kf6_appstreamdir}/org.kde.konversation.appdata.xml
%{_kf6_bindir}/konversation
%{_kf6_debugdir}/konversation.categories
%{_kf6_iconsdir}/hicolor/*/actions/konv_message.*
%{_kf6_iconsdir}/hicolor/*/apps/konversation.*
%{_kf6_knsrcfilesdir}/konversation_nicklist_theme.knsrc
%{_kf6_notificationsdir}/konversation.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.kde.konversation.service
%{_kf6_sharedir}/konversation/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/konversation

%changelog
