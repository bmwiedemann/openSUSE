#
# spec file for package lxqt-panel
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


Name:           lxqt-panel
Version:        1.2.1
Release:        0
Summary:        Desktop Panel for LXQt
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libsensors4-devel
BuildRequires:  lxqt-build-tools-devel >= 0.11.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Solid) >= 5.36.0
BuildRequires:  cmake(KF5WindowSystem) >= 5.36.0
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(lxqt) >= 1.1.0
BuildRequires:  pkgconfig(lxqt-globalkeys) >= 1.1.0
BuildRequires:  pkgconfig(lxqt-globalkeys-ui)
BuildRequires:  pkgconfig(sysstat-qt5)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
Requires:       lxmenu-data
Recommends:     %{name}-lang

%description
Brand new desktop Panel for LXQt

%lang_package

%package devel
Summary:        Devel files for lxqt-panel
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
LXQt panel development files and headers

%prep
%setup -q

%build
%define _lto_cflags %{nil}
export CXXFLAGS="%{optflags} $(pkg-config --cflags xkbcommon-x11)"
%cmake -DPULL_TRANSLATIONS=No -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"

%install
%cmake_install
%fdupes -s %{buildroot}/%{_datadir}

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS CHANGELOG
%{_bindir}/%{name}
%dir %{_datadir}/desktop-directories/
%dir %{_datadir}/lxqt
%dir %{_sysconfdir}/xdg
%dir %{_sysconfdir}/xdg/autostart
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/lxqt-applications.menu
%config %{_sysconfdir}/xdg/menus/lxqt-applications-compact.menu
%config %{_sysconfdir}/xdg/menus/lxqt-applications-simple.menu
%{_libdir}/%{name}
%{_datadir}/lxqt/panel
%{_datadir}/lxqt/lxqt-panel
%{_datadir}/lxqt/panel/qeyes-types
%{_mandir}/man1/lxqt-panel.1%{?ext_man}
%config %{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_datadir}/desktop-directories/lxqt-leave.directory
%{_datadir}/desktop-directories/lxqt-settings.directory
%{_datadir}/lxqt/panel.conf

%files devel
%license LICENSE
%{_includedir}/lxqt

%files lang -f %{name}.lang
%license LICENSE
%dir %{_datadir}/lxqt/translations/
%{_datadir}/lxqt/translations/%{name}

%changelog
