#
# spec file for package kgpg
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
%define qt6_version 6.4.0

%bcond_without released
Name:           kgpg
Version:        24.02.2
Release:        0
Summary:        Encryption Tool
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kgpg
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch0:         kgpg-autostart.diff
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libgpgme-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
Requires:       gpg2

%description
Kgpg is a simple GUI for gpg

%lang_package

%prep
%autosetup -p0

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%files
%license LICENSES/*
%doc AUTHORS
%config %{_kf6_configdir}/autostart/org.kde.kgpg.desktop
%doc %lang(en) %{_kf6_htmldir}/en/kgpg/
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_applicationsdir}/org.kde.kgpg.desktop
%{_kf6_appstreamdir}/org.kde.kgpg.appdata.xml
%{_kf6_bindir}/kgpg
%{_kf6_configkcfgdir}/kgpg.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.kgpg.Key.xml
%{_kf6_debugdir}/kgpg.categories
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_sharedir}/kio/servicemenus/kgpg_encryptfile.desktop
%{_kf6_sharedir}/kio/servicemenus/kgpg_encryptfolder.desktop
%{_kf6_sharedir}/kio/servicemenus/kgpg_viewdecrypted.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kgpg/

%changelog
