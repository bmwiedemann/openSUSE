#
# spec file for package deepin-kwin
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

%define   _name           dde-kwin
%define   sover           0
%define   kwin_version    %(rpm -q --queryformat '%%{VERSION}' kwin5)
%define   kwin_max        5.25.1

Name:           deepin-kwin
Version:        5.5.11
Release:        0
Summary:        KWin configures/plugins on the DDE
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Url:            https://github.com/linuxdeepin/dde-kwin
Source0:        https://github.com/linuxdeepin/dde-kwin/archive/%{version}/%{_name}-%{version}.tar.gz
Patch0:         %{name}-tabbox-chameleon-rename.patch
# Patch1:         fix-build-on-5_18_6.patch
Patch2:         fix-build-on-5_25_3.patch
# PATCH-FIX-UPSTRAM fix-library-links.patch hillwood@opensuse.org - Fix build on Tumbleweed
# https://github.com/linuxdeepin/dde-kwin/pull/154
Patch3:         fix-library-links.patch
Patch4:         drop-nonexistent-translations.patch
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  kwin5-devel
BuildRequires:  libepoxy-devel
BuildRequires:  plasma5-workspace-devel
BuildRequires:  libQt5Gui-private-headers-devel 
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5PlatformSupport-devel-static
Requires:       deepin-wallpapers
Requires:       dbus-1
Requires:       kwin5
Provides:       deepin-kwin5

%description
KWin configures/plugins on the DDE
Let kwin work well in the Deepin Desktop Environment.

%package -n libkwin-xcb%{sover}
Summary:        Deepin Kwin libraries
Group:          System/Libraries

%description -n libkwin-xcb%{sover}
KWin configures/plugins on the DDE
Let kwin work well in the Deepin Desktop Environment.

%package devel
Summary:        Development tools for deepin-plugin-kwin
Group:          Development/Libraries/C and C++
Requires:       libkwin-xcb%{sover}

%description devel
The deepin-plugin-kwin-devel package contains the header files and developer
docs for deepin-plugin-kwin.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i 's|backgrounds/default_background.jpg|wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|g' \
deepin-wm-dbus/deepinwmfaker.cpp plugins/kwineffects/multitasking/background.cpp
sed -i 's/lrelease/lrelease-qt5/g' plugins/platforms/plugin/translate_generation.sh
sed -i 's|/usr/lib|%{_libdir}|g' plugins/platforms/plugin/{main.cpp,main_wayland.cpp}

%if "%{kwin_version}" >= "%{kwin_max}"
# Workaround issue#3246 (https://github.com/linuxdeepin/developer-center/issues/3246)
# sed -i 's|GLRenderTarget|GLFramebuffer|g' plugins/kwineffects/scissor-window/scissorwindow.cpp
# sed -i '/(!w->isPaintingEnabled() || (mask & PAINT_WINDOW_LANCZOS)/,+2d' plugins/kwineffects/scissor-window/scissorwindow.cpp
sed -i '/add_subdirectory(kdecoration)/d' plugins/CMakeLists.txt
%endif

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} \
         -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
         -DUSE_WINDOW_TOOL=OFF \
         -DENABLE_BUILTIN_BLUR=OFF \
         -DENABLE_KDECORATION=ON \
         -DENABLE_BUILTIN_MULTITASKING=OFF \
         -DENABLE_BUILTIN_BLACK_SCREEN=OFF \
%if "%{kwin_version}" >= "%{kwin_max}"
         -DENABLE_BUILTIN_SCISSOR_WINDOW=OFF \
%endif
         -DUSE_DEEPIN_WAYLAND=OFF
%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/kwin/*/*/LICENSE

rm -rf \
    %{buildroot}%{_sysconfdir}/xdg/kwinrc \
    %{buildroot}%{_sysconfdir}/xdg/kdeglobals
    
rm -rf %{buildroot}%{_libdir}/libkwin.so

%fdupes %{buildroot}

%post -n libkwin-xcb%{sover} -p /sbin/ldconfig

%postun -n libkwin-xcb%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md
%license LICENSE
%config %{_sysconfdir}/xdg/*
%{_bindir}/kwin_no_scale
%dir %{_datadir}/kwin
%dir %{_datadir}/kwin/scripts
%dir %{_datadir}/kwin/tabbox
%{_datadir}/kwin/scripts/*
%{_datadir}/kwin/tabbox/*
%{_bindir}/deepin-wm-dbus
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/com.deepin.wm.service
%{_kf5_plugindir}/platforms/libdde-kwin-xcb.so
%if "%{kwin_version}" <= "%{kwin_max}"
%{_kf5_plugindir}/org.kde.kdecoration2/libdeepin-chameleon.so
%dir %{_kf5_plugindir}/kwin/effects/plugins/
#%{_kf5_plugindir}/kwin/effects/plugins/libblur.so
# %{_kf5_plugindir}/kwin/effects/plugins/libmultitasking.so
%{_kf5_plugindir}/kwin/effects/plugins/libscissor-window.so
%else
# %{_libdir}/libkwin.so
%endif
%{_kf5_plugindir}/platforms/libdde-kwin-wayland.so

%files -n libkwin-xcb%{sover}
%defattr(-,root,root,-)
%{_libdir}/libkwin-xcb.so.*

%files lang
%defattr(-,root,root,-)
%{_datadir}/dde-kwin-xcb

%files devel
%defattr(-,root,root,-)
%{_libdir}/libkwin-xcb.so
%{_includedir}/%{_name}
%{_libdir}/pkgconfig/dde-kwin.pc

%changelog


