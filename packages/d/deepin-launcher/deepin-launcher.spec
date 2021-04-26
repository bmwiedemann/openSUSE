#
# spec file for package deepin-launcher
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define _name dde-launcher

Name:           deepin-launcher
Version:        5.4.4
Release:        0
Summary:        Deepin Launcher
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/dde-launcher
Source0:        https://github.com/linuxdeepin/dde-launcher/archive/%{version}/%{_name}-%{version}.tar.gz
Group:          System/GUI/Other
BuildRequires:  cmake
BuildRequires:  gtest
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dframeworkdbus) >= 0.4.1
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  libQt5Gui-private-headers-devel 
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-linguist
BuildRequires:  hicolor-icon-theme
Requires:       deepin-desktop-schemas >= 5.9.3
Requires:       deepin-daemon
Requires:       deepin-start
Requires:       libqt5-qdbus
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin desktop-environment - Launcher module

%package devel
Summary:        Development tools for deepin-launchers
Group:          Development/Libraries/C and C++

%description devel
Deepin desktop-environment - Launcher module

The deepin-launcher-devel package contains the header files and developer
docs for deepin-launcher.

%prep
%setup -q -n %{_name}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh
sed -i 's|qdbus|qdbus-qt5|g' dde-launcher-wapper

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DWITHOUT_UNINSTALL_APP=1
%make_build

%install
%cmake_install

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{_name}
%{_bindir}/%{_name}-wapper
%{_datadir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/com.deepin.dde.launcher.gschema.xml

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{_name}

%changelog
