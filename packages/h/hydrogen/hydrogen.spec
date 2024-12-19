#
# spec file for package hydrogen
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


%bcond_with lash
# The use of librubberband2 is marked as experimental.
# Because the current implementation produce wrong timing!
# So long this bug isn't solved, please disable this option.
# If rubberband-cli is installed, the hydrogen rubberband-function
# will work properly as expected.
%bcond_with librubberband
Name:           hydrogen
Version:        1.2.4
%define soversion 1_2_4
Release:        0
Summary:        A Real-Time Drum Machine and Sequencer
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            http://www.hydrogen-music.org/
Source0:        https://github.com/hydrogen-music/hydrogen/archive/%{version}/%{name}-%{version}.tar.gz
Patch2:         release-version.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa
BuildRequires:  ladspa-devel
BuildRequires:  libtar-devel
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.6
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc9
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
%if %{with lash}
BuildRequires:  pkgconfig(lash-1.0)
%endif
%if %{with librubberband}
BuildRequires:  pkgconfig(rubberband)
%else
BuildRequires:  rubberband-cli
Requires:       rubberband-cli
%endif

%description
Hydrogen is a software synthesizer which can be used alone, emulating
a drum machine based on patterns, or via an external MIDI
keyboard/sequencer software.

It features a modular and graphical interface based on QT5, has a
sample-based stereo audio engine, with import of sound samples in PCM
formats. Furthermore, a pattern-based sequencer with the ability to
chain patterns into a song. Up to 64 ticks per pattern with
individual level per event and variable pattern length are possible.
32 instrument tracks with volume, mute, solo, pan capabilities are
provided, and there is multi-layer support for instruments (up to 16
samples for each instrument). Human velocity, human time, pitch and
swing functions are implemented as well.

%package -n libhydrogen-core-%{soversion}
Summary:        Library essential for the hydrogen drum machine software
Group:          System/Libraries

%description -n libhydrogen-core-%{soversion}
Hydrogen is a software synthesizer which can be used alone, emulating
a drum machine based on patterns, or via an external MIDI
keyboard/sequencer software.

This library is the core of hydrogen's operation.

%package -n libhydrogen-core-devel
BuildArch:      noarch
Summary:        Development files and headers for libhydrogen-core
Group:          Development/Libraries/C and C++
Requires:       libhydrogen-core-%{soversion} = %{version}

%description -n libhydrogen-core-devel
These are the headers needed to develop apps that
link with libhydrogen-core.

%prep
%autosetup -p1

%build
export LADSPA_PATH=%{_libdir}/ladspa

%cmake \
%if 0%{?suse_version} <= 1500
	-DCMAKE_C_COMPILER=gcc-9 \
	-DCMAKE_CXX_COMPILER=g++-9 \
%endif
%if %{with lash}
	-DWANT_LASH:BOOL=ON \
%endif
	-DWANT_LIBARCHIVE:BOOL=ON \
	-DWANT_LRDF:BOOL=ON \
	-DWANT_PORTAUDIO:BOOL=ON \
	-DWANT_PORTMIDI:BOOL=ON \
%if %{with librubberband}
	-DWANT_RUBBERBAND:BOOL=ON \
%endif
	-DWANT_SHARED:BOOL=ON

%cmake_build

%install
%cmake_install

# Install the h2cli man page created by help2man
install -d -m 0755 %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
	help2man -N -o %{buildroot}%{_mandir}/man1/h2cli.1 %{buildroot}%{_bindir}/h2cli

%suse_update_desktop_file -i org.hydrogenmusic.Hydrogen AudioVideo Sequencer

%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/org.hydrogenmusic.Hydrogen.metainfo.xml
%{_mandir}/man1/h2cli.1%{?ext_man}
%{_mandir}/man1/hydrogen.1%{?ext_man}

%files -n libhydrogen-core-%{soversion}
%{_libdir}/libhydrogen-core-%{version}.so

%files -n libhydrogen-core-devel
%{_includedir}/%{name}

%changelog
