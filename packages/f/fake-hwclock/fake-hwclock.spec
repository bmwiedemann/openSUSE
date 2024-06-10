#
# spec file for package fake-hwclock
#
# Copyright (c) 2022 B1 Systems GmbH, Vohburg
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


Name:           fake-hwclock
Version:        0.13
Release:        0
Summary:        Save/restore system clock on machines without working RTC hardware
License:        GPL-2.0-only
URL:            https://tracker.debian.org/pkg/fake-hwclock
Source:         %{name}-%{version}.tar.xz
Source1:        Makefile
BuildArch:      noarch

%description
Some machines don't have a working realtime clock (RTC) unit, or no
driver for the hardware that does exist. fake-hwclock is a simple set
of scripts to save the kernel's current clock periodically (including
at shutdown) and restore it at boot so that the system clock keeps at
least close to realtime. This will stop some of the problems that may
be caused by a system believing it has travelled in time back to
1970, such as needing to perform filesystem checks at every boot.

On top of this, use of NTP is still recommended to deal with the fake
clock "drifting" while the hardware is halted or rebooting.

%prep
%autosetup -p1

%build
cp -p %{SOURCE1} .

%install
%make_install

%pre
%service_add_pre fake-hwclock-load.service
%service_add_pre fake-hwclock-save.service
%service_add_pre fake-hwclock-save.timer

%post
%service_add_post fake-hwclock-load.service
%service_add_post fake-hwclock-save.service
%service_add_post fake-hwclock-save.timer

%preun
%service_del_preun fake-hwclock-load.service
%service_del_preun fake-hwclock-save.service
%service_del_preun fake-hwclock-save.timer

%postun
%service_del_postun fake-hwclock-load.service
%service_del_postun fake-hwclock-save.service
%service_del_postun fake-hwclock-save.timer


%files
%license COPYING
%doc debian/changelog debian/copyright
%doc %{_mandir}/man8/*
%config(noreplace) /etc/default/fake-hwclock
/usr/lib/systemd/system/
/usr/sbin/fake-hwclock

%changelog
