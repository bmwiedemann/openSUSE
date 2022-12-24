#
# spec file for package qt5platform-plugins
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
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

# %define   commit          f5fe61fb6a641f8f34f6e916b6dda27657266646
# %define   shortcommit     %(c=%{commit}; echo ${c:0:7})
# %define   qt_version      5.15.5

Name:           qt5platform-plugins
Version:        5.0.70
Release:        0
Summary:        Qt platform integration plugins
License:        LGPL-3.0-or-later
Group:          Development/Libraries/X11
Url:            https://github.com/linuxdeepin/qt5platform-plugins
Source0:        https://github.com/linuxdeepin/qt5platform-plugins/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libqt5-linguist
BuildRequires:  wayland-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libQt5Core-private-headers-devel 
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
# BuildRequires:  pkgconfig(dde-wayland-client)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  git-core
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The qt5dxcb-plugin is the Qt platform integration plugin for Deepin Desktop
Environment.

%package -n libqt5-dxcbplugin
Summary:        A Qt platform integration plugin
Group:          Development/Libraries/X11

%description -n libqt5-dxcbplugin
The libqt5-dxcbplugin is the Qt platform dxcbp plugin for Deepin Desktop
Environment.

# %package -n libqt5-dwaylandplugin
# Summary:        A Qt platform integration plugin
# Group:          Development/Libraries/X11

# %description -n libqt5-dwaylandplugin
# The libqt5-dxcbplugin is the Qt platform dwayland plugin for Deepin Desktop
# Environment.

# %package -n libqt5-kwayland-shellplugin
# Summary:        A Qt platform integration plugin
# Group:          Development/Libraries/X11

# %description -n libqt5-kwayland-shellplugin
# The libqt5-dxcbplugin is the Qt platform kwayland-shell plugin for Deepin Desktop
# Environment.

%prep
# %setup -q -a1 -n %{name}-%{version}
%setup -q -n %{name}-%{version}
if [ "`rpm -q --queryformat '%%{VERSION}' libQt5Core5`" = "5.9.7" ]; then
    cp -r xcb/libqt5xcbqpa-dev/5.9.4 xcb/libqt5xcbqpa-dev/5.9.7
elif [ "`rpm -q --queryformat '%%{VERSION}' libQt5Core5`" = "5.12.7" ]; then
    cp -r xcb/libqt5xcbqpa-dev/5.12.3 xcb/libqt5xcbqpa-dev/5.12.7
elif [ "`rpm -q --queryformat '%%{VERSION}' libQt5Core5`" = "5.15.6+kde177" ]; then
    cp -r xcb/libqt5xcbqpa-dev/5.15.5 xcb/libqt5xcbqpa-dev/5.15.6
elif [ "`rpm -q --queryformat '%%{VERSION}' libQt5Core5`" = "5.15.7+kde167" ]; then
    cp -r xcb/libqt5xcbqpa-dev/5.15.5 xcb/libqt5xcbqpa-dev/5.15.7
elif [ "`rpm -q --queryformat '%%{VERSION}' libQt5Core5`" = "5.15.7+kde177" ]; then
    cp -r xcb/libqt5xcbqpa-dev/5.15.5 xcb/libqt5xcbqpa-dev/5.15.7
fi

# Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
sed -i '/wayland/d' qt5platform-plugins.pro

%build
qmake-qt5 DEFINES+=QT_NO_DEBUG_OUTPUT \
          PREFIX=%{_prefix} \
          LIB_INSTALL_DIR=%{_libdir} \
          LIBSUFFIX=%{lib}
%make_build

%install
%qmake5_install

%files -n libqt5-dxcbplugin
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{_libdir}/qt5/plugins/platforms/
%{_libdir}/qt5/plugins/platforms/libdxcb.so

# %files -n libqt5-dwaylandplugin
# %defattr(-,root,root,-)
# %doc CHANGELOG.md README.md
# %license LICENSE
# %dir %{_libdir}/qt5/plugins/platforms/
# %{_libdir}/qt5/plugins/platforms/libdwayland.so

# %files -n libqt5-kwayland-shellplugin
# %defattr(-,root,root,-)
# %doc CHANGELOG.md README.md
# %license LICENSE
# %dir %{_libdir}/qt5/plugins/wayland-shell-integration/
# %{_libdir}/qt5/plugins/wayland-shell-integration/libkwayland-shell.so

%changelog
