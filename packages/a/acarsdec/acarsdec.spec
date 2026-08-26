#
# spec file for package acarsdec
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2017-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           acarsdec
Version:        4.6
Release:        0
Summary:        ACARS SDR decoder
# Legal-Review-Notice: every source file carries a boilerplate naming the "GNU
# Library General Public License version 2". That wording predates the project
# ever shipping a license text and is a long-standing upstream typo: the
# LICENSE.md added in 4.0 is the GPL version 2 text, and README.md states
# "GPLv2-only". The distribution license is therefore GPL-2.0-only.
License:        GPL-2.0-only
URL:            https://github.com/f00b4r0/acarsdec
#Git-Clone:     https://github.com/f00b4r0/acarsdec.git
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.12
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libacars-2) >= 2.0.0
BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(sndfile)

%description
A multi-channel ACARS decoder with built-in rtl_sdr and airspy front ends,
which can also decode from an ALSA capture device or from an audio file.
Decoded messages can be written to files or sent over UDP in one-line, full
text, PlanePlotter, acarsserv or JSON format, and ARINC-622 ATS applications
(ADS-C, CPDLC) are decoded through libacars. It comes with a database
backend, acarsserv, to store received ACARS messages.

%prep
%autosetup -p1

%build
# SOAPYSDR: SoapySDR is not packaged in openSUSE.
# SDRPLAY:  the sdrplay_api v3 library is proprietary and not packaged;
#           upstream also marks this backend untested and unmaintained.
# MQTT:     kept off, as it was before the 4.x switch, to avoid pulling
#           paho-mqtt-c into every installation.
%cmake \
  -DAIRSPY=ON \
  -DALSA=ON \
  -DCJSON=ON \
  -DLIBACARS=ON \
  -DRTLSDR=ON \
  -DSNDFILE=ON \
  -DMQTT=OFF \
  -DSDRPLAY=OFF \
  -DSOAPYSDR=OFF
%cmake_build

%install
%cmake_install

%check
# Upstream ships no test suite; decode the sample recording it ships instead.
%{buildroot}%{_bindir}/%{name} --sndfile test.wav --output oneline:file

%files
%license LICENSE.md
%doc README.md
%{_bindir}/acarsdec

%changelog
