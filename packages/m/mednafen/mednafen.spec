#
# spec file for package mednafen
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


Name:           mednafen
Version:        1.27.0
Release:        0
Summary:        Multiple video game console emulator
License:        GPL-2.0-only
URL:            https://mednafen.github.io
Source0:        https://mednafen.github.io/releases/files/%{name}-%{version}-UNSTABLE.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)

%description
Mednafen is a command-line-driven multi-system emulator utilizing
OpenGL and SDL. Mednafen has the ability to remap hotkey functions
and virtual system inputs to a keyboard, a joystick, or both
simultaneously. Save states are supported, as is real-time game
rewinding. Screen snapshots may be taken, in the PNG file format, at
the press of a button. Mednafen can record audiovisual movies in the
QuickTime file format, with several different lossless codecs
supported.

Nintendo: NES, FDS, Game Boy (Color|Advance), Super Nintendo, Virtual Boy.
Sega: Master System, Game Gear, Genesis/MegaDrive, Saturn.
Nec: TurboGrafx-16/PC Engine (CD), SuperGrafx, PC-FX.
Sony: PlayStation.
Apple: II/II+.
Atari: Lynx.
SNK: Neo Geo Poket (Color).
Bandai: Wonderswan (Color).

%package doc
Summary:        Additional Package Documentation
BuildArch:      noarch

%description doc
This package contains optional documentation provided in addition to this package's base documentation.

%lang_package

%prep
%autosetup -p1 -n %{name}

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

%files
%license COPYING
%doc ChangeLog TODO
%{_bindir}/%{name}

%files doc
%doc Documentation/?*.{css,def,html,png,txt}

%files -f %{name}.lang lang

%changelog
