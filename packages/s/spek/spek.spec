#
# spec file for package spek
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


Name:           spek
Version:        0.8.3
Release:        0
Summary:        Tool for audio spectrum analysis and visualization
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://spek.cc/
Source:         https://github.com/alexkay/spek/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         ffmpeg_2.9.patch
Patch1:         fix-compilation-with-libav-8.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK-devel
BuildRequires:  pkgconfig(libavcodec) >= 53.25
BuildRequires:  pkgconfig(libavformat) >= 53.17
BuildRequires:  pkgconfig(libavutil) >= 51.17

%description
Spek helps to analyse your audio files by showing their spectrogram.
It supports all popular lossy and lossless audio file formats.

Features:
  * Ultra-fast signal processing, uses multiple threads to further
    speed up the analysis
  * Shows the codec name and the audio signal parameters
  * Can save the spectrogram as an image file
  * Drag-and-drop support; associates with common audio file formats
  * Auto-fitting time, frequency and spectral density rulers
  * Adjustable spectral density range

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -r %{name} AudioVideo Player
%find_lang %{name}

%files -f %{name}.lang
%license LICENCE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
