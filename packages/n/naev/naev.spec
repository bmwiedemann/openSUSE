#
# spec file for package naev
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


Name:           naev
Version:        0.8.1
Release:        0
Summary:        2D action RPG space game
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Other
URL:            http://naev.org/
Source0:        %{name}-%{version}-source.tar.gz
Source1:        %{name}-%{version}-overlay.tar.gz
BuildRequires:  SDL2-devel
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libSDL2_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua51-devel
BuildRequires:  openal-soft-devel
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files

%description
Naev is a 2D space trading and combat game, in a similar vein to Escape Velocity.

Naev is played from a top-down perspective, featuring fast-paced combat, many ships,
a large variety of equipment and a large galaxy to explore. The game is
open-ended, letting you proceed at your own pace.

%prep
%autosetup -b1

%build
# Remove 'docs' directory - fails in configure script, not needed for gameplay
rm -r docs

%configure --enable-lua=shared --enable-debug=no
%make_build

%install
%make_install

install -D -m 0644 extras/logos/logo16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/naev.png
install -D -m 0644 extras/logos/logo32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/naev.png
install -D -m 0644 extras/logos/logo64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/naev.png
install -D -m 0644 extras/logos/logo128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/naev.png

# Don't know how to handle locale files yet...
rm -rf %{buildroot}%{_datadir}/locale/

# Already handle doc files
rm -rf %{buildroot}%{_datadir}/doc/%{name}
rm -f %{buildroot}%{_datadir}/%{name}/dat/AUTHORS
rm -f %{buildroot}%{_datadir}/%{name}/dat/LICENSE

# Clean up some scripts
find %{buildroot}%{_datadir}/%{name} -name '*.sh' -exec rm {} \;

%suse_update_desktop_file org.naev.naev

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc LICENSE README TODO dat/AUTHORS
%doc %{_mandir}/man6/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/icons/hicolor/*x*/apps/naev.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%lang(de) %{_datadir}/%{name}/dat/gettext/de/LC_MESSAGES/naev.mo
%lang(ja) %{_datadir}/%{name}/dat/gettext/ja/LC_MESSAGES/naev.mo
%lang(ko) %{_datadir}/%{name}/dat/gettext/ko/LC_MESSAGES/naev.mo

%changelog
