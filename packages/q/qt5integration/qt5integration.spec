#
# spec file for package qt5integration
#
# Copyright (c) 2022 SUSE LLC
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


Name:           qt5integration
Version:        5.5.24
Release:        0
License:        GPL-3.0-or-later
Summary:        Qt platform theme integration plugins
URL:            https://github.com/linuxdeepin/qt5integration
Group:          System/GUI/Other
Source0:        https://github.com/linuxdeepin/qt5integration/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gtest
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformSupport-devel-static
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(Qt5XdgIconLoader)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrender)

%description
Multiple Qt plugins to provide better Qt5 integration for DDE are included.

%prep
%autosetup -p1

%build
%qmake5 BASED_DTK_DIR=based-dtk
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
%dir %{_kf5_plugindir}/styles/based-dtk
%dir %{_kf5_plugindir}/iconengines/based-dtk
%dir %{_kf5_plugindir}/imageformats/based-dtk
%dir %{_kf5_plugindir}/platformthemes/based-dtk
%{_kf5_plugindir}/iconengines/libdtkbuiltin.so
%{_kf5_plugindir}/iconengines/libxdgicon.so
%{_kf5_plugindir}/imageformats/libdsvg.so
%{_kf5_plugindir}/platformthemes/libqdeepin.so
%{_kf5_plugindir}/styles/libchameleon.so
%{_kf5_plugindir}/iconengines/libdsvgicon.so
%{_kf5_plugindir}/iconengines/based-dtk/libdtkbuiltin.so
%{_kf5_plugindir}/iconengines/based-dtk/libxdgicon.so
%{_kf5_plugindir}/imageformats/based-dtk/libdsvg.so
%{_kf5_plugindir}/platformthemes/based-dtk/libqdeepin.so
%{_kf5_plugindir}/styles/based-dtk/libchameleon.so
%{_kf5_plugindir}/iconengines/based-dtk/libdsvgicon.so

%changelog
