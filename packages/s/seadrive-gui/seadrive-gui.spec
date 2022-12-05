#
# spec file for package seadrive-gui
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


Name:           seadrive-gui
Version:        2.0.25
Release:        0
Summary:        GUI part of seafile drive
License:        GPL-3.0-only
URL:            https://github.com/haiwen/seadrive-gui/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch1:         fix-cmake-exec-name.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libsearpc-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(uuid)
Requires:       seadrive-fuse >= 2.0.6
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  jansson-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtconnectivity-devel
BuildRequires:  qt5-qtwebkit
BuildRequires:  sqlite-devel
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebEngineCore)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(sqlite3)
%endif

%description
This package provides a graphical user interface for seadrive-fuse

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags} -fPIE -pie"
export CXXFLAGS="%{optflags} -fPIE -pie"
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_ENABLE_WARNINGS=OFF

%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/seadrive-gui
%{_datadir}/applications/seadrive.desktop

%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/22x22/apps
%dir %{_datadir}/icons/hicolor/24x24/
%dir %{_datadir}/icons/hicolor/24x24/apps
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/128x128/
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/16x16/apps/seadrive.png
%{_datadir}/icons/hicolor/22x22/apps/seadrive.png
%{_datadir}/icons/hicolor/24x24/apps/seadrive.png
%{_datadir}/icons/hicolor/32x32/apps/seadrive.png
%{_datadir}/icons/hicolor/48x48/apps/seadrive.png
%{_datadir}/icons/hicolor/128x128/apps/seadrive.png
%{_datadir}/icons/hicolor/scalable/apps/seadrive.svg

%{_datadir}/pixmaps/seadrive.png

%changelog
