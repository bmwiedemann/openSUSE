#
# spec file for package hamclock
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           hamclock
Version:        4.16
Release:        0
Summary:        Clock and map with additional information for amateur radio
License:        MIT
URL:            https://clearskyinstitute.com/ham/HamClock/
Source:         https://clearskyinstitute.com/ham/HamClock/ESPHamClock.tgz
Patch0:         hamclock-4.15-no-phone-home.patch
Patch1:         hamclock-4.15-no-libgpiod.patch
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)

%description
HamClock is a kiosk-style application that provides real time space weather,
radio propagation models, operating events and other information particularly
useful to the radio amateur.

%prep
%autosetup -p1 -n ESPHamClock

%build
%make_build hamclock-800x480

%install
## %%make_build install is broken
mkdir -p %{buildroot}%{_bindir}
install -D -m 755 hamclock-800x480 %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/*

%changelog
