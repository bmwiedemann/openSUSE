#
# spec file for package solarus
#
# Copyright (c) 2021 SUSE LLC
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


Name:           solarus
Version:        1.6.4
Release:        0
Summary:        Game engine for action RPGs
License:        GPL-3.0-or-later
Group:          Amusements/Games/RPG
URL:            https://www.solarus-games.org/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  physfs-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
Suggests:       %{name}-gui

%description
Solarus is a 2D game engine written in C++, and it executes games
made in Lua. It is designed with 16-bit classic action RPGs in
mind.

This package contains the 'solarus-run' executable required to run
games based on the Solarus engine.

%package gui
Summary:        Graphical user interface to launch Solarus games
# Package "gui" was split from main package on 1.6.1
# Make sure upgrade of main package from version < 1.6.1
# installs "gui" as well with a specific Provides
Group:          Amusements/Games/RPG
Provides:       %{name}:%{_bindir}/solarus-launcher

%description gui
This package provides a graphical user interface to launch games
based on the Solarus engine.

%package -n libsolarus1
Summary:        Solarus game engine shared library
Group:          System/Libraries

%description -n libsolarus1
This package provides the main shared library of the Solarus game
engine.

%package -n libsolarus-gui1
Summary:        Solarus game engine shared library (GUI parts)
Group:          System/Libraries

%description -n libsolarus-gui1
This package provides the GUI shared library of the Solarus game
engine.

%package devel
Summary:        Development files for solarus
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-gui = %{version}

%description devel
Development files for Solarus, including header files.

%lang_package -n solarus-gui

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%if 0%{?suse_version} > 1510
%check
# Tweak path to find libsolarus.so and libsolarus-testing.so
export LD_LIBRARY_PATH="$PWD/build:$PWD/build/tests"
# Tests 1200 and 1210 require a graphical display
%ctest --exclude-regex "lua/bugs/(1200_.*|1210_.*)"
%endif

%post   -n libsolarus1 -p /sbin/ldconfig
%postun -n libsolarus1 -p /sbin/ldconfig
%post   -n libsolarus-gui1 -p /sbin/ldconfig
%postun -n libsolarus-gui1 -p /sbin/ldconfig

%files
%doc changelog.txt readme.md
%license license.txt license_gpl.txt
%{_bindir}/solarus-run
%{_mandir}/man6/solarus-run.6%{?ext_man}

%files gui
%license license.txt license_gpl.txt
%dir %{_datadir}/appdata/
%dir %{_datadir}/icons/hicolor/20x20
%dir %{_datadir}/icons/hicolor/20x20/apps
%{_bindir}/solarus-launcher
%{_datadir}/appdata/solarus-launcher.appdata.xml
%{_datadir}/applications/solarus-launcher.desktop
%{_datadir}/icons/hicolor/*/apps/solarus-launcher*
%{_datadir}/pixmaps/solarus-launcher.png
%{_mandir}/man6/solarus-launcher.6%{?ext_man}

%files gui-lang -f %{name}.lang
%dir %{_datadir}/%{name}-gui
%dir %{_datadir}/%{name}-gui/translations

%files -n libsolarus1
%{_libdir}/libsolarus.so.*

%files -n libsolarus-gui1
%{_libdir}/libsolarus-gui.so.*

%files devel
%{_includedir}/solarus
%{_libdir}/libsolarus.so
%{_libdir}/libsolarus-gui.so

%changelog
