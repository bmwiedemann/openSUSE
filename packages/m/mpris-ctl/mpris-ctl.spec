#
# spec file for package mpris-ctl
#
# Copyright (c) 2022 SUSE LLC
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


Name:           mpris-ctl
Version:        0.8.5
Release:        0
Summary:        Basic mpris player control for linux command line
License:        MIT
URL:            https://github.com/mariusor/mpris-ctl
Source:         https://github.com/mariusor/mpris-ctl/archive/refs/tags/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM openSUSE-install.patch gh#mariusor/mpris-ctl#21 mcepl@suse.com
# Fix Makefile for install to create required directories
Patch0:         openSUSE-install.patch
BuildRequires:  dbus-1-devel
BuildRequires:  scdoc

%description
Minimalistic cli tool for controlling audio players exposing a MPRIS
DBus interface, targeted at keyboard based WMs.

%prep
%autosetup -p1

%build
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL_PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/mpris-ctl
%{_mandir}/man1/mpris-ctl.1%{?ext_man}

%changelog
