#
# spec file for package dumpvdl2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dumpvdl2
Version:        1.6.0
Release:        0
Summary:        A VDL Mode 2 message decoder and protocol analyzer
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/szpajder/dumpvdl2
#Git-Clone:     https://github.com/szpajder/dumpvdl2.git
Source:         https://github.com/szpajder/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libacars)
BuildRequires:  pkgconfig(librtlsdr)

%description
A VDL Mode 2 message decoder and protocol analyzer.

Features:
 * Supports following SDR hardware:
   - RTLSDR (via rtl-sdr library)
   - Mirics SDR (via libmirisdr-4)
   - reads prerecorded IQ data from file
 * Decodes up to 8 VDL2 channels simultaneously
 * Outputs messages to standard output or to a file (with optional daily
   or hourly file rotation)
 * Outputs ACARS messages to PlanePlotter over UDP/IP socket
 * Supports message filtering by type or direction (uplink, downlink)
 * Outputs decoding statistics using Etsy StatsD protocol

%prep
%setup -q

%build
%cmake \
    -DRTLSDR=ON \
    -DSOAPYSDR=ON \
    -DMIRISDR=OFF \
    -DSDRPLAY=OFF \
    -DETSY_STATSD=OFF
%make_jobs

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dumpvdl2

%changelog
