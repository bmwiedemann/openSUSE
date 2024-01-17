#
# spec file for package storeBackup
#
# Copyright (c) 2021 SUSE LLC
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


Name:           storeBackup
Version:        3.5
Release:        0
Summary:        A disk-to-disk backup tool for Linux
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
Source0:        storeBackup-%{version}.tar.bz2
Source1:        storeBackup-%{version}.config.default
Source2:        storeBackup-README.SUSE
Source3:        storeBackup.service
Source4:        storeBackup.timer
Source5:        storeBackup-run-all
# PATCH-FIX-UPSTREAM earlier_execute_precommand.patch http://savannah.nongnu.org/bugs/?46605
Patch0:         earlier_execute_precommand.patch
# PATCH-FIX-OPENSUSE fix-rpmlint-env-script-interpreter.patch
Patch1:         fix-rpmlint-env-script-interpreter.patch
# PATCH-FIX-UPSTREAM fix-tmp-lock-file-race-condition.patch CVE-2020-7040 bsc#1156767
Patch2:         fix-tmp-lock-file-race-condition.patch
URL:            http://storebackup.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       bzip2
Requires:       e2fsprogs
Requires:       fileutils
Requires:       sh-utils
Requires:       textutils
Requires:       which

%description
storeBackup is a disk-to-disk backup tool. The backuped files can be
directly browsed (locally, via NFS, via SAMBA or whatever). This
gives the users the possibility to restore files. They only have to
copy (and possibly uncompress) the file. The is also a tool for
restoring (sub) trees for the administrator. Every single backup of a
specific time can be deleted without affecting the other existing
backups.

Before you can start using storeBackup, please carefully read
        /usr/share/doc/packages/storeBackup/README.1ST
and create an appropriate configuration file
        /etc/storebackup.d/storebackup.config
using
        /usr/share/doc/packages/storeBackup/storebackup.config.default
as a template.

%prep
%setup -n storeBackup
%patch0 -p 0
%patch1 -p 1
%patch2 -p 1

%build
# make

%install
#
install		-d	%{buildroot}					\
			%{buildroot}/usr/lib/storeBackup/			\
			%{buildroot}/usr/bin/				\
			%{buildroot}/usr/share/doc/packages/storeBackup/	\
			%{buildroot}/etc/storebackup.d/			\
			%{buildroot}%{_sbindir}/			\
			%{buildroot}/%{_unitdir}/				\
			%{buildroot}/%{_mandir}/man1
#
cp -a %{S:1}								./doc/storebackup.config.default
cp -a %{S:2}								./doc/README.SUSE
cp -a _ATTENTION_ correct.sh						./doc/
cp -aRpv bin/ lib/							%{buildroot}/usr/lib/storeBackup/
ln -sf /usr/lib/storeBackup/bin/storeBackup.pl				%{buildroot}/usr/bin/storeBackup.pl
ln -sf /usr/lib/storeBackup/bin/storeBackup.pl				%{buildroot}/usr/bin/storeBackup
ln -sf /usr/lib/storeBackup/bin/storeBackupCheckBackup.pl		%{buildroot}/usr/bin/storeBackupCheckBackup.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupCheckSource.pl		%{buildroot}/usr/bin/storeBackupCheckSource.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupConvertBackup.pl		%{buildroot}/usr/bin/storeBackupConvertBackup.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupDel.pl			%{buildroot}/usr/bin/storeBackupDel.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupMergeIsolatedBackup.pl	%{buildroot}/usr/bin/storeBackupMergeIsolatedBackup.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupMount.pl			%{buildroot}/usr/bin/storeBackupMount.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupRecover.pl			%{buildroot}/usr/bin/storeBackupRecover.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupReplicationWizard.pl		%{buildroot}/usr/bin/storeBackupReplicationWizard.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupSearch.pl			%{buildroot}/usr/bin/storeBackupSearch.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupSetupIsolatedMode.pl		%{buildroot}/usr/bin/storeBackupSetupIsolatedMode.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupUpdateBackup.pl		%{buildroot}/usr/bin/storeBackupUpdateBackup.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupVersions.pl			%{buildroot}/usr/bin/storeBackupVersions.pl
ln -sf /usr/lib/storeBackup/bin/storeBackupls.pl			%{buildroot}/usr/bin/storeBackupls.pl
ln -sf /usr/lib/storeBackup/bin/storeBackup_du.pl			%{buildroot}/usr/bin/storeBackup_du.pl
#
install -m 644 man/man1/*.1 %{buildroot}/%{_mandir}/man1
ln -sf storeBackup.pl.1 %{buildroot}/%{_mandir}/man1/storeBackup.1
install -m 644 %{S:3} %{buildroot}/%{_unitdir}/%{name}.service
install -m 644 %{S:4} %{buildroot}/%{_unitdir}/%{name}.timer
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -m 755 %{S:5} %{buildroot}/%{_prefix}/lib/%{name}/%{name}-run-all
%{?suse_check}

%pre
%service_add_pre %{name}.service %{name}.timer

%post
%service_add_post %{name}.service %{name}.timer

%preun
%service_del_preun %{name}.service %{name}.timer

%postun
%service_del_postun %{name}.service %{name}.timer

%files
%defattr(-,root,root)
%doc doc/*
%doc %{_mandir}/man1/*.1.gz
# ChangeLog LICENSE README.1ST _ATTENTION_ README storebackup.config.default README.SUSE
/usr/lib/storeBackup/
%dir /etc/storebackup.d/
# %attr(755, root, root) %config(noreplace) /etc/storebackup.d/storebackup.config
%attr(755, root, root) /usr/bin/*
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer

%changelog
