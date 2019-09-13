#
# spec file for package fxload
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 B1 Systems GmbH, Vohburg, Germany.
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


Name:           fxload
Version:        2008_10_13
Release:        0
Summary:        Download Firmware into USB FX and FX2 Devices
License:        LGPL-2.1+
Group:          System/Kernel
Url:            http://linux-hotplug.sf.net/
Source0:        http://mesh.dl.sourceforge.net/sourceforge/linux-hotplug/fxload-%{version}.tar.bz2
Source1:        %{name}.changes
Patch0:         fxload-2002_04_11.patch
# PATCH-FIX-UPSTREAM fxload-2008_10_13-prefer_DEVNAME.patch lp#156085 -- seife+obs@b1-systems.com
Patch1:         fxload-2008_10_13-prefer_DEVNAME.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program can download firmware into FX and FX2 EZ-USB devices as
well as the original AnchorChips EZ-USB.  It is intended to be invoked
by hotplug scripts when the unprogrammed device appears on the bus.

Primarily as an aid for developers, this can also be used to update
firmware on devices that boot from I2C serial EEPROMs.	For that use,
as well as downloading firmware to all other off-chip memory, a second
stage loader must first be downloaded.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# use date of .changes file instead of __DATE__
# to avoid useless republishing
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{SOURCE1} '+%%b %%e %%Y')
make %{?_smp_mflags} CC="gcc" CFLAGS="%{optflags} -Wall -g -DFXLOAD_VERSION=\"\\\"$FAKE_BUILDDATE (development)\\\"\""

%install
%make_install
#UsrMerge
mkdir %{buildroot}/sbin
ln -sf %{_sbindir}/fxload %{buildroot}/sbin
#EndUsrMere

%files
%defattr(-,root,root)
#UsrMerge
/sbin/*
#EndUsrMerge
%attr(755,root,root) %{_sbindir}/fxload
%{_mandir}/man?/*
%dir %{_datadir}/usb
%{_datadir}/usb/a3load.hex
%doc COPYING README.txt

%changelog
