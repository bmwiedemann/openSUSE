#
# spec file for package 3omns
#
# Copyright (c) 2021 SUSE LLC
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


%if 0%{?suse_version} > 1320
%bcond_without lua53
%else
%bcond_with lua53
%endif
Name:           3omns
Version:        0.2
Release:        0
Summary:        Old-school Arcade-style Tile-based Bomb-dropping Deathmatch Game
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://chaz.human.codes/3omns/
Source:         https://lab.burn.capital/chaz/3omns/-/archive/%{version}/3omns-%{version}.tar.bz2
# PATCH-FEATURE-UPSTREAM -- https://lab.burn.capital/chaz/3omns/-/commit/2567b6150ef773b5f0a53a494779ac23a37153d1
Patch0:         appdata.patch
# PATCH-FEATURE-UPSTREAM upgrade to Lua 5.3 https://lab.burn.capital/chaz/3omns/-/commit/1524b7cc7b8e6e18cc1575118e87ea464d6ae494
Patch1:         lua53.patch
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bitstream-vera-fonts
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_5
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(sdl2)
Requires:       bitstream-vera-fonts
%if %{with lua53}
BuildRequires:  lua53-devel
%else
BuildRequires:  lua-devel < 5.3
BuildRequires:  lua-devel >= 5.2
%endif

%description
3omns is an old-school arcade-style tile-based bomb-dropping deathmatch game.

%prep
%setup -q
%patch0 -p1
%if %{with lua53}
%patch1 -p1
%endif

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

# Use system fonts instead of bundling our own
rm -f %{buildroot}%{_datadir}/%{name}/ttf/Vera.ttf
ln -s ../../fonts/truetype/Vera.ttf %{buildroot}%{_datadir}/%{name}/ttf/Vera.ttf

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}
%dir %{_datadir}/appdata
%{_datadir}/appdata/3omns.appdata.xml

%changelog
