#
# spec file for package international-doom
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           international-doom
Version:        9.0
Release:        0
Summary:        Limit-removing source port of DOOM
License:        GPL-2.0-or-later
URL:            https://jnechaevsky.github.io/inter-doom/
Source:         https://github.com/JNechaevsky/international-doom/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fluidsynth
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(samplerate)
Requires:       %{name}-common

%description
Source port of Doom based on Chocolate Doom and Crispy Doom
with significant additions from DOOM Retro.

The game data files are required. They will be automatically picked up
if 'Doom + Doom II' is installed from Steam.

International Doom supports high rendering resolutions, visual improvements
and optional gameplay adjustments, while preserving the ability to play in the
spirit of the original vanilla game.

Major Features:

- Support for the Doom + Doom II re-release
- Optional True Color renderer
- Up to x6 (1200p) rendering resolutions
- Uncapped framerate
- Additional, darker gamma-correction levels
- Post-processing effects
- Support for OPL2, OPL3, MIDI, Fluidsynth and GUS music playback
- In-game keyboard and mouse bindings
- Various visual, audible, physical and demo enhancements
- Compatibility with vanilla-engine demos
- Removed limitations of vanilla engine
- Support for nodes in extended format (ZDBSP and DeePBSP)
- Support for BEX/DEHEXTRA DeHackEd extensions

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
chmod 755 %{buildroot}%{_bindir}/*
for i in doom heretic hexen
do
    install -Dpm644 data/$i.png %{buildroot}%{_datadir}/pixmaps/inter-$i.png
    install -Dpm644 data/$i.desktop %{buildroot}%{_datadir}/applications/inter-$i.desktop
done

%files
%{_bindir}/inter-doom
%{_datadir}/applications/inter-doom.desktop
%{_datadir}/pixmaps/inter-doom.png

%package common
Summary:        Common files for international-doom, international-heretic and international-hexen
Recommends:     timidity
Suggests:       freedoom

%description common
Common files for international-doom, international-heretic and international-hexen

%files common
%license COPYING
%doc README.md THANKS.md
%{_bindir}/inter-setup

%package -n international-heretic
Summary:        Limit-removing source port of Heretic
Requires:       %{name}-common

%description -n international-heretic
Source port of Heretic based on Chocolate Doom and Crispy Doom
with significant additions from DOOM Retro.

The game data files are required. They will be automatically picked up
if 'Heretic + Hexen' is installed from Steam.

International Heretic supports high rendering resolutions, visual improvements
and optional gameplay adjustments, while preserving the ability to play in the
spirit of the original vanilla game.

Major Features:

- Support for the Heretic re-release (part of 'Heretic + Hexen')
- Optional True Color renderer
- Up to x6 (1200p) rendering resolutions
- Uncapped framerate
- Additional, darker gamma-correction levels
- Post-processing effects
- Support for OPL2, OPL3, MIDI, Fluidsynth and GUS music playback
- In-game keyboard and mouse bindings
- Various visual, audible, physical and demo enhancements
- Compatibility with vanilla-engine demos
- Removed limitations of vanilla engine
- Support for nodes in extended format (ZDBSP and DeePBSP)
- Support for BEX/DEHEXTRA DeHackEd extensions

%files -n international-heretic
%{_bindir}/inter-heretic
%{_datadir}/applications/inter-heretic.desktop
%{_datadir}/pixmaps/inter-heretic.png

%package -n international-hexen
Summary:        Limit-removing source port of Hexen
Requires:       %{name}-common

%description -n international-hexen
Source port of Hexen based on Chocolate Doom and Crispy Doom
with significant additions from DOOM Retro.

The game data files are required. They will be automatically picked up
if 'Heretic + Hexen' is installed from Steam.

International Hexen supports high rendering resolutions, visual improvements
and optional gameplay adjustments, while preserving the ability to play in the
spirit of the original vanilla game.

Major Features:

- Support for the Hexen re-release (part of 'Heretic + Hexen')
- Optional True Color renderer
- Up to x6 (1200p) rendering resolutions
- Uncapped framerate
- Additional, darker gamma-correction levels
- Post-processing effects
- Support for OPL2, OPL3, MIDI, Fluidsynth and GUS music playback
- In-game keyboard and mouse bindings
- Various visual, audible, physical and demo enhancements
- Compatibility with vanilla-engine demos
- Removed limitations of vanilla engine
- Support for nodes in extended format (ZDBSP and DeePBSP)
- Support for BEX/DEHEXTRA DeHackEd extensions

%files -n international-hexen
%{_bindir}/inter-hexen
%{_datadir}/applications/inter-hexen.desktop
%{_datadir}/pixmaps/inter-hexen.png

%changelog
