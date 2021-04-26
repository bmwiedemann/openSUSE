#
# spec file for package deepin-dock
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Hillwood Yang <hillwood@opensuse.org>
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

%define _name dde-dock

Name:           deepin-dock
Version:        5.4.4
Release:        0
License:        GPL-3.0+
Summary:        Deepin dock
Url:            https://github.com/linuxdeepin/dde-dock
Group:          System/GUI/Other
Source0:        https://github.com/linuxdeepin/dde-dock/archive/%{version}/%{_name}-%{version}.tar.gz
Patch0:         %{name}-link-libraries.patch
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  dtkcore >= 5.0.0
BuildRequires:  gtest
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  cmake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
deepin desktop-environment - dock module

%package devel
Summary:        Development tools for deepin dock
Group:          Development/Libraries/C and C++

%description devel
The deepin-dock-devel package contains the header files for deepin-dock.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
sed -i "s/lrelease/lrelease-qt5/g" translate_generation.sh
sed -i 's|no</allow_any>|auth_admin</allow_any>|g' plugins/overlay-warning/com.deepin.dde.dock.overlay.policy

%build
%cmake

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/polkit-1

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md
%license LICENSE
%dir %{_sysconfdir}/dde-dock
%dir %{_sysconfdir}/dde-dock/indicator
%config %{_sysconfdir}/dde-dock/indicator/keybord_layout.json
%{_bindir}/dde-dock
%{_prefix}/lib/dde-dock
%{_datadir}/dde-dock
# %dir %{_datadir}/polkit-1
# %dir %{_datadir}/polkit-1/actions
# %{_datadir}/polkit-1/actions/com.deepin.dde.dock.overlay.policy
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml

%files devel
%defattr(-,root,root)
%{_includedir}/dde-dock
%dir %{_libdir}/cmake/DdeDock
%{_libdir}/cmake/DdeDock/DdeDockConfig.cmake
%{_libdir}/pkgconfig/%{_name}.pc

%changelog

