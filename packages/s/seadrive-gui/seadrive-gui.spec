#
# spec file for package seadrive-gui
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Version:        3.0.24
Release:        0
Summary:        GUI part of seafile drive
License:        GPL-3.0-only
URL:            https://github.com/haiwen/seadrive-gui/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch1:         fix-cmake-exec-name.patch
# PATCH-FIX-UPSTREAM
Patch2:         fix-return-value.patch
# PATCH-FIX-UPSTREAM
Patch3:         issue446.patch
# PATCH-FIX-UPSTREAM
Patch4:         fix-cmake-link-signature.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libsearpc-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
Requires:       hicolor-icon-theme
Requires:       seadrive-fuse >= 3.0.18
# Qt6 WebEngine is not available on 32-bit architectures
ExcludeArch:    %{ix86} %{arm}

%description
This package provides a graphical user interface for seadrive-fuse

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fPIE -pie"
export CXXFLAGS="%{optflags} -fPIE -pie"
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_ENABLE_WARNINGS=OFF \
  %{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%license LICENSE
%{_bindir}/seadrive-gui
%{_datadir}/applications/seadrive.desktop

%{_datadir}/icons/hicolor/16x16/apps/seadrive.png
%{_datadir}/icons/hicolor/22x22/apps/seadrive.png
%{_datadir}/icons/hicolor/24x24/apps/seadrive.png
%{_datadir}/icons/hicolor/32x32/apps/seadrive.png
%{_datadir}/icons/hicolor/48x48/apps/seadrive.png
%{_datadir}/icons/hicolor/128x128/apps/seadrive.png
%{_datadir}/icons/hicolor/scalable/apps/seadrive.svg

%{_datadir}/pixmaps/seadrive.png

%changelog
