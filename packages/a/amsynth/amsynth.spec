#
# spec file for package amsynth
#
# Copyright (c) 2020 SUSE LLC
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


Name:           amsynth
Version:        1.11.0
Release:        0
Summary:        Analog modelling (a.k.a virtual analog) software synthesizer
License:        GPL-2.0-or-later
URL:            http://amsynth.github.io/
Source:         https://github.com/amsynth/amsynth/releases/download/release-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(sndfile)
Recommends:     %{name}-lang

%description
Amsynth is an analog modelling (a.k.a virtual analog) software synthesizer.
It mimics the operation of early analog subtractive synthesizers with
classic oscillator waveforms, envelopes, filter, modulation and effects.
The aim is to make it easy to create and modify sounds.

Features:
 * Dual oscillators (sine / saw / square / noise) with hard sync
 * 12/24 dB/oct resonant filter (low-pass / high-pass / band-pass / notch)
 * Mono / poly / legato keyboard modes
 * Dual ADSR envelope generators (filter & amplitude)
 * LFO which can modulate the oscillators, filter, and amplitude
 * Distortion and reverb
 * Hundreds of presets

There are currently several different ways to run amsynth:
 * Stand-alone application using JACK, ALSA or OSS
 * DSSI plug-in
 * LV2 plug-in
 * VST plug-in

%package plugin-dssi
Summary:        Analog modelling (a.k.a virtual analog) software synthesizer
Requires:       %{name} = %{version}
Requires:       dssi

%description plugin-dssi
Amsynth is an analog modelling (a.k.a virtual analog) software synthesizer.
It mimics the operation of early analog subtractive synthesizers with
classic oscillator waveforms, envelopes, filter, modulation and effects.
The aim is to make it easy to create and modify sounds.

Features:
 * Dual oscillators (sine / saw / square / noise) with hard sync
 * 12/24 dB/oct resonant filter (low-pass / high-pass / band-pass / notch)
 * Mono / poly / legato keyboard modes
 * Dual ADSR envelope generators (filter & amplitude)
 * LFO which can modulate the oscillators, filter, and amplitude
 * Distortion and reverb
 * Hundreds of presets

There are currently several different ways to run amsynth:
 * Stand-alone application using JACK, ALSA or OSS
 * DSSI plug-in
 * LV2 plug-in
 * VST plug-in

This package includes the DSSI implementation of the synthesizer.

%package plugin-lv2
Summary:        Analog modelling (a.k.a virtual analog) software synthesizer
Requires:       %{name} = %{version}

%description plugin-lv2
Amsynth is an analog modelling (a.k.a virtual analog) software synthesizer.
It mimics the operation of early analog subtractive synthesizers with
classic oscillator waveforms, envelopes, filter, modulation and effects.
The aim is to make it easy to create and modify sounds.

Features:
 * Dual oscillators (sine / saw / square / noise) with hard sync
 * 12/24 dB/oct resonant filter (low-pass / high-pass / band-pass / notch)
 * Mono / poly / legato keyboard modes
 * Dual ADSR envelope generators (filter & amplitude)
 * LFO which can modulate the oscillators, filter, and amplitude
 * Distortion and reverb
 * Hundreds of presets

There are currently several different ways to run amsynth:
 * Stand-alone application using JACK, ALSA or OSS
 * DSSI plug-in
 * LV2 plug-in
 * VST plug-in

This package includes the LV2 implementation of the synthesizer.

%package plugin-vst
Summary:        Analog modelling (a.k.a virtual analog) software synthesizer
Requires:       %{name} = %{version}

%description plugin-vst
Amsynth is an analog modelling (a.k.a virtual analog) software synthesizer.
It mimics the operation of early analog subtractive synthesizers with
classic oscillator waveforms, envelopes, filter, modulation and effects.
The aim is to make it easy to create and modify sounds.

Features:
 * Dual oscillators (sine / saw / square / noise) with hard sync
 * 12/24 dB/oct resonant filter (low-pass / high-pass / band-pass / notch)
 * Mono / poly / legato keyboard modes
 * Dual ADSR envelope generators (filter & amplitude)
 * LFO which can modulate the oscillators, filter, and amplitude
 * Distortion and reverb
 * Hundreds of presets

There are currently several different ways to run amsynth:
 * Stand-alone application using JACK, ALSA or OSS
 * DSSI plug-in
 * LV2 plug-in
 * VST plug-in

This package includes the VST implementation of the synthesizer.

%lang_package

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file %{name} Audio Midi
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/%{name}/skins/

%if 0%{?suse_version} < 1550
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS README NEWS
%{_bindir}/amsynth
%{_datadir}/amsynth
%{_datadir}/applications/amsynth.desktop
%{_datadir}/icons/hicolor/*/apps/amsynth.*
%dir %{_datadir}/appdata
%{_datadir}/appdata/amsynth.appdata.xml
%{_mandir}/man1/amsynth.1%{?ext_man}

%files plugin-dssi
%{_libdir}/dssi/
%dir %{_datadir}/appdata
%{_datadir}/appdata/dssi-amsynth-plugin.metainfo.xml

%files plugin-lv2
%{_libdir}/lv2/
%dir %{_datadir}/appdata
%{_datadir}/appdata/lv2-amsynth-plugin.metainfo.xml

%files plugin-vst
%{_libdir}/vst/
%dir %{_datadir}/appdata
%{_datadir}/appdata/vst-amsynth-plugin.metainfo.xml

%files lang -f %{name}.lang
%{_mandir}/de/man1/amsynth.1%{?ext_man}
%{_mandir}/fr/man1/amsynth.1%{?ext_man}

%changelog
