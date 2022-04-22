#
# spec file for package deepin-session-shell
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define _name dde-session-shell

Name:           deepin-session-shell
Version:        5.5.24
Release:        0
Summary:        Deepin desktop-environment - Session UI Shell
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/dde-session-shell
Source0:        https://github.com/linuxdeepin/dde-session-shell/archive/%{version}/%{_name}-%{version}.tar.gz
Source1:        https://github.com/linuxdeepin/startdde/raw/master/misc/lightdm.conf
Group:          System/GUI/Other
BuildRequires:  gtest
BuildRequires:  update-desktop-files
BuildRequires:  deepin-gettext-tools
BuildRequires:  dtkcore
BuildRequires:  libqt5-linguist
BuildRequires:  pam-devel
BuildRequires:  lightdm
%if 0%{?suse_version} <= 1500
BuildRequires:  lightdm-gtk-greeter 
%endif
BuildRequires:  pkgconfig(dtkwidget) >= 5.5.0
BuildRequires:  libdframeworkdbus-devel >= 5.4.20
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
BuildRequires:  pkgconfig(openssl)
BuildRequires:  plasma5-theme-openSUSE
Requires:       deepin-wallpapers
Recommends:     %{name}-lang = %{version}-%{release}

%description
This project include those sub-project:

- deepin-shutdown: User interface of shutdown.
- deepin-lock: User interface of lock screen.
- deepin-lockservice: The back-end service of locking screen.
- lightdm-deepin-greeter: The user interface when you login in.
- deepin-switchtogreeter: The tools to switch the user to login in.
- deepin-lowpower: The user interface of reminding low power.
- deepin-osd: User interface of on-screen display.
- deepin-hotzone: User interface of setting hot zone.

%package -n lightdm-deepin-greeter
Summary:        Simple display manager (Deepin Desktop)
Group:          System/X11/Displaymanagers
Requires:       lightdm
Requires:       deepin-start
Requires:       libgnome-keyring0
Recommends:     %{name}-lang = %{version}-%{release}

%description -n lightdm-deepin-greeter
A LightDM greeter that uses the Deepin Desktop. This is the reference implementation 
of a LightDM greeter based on the Deepin Desktop.

%package devel
Summary:        Development tools for deepin-session-shell
Group:          Development/Languages/C and C++

%description devel
The deepin-session-shell-devel package contains the header files and developer
docs for deepin-session-shell-devel.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh
sed -i 's|qdbusxml2cpp|qdbusxml2cpp-qt5|g' CMakeLists.txt
sed -i 's|backgrounds/default_background.jpg|wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|g' \
src/widgets/fullscreenbackground.cpp
sed -i 's|backgrounds/deepin/desktop.jpg|wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|g' \
src/session-widgets/lockcontent.cpp
cp %{_datadir}/icons/hicolor/scalable/apps/openSUSE-distributor-logo.svg src/widgets/img/logo.svg

%build
%cmake
%make_build

%install
%cmake_install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/60-deepin.conf
chmod +x %{buildroot}%{_bindir}/*

%files
# %doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE
%{_bindir}/dde-*
%{_bindir}/deepin-greeter
%dir %{_sysconfdir}/deepin
%dir %{_sysconfdir}/deepin/greeters.d
%{_sysconfdir}/deepin/greeters.d/00-xrandr
%{_datadir}/dbus-1/services/*.service
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/com.deepin.dde.session-shell.gschema.xml
%dir %{_datadir}/deepin-authentication/
%dir %{_datadir}/deepin-authentication/privileges
%{_datadir}/deepin-authentication/privileges/lightdm-deepin-greeter.conf
%dir %{_datadir}/dsg
%dir %{_datadir}/dsg/apps/
%{_datadir}/dsg/apps/dde-lock

%files -n lightdm-deepin-greeter
%license LICENSE
%dir %{_sysconfdir}/lightdm/deepin
%config %{_sysconfdir}/lightdm/deepin/qt-theme.ini
%{_bindir}/lightdm-deepin-greeter
%{_sysconfdir}/deepin/greeters.d/lightdm-deepin-greeter
%{_sysconfdir}/deepin/greeters.d/10-cursor-theme
# %dir %{_datadir}/lightdm
# %dir %{_datadir}/lightdm/lightdm.conf.d
%{_datadir}/lightdm/lightdm.conf.d/60-deepin.conf
%dir %{_datadir}/xgreeters
%{_datadir}/xgreeters/lightdm-deepin-greeter.desktop
%{_datadir}/dsg/apps/lightdm-deepin-greeter

%files devel
%{_includedir}/%{_name}
%{_libdir}/cmake/DdeSessionShell

%files lang
%{_datadir}/%{_name}

%changelog

