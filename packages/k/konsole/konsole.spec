#
# spec file for package konsole
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
Name:           konsole
Version:        24.05.1
Release:        0
Summary:        KDE Terminal
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/konsole
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        Root_Shell.profile
Source4:        konsolesu.desktop
Source21:       utilities-terminal-su-16.png
Source22:       utilities-terminal-su-22.png
Source23:       utilities-terminal-su-32.png
Source24:       utilities-terminal-su-48.png
Source25:       utilities-terminal-su-64.png
Source26:       utilities-terminal-su-128.png
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Pty) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(icu-i18n) >= 61.0
BuildRequires:  pkgconfig(icu-uc) >= 61.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
Requires:       konsole-part = %{version}
Obsoletes:      konsole5 < %{version}
Provides:       konsole5 = %{version}

%description
Konsole is a terminal emulator for the K Desktop Environment.

%package part
Summary:        KDE Terminal
Recommends:     konsole-part-lang
Obsoletes:      konsole5-part < %{version}

%description part
Konsole is a terminal emulator for the K Desktop Environment.
This package provides KPart of the Konsole application.

%package -n konsole-part-lang
Summary:        Translations for package konsole
Requires:       konsole-part = %{version}
Provides:       konsole-lang = %{version}
Obsoletes:      konsole-lang < %{version}
Provides:       konsole-part-lang-all = %{version}
BuildArch:      noarch

%description -n konsole-part-lang
Provides translations for the "konsole-part" package.

%package zsh-completion
Summary:        ZSH completion for konsole
Requires:       konsole = %{version}
Supplements:    (konsole and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for konsole.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

install -D -m 0644 %{SOURCE3}  "%{buildroot}%{_kf6_sharedir}/konsole/Root Shell.profile"
install -D -m 0644 %{SOURCE4}  %{buildroot}%{_kf6_applicationsdir}/
install -D -m 0644 %{SOURCE21} %{buildroot}%{_kf6_iconsdir}/hicolor/16x16/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE22} %{buildroot}%{_kf6_iconsdir}/hicolor/22x22/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE23} %{buildroot}%{_kf6_iconsdir}/hicolor/32x32/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE24} %{buildroot}%{_kf6_iconsdir}/hicolor/48x48/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE25} %{buildroot}%{_kf6_iconsdir}/hicolor/64x64/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE26} %{buildroot}%{_kf6_iconsdir}/hicolor/128x128/apps/utilities-terminal_su.png

%fdupes -s %{buildroot}

%ldconfig_scriptlets
%ldconfig_scriptlets part

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/konsole/
%{_kf6_applicationsdir}/konsolesu.desktop
%{_kf6_applicationsdir}/org.kde.konsole.desktop
%{_kf6_appstreamdir}/org.kde.konsole.appdata.xml
%{_kf6_bindir}/konsole
%{_kf6_bindir}/konsoleprofile
%{_kf6_configdir}/konsolerc
%{_kf6_iconsdir}/hicolor/*/apps/utilities-terminal_su.png
%{_kf6_knsrcfilesdir}/konsole.knsrc
%dir %{_kf6_plugindir}/konsoleplugins
%{_kf6_plugindir}/konsoleplugins/konsole_quickcommandsplugin.so
%{_kf6_plugindir}/konsoleplugins/konsole_sshmanagerplugin.so
%{_kf6_libdir}/libkonsoleapp.so.*
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/konsolerun.desktop
%{_kf6_sharedir}/kglobalaccel/org.kde.konsole.desktop
%{_kf6_libdir}/kconf_update_bin/konsole_globalaccel
%{_kf6_libdir}/kconf_update_bin/konsole_show_menubar
%{_kf6_sharedir}/kconf_update/konsole.upd
%{_kf6_sharedir}/kconf_update/konsole_add_hamburgermenu_to_toolbar.sh

%files part
%{_kf6_debugdir}/konsole.categories
%{_kf6_libdir}/libkonsoleprivate.so.*
%{_kf6_notificationsdir}/konsole.notifyrc
%dir %{_kf6_plugindir}/kf6/parts
%{_kf6_plugindir}/kf6/parts/konsolepart.so
%{_kf6_sharedir}/konsole/

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_konsole

%files part-lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/konsole/

%changelog
