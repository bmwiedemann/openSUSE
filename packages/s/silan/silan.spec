#
# spec file for package silan
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           silan
Version:        0.4.0
Release:        0
Summary:        CLI tool to detect silence in audio-files
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/x42/silan
Source:         https://github.com/x42/silan/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavcodec) <= 58.134.100
BuildRequires:  pkgconfig(libavformat) <= 58.76.100
BuildRequires:  pkgconfig(libavutil) <= 56.70.100
BuildRequires:  pkgconfig(sndfile)

%description
Standalone application to analyze audio files for silence and
print ranges of detected signals.

Silan uses ffmpeg/libav and supports a wide variety of audio
codecs and formats.

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/silan
%{_mandir}/man1/silan.1%{?ext_man}

%changelog
