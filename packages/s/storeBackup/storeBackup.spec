#
# spec file for package storeBackup
#
# Copyright (c) 2024 SUSE LLC
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
Version:        3.5.2
Release:        0
Summary:        A disk-to-disk backup tool for Linux
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            http://storebackup.org/
Source0:        https://download.savannah.nongnu.org/releases/storebackup/storeBackup-%{version}.tar.bz2
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
BuildRequires:  systemd-rpm-macros
Requires:       bzip2
Requires:       e2fsprogs
Requires:       fileutils
Requires:       sh-utils
Requires:       textutils
Requires:       which
BuildArch:      noarch

%description
storeBackup is a disk-to-disk backup tool. The backuped files can be
directly browsed (locally, via NFS, via SAMBA or whatever). This
gives the users the possibility to restore files. They only have to
copy (and possibly uncompress) the file. The is also a tool for
restoring (sub) trees for the administrator. Every single backup of a
specific time can be deleted without affecting the other existing
backups.

Before you can start using storeBackup, please carefully read
        %{_docdir}/storeBackup/README.1ST
and create an appropriate configuration file
        %{_sysconfdir}/storebackup.d/storebackup.config
using
        %{_docdir}/storeBackup/storebackup.config.default
as a template.

%prep
%setup -q -n storeBackup
%patch -P 0 -p 0
%patch -P 1 -p 1
%patch -P 2 -p 1

%build
# make

%install
#
install		-d	%{buildroot}					\
			%{buildroot}%{_prefix}/lib/storeBackup/			\
			%{buildroot}%{_bindir}/				\
			%{buildroot}%{_docdir}/storeBackup/	\
			%{buildroot}%{_sysconfdir}/storebackup.d/			\
			%{buildroot}%{_sbindir}/			\
			%{buildroot}/%{_unitdir}/				\
			%{buildroot}/%{_mandir}/man1
#
cp -a %{SOURCE1}								./doc/storebackup.config.default
cp -a %{SOURCE2}								./doc/README.SUSE
cp -a _ATTENTION_ correct.sh						./doc/
cp -aRpv bin/ lib/							%{buildroot}%{_prefix}/lib/storeBackup/
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackup.pl				%{buildroot}%{_bindir}/storeBackup.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackup.pl				%{buildroot}%{_bindir}/storeBackup
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupCheckBackup.pl		%{buildroot}%{_bindir}/storeBackupCheckBackup.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupCheckSource.pl		%{buildroot}%{_bindir}/storeBackupCheckSource.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupConvertBackup.pl		%{buildroot}%{_bindir}/storeBackupConvertBackup.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupDel.pl			%{buildroot}%{_bindir}/storeBackupDel.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupMergeIsolatedBackup.pl	%{buildroot}%{_bindir}/storeBackupMergeIsolatedBackup.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupMount.pl			%{buildroot}%{_bindir}/storeBackupMount.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupRecover.pl			%{buildroot}%{_bindir}/storeBackupRecover.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupReplicationWizard.pl		%{buildroot}%{_bindir}/storeBackupReplicationWizard.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupSearch.pl			%{buildroot}%{_bindir}/storeBackupSearch.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupSetupIsolatedMode.pl		%{buildroot}%{_bindir}/storeBackupSetupIsolatedMode.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupUpdateBackup.pl		%{buildroot}%{_bindir}/storeBackupUpdateBackup.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupVersions.pl			%{buildroot}%{_bindir}/storeBackupVersions.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackupls.pl			%{buildroot}%{_bindir}/storeBackupls.pl
ln -sf %{_prefix}/lib/storeBackup/bin/storeBackup_du.pl			%{buildroot}%{_bindir}/storeBackup_du.pl
#
install -m 644 man/man1/*.1 %{buildroot}/%{_mandir}/man1
ln -sf storeBackup.pl.1 %{buildroot}/%{_mandir}/man1/storeBackup.1
install -m 644 %{SOURCE3} %{buildroot}/%{_unitdir}/%{name}.service
install -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}/%{name}.timer
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -m 755 %{SOURCE5} %{buildroot}/%{_prefix}/lib/%{name}/%{name}-run-all
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
%doc doc/*
%{_mandir}/man1/*.1%{?ext_man}
# ChangeLog LICENSE README.1ST _ATTENTION_ README storebackup.config.default README.SUSE
%{_prefix}/lib/storeBackup/
%dir %{_sysconfdir}/storebackup.d/
%attr(755, root, root) %{_bindir}/*
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer

%changelog
