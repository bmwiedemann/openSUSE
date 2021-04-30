#
# spec file for package opentyrian
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


Name:           opentyrian
# Upstream haven not tagged a version for more than seven years now.
# There quite many bugfixes in the git version and it seems upstreams
# develops it as rolling release.
Version:        2.1.20201203
Release:        0
Summary:        An arcade-style vertical scrolling shooter
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/opentyrian/opentyrian
Source:         %{name}-%{version}.tar.xz
# PATCH-FEATURE-UPSTREAM https://github.com/opentyrian/opentyrian/pull/13
Patch0:         appdata.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)

%description
OpenTyrian is a port of the DOS shoot-em-up Tyrian. Thanks to Jason Emery,
the developers were given a copy of the Tyrian source to port but
not redistribute. That code has since been ported from Turbo Pascal to C
using SDL, making it easily cross-platform. The 'Classic' port involves
minimal changes, but the 'Enhanced' port will feature further development.
Tyrian is an arcade-style vertical scrolling shooter. The story is set
in 20,031 where you play as Trent Hawkins, a skilled fighter-pilot employed
to fight Microsol and save the galaxy.

%prep
%autosetup -p1
chmod -x CREDITS

%build
make %{?_smp_mflags} all \
  STRIP=/bin/true \
  prefix="%{_prefix}" \
  gamesdir="%{_datadir}" \
  OPENTYRIAN_VERSION=%{version}

%install
make %{?_smp_mflags} install \
  DESTDIR="%{buildroot}" \
  docdir="%{_docdir}/%{name}" \
  prefix="%{_prefix}" \
  gamesdir="%{_datadir}" \
  OPENTYRIAN_VERSION=%{version}
# Gamedata directory (for the Freeware Tyrian21 files
mkdir -p %{buildroot}%{_datadir}/%{name}

# Install .desktop file and appdata
cd linux
install -D %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%suse_update_desktop_file -i %{name}
for size in 128 24 32 48; do
  install -D icons/tyrian-$size.png "%{buildroot}%{_datadir}/icons/hicolor/${size}x$size/apps/%{name}.png"
done
%fdupes -s %{buildroot}%{_datadir}

%post
echo "For running %{name} you have to download the Tyrian Freeware game assets.
They can be be found here: https://www.camanis.net/tyrian/tyrian21.zip
Unpack them and put them into %{_datadir}/%{name}
"

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_mandir}/man6/*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
