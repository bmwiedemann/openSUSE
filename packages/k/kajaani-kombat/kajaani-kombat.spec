#
# spec file for package kajaani-kombat
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           kajaani-kombat
Version:        0.7
Release:        0
Summary:        A remake of the classic arcade game Rampart
License:        GPL-2.0-only
Group:          Amusements/Games/Action/Arcade
URL:            http://kombat.kajaani.net/
Source0:        http://kombat.kajaani.net/dl/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-fullscreen.desktop
Patch0:         %{name}-fix-build.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sdl)

%description
A remake of the classis arcade game Rampart, with the change
of the medieval world to a space-world.
Playable on one machine but also over the net with 2-4 players (2 players
may always use the same machine).

This package includes the client binary with built-in server.

%package server
Summary:        Dedicated server for kajaani-kombat, a remake of the arcade game Rampart
Group:          Amusements/Games/Action/Arcade

%description server
A remake of the classis arcade game Rampart, with the change
of the medieval world to a space-world.
Playable on one machine but also over the net with 2-4 players (2 players
may always use the same machine).

This subpackage includes the server binary.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags}"
make all server %{?_smp_mflags}

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0755 %{name}-server %{buildroot}/%{_bindir}/%{name}-server
install -d %{buildroot}/%{_datadir}/%{name}
install -m 0644 *.{png,ttf,ogg} %{buildroot}/%{_datadir}/%{name}
install -D -m 0644 kajaani-kombat.6 %{buildroot}/%{_mandir}/man6/%{name}.6%{?ext_man}

# Install icons and desktop file
for size in 256 128 96 64 48 32 16; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps"
    convert -strip 1face.png -resize "$size"x"$size" %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps/%{name}.png"
done
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/%{name}-fullscreen.desktop

%fdupes -s %{buildroot}/%{_datadir}/%{name}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/kajaani-kombat
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-fullscreen.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6%{?ext_man}

%files server
%{_bindir}/kajaani-kombat-server

%changelog
