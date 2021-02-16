#
# spec file for package deepin-qt5integration
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

Name:           qt5integration
Version:        5.1.5
Release:        0
License:        GPL-3.0
Summary:        Qt platform theme integration plugins
Url:            https://github.com/linuxdeepin/qt5integration
Group:          System/GUI/Other
Source0:        https://github.com/linuxdeepin/qt5integration/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libQt5PlatformSupport-devel-static
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(Qt5XdgIconLoader)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)

%description
Multiple Qt plugins to provide better Qt5 integration for DDE are included.

%prep
%autosetup -p1

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%qmake5_install

%files
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{_kf5_plugindir}/styles
%dir %{_kf5_plugindir}/iconengines
%dir %{_kf5_plugindir}/imageformats
%dir %{_kf5_plugindir}/platformthemes
%{_kf5_plugindir}/iconengines/libdsvgicon.so
%{_kf5_plugindir}/iconengines/libdtkbuiltin.so
%{_kf5_plugindir}/imageformats/libdsvg.so
%{_kf5_plugindir}/platformthemes/libqdeepin.so
%{_kf5_plugindir}/styles/libchameleon.so

%changelog
