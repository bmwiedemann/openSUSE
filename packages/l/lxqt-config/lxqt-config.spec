#
# spec file for package lxqt-config
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.16.0
Release:        0
Summary:        LXQt Control Center
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        lxqt-config.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Screen)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg) >= 1.3.0
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lxqt) >= %{version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(zlib)
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils
Recommends:     %{name}-lang

%description
System Configuration and Control Center for LXQt

%lang_package

%prep
%setup -q
# Changing LXQt into X-LXQt in desktop files to be freedesktop compliant and shut rpmlint warnings
#find -name '*desktop.in*' -exec sed -ri 's/(LXQt;)/X-\1/' {} +

%build
#We normally use _libdir but LXQt expects _lib
%cmake \
-DCMAKE_SKIP_RPATH:BOOL=Off \
-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
-DPULL_TRANSLATIONS=No

%make_build

%install
%cmake_install
install -Dm 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 0644 lib%{name}-cursor/man/%{name}-mouse.1 %{buildroot}%{_mandir}/man1/%{name}-mouse.1
install -Dm 0644 %{name}-appearance/man/%{name}-appearance.1 %{buildroot}%{_mandir}/man1/%{name}-appearance.1
%fdupes -s %{buildroot}/%{_datadir}

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS
%dir %{_libdir}/lxqt-config
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/icons
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/*.menu
%{_bindir}/%{name}
%{_bindir}/%{name}-appearance
%{_bindir}/%{name}-file-associations
%{_bindir}/%{name}-input
%{_bindir}/%{name}-monitor
%{_bindir}/%{name}-locale
%{_libdir}/%{name}/lib%{name}-cursor.so
%{_bindir}/lxqt-config-brightness
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/brightnesssettings.svg
%{_datadir}/lxqt/icons/monitor.svg
%{_mandir}/man?/%{name}*.?%{ext_man}
%{_datadir}/desktop-directories/

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%{_datadir}/lxqt/translations/lxqt-config
%{_datadir}/lxqt/translations/lxqt-config-appearance
%{_datadir}/lxqt/translations/lxqt-config-brightness
%{_datadir}/lxqt/translations/lxqt-config-cursor
%{_datadir}/lxqt/translations/lxqt-config-file-associations
%{_datadir}/lxqt/translations/lxqt-config-input
%{_datadir}/lxqt/translations/lxqt-config-locale
%{_datadir}/lxqt/translations/lxqt-config-monitor

%changelog
