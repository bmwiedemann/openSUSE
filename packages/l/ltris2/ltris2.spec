#
# spec file for package ltris2
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


Name:           ltris2
Version:        2.0.3
Release:        0
Summary:        Tetris Clone with Multiplayer and CPU Opponents
License:        GPL-3.0-or-later
URL:            https://github.com/kulkanie/ltris2
Source:         https://download.sourceforge.net/lgames/ltris/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)

%lang_package

%description
LTris2 is a highly configurable, polished, HD-screen ready Tetris clone. It
offers the well-known Classic game, a funny game type Figures (a new figure
each level, suddenly appearing tiles and lines), and multiplayer against up
to two CPU players or human versus human.

%prep
%autosetup -p1

%build
%configure \
  %{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/%{name}

%files
%license COPYING
%doc Changelog README
%{_bindir}/ltris2
%{_datadir}/ltris2/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# Do not use world-writable hiscore file
%exclude %{_localstatedir}/%{name}.hscr

%files lang -f %{name}.lang

%changelog
