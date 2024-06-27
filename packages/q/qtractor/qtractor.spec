#
# spec file for package qtractor
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


Name:           qtractor
Version:        1.0.0
Release:        0
Summary:        An Audio/MIDI multi-track sequencer
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://qtractor.org/
Source0:        https://download.sourceforge.net/qtractor/qtractor-%{version}.tar.gz
Source1:        https://download.sf.net/qtractor/qtractor-manual-and-howtos.pdf
BuildRequires:  alsa-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  librubberband-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel >= 1.0.11
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(aubio)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(suil-0)
BuildRequires:  pkgconfig(xcb)
Recommends:     %{name}-doc-pdf

%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt6 toolkit.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%package doc-pdf
Summary:        Documentation for Qtractor
BuildArch:      noarch

%description doc-pdf
This package contains qtractor-manual-and-howtos.pdf
For your reading

%prep
%setup -q
cp -v %{S:1} qtractor-manual-and-howtos.pdf

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}
mv %{buildroot}%{_libdir}/qtractor/qtractor_plugin_scan %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/qtractor/palette/"Wonton Soup.conf" %{buildroot}%{_datadir}/qtractor/palette/Wonton_Soup.conf

%files
%doc ChangeLog README
%license LICENSE
%dir %{_datadir}/metainfo/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/qtractor/audio
%dir %{_datadir}/qtractor/instruments
%dir %{_datadir}/qtractor/palette
%{_bindir}/%{name}
%{_bindir}/qtractor_plugin_scan
%{_datadir}/applications/org.rncbc.qtractor.desktop
%{_datadir}/metainfo/org.rncbc.qtractor.metainfo.xml
%{_datadir}/icons/*/*/apps/org.rncbc.qtractor*
%{_datadir}/icons/*/*/mimetypes/org.rncbc.qtractor.*
%{_datadir}/mime/packages/org.rncbc.qtractor.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/fr/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}/translations/*
%{_datadir}/qtractor/audio/metro_bar.wav
%{_datadir}/qtractor/audio/metro_beat.wav
%{_datadir}/qtractor/instruments/Standard1.ins
%{_datadir}/qtractor/palette/KXStudio.conf
%{_datadir}/qtractor/palette/Wonton_Soup.conf

%files doc-pdf
%doc qtractor-manual-and-howtos.pdf

%changelog
