#
# spec file for package xquarto
#
# Copyright (c) 2025 SUSE LLC
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


Name:           xquarto
Version:        2.5
Release:        0
Summary:        Xquarto is a board game designed for the X windows environment
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            ftp://ftp.ac-grenoble.fr/ge/educational_games/
Source:         ftp://ftp.ac-grenoble.fr/ge/educational_games/%name-%version.tar.bz2
Patch0:         xquarto-2.5-imake_font.patch
Patch1:         xquarto-gcc15.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
#%define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
The game is a two-player game. Player 1 chooses one of the 16 pieces.
Player 2 then places this piece on one of the 16 squares of the board
and chooses a piece out of the remaining 15 pieces which he gives to
player 1, who places this piece on one of the remaining 15 squares on
the board, etc...

Xquarto supports three different player combinations: human vs
computer, computer vs human and human vs human (possibly through the
local network in the latter case). The default combination is human vs
computer, i.e. the human player starts the game against the computer.
This can be changed by clicking on the "Actions" menu (see below for
more details).

%prep
%autosetup -p0

%build
xmkmf -a
make %{?jobs:-j%jobs} CCOPTIONS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%files
%defattr(-, root, root)
%{_bindir}/xquarto
%doc %{_xorg7_mandir}/man1/xquarto.1x.gz

%changelog
