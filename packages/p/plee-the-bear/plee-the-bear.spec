#
# spec file for package plee-the-bear
#
# Copyright (c) 2020 SUSE LLC
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


%define bear_ver 0.0.0.git20200220
Name:           plee-the-bear
Version:        0.7.1
Release:        0
Summary:        Plee the Bear, a 2D platform game
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            https://github.com/j-jorge/plee-the-bear
Source0:        https://github.com/j-jorge/plee-the-bear/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        bear-%{bear_ver}.tar.xz
Source2:        CMakeLists.txt
# PATCH-FIX-UPSTREAM ptb-boost-placeholders.patch
Patch0:         ptb-boost-placeholders.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libxslt-tools
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(SDL2_mixer)
# Cmake suggests it but "parser error" will be got.
BuildConflicts: docbook2x

%description
Plee the Bear is a 2D platform game like those found on consoles in
the beginning of the 1990s. The storyline centeres around an angry
bear whose son has been kidnapped by God.

%package        data
Summary:        Game data files for "Plee the Bear"
License:        CC-BY-SA-3.0
Group:          Amusements/Games/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Plee the Bear is a 2D platform game like those found on consoles in
the beginning of the 1990s. The storyline centeres around an angry
bear whose son has been kidnapped by God.

This subpackage contains the game data files.

%prep
%setup -q -D -T -c -n bear-project -a0
%setup -q -T -D -n bear-project -a1
cp %{S:2} ./
%autopatch -p1

%build
mv %{name}-%{version} %{name}
mv bear-%{bear_ver} bear
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -Wno-dev \
       -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib}/%{name} \
       -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib}/%{name} \
       -DBEAR_EDITORS_ENABLED=False
%cmake_build

%install
%cmake_install

# Move appdata to metainfo dir
mkdir -p %{buildroot}%{_datadir}/metainfo
mv %{buildroot}%{_datadir}/appdata/* %{buildroot}%{_datadir}/metainfo/

# Translations
%find_lang %{name}
%find_lang bear-engine
cat bear-engine.lang >>%{name}.lang

%suse_update_desktop_file -r plee-the-bear 'Game;ArcadeGame;'

# W: non-executable-script
chmod +x %{buildroot}%{_datadir}/%{name}/gfx/title_screen/mk.sh
chmod +x %{buildroot}%{_datadir}/%{name}/gfx/forest/bk/*/mk.sh

%fdupes -s %{buildroot}%{_datadir}

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%doc %{name}/README.md
%license %{name}/LICENSE %{name}/license/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

%files data -f %{name}.lang
%{_datadir}/%{name}
%dir %{_datadir}/bear-factory
%{_datadir}/bear-factory/%{name}
%{_datadir}/icons/hicolor/*/apps/ptb.png
%{_datadir}/pixmaps/ptb.*
%{_datadir}/cmake/bear-engine

%changelog
