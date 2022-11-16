#
# spec file for package naev
#
# Copyright (c) 2022 SUSE LLC
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
Version:        0.9.4
Release:        0
Summary:        2D action RPG space game
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Other
URL:            http://naev.org/
Source:         %{name}-%{version}-source.tar.xz
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  glpk-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  libphysfs-devel
BuildRequires:  libpng-devel
BuildRequires:  libunibreak-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxml2-devel
BuildRequires:  luajit-devel
BuildRequires:  meson
BuildRequires:  openal-soft-devel
BuildRequires:  python3-pyaml
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel
BuildRequires:  update-desktop-files

%description
Naev is a 2D space trading and combat game, in a similar vein to Escape Velocity.

Naev is played from a top-down perspective, featuring fast-paced combat, many ships,
a large variety of equipment and a large galaxy to explore. The game is
open-ended, letting you proceed at your own pace.

%prep
%setup -q -n naev-%{version}

%build
meson setup -Dprefix=%{_prefix} build .
cd build
meson compile

%install
cd build
DESTDIR="%{buildroot}" meson install

# Already handle doc files
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Clean up some scripts
find %{buildroot}%{_datadir}/%{name} -name '*.sh' -exec rm {} \;

%suse_update_desktop_file org.naev.Naev

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc LICENSE Readme.md CHANGELOG dat/AUTHORS
%doc %{_mandir}/man6/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/icons/hicolor/*x*/apps/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%lang(de) %{_datadir}/%{name}/dat/gettext/de/LC_MESSAGES/naev.mo
%lang(ja) %{_datadir}/%{name}/dat/gettext/ja/LC_MESSAGES/naev.mo
%lang(ko) %{_datadir}/%{name}/dat/gettext/ko/LC_MESSAGES/naev.mo

%changelog
