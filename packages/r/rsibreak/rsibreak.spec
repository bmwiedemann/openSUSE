#
# spec file for package rsibreak
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


%define kf6_version 6.8
%define qt6_version 6.7.0

%define base_ver 0.13
%bcond_without released
Name:           rsibreak
Version:        0.13.0
Release:        0
Summary:        Repetetive Strain Injury recovery and prevention assistance utility
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/rsibreak
Source0:        https://download.kde.org/stable/rsibreak/%{base_ver}/rsibreak-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/rsibreak/%{base_ver}/rsibreak-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/aacid@key1.asc
Source2:        rsibreak.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
Requires:       hicolor-icon-theme
Recommends:     rsibreak-lang = %{version}
Obsoletes:      rsibreak-doc < %{version}

%description
Repetitive Strain Injury is an illness which can occur as a result of
working with a mouse and keyboard. This utility can be used to remind
you to take a break now and then.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%files
%license LICENSES/*
%doc AUTHORS ChangeLog NEWS
%doc %lang(en) %{_kf6_htmldir}/en/
%{_kf6_applicationsdir}/org.kde.rsibreak.desktop
%{_kf6_appstreamdir}/org.kde.rsibreak.appdata.xml
%{_kf6_bindir}/rsibreak
%{_kf6_configdir}/autostart/rsibreak_autostart.desktop
%{_kf6_dbusinterfacesdir}/org.rsibreak.rsiwidget.xml
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_notificationsdir}/rsibreak.notifyrc

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
