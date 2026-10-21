#
# spec file for package rtlsdr-airband
#
# Copyright (c) 2017-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           rtlsdr-airband
Version:        6.2.0
Release:        0
Summary:        RTLSDR AM demodulator, support multiple channels per dongle
License:        GPL-3.0-only
URL:            https://github.com/rtl-airband/RTLSDR-Airband/
#Git-Clone:     https://github.com/rtl-airband/RTLSDR-Airband.git
Source:         https://github.com/rtl-airband/RTLSDR-Airband/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Patch0:         rtlsdr-airband-set-config-path.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libmp3lame-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libconfig++)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(vorbisenc)

%description
RTLSDR AM demodulator, support multiple channels per dongle.

%prep
%autosetup -p1 -n RTLSDR-Airband-%{version}

%build
%cmake
%make_build

%install
mkdir -p "%{buildroot}/%{_sysconfdir}/rtl_airband"
install -Dm 0644 config/* "%{buildroot}%{_sysconfdir}/rtl_airband/"
%cmake_install

%files
%license LICENSE
%doc NEWS.md README.md
%{_bindir}/rtl_airband
%dir %{_sysconfdir}/rtl_airband
%config %{_sysconfdir}/rtl_airband/*.conf

%changelog
