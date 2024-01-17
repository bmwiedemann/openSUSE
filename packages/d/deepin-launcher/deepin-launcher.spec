#
# spec file for package deepin-launcher
#
# Copyright (c) 2023 SUSE LLC
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


%define _name dde-launcher

Name:           deepin-launcher
Version:        5.5.31
Release:        0
Summary:        Deepin Launcher
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-launcher
Source0:        https://github.com/linuxdeepin/dde-launcher/archive/%{version}/%{_name}-%{version}.tar.gz
# https://github.com/linuxdeepin/dde-launcher/commit/0612c1181f232eb1c7be05a40c9c951a51cd0f2a
Patch2:         fix-stuck-issue.patch
Group:          System/GUI/Other
BuildRequires:  cmake
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dframeworkdbus) >= 0.4.1
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(xcb-ewmh)
Requires:       dbus-1
Requires:       deepin-daemon
Requires:       deepin-desktop-schemas >= 5.9.3
Requires:       deepin-start

%description
Deepin desktop-environment - Launcher module

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

%build
%cmake -DWITHOUT_UNINSTALL_APP=1
%cmake_build

%install
%cmake_install
%find_lang %{_name} --with-qt

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{_name}
%{_bindir}/%{_name}-wapper
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/com.deepin.dde.launcher.gschema.xml
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/translations
%{_datadir}/%{_name}/translations/dde-launcher.qm
%dir %{_datadir}/dsg
%dir %{_datadir}/dsg/configs
%dir %{_datadir}/dsg/configs/org.deepin.dde.launcher
%{_datadir}/dsg/configs/org.deepin.dde.launcher/org.deepin.dde.launcher.json

%files lang -f %{_name}.lang
%if 0%{?suse_version} <= 1500
# unusual languages not autodetected by find_lang (boo#1187036)
%lang(ast) %{_datadir}/%{_name}/translations/dde-launcher_ast.qm
%lang(fil) %{_datadir}/%{_name}/translations/dde-launcher_fil.qm
%lang(kab) %{_datadir}/%{_name}/translations/dde-launcher_kab.qm
%lang(pam) %{_datadir}/%{_name}/translations/dde-launcher_pam.qm
%endif

%changelog
