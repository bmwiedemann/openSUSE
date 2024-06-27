#
# spec file for package wesnoth
#
# Copyright (c) 2024 SUSE LLC
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


%define boost_min_version 1.67
Name:           wesnoth
Version:        1.18.1
Release:        0
Summary:        Fantasy Turn-Based Strategy Game
License:        EPL-1.0 AND GPL-2.0-or-later
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://www.wesnoth.org/
# https://github.com/wesnoth/wesnoth/issues/6986 - How about adding a note to the GitHub release page saying "Don't download the tarballs from here"?
Source:         http://files.wesnoth.org/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE wesnoth-cmake-fix-find-readline.patch - cmake 3.20 (used on leap) can't find readline via pkg_check_modules
Patch0:         wesnoth-cmake-fix-find-readline.patch
BuildRequires:  cmake >= 3.14
BuildRequires:  dejavu
BuildRequires:  fdupes
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  libboost_atomic1_75_0-devel
BuildRequires:  libboost_chrono1_75_0-devel
BuildRequires:  libboost_coroutine1_75_0-devel
BuildRequires:  libboost_date_time1_75_0-devel
BuildRequires:  libboost_filesystem1_75_0-devel
BuildRequires:  libboost_graph1_75_0-devel
BuildRequires:  libboost_iostreams1_75_0-devel
BuildRequires:  libboost_locale1_75_0-devel
BuildRequires:  libboost_program_options1_75_0-devel
BuildRequires:  libboost_random1_75_0-devel
BuildRequires:  libboost_regex1_75_0-devel
BuildRequires:  libboost_system1_75_0-devel
BuildRequires:  libboost_thread1_75_0-devel
%else
BuildRequires:  libboost_atomic-devel >= %{boost_min_version}
BuildRequires:  libboost_chrono-devel >= %{boost_min_version}
BuildRequires:  libboost_coroutine-devel >= %{boost_min_version}
BuildRequires:  libboost_date_time-devel >= %{boost_min_version}
BuildRequires:  libboost_filesystem-devel >= %{boost_min_version}
BuildRequires:  libboost_graph-devel >= %{boost_min_version}
BuildRequires:  libboost_iostreams-devel >= %{boost_min_version}
BuildRequires:  libboost_locale-devel >= %{boost_min_version}
BuildRequires:  libboost_program_options-devel >= %{boost_min_version}
BuildRequires:  libboost_random-devel >= %{boost_min_version}
BuildRequires:  libboost_regex-devel >= %{boost_min_version}
BuildRequires:  libboost_system-devel >= %{boost_min_version}
BuildRequires:  libboost_thread-devel >= %{boost_min_version}
%endif
BuildRequires:  libopenssl-3-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  sazanami-fonts
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL2_image) >= 2.0.2
BuildRequires:  pkgconfig(SDL2_mixer) >= 2.0.0
BuildRequires:  pkgconfig(SDL2_ttf) >= 2.0.12
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig) >= 2.4.1
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(pangocairo) >= 1.44.0
BuildRequires:  pkgconfig(sdl2) >= 2.0.10
Requires:       dejavu
Requires:       sazanami-fonts
Requires:       wesnoth-data = %{version}
Requires:       wesnoth-fslayout = %{version}

%description
Battle for Wesnoth is a fantasy turn-based strategy game. Battle for
control of villages, using variety of units which have advantages and
disadvantages in different types of terrains and against different
types of attacks. Units gain experience and advance levels, and are
carried over from one scenario to the next campaign.

%package data
Summary:        Architecture independent data for Battle for Wesnoth
Group:          Amusements/Games/Strategy/Turn Based
Requires:       wesnoth-fslayout
Obsoletes:      wesnoth-data-base <= %{version}
Obsoletes:      wesnoth-data-full <= %{version}
Obsoletes:      wesnoth-data-small <= %{version}
BuildArch:      noarch

%package campaign-server
Summary:        Battle for Wesnoth: campaign server
Group:          Amusements/Games/Strategy/Turn Based
Requires:       wesnoth-fslayout

%package server
Summary:        Multiplayer server for Battle for Wesnoth
Group:          Amusements/Games/Strategy/Turn Based
Requires:       wesnoth-fslayout

%package fslayout
Summary:        Battle for Wesnoth: Basic file system layout
Group:          Amusements/Games/Strategy/Turn Based
BuildArch:      noarch

%description data
This package contains the game data for Battle For Wesnoth.
It is required to play the game.

%description server
This package contains the server program hosting multiplayer games of
Battle for Wesnoth.

%description campaign-server
The campaign server acts as a simple download server, much like ftp, to
provide a collection of Wesnoth campaigns to players.

%description fslayout
This package solely contains the basic file structure in order to have it owned by a package.

%prep
%setup -q
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
%patch -P 0 -p1
%endif

# Fix rpmlint's "E: env-script-interpreter".
sed -i "s:/usr/bin/env python:/usr/bin/python:g" $(find data/tools -type f)

%build
%cmake -DCMAKE_INSTALL_DOCDIR="%{_docdir}/wesnoth" \
       -DENABLE_GAME=ON \
       -DENABLE_CAMPAIGN_SERVER=ON \
       -DENABLE_SERVER=ON \
       -DENABLE_TESTS=OFF \
       -DENABLE_NLS=ON \
       -DENABLE_DESKTOP_ENTRY=ON \
       -DSERVER_UID=root \
       -DSERVER_GID=root
%cmake_build

%install
%cmake_install

# Use system fonts
ln -snf %{_datadir}/fonts/truetype/sazanami-gothic.ttf %{buildroot}/%{_datadir}/%{name}/fonts
ln -snf %{_datadir}/fonts/truetype/DejaVuSans.ttf      %{buildroot}/%{_datadir}/%{name}/fonts

# find_lang only finds one type of filename, this one all .mo files.
for dir in %{buildroot}/%{_datadir}/wesnoth/translations/*; do
    for file in "$dir/LC_MESSAGES/"*.mo; do
        echo "%%lang($(basename "$dir")) /$(realpath --relative-to %{buildroot} "$file")" >> %{name}.lang
    done
done

%fdupes -s %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/org.wesnoth.Wesnoth.desktop
%{_datadir}/icons/hicolor/*/apps/wesnoth-icon.png
%dir %{_datadir}/icons/HighContrast
%dir %{_datadir}/icons/HighContrast/scalable
%dir %{_datadir}/icons/HighContrast/scalable/apps
%{_datadir}/icons/HighContrast/*/apps/wesnoth-icon.*
%{_datadir}/metainfo/org.wesnoth.Wesnoth.appdata.xml
%{_mandir}/man*/wesnoth.*%{ext_man}
%{_mandir}/*/man*/wesnoth.*%{ext_man}

%files data -f %{name}.lang
%license COPYING copyright
%doc changelog.md README.md
%{_datadir}/wesnoth/
%{_docdir}/wesnoth/

%files server
%{_bindir}/%{name}d
%{_mandir}/man*/%{name}d.*%{ext_man}
%{_mandir}/*/man*/%{name}d.*%{ext_man}

%files campaign-server
%{_bindir}/campaignd

%files fslayout
%dir %{_mandir}/bg
%dir %{_mandir}/bg/man6
%dir %{_mandir}/en_GB
%dir %{_mandir}/en_GB/man6
%dir %{_mandir}/et
%dir %{_mandir}/et/man6
%dir %{_mandir}/fi
%dir %{_mandir}/fi/man6
%dir %{_mandir}/fr/man6
%dir %{_mandir}/gl
%dir %{_mandir}/gl/man6
%dir %{_mandir}/hu
%dir %{_mandir}/hu/man6
%dir %{_mandir}/id
%dir %{_mandir}/id/man6
%dir %{_mandir}/it/man6
%dir %{_mandir}/lt
%dir %{_mandir}/lt/man6
%dir %{_mandir}/racv
%dir %{_mandir}/racv/man6
%dir %{_mandir}/sr
%dir %{_mandir}/sr/man6
%dir %{_mandir}/sr@latin
%dir %{_mandir}/sr@latin/man6
%dir %{_mandir}/sr@ijekavian
%dir %{_mandir}/sr@ijekavian/man6
%dir %{_mandir}/sr@ijekavianlatin
%dir %{_mandir}/sr@ijekavianlatin/man6
%dir %{_mandir}/tr
%dir %{_mandir}/tr/man6
%dir %{_mandir}/uk
%dir %{_mandir}/uk/man6
%dir %{_mandir}/vi
%dir %{_mandir}/vi/man6

%changelog
