#
# spec file for package gude-mouseclock-udev
#
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


Name:           gude-mouseclock-udev
Version:        0.1
Release:        0
Summary:        Udev rules for GUDE DCF77 receivers
License:        MIT
Group:          Hardware/Other
URL:            http://wiki.gude.info
Source:         94-gude-mouseclock.rules
Requires(pre):  user(ntp)
BuildArch:      noarch
%{?systemd_requires}

%description
Udev rules for GUDE DCF77 receivers.

* creates the symlink for /dev/refclock-0 to the TTY your DCF receiver
  is connected to.
* set group permission to "ntp" for your DCF receiver's TTY to give
  ntpd access to your device.

Supported devices
 * GUDE Expert mouseCLOCK USB II

NOTE: You still have to manually adjust ntpd's AppArmor profile to give ntpd
access to your DCF receiver's serial port (%{_sysconfdir}/apparmor.d/tunables/ntpd)

%prep
%setup -q -c -T

%build

%install
install -D -m0644 %{SOURCE0} %{buildroot}%{_udevrulesdir}/94-gude-mouseclock.rules

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%{_udevrulesdir}/94-gude-mouseclock.rules

%changelog
