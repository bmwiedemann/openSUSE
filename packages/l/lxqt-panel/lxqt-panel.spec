#
# spec file for package lxqt-panel
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


Name:           lxqt-panel
Version:        2.0.1
Release:        0
Summary:        LXQt desktop panel
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-panel
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch1:         001-fix-plugin-loader.patch
BuildRequires:  cmake >= 3.27.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libsensors4-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt) >= 6.0.0
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(lxqt-menu-data) >= 2.0.0
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbusmenu-lxqt)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(lxqt) >= 2.0.0
BuildRequires:  pkgconfig(lxqt-globalkeys-ui)
BuildRequires:  pkgconfig(sysstat-qt6)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xtst)
Requires:       lxqt-menu-data
Requires:       menu-cache
Recommends:     %{name}-lang = %{version}-%{release}

%description
lxqt-panel represents the taskbar of LXQt.

%lang_package

%package devel
Summary:        Devel files for lxqt-panel
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
LXQt panel development files and headers

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
export CXXFLAGS="%{optflags} $(pkg-config --cflags xkbcommon-x11)"
%cmake_qt6 \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"
%{qt6_build}

%install
%{qt6_install}
%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt --all-name

%files
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/lxqt/%{name}
%dir %{_datadir}/lxqt/panel
%{_datadir}/lxqt/panel/qeyes-types/
%{_datadir}/lxqt/panel.conf
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%license LICENSE

%files devel
%{_includedir}/lxqt

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/%{name}
%dir %{_datadir}/lxqt/translations/%{name}/colorpicker
%dir %{_datadir}/lxqt/translations/%{name}/cpuload
%dir %{_datadir}/lxqt/translations/%{name}/customcommand
%dir %{_datadir}/lxqt/translations/%{name}/desktopswitch
%dir %{_datadir}/lxqt/translations/%{name}/directorymenu
%dir %{_datadir}/lxqt/translations/%{name}/dom
%dir %{_datadir}/lxqt/translations/%{name}/fancymenu
%dir %{_datadir}/lxqt/translations/%{name}/kbindicator
%dir %{_datadir}/lxqt/translations/%{name}/mainmenu
%dir %{_datadir}/lxqt/translations/%{name}/mount
%dir %{_datadir}/lxqt/translations/%{name}/networkmonitor
%dir %{_datadir}/lxqt/translations/%{name}/qeyes
%dir %{_datadir}/lxqt/translations/%{name}/quicklaunch
%dir %{_datadir}/lxqt/translations/%{name}/sensors
%dir %{_datadir}/lxqt/translations/%{name}/showdesktop
%dir %{_datadir}/lxqt/translations/%{name}/spacer
%dir %{_datadir}/lxqt/translations/%{name}/statusnotifier
%dir %{_datadir}/lxqt/translations/%{name}/sysstat
%dir %{_datadir}/lxqt/translations/%{name}/taskbar
%dir %{_datadir}/lxqt/translations/%{name}/volume
%dir %{_datadir}/lxqt/translations/%{name}/worldclock

%changelog
