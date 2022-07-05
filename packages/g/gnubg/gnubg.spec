#
# spec file for package gnubg
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2003 Achim Mueller, Germany.
# Updated by Christopher Hofmann in 2010
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


Name:           gnubg
Version:        1.06.002
Release:        0
Summary:        Backgammon game with analysis tools and neural network AI
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
URL:            http://www.gnubg.org
Source:         http://gnubg.org/media/sources/gnubg-release-%{version}-sources.tar.gz
Source1:        %{name}.desktop
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  glibc-devel
BuildRequires:  glu-devel
BuildRequires:  gmp-devel
BuildRequires:  gtkglext-devel
BuildRequires:  libcanberra-gtk-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
Recommends:     %{name}-lang
Recommends:     gnubg-databases = %{version}
Recommends:     gnubg-doc = %{version}
Recommends:     gnubg-sounds = %{version}
Recommends:     python3-MySQL-python

%description
Program for playing and analysing backgammon positions, games and matches. It is
based on a neural network. It currently plays at about the level of a
championship flight tournament player. Depending on its parameters and its luck
in recent games, it rates from around 1900 to 2000 on FIBS, the First Internet
Backgammon Server -- at its strongest, it ranks in the top 5 of over 6000 rated
players there and is gradually improving.

%package databases
Summary:        Bearoff databases for gnubg
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description databases
Precalculated GNU Backgammon bearoff databases - its intelligence. If you prefer
a stronger or weaker opponent calculate you own with tweaked parameters
according to the documentation.

%package sounds
Summary:        Sounds for gnubg
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description sounds
Sounds for GNU Backgammon. See description of gnubg for more details.

%package doc
Summary:        Documentation for gnubg
License:        GFDL-1.3-only
Group:          Amusements/Games/Board/Other
BuildArch:      noarch

%description doc
Manual for GNU Backgammon. See description of gnubg for more details.

%lang_package

%prep
%setup -q gnubg
# if we have a glib-gettext.m4 installed in the system, we drop the
# local copy in gnubg. It certainly is older
if [ -f %{_datadir}/aclocal/glib-gettext.m4 ]; then
  rm m4/glib-gettext.m4
fi
# Replace ax_python_devel.m4 for compatibility with Python 3.10.
rm -f m4/ax_python_devel.m4
cp -a %{_datadir}/aclocal/ax_python_devel.m4 m4/

%build
autoreconf -fi
simd=no
%ifarch %{ix86} x86_64
simd=sse2
%endif
%configure --docdir=%{_docdir}/%{name} --enable-simd=$simd
%make_build

%install
%make_install

%suse_update_desktop_file -i %{name}

%find_lang %{name}

%files
%license COPYING
%doc NEWS README TODO
%{_bindir}/*
%{_mandir}/man?/%{name}*
%{_mandir}/man?/bearoffdump.*
%{_mandir}/man?/makebearoff.*
%{_mandir}/man?/makehyper.*
%{_mandir}/man?/makeweights.*
%{_datadir}/applications/gnubg.desktop
%{_datadir}/icons/hicolor/*/apps/gnubg.png
%{_datadir}/gnubg
%attr(755,-,root) %{_datadir}/gnubg/scripts/query_player.sh
%exclude %{_datadir}/gnubg/*.bd
%exclude %{_datadir}/gnubg/sounds
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/images
%exclude %{_docdir}/%{name}/gnubg.html
%exclude %{_docdir}/%{name}/allabout.html

%files databases
%{_datadir}/gnubg/*.bd

%files sounds
%{_datadir}/gnubg/sounds

%files doc
%doc %{_docdir}/%{name}/images
%doc %{_docdir}/%{name}/gnubg.html
%doc %{_docdir}/%{name}/allabout.html

%files lang -f %{name}.lang

%changelog
