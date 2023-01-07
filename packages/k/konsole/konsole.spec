#
# spec file for package konsole
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

%global libsover 21
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           konsole
Version:        22.12.1
Release:        0
Summary:        KDE Terminal
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/konsole
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(icu-i18n)
%if 0%{?suse_version} <= 1500
# std::for_each_n is not available in GCC7
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
Requires:       %{name}-part = %{version}
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Konsole is a terminal emulator for the K Desktop Environment.

%package part
Summary:        KDE Terminal
Recommends:     %{name}-part-lang
Obsoletes:      konsole5-part < %{version}

%description part
Konsole is a terminal emulator for the K Desktop Environment.
This package provides KPart of the Konsole application.

%package -n %{name}-part-lang
Summary:        Translations for package %{name}
Requires:       %{name}-part = %{version}
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
Provides:       %{name}-part-lang-all = %{version}
BuildArch:      noarch

%description -n %{name}-part-lang
Provides translations for the "konsole-part" package.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

install -D -m 0644 %{SOURCE3}  "%{buildroot}%{_kf5_sharedir}/konsole/Root Shell.profile"
install -D -m 0644 %{SOURCE4}  %{buildroot}%{_kf5_applicationsdir}/
install -D -m 0644 %{SOURCE21} %{buildroot}%{_kf5_iconsdir}/hicolor/16x16/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE22} %{buildroot}%{_kf5_iconsdir}/hicolor/22x22/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE23} %{buildroot}%{_kf5_iconsdir}/hicolor/32x32/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE24} %{buildroot}%{_kf5_iconsdir}/hicolor/48x48/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE25} %{buildroot}%{_kf5_iconsdir}/hicolor/64x64/apps/utilities-terminal_su.png
install -D -m 0644 %{SOURCE26} %{buildroot}%{_kf5_iconsdir}/hicolor/128x128/apps/utilities-terminal_su.png
%suse_update_desktop_file org.kde.konsole TerminalEmulator
%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post part -p /sbin/ldconfig
%postun part -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%dir %{_kf5_plugindir}/konsoleplugins
%dir %{_kf5_sharedir}/kconf_update
%dir %{_kf5_libdir}/kconf_update_bin
%dir %{_kf5_sharedir}/kio
%dir %{_kf5_sharedir}/kio/servicemenus
%doc %lang(en) %{_kf5_htmldir}/en/konsole/
%{_kf5_applicationsdir}/konsolesu.desktop
%{_kf5_applicationsdir}/org.kde.konsole.desktop
%{_kf5_appstreamdir}/org.kde.konsole.appdata.xml
%{_kf5_bindir}/konsole
%{_kf5_bindir}/konsoleprofile
%{_kf5_iconsdir}/hicolor/*/apps/utilities-terminal_su.png
%{_kf5_knsrcfilesdir}/konsole.knsrc
%{_kf5_plugindir}/konsoleplugins/konsole_quickcommandsplugin.so
%{_kf5_plugindir}/konsoleplugins/konsole_sshmanagerplugin.so
%{_kf5_libdir}/libkonsoleapp.so.*
%{_kf5_sharedir}/kio/servicemenus/konsolerun.desktop
%{_kf5_sharedir}/kconf_update/konsole_globalaccel.upd
%{_kf5_libdir}/kconf_update_bin/konsole_globalaccel

%files part
%{_kf5_debugdir}/konsole.categories
%{_kf5_libdir}/libkonsoleprivate.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/konsolepart.so
%{_kf5_servicesdir}/konsolepart.desktop
%{_kf5_servicetypesdir}/terminalemulator.desktop
%{_kf5_sharedir}/konsole/

%files part-lang -f %{name}.lang

%changelog
