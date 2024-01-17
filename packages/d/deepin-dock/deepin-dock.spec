#
# spec file for package deepin-dock
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Hillwood Yang <hillwood@opensuse.org>
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


%define _name dde-dock

Name:           deepin-dock
Version:        5.5.65
Release:        0
Summary:        Deepin dock
License:        LGPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dde-dock
Source0:        https://github.com/linuxdeepin/dde-dock/archive/%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  dtkcommon >= 5.5.20
BuildRequires:  dtkcore >= 5.0.0
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  cmake(DdeControlCenter)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libdeepin_pw_check)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
deepin desktop-environment - dock module

%package devel
Summary:        Development tools for deepin dock
Group:          Development/Libraries/C and C++

%description devel
The deepin-dock-devel package contains the header files for deepin-dock.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i "s/lrelease/lrelease-qt5/g" translate_generation.sh
sed -i 's|no</allow_any>|auth_admin</allow_any>|g' plugins/overlay-warning/com.deepin.dde.dock.overlay.policy
# sed -i 's|lib/|${CMAKE_INSTALL_LIBDIR}/|g' plugins/*/CMakeLists.txt
# sed -i 's|/usr/lib|@CMAKE_INSTALL_LIBDIR@|g' frame/controller/dockpluginscontroller.cpp \
# plugins/tray/system-trays/systemtrayscontroller.cpp

sed -i '/TARGETS/s|lib|%{_lib}|' plugins/*/CMakeLists.txt \
                                 plugins/plugin-guide/plugins-developer-guide.md

sed -i 's|/usr/lib|%{_libdir}|' frame/controller/dockpluginscontroller.cpp \
                          frame/window/mainpanelcontrol.cpp \
                          plugins/tray/system-trays/systemtrayscontroller.cpp

sed -i 's|libdir.*|libdir=%{_libdir}|' dde-dock.pc.in

sed -i 's|/usr/lib/dde-dock/plugins|%{_libdir}/dde-dock/plugins|' plugins/plugin-guide/plugins-developer-guide.md
sed -i 's|local/lib/dde-dock/plugins|local/%{_lib}/dde-dock/plugins|' plugins/plugin-guide/plugins-developer-guide.md

%build
%cmake
%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/polkit-1

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/%{_name}
%{_libdir}/%{_name}
%{_datadir}/%{_name}
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml
%dir %{_sysconfdir}/dde-dock
%dir %{_sysconfdir}/dde-dock/indicator
%config %{_sysconfdir}/dde-dock/indicator/keybord_layout.json
%dir %{_datadir}/dsg
%dir %{_datadir}/dsg/configs
%dir %{_datadir}/dsg/configs/org.deepin.dde.control-center
%dir %{_datadir}/dsg/configs/org.deepin.dde.dock
%{_datadir}/dsg/configs/org.deepin.dde.control-center/*.json
%{_datadir}/dsg/configs/org.deepin.dde.dock/*.json
%dir %{_libdir}/dde-control-center
%dir %{_libdir}/dde-control-center/modules
%{_libdir}/dde-control-center/modules/libdcc-dock-plugin.so

%files devel
%{_includedir}/%{_name}
%dir %{_libdir}/cmake/DdeDock
%{_libdir}/cmake/DdeDock/DdeDockConfig.cmake
%{_libdir}/pkgconfig/%{_name}.pc

%files lang
%{_datadir}/dcc-dock-plugin

%changelog
