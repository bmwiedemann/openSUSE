#
# spec file for package naev
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


Name:           naev
Version:        0.11.5
Release:        0
Summary:        2D action RPG space game
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Other
URL:            https://naev.org/
Source:         https://github.com/naev/naev/releases/download/v%{version}/%{name}-%{version}-source.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  glpk-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  luajit-devel
BuildRequires:  meson
BuildRequires:  openal-soft-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-pyaml
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libunibreak)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)

%description
Naev is a 2D space trading and combat game, in a similar vein to Escape Velocity.

Naev is played from a top-down perspective, featuring fast-paced combat, many ships,
a large variety of equipment and a large galaxy to explore. The game is
open-ended, letting you proceed at your own pace.

%prep
%setup -q -n naev-%{version}

# Remove third part libraries so we're guaranteed to use system libraries
rm -rf subprojects/packagefiles

%build
# Disabling C and LUA docs since those are only required if you're hacking on Naev
# Disabling debug because it would need BuildRequires backtrace which is only in available in repo network:cryptocurrencies
%meson \
    -Ddocs_c=disabled \
    -Ddocs_lua=disabled \
    -Ddebug=false
%meson_build

%install
%meson_install

# Remove already handled doc files
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Clean up some unneeded scripts and other development files
find %{buildroot}%{_datadir}/%{name} -name '*.sh' -exec rm {} \;
rm -rf %{buildroot}%{_datadir}/%{name}/dat/lua-repl
rm -rf %{buildroot}%{_datadir}/%{name}/dat/.pre-commit-config.yaml

%suse_update_desktop_file org.naev.Naev

%fdupes %{buildroot}%{_datadir}/%{name}

# find_lang only finds one type of filename, this one all .mo files.
for dir in %{buildroot}/%{_datadir}/naev/dat/gettext/*; do
    for file in "$dir/LC_MESSAGES/"*.mo; do
        echo "%%lang($(basename "$dir")) /$(realpath --relative-to %{buildroot} "$file")" >> %{name}.lang
    done
done

%files -f %{name}.lang
%license LICENSE
%doc Readme.md CHANGELOG dat/AUTHORS
%{_mandir}/man6/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/icons/hicolor/*x*/apps/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
