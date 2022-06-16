#
# spec file for package deepin-kwin
#
# Copyright (c) 2022 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define   _name           dde-kwin
%define   sover           0
%define   kwin_version    %(rpm -q --queryformat '%%{VERSION}' kwin5)
%define   kwin_max        5.21.5

Name:           deepin-kwin
Version:        5.4.12
Release:        0
Summary:        KWin configures/plugins on the DDE
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dde-kwin
Source0:        https://github.com/linuxdeepin/dde-kwin/archive/%{version}/%{_name}-%{version}.tar.gz
Patch0:         deepin-kwin-tabbox-chameleon-rename.patch
%if 0%{suse_version} > 1500 || 0%{?sle_version} > 150300
Patch1:         deepin-kwin-crash.patch
%endif
# PATCH-FIX-UPSTRAM fix-library-links.patch hillwood@opensuse.org - Fix build on Tumbleweed
# https://github.com/linuxdeepin/dde-kwin/pull/154
Patch2:         fix-library-links.patch
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  kwin5-devel
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformSupport-devel-static
BuildRequires:  libepoxy-devel
BuildRequires:  libqt5-linguist
BuildRequires:  plasma5-workspace-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(xcb)
Requires:       dbus-1
Requires:       deepin-wallpapers
Requires:       kwin5
Provides:       deepin-kwin5
%if "%{kwin_version}" > "%{kwin_max}"
BuildArch:      noarch
%endif

%description
KWin configures/plugins on the DDE
Let kwin work well in the Deepin Desktop Environment.

%if "%{kwin_version}" <= "%{kwin_max}"
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
%endif

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
%cmake_build

%install
%cmake_install

%if "%{kwin_version}" <= "%{kwin_max}"
chmod -x %{buildroot}%{_datadir}/kwin/tabbox/chameleon/contents/ui/main.qml \
           %{buildroot}%{_datadir}/kwin/tabbox/chameleon/metadata.desktop
%endif

chmod +x %{buildroot}%{_bindir}/kwin_no_scale
rm -rf %{buildroot}%{_datadir}/kwin/*/*/LICENSE

rm -rf \
%if "%{kwin_version}" <= "%{kwin_max}"
    %{buildroot}%{_datadir}/kwin/tabbox/thumbnail_grid/metadata.desktop \
    %{buildroot}%{_datadir}/kwin/tabbox/thumbnail_grid/contents/ui/main.qml \
%endif
    %{buildroot}%{_sysconfdir}/xdg/kwinrc \
    %{buildroot}%{_sysconfdir}/xdg/kdeglobals

%fdupes %{buildroot}

%if "%{kwin_version}" <= "%{kwin_max}"
%post -n libkwin-xcb%{sover} -p /sbin/ldconfig

%postun -n libkwin-xcb%{sover} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md
%license LICENSE
%config %{_sysconfdir}/xdg/*
%{_bindir}/kwin_no_scale
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150300
%dir %{_datadir}/kwin
%dir %{_datadir}/kwin/scripts
%dir %{_datadir}/kwin/tabbox
%{_datadir}/kwin/scripts/*
%{_datadir}/kwin/tabbox/*
%{_bindir}/deepin-wm-dbus
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/com.deepin.wm.service
%{_kf5_plugindir}/platforms/libdde-kwin-xcb.so
%{_kf5_plugindir}/org.kde.kdecoration2/libdeepin-chameleon.so
%dir %{_kf5_plugindir}/kwin/effects/plugins/
%{_kf5_plugindir}/kwin/effects/plugins/libblur.so
%{_kf5_plugindir}/kwin/effects/plugins/libmultitasking.so
%{_kf5_plugindir}/kwin/effects/plugins/libscissor-window.so
%{_kf5_plugindir}/platforms/libdde-kwin-wayland.so
%endif

%if "%{kwin_version}" <= "%{kwin_max}"
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
%endif

%changelog
