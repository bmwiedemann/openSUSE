#
# spec file for package rtl_433
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           rtl_433
Version:        25.02
Release:        0
Summary:        Application turning the RTL2832 dongle into a 433.92MHz generic data receiver
License:        GPL-2.0-only
URL:            https://github.com/merbanan/rtl_433.git
Source:         https://github.com/merbanan/rtl_433/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(openssl)

%description
An application using librtlsdr to decode the temperature from
wireless temperature sensors (433.92MHz)

%package devel
Summary:        Header files for the RTL2832 dongle library
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
Turns RTL2832 dongle into a 433.92MHz generic data receiver.

This subpackage contains header files for developing applications that want
to make use of rtl_433.

%prep
%setup -q

%build
%cmake \
    -DBUILD_TESTING=OFF \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/rtl_433
%dir %{_sysconfdir}/rtl_433
%config %{_sysconfdir}/rtl_433/*.conf
%{_mandir}/man1/rtl_433.1%{?ext_man}

%files devel
%{_includedir}/rtl_433.h
%{_includedir}/rtl_433_devices.h

%changelog
