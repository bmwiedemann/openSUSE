#
# spec file for package fs-check
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


Name:           fs-check
Version:        0.9
Release:        0
Summary:        Check File System Usage
License:        GPL-2.0+
Group:          System/Monitoring
Url:            http://fs-check.sourceforge.net
Source:         http://sourceforge.net/projects/fs-check/files/fs-check/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.cf
Patch0:         %{name}-%{version}.dif
BuildRequires:  mailx
Requires:       mailx
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
fs-check checks file system sizes to see if they are getting too full.
It uses a configuration file that specifies the file systems to check,
e-mail contacts, trigger thresholds (percentage or amount used and
unused), and a report program to run. It includes fs-report, which
shows things like the largest files, the newest files, and core files.
It can be run from cron or as a daemon.

%prep
%setup -q
%patch0

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/etc
cp %{SOURCE1} %{buildroot}/etc
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -D -m 644 doc/fs-report.8 %{buildroot}%{_mandir}/man8/fs-report.8
install -D -m 644 doc/fs-check.8 %{buildroot}%{_mandir}/man8/fs-check.8

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS sample/crontab.add
%config(noreplace) %{_sysconfdir}/fs-check.cf
%{_mandir}/man8/fs-check.8.gz
%{_mandir}/man8/fs-report.8.gz
%{_bindir}/fs-check
%{_bindir}/fs-report

%changelog
