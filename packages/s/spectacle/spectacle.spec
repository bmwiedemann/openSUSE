#
# spec file for package spectacle
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
Name:           spectacle
Version:        24.05.1
Release:        0
Summary:        Screen Capture Program
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://apps.kde.org/spectacle
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPipeWire) >= %{plasma6_version}
BuildRequires:  cmake(LayerShellQt) >= %{plasma6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickTemplates2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(ZXing) >= 1.2.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)

%description
Spectactle is a screenshot-taking program made by KDE. It allows taking screenshots
of screens, windows, regions of the screen, and to export them to files or other
online services.

%package doc
Summary:        Documentation for Spectacle
Requires:       spectacle

%description doc
This package contains the documentation available for Spectacle, which is a
screenshot capture program by KDE.

%lang_package
%lang_package -n spectacle-doc

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name
%find_lang %{name}-doc --with-html --without-mo --all-name

%post
%{systemd_user_post app-org.kde.spectacle.service}

%preun
%{systemd_user_preun app-org.kde.spectacle.service}

%postun
%{systemd_user_postun app-org.kde.spectacle.service}

%files
%license LICENSES/*
%doc %lang(en) %{_mandir}/man1/spectacle.1.gz
%{_kf6_applicationsdir}/org.kde.spectacle.desktop
%{_kf6_appstreamdir}/org.kde.spectacle.appdata.xml
%{_kf6_bindir}/spectacle
%{_kf6_dbusinterfacesdir}/org.kde.Spectacle.xml
%{_kf6_debugdir}/spectacle.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/spectacle.svg
%{_kf6_libdir}/kconf_update_bin/spectacle-24.02.0-change_placeholder_format
%{_kf6_libdir}/kconf_update_bin/spectacle-24.02.0-keep_old_filename_templates
%{_kf6_libdir}/kconf_update_bin/spectacle-24.02.0-keep_old_save_location
%{_kf6_libdir}/kconf_update_bin/spectacle-24.02.0-rename_settings
%{_kf6_libdir}/kconf_update_bin/spectacle-24.02.0-video_format
%{_kf6_notificationsdir}/spectacle.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.kde.Spectacle.service
%{_kf6_sharedir}/dbus-1/services/org.kde.spectacle.service
%dir %{_kf6_sharedir}/kglobalaccel
%{_kf6_sharedir}/kglobalaccel/org.kde.spectacle.desktop
%{_kf6_sharedir}/kconf_update/spectacle.upd
%{_userunitdir}/app-org.kde.spectacle.service

%files doc
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/spectacle/

%files lang -f %{name}.lang

%files doc-lang -f %{name}-doc.lang
%exclude %{_kf6_htmldir}/en/spectacle/

%changelog
