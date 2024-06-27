#
# spec file for package plasma6-sdk
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-sdk
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-sdk
Version:        6.1.1
Release:        0
Summary:        Plasma SDK
License:        GPL-2.0-only AND LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       bash
Requires:       kf6-kirigami-imports >= %{kf6_version}
Provides:       plasmaengineexplorer5 = %{version}
Obsoletes:      plasmaengineexplorer5 < %{version}
Provides:       plasmaengineexplorer6 = %{version}
Obsoletes:      plasmaengineexplorer6 < %{version}
Provides:       plasma5-sdk = %{version}
Obsoletes:      plasma5-sdk < %{version}
Obsoletes:      plasma5-sdk-lang < %{version}
Conflicts:      plasmate

%description
Plasma SDK taylored for development of Plasma components,
such as Widgets, Runners, Dataengines.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

mkdir -p %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/
cp -L %{_kf6_iconsdir}/breeze/apps/22/plasma-symbolic.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/plasma.svg
cp -L %{_kf6_iconsdir}/breeze/apps/48/cuttlefish.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/
cp -L %{_kf6_iconsdir}/breeze/actions/22/tools-wizard.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/

%find_lang %{name} --all-name --with-man

%files
%license LICENSES/*
%{_kf6_bindir}/iconexplorer
%{_kf6_bindir}/plasmaengineexplorer
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_kqml
%{_datadir}/zsh/site-functions/_plasmoidviewer
%{_kf6_applicationsdir}/org.kde.iconexplorer.desktop
%{_kf6_applicationsdir}/org.kde.plasma.themeexplorer.desktop
%{_kf6_applicationsdir}/org.kde.plasmaengineexplorer.desktop
%{_kf6_applicationsdir}/org.kde.plasmoidviewer.desktop
%{_kf6_appstreamdir}/org.kde.plasma.iconexplorer.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.lookandfeelexplorer.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.plasmoidviewershell.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.themeexplorer.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasmaengineexplorer.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasmoidviewer.appdata.xml
%{_kf6_bindir}/kqml
%{_kf6_bindir}/lookandfeelexplorer
%{_kf6_bindir}/plasmathemeexplorer
%{_kf6_bindir}/plasmoidviewer
%{_kf6_iconsdir}/*/*/*/*.*
%dir %{_kf6_plasmadir}/shells
%{_kf6_plasmadir}/shells/org.kde.plasma.plasmoidviewershell/
%dir %{_kf6_plugindir}/ktexteditor
%{_kf6_plugindir}/ktexteditor/iconexplorerplugin.so
%dir %{_kf6_sharedir}/kpackage/
%dir %{_kf6_sharedir}/kpackage/genericqml
%{_kf6_sharedir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/
%{_kf6_sharedir}/kpackage/genericqml/org.kde.plasma.themeexplorer/
%{_mandir}/man1/kqml.1%{?ext_man}
%{_mandir}/man1/plasmaengineexplorer.1%{?ext_man}
%{_mandir}/man1/plasmoidviewer.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
