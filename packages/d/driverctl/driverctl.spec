#
# spec file for package driverctl
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


Name:           driverctl
Version:        0.111
Release:        0
Summary:        Device driver control utility
License:        LGPL-2.0-only
URL:            https://gitlab.com/driverctl/driverctl
Source0:        https://gitlab.com/driverctl/driverctl/-/archive/%{version}/driverctl-%{version}.tar.bz2
Patch0:         add_list-persisted_command-ec102481.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       coreutils
Requires:       udev
BuildArch:      noarch

%description
driverctl is a tool for manipulating and inspecting the system
device driver choices.

Devices are normally assigned to their sole designated kernel driver
by default. However in some situations it may be desireable to
override that default, for example to try an older driver to
work around a regression in a driver or to try an experimental alternative
driver. Another common use-case is pass-through drivers and driver
stubs to allow userspace to drive the device, such as in case of
virtualization.

driverctl integrates with udev to support overriding
driver selection for both cold- and hotplugged devices from the
moment of discovery, but can also change already assigned drivers,
assuming they are not in use by the system. The driver overrides
created by driverctl are persistent across system reboots
by default.

%prep
%setup -q
%patch0 -p1

%build
%make_build

%install
%make_install

%files
%license COPYING
%doc README TODO
%{_sbindir}/driverctl
%{_udevrulesdir}/*.rules
%{_udevrulesdir}/../vfio_name
%{_unitdir}/driverctl@.service
%dir %{_sysconfdir}/driverctl.d
%{_datadir}/bash-completion/
%{_mandir}/man8/driverctl.8*

%post
%udev_rules_update

%postun
%udev_rules_update

%changelog
