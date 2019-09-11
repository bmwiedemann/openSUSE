#
# spec file for package widelands
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           widelands
Version:        build20
Release:        0
Summary:        Realtime strategy game involving map control
License:        GPL-2.0-or-later
Group:          Amusements/Games/Strategy/Other
Url:            http://www.widelands.org
Source:         https://launchpad.net/%{name}/%{version}/%{version}/+download/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM properly add -lGL as library for correct argument order
Patch1:         build20-libGL.patch
BuildRequires:  SDL2_gfx-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glew-devel
BuildRequires:  graphviz-gnome
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  lua51-devel
BuildRequires:  ninja
BuildRequires:  openSUSE-release
BuildRequires:  optipng
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
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
Group:          Amusements/Games/Strategy/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Data files for Widelands. Includes localization, maps graphics and music.

%package debug
Summary:        Debugging tools for Widelands
Group:          Amusements/Games/Strategy/Other

%description debug
Additional debugging data for Widelands. This package is not needed for normal
operation.

%prep
%setup -q
%patch1 -p1
sed -i '/wl_add_flag(WL_COMPILE_DIAGNOSTICS "-Werror=uninitialized")/d' CMakeLists.txt
sed -i 's/\(install(TARGETS ${NAME} DESTINATION \)"."\( COMPONENT ExecutableFiles)\)/\1bin\2/' cmake/WlFunctions.cmake

%build
mkdir -p build/locale
%define __builder ninja
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DWL_INSTALL_PREFIX=%{_prefix} \
  -DWL_INSTALL_BINDIR=bin \
  -DWL_INSTALL_DATADIR=%{_datadir}/%{name} \
  -DWL_INSTALL_LOCALEDIR=%{_datadir}/%{name}/locale \
  -DCMAKE_BUILD_TYPE="Release" \
  -DBoost_USE_STATIC_LIBS=OFF \
  ..

%make_jobs

%install
%cmake_install

for i in 16 32 48 64 128; do
  install -D -m 0644 data/images/logos/wl-ico-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

install -D -m 0644 debian/org.widelands.widelands.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name} -r Game StrategyGame
desktop-file-edit --set-icon=%{name} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -m 0644 debian/widelands.6 %{buildroot}%{_mandir}/man6/widelands.6

install -D -m 0644 debian/widelands.appdata.xml %{buildroot}%{_datadir}/appdata/widelands.appdata.xml

%fdupes %{buildroot}%{_datadir}

%find_lang %{name} --all-name

rm -f %{buildroot}%{_prefix}/{COPYING,CREDITS,ChangeLog,VERSION}

# No need to execute tests as they are already executed implicitly on install
# instead do post-install test
PATH=%{buildroot}%{_bindir}:$PATH widelands --help | grep 'This is Widelands'

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc CREDITS ChangeLog
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/widelands.*
%{_datadir}/appdata/widelands.appdata.xml

%files data -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/locale/*
%dir %{_datadir}/%{name}/locale/*/LC_MESSAGES
%{_datadir}/%{name}/[^l]*

%files debug
%{_bindir}/wl_*

%changelog
