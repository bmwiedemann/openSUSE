#
# spec file for package ipcalc
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ipcalc
Version:        1.0.2
Release:        0
Summary:        IPv4/IPv6 tool assisting in network calculations on the command line
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://gitlab.com/ipcalc/ipcalc
Source0:        https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE ipcalc-disable-network-tests.patch badshah400@gmail.com -- Disable tests requiring network
Patch0:         ipcalc-disable-network-tests.patch
BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  rubygem(ronn)
Conflicts:      netcalc

%description
ipcalc is a modern tool to assist in network address calculations for IPv4 and
IPv6. It acts both as a tool to output human readable information about a
network or address, as well as a tool suitable to be used by scripts or other
programs.  It supports printing a summary about the provided network address,
multiple command line options per information to be printed, transparent IPv6
support, and in addition it will use libGeoIP if available to provide
geographic information.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md NEWS
%license COPYING
%{_bindir}/ipcalc
%{_mandir}/man1/ipcalc.1%{?ext_man}

%changelog
