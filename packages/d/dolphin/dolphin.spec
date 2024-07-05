#
# spec file for package dolphin
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
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           dolphin
Version:        24.05.2
Release:        0
Summary:        KDE File Manager
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/dolphin
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        dolphinsu.desktop
Patch0:         dolphin-go_up.diff
# PATCH-FIX-OPENSUSE
Patch1:         0001-Revert-Disallow-executing-Dolphin-as-root-on-Linux.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6BalooWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6)
Requires:       dolphin-part = %{version}-%{release}
Requires:       kf6-baloo-kioslaves >= %{kf6_version}
Recommends:     kio-extras6
Recommends:     konsole-part
Obsoletes:      dolphin5

%description
This package contains the default file manager of KDE Workspaces.

%package part
Summary:        KDE File Manager
Obsoletes:      dolphin5-part
%if %{with released}
%requires_ge    kf6-kio
%endif

%description part
This package contains the libraries used by Dolphin and Konqueror.

%package -n libdolphinvcs6
Summary:        KDE File Manager

%description -n libdolphinvcs6
This package contains the libraries used by Dolphin and Konqueror.

%package devel
Summary:        KDE File Manager
Requires:       libdolphinvcs6 = %{version}
Obsoletes:      dolphin5-devel < %{version}
Provides:       dolphin5-devel = %{version}

%description devel
This package contains the libraries used by Dolphin and Konqueror.

%package zsh-completion
Summary:        ZSH completion for dolphin
Requires:       dolphin = %{version}
Supplements:    (dolphin and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for dolphin.

%package -n dolphin-part-lang
Summary:        Translations for package dolphin
Requires:       dolphin-part = %{version}
Supplements:    (bundle-lang-other and dolphin-part)
Provides:       dolphin-lang = %{version}
Obsoletes:      dolphin-lang < %{version}
Provides:       dolphin-part-lang-all = %{version}
BuildArch:      noarch

%description -n dolphin-part-lang
Provides translations for the dolphin package.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-man --with-html

install -D -m 0644 %{SOURCE3} %{buildroot}%{_kf6_applicationsdir}/org.kde.dolphinsu.desktop

%ldconfig_scriptlets
%ldconfig_scriptlets -n libdolphinvcs6
%ldconfig_scriptlets part

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/dolphin/
%{_kf6_applicationsdir}/org.kde.dolphin.desktop
%{_kf6_applicationsdir}/org.kde.dolphinsu.desktop
%{_kf6_appstreamdir}/org.kde.dolphin.appdata.xml
%{_kf6_bindir}/dolphin
%{_kf6_bindir}/servicemenuinstaller
%{_kf6_configkcfgdir}/dolphin_*.kcfg
%{_kf6_dbusinterfacesdir}/org.freedesktop.FileManager1.xml
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.dolphin.svg
%{_kf6_sharedir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%{_kf6_sharedir}/kconf_update/dolphin_detailsmodesettings.upd
%{_kf6_sharedir}/kconf_update/dolphin_directorysizemode.py
%{_kf6_sharedir}/kconf_update/dolphin_directorysizemode.upd

%dir %{_kf6_sharedir}/kglobalaccel
%{_kf6_sharedir}/kglobalaccel/org.kde.dolphin.desktop
%{_userunitdir}/plasma-dolphin.service

%files part
%{_kf6_debugdir}/dolphin.categories
%{_kf6_knsrcfilesdir}/servicemenu.knsrc
%{_kf6_libdir}/libdolphinprivate.so.*
%dir %{_kf6_plugindir}/dolphin
%dir %{_kf6_plugindir}/dolphin/kcms
%{_kf6_plugindir}/dolphin/kcms/kcm_dolphin*.so
%{_kf6_plugindir}/kf6/parts/dolphinpart.so
%dir %{_kf6_sharedir}/dolphin
%{_kf6_sharedir}/dolphin/dolphinpartactions.desktop

%files -n libdolphinvcs6
%{_kf6_libdir}/libdolphinvcs.so.*

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_dolphin

%files devel
%{_includedir}/Dolphin/
%{_includedir}/dolphin_export.h
%{_includedir}/dolphinvcs_export.h
%{_kf6_cmakedir}/DolphinVcs/
%{_kf6_libdir}/libdolphinvcs.so

%files part-lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/dolphin/

%changelog
