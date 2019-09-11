#
# spec file for package teeworlds
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           teeworlds
Version:        0.7.3.1
Release:        0
Summary:        A retro multiplayer jump-and-swing shooter
License:        Zlib AND CC-BY-SA-3.0
Group:          Amusements/Games/Action/Arcade
URL:            http://www.teeworlds.com
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  dejavu-fonts
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pnglite-devel
BuildRequires:  python
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)
Requires:       dejavu-fonts
Provides:       teewars = %{version}
Obsoletes:      teewars < 0.4.0

%description
Teeworlds is an online multiplayer game. Battles can be played with
up to 16 players in a variety of game modes, including Team
Deathmatch and Capture The Flag. Own maps can be designed.

%prep
%setup -q

# we use system libs instead
rm -r src/engine/external/{pnglite,wavpack,zlib}

# Fix line-endings
sed -i 's/\r$//' readme.md

%build
%cmake

%install
%cmake_install
install -D -m 0644 other/teeworlds.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
index=0
for res in 256 128 48 32 24 16; do
    install -d "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps"
    convert -strip "other/icons/teeworlds.ico[$index]" "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps/%{name}.png"
    index=$((index+1))
done
%suse_update_desktop_file %{name}
install -D -m 0644 other/teeworlds.appdata.xml %{buildroot}%{_datadir}/appdata/teeworlds.appdata.xml

# Unbundle DejaVu font
rm -rf %{buildroot}%{_datadir}/%{name}/data/fonts/*
ln -s %{_ttfontsdir}/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/data/fonts/DejaVuSans.ttf

%if 0%{?suse_version} < 1330
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%license license.txt
%doc readme.md
%{_bindir}/teeworlds
%{_bindir}/teeworlds_srv
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
