#
# spec file for package ibp
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ibp
Version:        0.21
Release:        0
Summary:        Monitoring the International Beacon Project
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://www.pa3fwm.nl/software/ibp/
Source:         https://www.pa3fwm.nl/software/ibp/%{name}-%{version}.tgz
Patch0:         ibp-0.21-ncurses.patch
Patch1:         ibp-0.21-xdisp-makeClockContext-gc.patch
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(x11)
BuildRequires:  imake

%description
This program continuously shows which beacon of the International Beacon
Project (on the HF bands from 14 through 28 MHz) is currently transmitting. On
X11 systems, it can also show a sunclock-like map with the short and long paths
to the active beacons.

%prep
%autosetup -p1

%build
xmkmf
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 ibp.1 %{buildroot}%{_mandir}/man1/

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/ibp.1%{?ext_man}

%changelog
