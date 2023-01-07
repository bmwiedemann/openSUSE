#
# spec file for package spectacle
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


%define kf5_version 5.90.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           spectacle
Version:        22.12.1
Release:        0
Summary:        Screen Capture Program
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://apps.kde.org/spectacle
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kipi)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Screen)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(kColorPicker)
BuildRequires:  cmake(kImageAnnotator)
Obsoletes:      kscreengenie < %{version}
Provides:       kscreengenie = %{version}
# Upstream changed name twice (kscreengenie - kapture - spectacle)
Obsoletes:      kapture < %{version}
Provides:       kapture = %{version}

%description
Spectactle is a screenshot-taking program made by KDE. It allows taking screenshots
of screens, windows, regions of the screen, and to export them to files or other
online services.

%package doc
Summary:        Documentation for Spectacle
Requires:       %{name}

%description doc
This package contains the documentation available for Spectacle, which is a
screenshot capture program by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.spectacle Utility DesktopUtility

%post
%systemd_user_post

%preun
%systemd_user_preun

%postun
%systemd_user_postun

%files
%license LICENSES/*
%dir %{_kf5_libdir}/kconf_update_bin
%dir %{_kf5_sharedir}/kconf_update
%dir %{_kf5_sharedir}/kglobalaccel
%doc %lang(en) %{_mandir}/man1/spectacle.1.gz
%{_kf5_applicationsdir}/org.kde.spectacle.desktop
%{_kf5_appstreamdir}/org.kde.spectacle.appdata.xml
%{_kf5_bindir}/spectacle
%{_kf5_dbusinterfacesdir}/org.kde.Spectacle.xml
%{_kf5_debugdir}/spectacle.categories
%{_kf5_iconsdir}/hicolor/*/*/spectacle*
%{_kf5_libdir}/kconf_update_bin/spectacle-migrate-shortcuts
%{_kf5_libdir}/kconf_update_bin/spectacle-migrate-rememberregion
%{_kf5_notifydir}/spectacle.notifyrc
%{_kf5_sharedir}/dbus-1/services/org.kde.Spectacle.service
%{_kf5_sharedir}/kconf_update/spectacle_newConfig.upd
%{_kf5_sharedir}/kconf_update/spectacle_shortcuts.upd
%{_kf5_sharedir}/kconf_update/50-clipboard_settings_change.py
%{_kf5_sharedir}/kconf_update/spectacle_clipboard.upd
%{_kf5_sharedir}/kconf_update/spectacle_rememberregion.upd
%{_kf5_sharedir}/kglobalaccel/org.kde.spectacle.desktop
%{_userunitdir}/app-org.kde.spectacle.service

%files doc
%doc README.md
%doc %lang(en) %{_kf5_htmldir}/en/spectacle/


%files lang -f %{name}.lang

%changelog
