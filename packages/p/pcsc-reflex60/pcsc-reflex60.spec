#
# spec file for package pcsc-reflex60
#
# Copyright (c) 2025 SUSE LLC
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


Name:           pcsc-reflex60
Version:        2.2.0
Release:        0
Group:          Productivity/Security
License:        BSD-3-Clause
URL:            http://musclecard.com/sourcedrivers.html
Summary:        PCSC driver for Schlumberger Reflex 60 smartcard readers
Source0:        slb_rf60-drv-%{version}.tar.bz2
Patch0:         slb_rf60-drv-%{version}-cflags.diff
Patch1:         slb_rf60-drv-%{version}-prototypes.diff
Patch2:         slb_rf60-drv-%{version}-uninitialized.diff
Patch3:         slb_rf60-drv-%{version}-fmt.diff
Patch4:         slb_rf60-drv-%{version}-ldflags.diff
Patch5:         slb_rf60-drv-%{version}-gcc15.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pcsc-lite
%define ifddir %{_libdir}/readers

%description
This package contains a driver for the Reflex 62 and Reflex 64 smart
card readers produced by Schlumberger.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%autosetup -p0 -n slb_rf60

%build
%make_build lib COPTS="$RPM_OPT_FLAGS -Wno-unused" LD="gcc $LDFLAGS"

%install
install -d $RPM_BUILD_ROOT%{ifddir}/
install -m755 libslb_rf60.so $RPM_BUILD_ROOT%{ifddir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README
%license LICENSE
%{ifddir}/

%changelog
