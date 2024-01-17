#
# spec file for package snd_sf2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           snd_sf2
Version:        0.1.2
Release:        0
Summary:        Soundfont and MIDI Sample
License:        SUSE-Freeware
Group:          Productivity/Multimedia/Sound/Midi
Source:         snd_sf2.tar.gz
Patch0:         snd_sf2-readme-encoding.patch
Requires:       awesfx
Provides:       soundfont
BuildArch:      noarch

%description
This package contains the following sound fonts: Vintage Dreams Waves v
2.0. by Ian Wilson and GeneralUser 1.1 by Samuel Collins. Vintage
Dreams Waves features 128 analog synthesizer patches and 8 drum kits.
The sound font can be used with Sound Blaster AWE and SB Live! sound
cards. The package also provides a sample MIDI file for this sound
font. The ROM sound font GeneralUser 1.1 only works with SB AWE
soundcards. It is General MIDI compatible.

%prep
%setup -q -c
%patch0 -p 1
mv doc/README.SuSE doc/README.SUSE
mv doc/README.SuSE.de doc/README.SUSE.de

%build

%install
mkdir -p %{buildroot}%{_datadir}/sounds
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a sf2 %{buildroot}%{_datadir}/sounds
cp -a mid %{buildroot}%{_datadir}/sounds
cp -a doc/* %{buildroot}%{_docdir}/%{name}

%files
%dir %{_datadir}/sounds/sf2
%{_datadir}/sounds/sf2/*
%dir %{_datadir}/sounds/mid
%{_datadir}/sounds/mid/*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%changelog
