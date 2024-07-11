#
# spec file for package systemd-generator-cron2timer
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


Name:           systemd-generator-cron2timer
Version:        0
Release:        0
Summary:        Systemd generator to create timer units
License:        MIT
Source:         cron2timers
Requires:       systemd
BuildArch:      noarch
Conflicts:      cron
Conflicts:      cronie

%description
Systemd generator to create timer units from scripts in
/etc/cron.{hourly,daily,weekly,monthly,yearly}

Using this method alleviates the need to install cron to run those
scripts. The cron implementation uses a shell script that wakes up
every hour, even when there's nothing to do. Timers on the other
hand are created only for scripts that actually exist and trigger at
the specific time the scripts must run.

%prep

%build

%install
install -d -m 755 %{buildroot}/etc/cron.{hourly,daily,weekly,monthly,yearly}
install -D -m 755 %{SOURCE0} %{buildroot}/usr/lib/systemd/system-generators/cron2timers

%files
/etc/cron.{hourly,daily,weekly,monthly,yearly}
/usr/lib/systemd/system-generators

%changelog
