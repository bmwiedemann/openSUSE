#
# spec file for package kdesvn
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.0
%define qt6_version 6.5.0

Name:           kdesvn
Version:        2.1.0git.20260824T015138~94bd2ad8
Release:        0
Summary:        KDE Subversion Client
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kdesvn
Source:         kdesvn-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  subversion-devel
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
# needed for the database
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
kdesvn is a GUI client for subversion repositories.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-man --with-html

%fdupes %{buildroot}%{_kf6_sharedir}

%files -f %{name}.lang
%license COPYING COPYING.OpenSSL
%doc AUTHORS ChangeLog
%doc %lang(en) %{_kf6_htmldir}/en/kdesvn/
%doc %lang(en) %{_kf6_mandir}/man1/kdesvn.1%{?ext_man}
%doc %lang(en) %{_kf6_mandir}/man1/kdesvnaskpass.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.kdesvn.desktop
%{_kf6_appstreamdir}/org.kde.kdesvn.appdata.xml
%{_kf6_bindir}/kdesvn
%{_kf6_bindir}/kdesvnaskpass
%{_kf6_configkcfgdir}/kdesvn_part.kcfg
%{_kf6_dbusinterfacesdir}/kf6_org.kde.kdesvnd.xml
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_plugindir}/kf6/kded/kdesvnd.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/ksvn_fileitemactions.so
%{_kf6_plugindir}/kf6/kio/kio_ksvn.so
%{_kf6_plugindir}/kf6/parts/kdesvnpart.so
%{_kf6_sharedir}/dbus-1/services/org.kde.kdesvnd.service
%{_kf6_sharedir}/kdesvn/

%changelog
