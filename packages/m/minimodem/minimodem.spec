#
# spec file for package minimodem
#
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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

Name:           minimodem
Version:        0.24
Release:        0
Summary:        General-purpose software audio FSK modem
License:        GPL-3.0+
Group:          Productivity/Hamradio/Other
URL:            http://www.whence.com/minimodem/
Source:         http://www.whence.com/minimodem/%{name}-%{version}.tar.gz
#Git-Clone:     https://github.com/kamalmostafa/minimodem.git
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(sndfile)

%description
Minimodem is a command-line program which decodes (or generates) audio
modem tones at any specified baud rate, using various framing protocols.
It acts a general-purpose software FSK modem, and includes support for
various standard FSK protocols such as Bell103, Bell202, RTTY, TTY/TDD,
NOAA SAME, and Caller-ID.

Minimodem can play and capture audio modem tones in real-time via the
system audio device, or in batched mode via audio files.

Minimodem can be used to transfer data between nearby computers using an
audio cable (or just via sound waves), or between remote computers using
radio, telephone, or another audio communications medium.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc COPYING README
%{_bindir}/minimodem
%{_mandir}/man1/minimodem.1%{ext_man}

%changelog
