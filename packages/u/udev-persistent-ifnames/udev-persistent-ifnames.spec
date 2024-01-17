#
# spec file for package udev-persistent-ifnames
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           udev-persistent-ifnames
Version:        0.1
Release:        0
Summary:        Persistent classic network interface naming scheme
License:        GPL-2.0
Group:          System/Base

Source0:        75-persistent-net-generator.rules
Source1:        rule_generator.functions
Source2:        write_net_rules
Source3:        udev-generate-persistent-rule.sh
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package, when installed, disables the default "Predictable
Network Interface Naming" scheme[PNIN] in udev, and switches it to a
first-loaded-first-named, reboot-persistent scheme.

[PNIN] http://freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames/

Differences from PNIN:
* Re-enumeration when the L2 address changes.
* Interface names are not - and cannot be - derived from another property
  like PCI bus address.

%prep

%build

%install
b="%buildroot"
mkdir -p "$b/%_sysconfdir/udev/rules.d"
# We _absolutely do_ want to have this symlink in /etc, such that
# `systemd-delta` will show that something is not the same as upstream.
ln -s /dev/null "$b/%_sysconfdir/udev/rules.d/80-net-setup-link.rules"
mkdir -p "$b/%_prefix/lib/udev/rules.d"
install -pm0644 \
	"%_sourcedir"/*.rules \
	"$b/%_prefix/lib/udev/rules.d/"
install -pm0755 \
	"%_sourcedir"/rule_generator.functions \
	"%_sourcedir"/write_net_rules \
	"$b/%_prefix/lib/udev/"
install -pm0755 "%_sourcedir/udev-generate-persistent-rule.sh" \
	"%buildroot/%_prefix/lib/udev/udev-generate-persistent-rule"

%files
%defattr(-,root,root)
%_sysconfdir/udev/
%_prefix/lib/udev/

%changelog
