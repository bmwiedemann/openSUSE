#
# spec file for package mylvmbackup
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


Name:           mylvmbackup
Version:        0.16
Release:        0
Summary:        Utility for creating MySQL backups via LVM snapshots
License:        GPL-2.0+
Group:          Productivity/Archiving/Backup
Url:            http://www.lenzg.net/mylvmbackup/
Source0:        http://www.lenzg.net/mylvmbackup/mylvmbackup-%{version}.tar.gz
Source1:        http://www.lenzg.net/mylvmbackup/mylvmbackup-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Requires:       perl(Config::IniFiles)
Requires:       perl(DBD::mysql)
Requires:       perl(DBI)
Requires:       perl(Date::Format)
Requires:       perl(Fcntl)
Requires:       perl(File::Basename)
Requires:       perl(File::Copy)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(File::Path)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(Sys::Hostname)
Recommends:     perl(MIME::Lite)
Recommends:     perl(Net::SNMP)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
mylvmbackup is a script for quickly creating backups of MySQL server's data
files. To perform a backup, mylvmbackup obtains a read lock on all tables and
flushes all server caches to disk, makes an LVM snapshot of the volume
containing the MySQL data directory, and unlocks the tables again. The snapshot
process takes only a small amount of time. When it is done, the server can
continue normal operations, while the actual file backup proceeds.

%prep
%setup -q

%build

%install
make \
	DESTDIR=%{buildroot} \
	prefix=%{_prefix} \
	mandir=%{_mandir} \
	install

%files
%defattr(-, root, root)
%doc ChangeLog COPYING CREDITS README TODO
%config(noreplace,missingok) %attr(600, root, root) %{_sysconfdir}/mylvmbackup.conf
%{_datadir}/%{name}/*.pm
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
