#
# spec file for package lbreakouthd
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019-2023, Martin Hauke <mardnh@gmx.de>
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


Name:           lbreakouthd
Version:        1.1.2
Release:        0
Summary:        Classic Breakout-Style Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Breakout
URL:            https://lgames.sourceforge.net/LBreakoutHD/
Source:         https://downloads.sourceforge.net/project/lgames/%{name}/%{name}-%{version}.tar.gz
Source1:        https://sourceforge.net/projects/lgames/files/add-ons/lbreakout2/lbreakout2-levelsets-20160512.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(sdl2)
Requires(post): user(games)

%description
LBreakoutHD is a scaleable 16:9 remake of LBreakout2, a Breakout-style
arcade game for Linux featuring a number of added graphical enhancements
and effects. You control a paddle at the bottom of the playing field
and must destroy bricks at the top by bouncing balls against them.

%prep
%autosetup -p1

%build
%configure \
  --localstatedir=%{_localstatedir}/games
%make_build

%install
%make_install
%suse_update_desktop_file -r -G "Breakout-like Game" %{name} Game ArcadeGame

## install levels
tar -xf %{SOURCE1} -C %{buildroot}%{_datadir}/%{name}/levels

# Remove global hiscores files, not needed after Patch0
rm %{buildroot}%{_localstatedir}/games/*

%find_lang %{name}
%fdupes -s %{buildroot}/%{_datadir}

%files -f %{name}.lang
%license COPYING
%doc Changelog README TODO
%{_bindir}/lbreakouthd
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/lbreakouthd.png
%{_datadir}/applications/%{name}.desktop

%changelog
