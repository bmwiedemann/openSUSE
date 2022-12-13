#
# spec file for package spek
#
# Copyright (c) 2022 SUSE LLC
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
Version:        0.8.4
Release:        0
Summary:        Tool for audio spectrum analysis and visualization
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://spek.cc/
Source:         https://github.com/alexkay/spek/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 232.patch -- Replace deprecated FFmpeg APIs to support FFmpeg 5.x
Patch0:         https://patch-diff.githubusercontent.com/raw/alexkay/spek/pull/232.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext >= 0.21
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)

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
%autosetup -p1

%build
# Workaround upstreams issue https://github.com/alexkay/spek/issues/149
export CXXFLAGS="$CXXFLAGS -std=gnu++11 -Wall -Wextra -I/usr/include/ffmpeg"
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
