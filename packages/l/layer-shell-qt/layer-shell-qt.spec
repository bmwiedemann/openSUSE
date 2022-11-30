#
# spec file for package layer-shell-qt
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021 Fabian Vogt
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


# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}

%bcond_without released
Name:           layer-shell-qt
Version:        5.26.4
Release:        0
Summary:        wlr-layer-shell integration for Qt
License:        LGPL-3.0-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/layer-shell-qt-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/layer-shell-qt-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5XkbCommonSupport)
# Workaround missing requirement in libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.1
BuildRequires:  pkgconfig(wayland-client) >= 1.3.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server) >= 1.3.0

%description
This allows integration of Qt applications with wlr-layer-shell.

%package -n layer-shell-qt5
Summary:        wlr-layer-shell integration for Qt 5
Group:          Development/Libraries/KDE

%description -n layer-shell-qt5
This allows integration of Qt applications with wlr-layer-shell.

%package -n layer-shell-qt5-devel
Summary:        wlr-layer-shell integration for Qt 5 - development files
Group:          Development/Libraries/KDE
Requires:       layer-shell-qt5 = %{version}
Requires:       libqt5-qtwayland-private-headers-devel
Requires:       cmake(Qt5Qml)
Requires:       pkgconfig(wayland-client) >= 1.3.0

%description -n layer-shell-qt5-devel
This allows integration of Qt applications with wlr-layer-shell.

%prep
%autosetup -p1

%build
# Qt5XkbCommonSupportPrivate doesn't link publicly against xkbcommon
export CXXFLAGS="%optflags $(pkg-config xkbcommon --cflags)"
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%post -n layer-shell-qt5 -p /sbin/ldconfig
%postun -n layer-shell-qt5 -p /sbin/ldconfig

%files -n layer-shell-qt5
%license LICENSES/*.txt
%{_kf5_plugindir}/wayland-shell-integration/liblayer-shell.so
%{_kf5_libdir}/libLayerShellQtInterface.so.5
%{_kf5_libdir}/libLayerShellQtInterface.so.%{_plasma5_bugfix}

%files -n layer-shell-qt5-devel
%{_kf5_libdir}/libLayerShellQtInterface.so
%{_kf5_libdir}/cmake/LayerShellQt/
%{_includedir}/LayerShellQt/

%changelog
