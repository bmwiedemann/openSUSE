#
# spec file for package fluid-soundfont
#
# Copyright (c) 2013 Philipp Thomas
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


Name:           fluid-soundfont
Version:        3.1
Release:        0
Summary:        Fluid (R3) SoundFonts (GM and GS)
License:        MIT
Group:          Productivity/Multimedia/Sound/Midi
Source:         %{name}_%{version}.orig.tar.bz2
Source1:        fluidr3_gm.cfg
Source2:        fluidr3_gs.cfg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a GM SoundFont, for use with any modern MIDI synthesiser: hardware
(like the emu10k1 sound card), or software (like FluidSynth).

This package provides the larger GM sound set, without the Roland Sound
Canvas extensions.


%package    -n fluid-soundfont-gm
Summary:        Fluid (R3) General MIDI SoundFont (GM)
Group:          Productivity/Multimedia/Sound/Midi

%description -n fluid-soundfont-gm
This is a GM SoundFont, for use with any modern MIDI synthesiser: hardware
(like the emu10k1 sound card), or software (like FluidSynth).

This package provides the larger GM sound set, without the Roland Sound
Canvas extensions.

%package    -n fluid-soundfont-gs
Summary:        Fluid (R3) General MIDI SoundFont (GS)
Group:          Productivity/Multimedia/Sound/Midi
Requires:       fluid-soundfont-gm

%description -n fluid-soundfont-gs
This is a GS SoundFont, for use with any modern MIDI synthesiser: hardware
(like the emu10k1 sound card), or software (like FluidSynth).

This package provides the smaller GS sound set of Roland Sound Canvas
extensions.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}/sounds/sf2
install -d %{buildroot}%{_datadir}/timidity
install -d %{buildroot}%{_defaultdocdir}/%{name}

install -m 644 %{S:1} %{S:2} %{buildroot}%{_datadir}/timidity
install -m 644 FluidR3_G{M,S}.sf2 %{buildroot}%{_datadir}/sounds/sf2
install -m 644 COPYING README %{buildroot}%{_defaultdocdir}/%{name}

%files -n fluid-soundfont-gm
%defattr(-,root,root)
%doc %{_defaultdocdir}/fluid-soundfont
%dir %{_datadir}/sounds/sf2
%{_datadir}/sounds/sf2/FluidR3_GM.sf2
%dir %_datadir/timidity
%config %{_datadir}/timidity/fluidr3_gm.cfg

%files -n fluid-soundfont-gs
%defattr(-,root,root)
%dir %_datadir/sounds/sf2
%{_datadir}/sounds/sf2/FluidR3_GS.sf2
%dir %_datadir/timidity
%config %{_datadir}/timidity/fluidr3_gs.cfg

%changelog
