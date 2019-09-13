#
# spec file for package 3omns
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} > 1320
%bcond_without lua53
%else
%bcond_with lua53
%endif

Name:           3omns
Version:        0.2
Release:        0
Summary:        Old-school Arcade-style Tile-based Bomb-dropping Deathmatch Game
License:        GPL-3.0+
Group:          Amusements/Games/Action/Arcade
Url:            https://chazomaticus.github.io/3omns/
Source:         https://github.com/chazomaticus/3omns/releases/download/%{version}/3omns-%{version}.tar.xz
# PATCH-FEATURE-UPSTREAM https://github.com/chazomaticus/3omns/pull/4
Patch0:         appdata.patch
# PATCH-FEATURE-UPSTREAM upgrade to Lua 5.3 https://github.com/chazomaticus/3omns/commit/1524b7c
Patch1:         lua53.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bitstream-vera-fonts
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_5
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  xz
%if %{with lua53}
BuildRequires:  lua53-devel
%else
BuildRequires:  lua-devel < 5.3
BuildRequires:  lua-devel >= 5.2
%endif
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(sdl2)
Requires:       bitstream-vera-fonts

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
make %{?_smp_mflags}

%install
%make_install

# Use system fonts instead of bundling our own
rm -f %{buildroot}%{_datadir}/%{name}/ttf/Vera.ttf
ln -s ../../fonts/truetype/Vera.ttf %{buildroot}%{_datadir}/%{name}/ttf/Vera.ttf

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}
%dir %{_datadir}/appdata
%{_datadir}/appdata/3omns.appdata.xml

%changelog
