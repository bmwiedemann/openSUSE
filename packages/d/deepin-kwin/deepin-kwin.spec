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

Name:           deepin-kwin
Version:        5.2.0.13
Release:        0
Summary:        KWin configures/plugins on the DDE
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Url:            https://github.com/linuxdeepin/dde-kwin
Source0:        https://github.com/linuxdeepin/dde-kwin/archive/%{version}/%{_name}-%{version}.tar.gz
# Source0:        https://github.com/ukui/dde-kwin/archive/%{commit}/%{_name}-%{shortcommit}.tar.gz
Patch1:         deepin-kwin-unload-blur.patch
Patch0:         deepin-kwin-tabbox-chameleon-rename.patch
%if 0%{suse_version} > 1500
Patch2:         deepin-kwin-crash.patch
Patch4:         support-kwin-5_19+.patch
Patch5:         support-kwin-5_21+.patch
BuildRequires:  cmake(KWaylandServer)
%else
Patch3:         fix-crash-bug.patch
%endif
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%build
sed -i 's|backgrounds/default_background.jpg|wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|g' \
deepin-wm-dbus/deepinwmfaker.cpp plugins/kwineffects/multitasking/background.cpp
sed -i 's/lrelease/lrelease-qt5/g' plugins/platforms/plugin/translate_generation.sh
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} \
         -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%make_jobs

%install
%cmake_install

chmod 0644 %{buildroot}%{_datadir}/kwin/tabbox/chameleon/contents/ui/main.qml \
           %{buildroot}%{_datadir}/kwin/tabbox/chameleon/metadata.desktop
           
chmod +x %{buildroot}%{_bindir}/kwin_no_scale 
rm -rf %{buildroot}%{_datadir}/kwin/*/*/LICENSE

rm -rf %{buildroot}%{_datadir}/kwin/tabbox/thumbnail_grid/metadata.desktop \
%{buildroot}%{_datadir}/kwin/tabbox/thumbnail_grid/contents/ui/main.qml \
%{buildroot}%{_sysconfdir}/xdg/kwinrc \
%{buildroot}%{_sysconfdir}/xdg/kdeglobals
           
%fdupes %{buildroot}

%post -n libkwin-xcb%{sover} -p /sbin/ldconfig

%postun -n libkwin-xcb%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md
%license LICENSE
%config %{_sysconfdir}/xdg/*
%{_bindir}/deepin-wm-dbus
%{_bindir}/kwin_no_scale
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/com.deepin.wm.service
%dir %{_datadir}/kwin
%dir %{_datadir}/kwin/scripts
%dir %{_datadir}/kwin/tabbox
%{_datadir}/kwin/scripts/*
%{_datadir}/kwin/tabbox/*
%{_kf5_plugindir}/platforms/libdde-kwin-xcb.so
%{_kf5_plugindir}/org.kde.kdecoration2/libdeepin-chameleon.so
%dir %{_kf5_plugindir}/kwin/effects/plugins/
%{_kf5_plugindir}/kwin/effects/plugins/libblur.so
%{_kf5_plugindir}/kwin/effects/plugins/libmultitasking.so
%{_kf5_plugindir}/kwin/effects/plugins/libscissor-window.so
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

