#
# spec file for package hivelytracker
#
# # Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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

%define realver 1_9
Name:           hivelytracker
Version:        1.9
Release:        0
Summary:        Music tracker for AHX and HVL formats
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Players
URL:            http://www.hivelytracker.co.uk/
#Git-Clone:     https://github.com/pete-gordon/hivelytracker.git
Source:         https://github.com/pete-gordon/hivelytracker/archive/refs/tags/V%{realver}.tar.gz#/%{name}-%{realver}.tar.gz
Patch0:         hivelytracker-fontpath.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(sdl)
Requires:       texlive-dejavu-fonts

%description
Hively Tracker is a tracker program based upon the AHX format created
in the mid '90s by Dexter and Pink of Abyss. The format was relatively
popular, and many songs were created and used in scene productions and
games. AHX was designed to create a very SID-like sound on the Amiga.

HivelyTracker can import and export modules and instruments in the AHX
format, but it also improves on AHX in several ways and therefore has
its own instrument and module formats.

HivelyTracker offers the following features over AHX:
 * Multichannel (4 to 16 channels)
 * Per-channel stereo panning
 * Two commands per note instead of one
 * Ring modulation
 * A more feature rich editor

%prep
%setup -q -n %{name}-%{realver}
%patch0 -p1

%build
%make_build -C sdl -f Makefile.linux

%install
%make_install -C sdl -f Makefile.linux PREFIX=%{buildroot}%{_prefix}/
# unbundle DejaVu fonts
rm -R %{buildroot}/usr/share/hivelytracker/ttf
%fdupes %{buildroot}/%{_datadir}/hivelytracker/Skins

%files
%license LICENSE
%doc README.MD
%{_bindir}/hivelytracker
%{_datadir}/hivelytracker
%{_datadir}/applications/hivelytracker.desktop
%{_datadir}/icons/hivelytracker.png
%{_mandir}/man1/hivelytracker.1%{?ext_man}

%changelog
