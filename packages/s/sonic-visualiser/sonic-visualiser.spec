#
# spec file for package sonic-visualiser
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016 Tom Mbrt <tom.mbrt@googlemail.com>
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2011 Evstifeev Roman <someuniquename@gmail.com>
# Copyright (c) 2005-2010 oc2pus <oc2pus@arcor.de>
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


Name:           sonic-visualiser
Version:        4.0.1
Release:        0
Summary:        A program for viewing and analysing contents of audio files
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://www.sonicvisualiser.org/
Source:         https://code.soundsoftware.ac.uk/attachments/download/2607/%{name}-%{version}.tar.gz
Source1:        %{name}.xml
# PATCH-FIX-OPENSUSE sonic-visualiser-system-dataquay.patch aloisio@gmx.com -- force use of system libdataquay
Patch0:         sonic-visualiser-system-dataquay.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Fix-build-with-Qt-5.15.patch
BuildRequires:  capnproto
BuildRequires:  dssi
BuildRequires:  flac
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa
BuildRequires:  libqt5-qtbase-devel >= 5.2
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(capnp)
%if 0%{?BUILD_ORIG}
BuildRequires:  pkgconfig(dataquay) >= 0.9
%endif
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fishsound)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(oggz) >= 0.9.5
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(raptor2) >= 2.0.4
BuildRequires:  pkgconfig(rasqal)
BuildRequires:  pkgconfig(redland) >= 1.0.14
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(vamp-sdk) >= 2.5
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
Requires:       dssi
Requires:       ladspa

%description
Sonic Visualiser is a program for viewing and analysing the contents
of music audio files.

With Sonic Visualiser you can:
* Load audio files in various formats and view their waveforms

* Look at audio visualisations such as spectrogram views, with
  interactive adjustment of display parameters

* Annotate audio data by adding labelled time points and defining
  segments, point values and curves

* Run feature-extraction plugins to calculate annotations
  automatically, using algorithms such as beat trackers, pitch
  detectors and so on

* Import annotation data from various text formats and MIDI files

* Play back the original audio with synthesised annotations, taking
  care to synchronise playback with the display position

* Slow down playback and loop segments of interest, including
  seamless looping of complex non-contiguous areas

* Export annotations and audio selections to external files.

* Sonic Visualiser can also be controlled remotely using the Open Sound
  Control (OSC) protocol

%prep
%setup -q
%if 0%{?BUILD_ORIG}
%patch0 -p1
%endif
%patch1 -p1

# required with capnproto 0.7.0
for x in *.pr* config* Makefile* ; do perl -i -p -e 's/c\+\+11/c++14/g' "$x" ; done

# Don't use -Werror on releases
find . -name configure -o -name "*.pro" -o -name "*.pri" -exec sed -i s'# -Werror##g' {} \;

%build
export LC_ALL=en_US.UTF-8
%configure
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

# fix executable bit for helper programs
chmod +x %{buildroot}%{_bindir}/*vamp-*

# plugin dir
install -dm 755 %{buildroot}%{_libdir}/vamp

# icon
for size in 16 22 24 32 48 64 128 ; do
install -Dm 644 icons/sv-${size}x${size}.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

install -Dm 644 icons/sv-icon.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
ln -s sonic-visualiser.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/sv-icon.svg

# mime types
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
install -Dm 644 x-sonicvisualiser.desktop %{buildroot}/%{_datadir}/mimelnk/application/x-sonicvisualiser.desktop
install -Dm 644 x-sonicvisualiser-layer.desktop %{buildroot}/%{_datadir}/mimelnk/application/x-sonicvisualiser-layer.desktop

# Menu
%suse_update_desktop_file -i %{name} AudioVideo Audio Music

%post
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null || :

%files
%doc CHANGELOG README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/piper-vamp-simple-server
%{_bindir}/vamp-plugin-load-checker
%dir %{_libdir}/vamp
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/scalable/apps/sv-icon.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_datadir}/mimelnk/application/x-sonicvisualiser*

%changelog
