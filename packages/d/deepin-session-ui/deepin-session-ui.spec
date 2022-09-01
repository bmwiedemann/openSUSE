#
# spec file for package deepin-session-ui
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define _name dde-session-ui

Name:           deepin-session-ui
Version:        5.5.24
Release:        0
Summary:        Deepin desktop-environment - Session UI module
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-session-ui
Source0:        https://github.com/linuxdeepin/dde-session-ui/archive/%{version}/%{_name}-%{version}.tar.gz
# PATCH-FIX-UPSTEAM fix-library-path.patch hillwood@opensuse.org
Patch0:         fix-library-path.patch
Group:          System/GUI/Other
BuildRequires:  gtest
BuildRequires:  update-desktop-files
BuildRequires:  deepin-gettext-tools
BuildRequires:  dtkcore
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblightdm-qt5-3)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pam-devel
BuildRequires:  libqt5-linguist
Requires:       deepin-wallpapers
Recommends:     %{name}-lang = %{version}-%{release}

%description
This project include those sub-project:

- deepin-lowpower: The user interface of reminding low power.
- deepin-osd: User interface of on-screen display.
- deepin-hotzone: User interface of setting hot zone.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh
# sed -i 's|/usr/lib/dde-dock|%{_libdir}/dde-dock|' \
# dde-notification-plugin/notifications/notifications.pro
sed -i 's|backgrounds/default_background.jpg|wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|g' \
widgets/fullscreenbackground.cpp tests/dde-welcome/global_util/ut_publicfunc.cpp
sed -i 's|backgrounds/deepin/desktop.jpg|wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|g' \
widgets/fullscreenbackground.cpp tests/dde-welcome/global_util/ut_publicfunc.cpp
sed -i 's/qdbusxml2cpp/qdbusxml2cpp-qt5/g' CMakeLists.txt
#Use Geeko logo instead of deepin
# cp %{SOURCE1} lightdm-deepin-greeter/img/

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install
%find_lang %{_name} --with-qt

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{_bindir}/*
%{_datadir}/icons/hicolor/scalable/devices/computer.svg
%{_prefix}/lib/deepin-daemon
%dir %{_libdir}/dde-dock
%dir %{_libdir}/dde-dock/plugins
%{_libdir}/dde-dock/plugins/libnotifications.so
%dir %{_datadir}/dde-session-ui
%dir %{_datadir}/dde-session-ui/translations
%{_datadir}/dbus-1/services/com.deepin.dde.welcome.service
%{_datadir}/dbus-1/services/com.deepin.dde.osd.service
%{_datadir}/dbus-1/services/com.deepin.dde.Notification.service
%{_datadir}/dbus-1/services/com.deepin.dde.freedesktop.Notification.service
%{_datadir}/dbus-1/services/com.deepin.dde.MemoryWarningDialog.service
%{_datadir}/dbus-1/services/com.deepin.dde.WarningDialog.service
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.notifications.gschema.xml

%files lang -f %{_name}.lang
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/translations
%{_datadir}/%{_name}/translations/dde-session-ui.qm
%if 0%{?suse_version} <= 1500
%{_datadir}/%{_name}/translations/%{_name}_ast.qm
%{_datadir}/%{_name}/translations/%{_name}_fil.qm
%{_datadir}/%{_name}/translations/%{_name}_pam.qm
%endif

%changelog

