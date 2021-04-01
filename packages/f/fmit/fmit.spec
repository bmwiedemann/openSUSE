#
# spec file for package fmit
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


Name:           fmit
Version:        1.2.14
Release:        0
Summary:        A free musical instrument tuner
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://gillesdegottex.github.io/fmit
Source:         https://github.com/gillesdegottex/fmit/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fmit-correct-appdata-dir.patch badshah400@gmail.com -- install appdata file to the correct dir (/usr/share/metainfo instead of /usr/share/appdata)
Patch0:         fmit-correct-appdata-dir.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(portaudio-2.0)
ExclusiveArch:  i586 x86_64

%description
fmit is a free musical instrument tuner. It works with JACK, Alsa,
OSS and PortAudio audio input devices. It currently has the
following features:-
* Error history
* Volume history
* Statistics
* Tunning scales
* (Werckmeister III, Kirnberger III, Diatonic and Meantone)
* Microtonal tuning (with Scala file support)
* Harmonic ratios
* Wave shape
* Discrete Fourier Transform view

%prep
%autosetup -p1

%build
%qmake5 PREFIX=%{_prefix} \
        "CONFIG+=acs_qt acs_alsa acs_jack acs_portaudio" \
        ./fmit.pro

%make_jobs
%make_jobs lrelease

%install
%qmake5_install
%suse_update_desktop_file %{name}

%files
%license COPYING_GPL.txt COPYING_LGPL.txt
%doc README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{name}/
%{_datadir}/metainfo/*.appdata.xml

%changelog
