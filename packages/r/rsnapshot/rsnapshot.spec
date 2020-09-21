#
# spec file for package rsnapshot
#
# Copyright (c) 2020 SUSE LLC
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


Name:           rsnapshot
Version:        1.4.3
Release:        0
Summary:        Backup program using hardlinks
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Backup
URL:            http://www.rsnapshot.org/
Source0:        https://github.com/rsnapshot/rsnapshot/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        rsnapshot.logrotate
Patch1:         rsnapshot-config.patch
Patch2:         skip-ssh-test.patch
Patch3:         remove-dead-external-css-link.patch
Patch4:         backup_pgsql.patch
BuildRequires:  logrotate
BuildRequires:  openssh
BuildRequires:  perl
BuildRequires:  rsync
BuildRequires:  util-linux-systemd
Requires:       logrotate
Requires:       openssh
Requires:       perl
Requires:       rsync
Requires:       util-linux-systemd
BuildArch:      noarch

%description
rsnapshot is a filesystem snapshot utility for making backups of local
and remote systems. Using rsync and hard links, it is possible to keep
multiple, full backups instantly available. The disk space required is
just a little more than the space of one full backup, plus
incrementals. Depending on your configuration, it is quite possible to
set up in just a few minutes. Files can be restored by the users who
own them, without the root user getting involved. There are no tapes to
change, so once it's set up, you may never need to think about it
again.

%prep
%setup -q
%autopatch -p1

%build
# replace hardcoded /usr/local
find docs utils *pl *md *in -type f -exec sed -i "s|usr/local|usr|g" {} +

%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%make_install
install -d "%{buildroot}/%{_sysconfdir}"
install -m 644 rsnapshot.conf.default "%{buildroot}/%{_sysconfdir}/rsnapshot.conf.default"
install -m 600 rsnapshot.conf.default "%{buildroot}/%{_sysconfdir}/rsnapshot.conf"
install -m 644 -D %{SOURCE1} "%{buildroot}/%{_sysconfdir}/logrotate.d/rsnapshot"

%files
%license COPYING
%doc AUTHORS ChangeLog README.md docs utils
%{_bindir}/rsnapshot
%{_bindir}/rsnapshot-diff
%config(noreplace) %{_sysconfdir}/rsnapshot.conf
%config %{_sysconfdir}/rsnapshot.conf.default
%config(noreplace) %{_sysconfdir}/logrotate.d/rsnapshot
%{_mandir}/man1/rsnapshot.1%{?ext_man}
%{_mandir}/man1/rsnapshot-diff.1%{?ext_man}

%changelog
