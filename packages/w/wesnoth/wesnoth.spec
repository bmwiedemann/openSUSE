#
# spec file for package wesnoth
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


%define boost_min_version 1.56
Name:           wesnoth
Version:        1.15.5
Release:        0
Summary:        Fantasy Turn-Based Strategy Game
License:        GPL-2.0-or-later AND EPL-1.0
Group:          Amusements/Games/Strategy/Turn Based
URL:            http://www.wesnoth.org
Source:         https://github.com/wesnoth/wesnoth/archive/%{version}.tar.gz
BuildRequires:  cmake >= 2.8.5
BuildRequires:  dejavu
BuildRequires:  fdupes
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_chrono-devel >= %{boost_min_version}
BuildRequires:  libboost_date_time-devel >= %{boost_min_version}
BuildRequires:  libboost_filesystem-devel >= %{boost_min_version}
BuildRequires:  libboost_iostreams-devel >= %{boost_min_version}
BuildRequires:  libboost_locale-devel >= %{boost_min_version}
BuildRequires:  libboost_program_options-devel >= %{boost_min_version}
BuildRequires:  libboost_random-devel >= %{boost_min_version}
BuildRequires:  libboost_regex-devel >= %{boost_min_version}
BuildRequires:  libboost_system-devel >= %{boost_min_version}
BuildRequires:  libboost_thread-devel >= %{boost_min_version}
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  sazanami-fonts
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL2_image) >= 2.0.0
BuildRequires:  pkgconfig(SDL2_mixer) >= 2.0.0
BuildRequires:  pkgconfig(SDL2_ttf) >= 2.0.12
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig) >= 2.4.1
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(pangocairo) >= 1.22.0
BuildRequires:  pkgconfig(sdl2) >= 2.0.4
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
Obsoletes:      wesnoth-data-base
Obsoletes:      wesnoth-data-full
Obsoletes:      wesnoth-data-small
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

make %{?_smp_mflags} VERBOSE=1

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
