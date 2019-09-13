#
# spec file for package plee-the-bear
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           plee-the-bear
Version:        0.7.0
Release:        0
Summary:        Plee the Bear, a 2D platform game
License:        GPL-2.0+
Group:          Amusements/Games/Other
Url:            http://www.stuff-o-matic.com/ptb/
Source:         http://www.stuff-o-matic.com/plee-the-bear/download/file.php?platform=source#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM to be built via gcc6+.
Patch0:         ptb-sequencer-gcc6.patch
BuildRequires:  SDL_mixer-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
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
%setup -q -n %{name}-%{version}-light
%patch0

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -Wno-dev \
       -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib}/%{name} \
       -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib}/%{name} \
       -DBEAR_EDITORS_ENABLED=False
make V=1 %{?_smp_mflags}

%install
%cmake_install

# Translations
%find_lang %{name}
%find_lang bear-engine
cat bear-engine.lang >>%{name}.lang

%suse_update_desktop_file -r plee-the-bear 'Game;ArcadeGame;'

# W: non-executable-script
chmod +x %{buildroot}%{_datadir}/%{name}/gfx/title_screen/mk.sh
chmod +x %{buildroot}%{_datadir}/%{name}/gfx/forest/bk/*/mk.sh

%fdupes -s %{buildroot}%{_datadir}

%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%doc %{name}/LICENSE %{name}/README.md %{name}/license/*
%{_datadir}/applications/%{name}.desktop

%files data -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/%{name}
%dir %{_datadir}/bear-factory
%{_datadir}/bear-factory/%{name}
%{_datadir}/icons/hicolor/*/apps/ptb.png
%{_datadir}/pixmaps/ptb.*
%{_datadir}/cmake/bear-engine

%changelog
