#
# spec file for package dump1090-fa
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


Name:           dump1090-fa
Version:        10.1
Release:        0
Summary:        An ADS-B Mode S decoder for RTLSDR devices (Flightaware fork)
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/flightaware/dump1090
Source0:        https://github.com/flightaware/dump1090/archive/v10.1.tar.gz#/dump1090-%{version}.tar.gz
#PATCH-FIX-UPSTREAM dump1090-fix-gcc15.patch -- based on PR 261 Fix compilation with GCC15
Patch0:         dump1090-fix-gcc15.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbladeRF)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(ncursesw)

%description
An ADS-B Mode S decoder specifically designed for RTLSDR devices.
Flightaware fork.

%prep
%autosetup -p1 -n dump1090-%{version}

%build
%make_build CC="cc %{optflags} -fcommon"

%install
install -D -p -m 0755 dump1090 \
  %{buildroot}/%{_bindir}/dump1090-fa
install -D -p -m 0755 view1090 \
  %{buildroot}/%{_bindir}/view1090-fa

%check
%make_build test

%files
%license LICENSE
%doc README-json.md README.adaptive-gain.md README.md
%doc debian/changelog
%{_bindir}/dump1090-fa
%{_bindir}/view1090-fa

%changelog
