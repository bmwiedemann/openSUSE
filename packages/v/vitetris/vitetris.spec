#
# spec file for package vitetris
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2024, Martin Hauke <mardnh@gmx.de>
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


%bcond_without ncurses
# build with support for allegro - disabled by default
%bcond_with allegro
Name:           vitetris
Version:        0.59.1
Release:        0
Summary:        Terminal-based Tetris clone
License:        BSD-2-Clause
Group:          Amusements/Games/Action/Arcade
URL:            http://victornils.net/tetris/
#Git-Clone:     https://github.com/vicgeralds/vitetris.git
Source:         https://github.com/vicgeralds/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vitetris.6
Patch6:         vitetris-fix-font-path.patch
Patch7:         vitetris-fix-gcc14.patch
%if 0%{with allegro}
BuildRequires:  liballeg-devel
%endif
%if 0%{with ncurses}
BuildRequires:  ncurses-devel
%endif

%description
Vitetris is a terminal-based Tetris game. It can be played by one or
two players, over the network or on the same keyboard.

Vitetris comes with customizable appearance and netplay where both
players can choose difficulty (level and height). (No sound, though.)

Rotation, scoring, levels and speed resembles the early Tetris
games by Nintendo, with the addition of a short lock delay which
makes it possible to play at higher levels. (It does not make it
possible to prevent the piece from ever locking by abusing lock delay
resets.)

%prep
%autosetup -p1

sed -i 's|Exec=tetris|Exec=vitetris|' vitetris.desktop

%build
./configure \
    --prefix=%{_prefix} \
    --datarootdir=%{_datadir} \
%if 0%{with allegro}
    --with-allegro \
%else
    --without-allegro \
%endif
%if 0%{with ncurses}
    --with-ncurses \
%else
    --without-ncurses \
%endif
    --with-2player \
    --with-network \
    --with-term_resizing \
    --with-menu \
    --with-blockstyles \
    --with-pctimer

make CFLAGS='%{optflags} -Wno-return-type' %{?_smp_mflags}

%install
%make_install
install -Dm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man6/vitetris.6
mv %{buildroot}%{_bindir}/tetris %{buildroot}%{_bindir}/vitetris
rm -fR %{buildroot}%{_datadir}/doc/vitetris/

%files
%doc README changes.txt
%license licence.txt
%{_bindir}/vitetris
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%if 0%{with allegro}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pc8x16.fnt
%endif

%changelog
