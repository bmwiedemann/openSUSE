#
# spec file for package backupninja
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

Name:          backupninja
Version:       1.2.2
Release:       0
Summary:       Lightweight, extensible meta-backup system
License:       GPL-2.0
URL:           https://0xacab.org/liberate/backupninja
Source0:       %{name}-%{version}.tar.gz
Source1:       backupninja.service
Source2:       backupninja.timer
Group:         Productivity/Archiving/Backup
Requires:      bash
Requires:      dialog
Requires:      gawk
Requires:      gzip
Requires:      logrotate
Requires:      pkgconfig(systemd)
BuildRequires: automake
Recommends:    hwinfo
Recommends:    rdiff-backup
Recommends:    rsync
Recommends:    sfdisk

%description
Backupninja allows you to coordinate system backup by dropping a few simple
configuration files into /etc/backup.d/. Most programs you might use for making
backups don't have their own configuration file format. Backupninja provides a
centralized way to configure and coordinate many different backup utilities.
The key features of backupninja are:
- easy to read ini style configuration files.
- you can drop in scripts to handle new types of backups.
- backup actions can be scheduled.

%prep
%setup -q -n backupninja-backupninja-%{version}

%build
sh autogen.sh
%configure
%make_build

%install
%make_install
# We are using systemd
rm -rf %{buildroot}%{_sysconfdir}/cron.d
# Create other files needed
mkdir -p "%{buildroot}%{_localstatedir}/log"
mkdir -p "%{buildroot}%{_sysconfdir}/backup.d"
touch "%{buildroot}%{_localstatedir}/log/backupninja.log"
# Add the SystemD units
mkdir -p %{buildroot}%{_unitdir}
cp -Lv %{SOURCE1} %{buildroot}%{_unitdir}
cp -Lv %{SOURCE2} %{buildroot}%{_unitdir}

%pre
%service_add_pre %{name}.timer %{name}.service

%post
%service_add_post %{name}.timer %{name}.service

%preun
%service_del_preun %{name}.timer %{name}.service

%postun
%service_del_postun %{name}.timer
%service_del_postun_without_restart %{name}.service

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license COPYING
%{_datadir}/backupninja/*
%{_libdir}/backupninja/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_sbindir}/*
%{_unitdir}/backupninja.*
%ghost %{_localstatedir}/log/backupninja.log
%config(noreplace) %{_sysconfdir}/backupninja.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/backupninja
%dir %{_datadir}/backupninja
%dir %{_libdir}/backupninja
%defattr(0760,root,root,0760)
%dir %{_sysconfdir}/backup.d

%changelog
