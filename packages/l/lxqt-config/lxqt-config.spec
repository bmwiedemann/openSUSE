#
# spec file for package lxqt-config
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


Name:           lxqt-config
Version:        2.1.0
Release:        0
Summary:        LXQt Control Center
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/lxqt/lxqt-config
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(KF6Screen) >= 6.0.0
BuildRequires:  cmake(KF6WindowSystem) >= 6.0.0
BuildRequires:  cmake(Qt6Concurrent) >= 6.6
BuildRequires:  cmake(Qt6DBus) >= 6.6
BuildRequires:  cmake(Qt6LinguistTools) >= 6.6
BuildRequires:  cmake(Qt6Svg) >= 6.6
BuildRequires:  cmake(Qt6Xml) >= 6.6
BuildRequires:  cmake(lxqt) >= %{version}
BuildRequires:  cmake(lxqt-menu-data) >= %{version}
BuildRequires:  cmake(lxqt2-build-tools) >= %{version}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(zlib)

%description
System Configuration and Control Center for LXQt

%lang_package

%prep
%autosetup -p1

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}
%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt --all-name

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_qt6_libdir}/%{name}
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/icons
%{_bindir}/%{name}
%{_bindir}/%{name}-appearance
%{_bindir}/%{name}-brightness
%{_bindir}/%{name}-file-associations
%{_bindir}/%{name}-input
%{_bindir}/%{name}-locale
%{_bindir}/%{name}-monitor
%{_qt6_libdir}/%{name}/lib%{name}-cursor.so
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/brightnesssettings.svg
%{_datadir}/lxqt/icons/monitor.svg
%{_mandir}/man?/%{name}*.?%{?ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/%{name}
%dir %{_datadir}/lxqt/translations/%{name}-appearance
%dir %{_datadir}/lxqt/translations/%{name}-brightness
%dir %{_datadir}/lxqt/translations/%{name}-cursor
%dir %{_datadir}/lxqt/translations/%{name}-file-associations
%dir %{_datadir}/lxqt/translations/%{name}-input
%dir %{_datadir}/lxqt/translations/%{name}-locale
%dir %{_datadir}/lxqt/translations/%{name}-monitor

%changelog
