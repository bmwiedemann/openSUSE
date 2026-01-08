#
# spec file for package widelands
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# widelands needs gcc-c++ >= 8 at least according to sr#1270958
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%global force_gcc_version 13
%endif
# Build against glew for Leap 15.X, Leap 16.X
%if 0%{?suse_version} < 1650
%bcond_without glew
%else
# ...but disable glew and build with glbinding for Tumbleweed
%bcond_with glew
%endif
Name:           widelands
Version:        1.3
Release:        0
Summary:        Realtime strategy game involving map control
License:        GPL-2.0-or-later
URL:            https://www.widelands.org
Source0:        https://codeberg.org/wl/widelands/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildRequires:  cmake >= 3.12
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base >= 1.5.2
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(asio)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpng) >= 1.6
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
%if %{with glew}
BuildRequires:  glew-devel
%else
BuildRequires:  glbinding-devel
%endif
Requires:       %{name}-data = %{version}

%description
Widelands is a real-time strategy (RTS) game with singleplayer
campaigns and a multiplayer mode. The game was inspired by Settlers II
(Bluebyte) but has significantly more variety and depth to it.

The primary goal of this type of RTS is to build a settlement with a
functioning economy, producing sufficient military units so as to
conquer rival territories, ultimately gaining control of either the
entire map, or a certain predetermined section of it.

%package data
Summary:        Data files for Widelands
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Data files for Widelands. Includes localization, maps graphics and music.

%package debug
Summary:        Debugging tools for Widelands

%description debug
Additional debugging data for Widelands. This package is not needed for normal
operation.

%prep
%autosetup -p1 -n %{name}

sed -i '/wl_add_flag(WL_COMPILE_DIAGNOSTICS "-Werror=uninitialized")/d' CMakeLists.txt
sed -i 's/\(install(TARGETS ${NAME} DESTINATION \)"."\( COMPONENT ExecutableFiles)\)/\1bin\2/' cmake/WlFunctions.cmake
find . -type f -name "*.py" -exec sed -i -E 's/env python[3]?/python3/' {} \;

%build
%if 0%{?force_gcc_version}
export CXX="g++-%{force_gcc_version}"
%endif

mkdir -p build/locale
%define __builder ninja

%cmake \
  -DWL_INSTALL_BINDIR=%{_bindir} \
  -DWL_INSTALL_DATADIR=%{_datadir}/%{name} \
  -DCMAKE_BUILD_TYPE=Release \
  -DOPTION_USE_GLBINDING=%{?with_glew:OFF}%{!?with_glew:ON} \
  %{?nil}

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}

rm -f %{buildroot}%{_prefix}/{COPYING,CREDITS,ChangeLog,VERSION}

%check
# No need to execute tests as they are already executed implicitly on install
# instead do trivial post-install test
PATH=%{buildroot}%{_bindir}:$PATH %{name} --help | grep 'This is Widelands'

%files
%license COPYING
%doc CREDITS ChangeLog
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/org.widelands.Widelands.png
%{_datadir}/applications/org.widelands.Widelands.desktop
%{_mandir}/man6/%{name}.*
%{_datadir}/metainfo/org.widelands.Widelands.metainfo.xml

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/[^l]*

%files debug
%{_bindir}/wl_*

%changelog
