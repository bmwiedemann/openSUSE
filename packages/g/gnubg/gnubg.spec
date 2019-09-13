#
# spec file for package gnubg
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gnubg
Version:        1.06.002
Release:        0
Summary:        Backgammon game with analysis tools and neural network AI
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
Url:            http://www.gnubg.org
Source:         http://gnubg.org/media/sources/gnubg-release-%{version}-sources.tar.gz
Source1:        %{name}.desktop
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  glibc-devel
%if 0%{?suse_version} != 1230
BuildRequires:  glu-devel
BuildRequires:  gtkglext-devel
%endif
BuildRequires:  gmp-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  python-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1120
BuildRequires:  libpng-devel >= 1.4
%else
BuildRequires:  libpng-devel
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
Recommends:     gnubg-databases = %{version}
Recommends:     gnubg-sounds = %{version}
Recommends:     gnubg-doc = %{version}
Recommends:     python-MySQL-python
BuildRequires:  sqlite3-devel
%endif
%if 0%{?fedora}
BuildRequires:  sqlite-devel
%endif
Recommends:     %{name}-lang

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

%description databases
Precalculated GNU Backgammon bearoff databases - its intelligence. If you prefer
a stronger or weaker opponent calculate you own with tweaked parameters
according to the documentation.

%package sounds
Summary:        Sounds for gnubg
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
Requires:       %{name} = %{version}

%description sounds
Sounds for GNU Backgammon. See description of gnubg for more details.

%package doc
Summary:        Documentation for gnubg
License:        GFDL-1.3-only
Group:          Amusements/Games/Board/Other

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

%build
autoreconf -fi
export SUSE_ASNEEDED=1
simd=no
%ifarch %ix86 x86_64
simd=sse2
%endif
%configure --docdir=%{_docdir}/%{name} --enable-simd=$simd
make %{?_smp_mflags}

%install
%make_install

DOC="ABOUT-NLS COPYING NEWS README TODO"
install -m 0644 $DOC %{buildroot}/%{_docdir}/%{name}/

%if 0%{?suse_version}
%suse_update_desktop_file -i %{name}
%endif
%find_lang %{name}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man?/%{name}*
%{_mandir}/man?/bearoffdump.*
%{_mandir}/man?/makebearoff.*
%{_mandir}/man?/makehyper.*
%{_mandir}/man?/makeweights.*

%if 0%{?suse_version}
%{_datadir}/applications/gnubg.desktop
%endif
%{_datadir}/icons/hicolor/*/apps/gnubg.png
%{_datadir}/gnubg
%attr(755, -, root) %{_datadir}/gnubg/scripts/query_player.sh
%exclude %{_datadir}/gnubg/*.bd
%exclude %{_datadir}/gnubg/sounds
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/images
%exclude %{_docdir}/%{name}/gnubg.html
%exclude %{_docdir}/%{name}/allabout.html

%files databases
%defattr(-,root,root)
%{_datadir}/gnubg/*.bd

%files sounds
%defattr(-,root,root)
%{_datadir}/gnubg/sounds

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}/images
%doc %{_docdir}/%{name}/gnubg.html
%doc %{_docdir}/%{name}/allabout.html

%files lang -f %{name}.lang

%changelog
