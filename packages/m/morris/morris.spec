#
# spec file for package morris
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           morris
Version:        0.3
Release:        0
Summary:        Nine men's morris game
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            http://nine-mens-morris.net/index.html
Source:         http://nine-mens-morris.net/data/%{name}-%{version}.tar.bz2
Source1:        morris.6
Patch0:         workaround_autotools.patch
Patch1:         localedir.patch
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libicu-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4

%description
Morris is an implementation of the board game "Nine Men's Morris".
Other names for this game are: Mills, Merrills, Morris, or Mühle in
German.
This implementation of Nine Men's Morris supports not only the
standard game, but also several rule-variants and different board
layouts. You can play against the computer, or simply use the
program to present the board, but play against another human
opponent. The computer opponent learns from previous games and
tries not to make the same mistake twice.

Among others, the game plays the following variants:
  * Lasker variant (moves are also allowed in the set-phase)
  * the Möbius board (invented by Ingo Althöfer)
  * the Windmill board
  * Pentagon and Hexagon boards
  * Morabaraba
  * Six and Seven Men's Morris
  * Tapatan, Achi, Nine Holes

Furthermore, the game supports:
  * advanced AI controls to tweak AI playing style
  * giving hints for good moves
  * showing the principal variation
  * move takeback (undo and redo)
  * internationalization (English, German, Chinese)
  * many board and rule variations, as well as free customization
    of rules
  * configurable display

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -Wno-return-type"
autoreconf -fiv
%configure
%make_build

%install
%make_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man6/%{name}.6
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_datadir}/glib-2.0/schemas/net.nine-mens-morris.gschema.xml
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
