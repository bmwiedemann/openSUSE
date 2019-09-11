#
# spec file for package dirvish
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dirvish
Version:        1.2.1
Release:        0
Summary:        Fast, disk based, rotating network backup system
License:        OSL-2.0
Group:          Productivity/Archiving/Backup
Url:            http://www.dirvish.org/
Source0:        http://www.dirvish.org/dirvish-%{version}.tgz
Source1:        master.conf
# PATCH-FIX-UPSTREAM dirvish-1.2.1-install.patch jweberhofer@weberhofer.at -- Converts the installer to work in unattended mode
Patch0:         dirvish-1.2.1-install.patch
# PATCH-FIX-UPSTREAM dirvish-expire-vanished.patch jweberhofer@weberhofer.at -- Allows expiration of vanished backups
Patch1:         dirvish-expire-vanished.patch
# PATCH-FIX-UPSTREAM dirvish-imsort-reserved-warning.patch paul@debian.org -- Fix for future reserved word warning
Patch2:         dirvish-imsort-reserved-warning.patch
# PATCH-FIX-UPSTREAM dirvish-rsync-options.patch ondrej@debian.org -- Fix typo in docs about rsync-options which was deprecated
Patch3:         dirvish-rsync-options.patch
# PATCH-FIX-UPSTREAM dirvish-locate.patch paul@debian.org -- Get patch level of loadconfig.pl in case exit codes are needed.
Patch4:         dirvish-locate.patch
# PATCH-FIX-UPSTREAM dirvish-lock-vault-against-overlapping-runs.patch John Altstadt -- Lock vault against overlapping runs
Patch5:         dirvish-lock-vault-against-overlapping-runs.patch
Requires:       perl
Requires:       perl(Time::ParseDate)
Requires:       perl(Time::Period)
Requires:       rsync
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Dirvish is a fast, disk based, rotating network backup system. With dirvish you
can maintain a set of complete images of your filesystems with unattended
creation and expiration. A dirvish backup vault is like a time machine for your
data.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/master.conf

PREFIX=%{buildroot}%{_prefix} ./install.sh

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/dirvish
%config(noreplace) %{_sysconfdir}/%{name}/master.conf
%{_bindir}/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%doc CHANGELOG FAQ.html RELEASE.html TODO.html COPYING

%changelog
