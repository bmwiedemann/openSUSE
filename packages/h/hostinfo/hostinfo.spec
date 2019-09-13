#
# spec file for package hostinfo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hostinfo
Version:        1.0
Release:        0
Summary:        Gathers basic server information
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/g23guy/hostinfo
Source:         %{name}-%{version}.tar.gz
Requires:       iproute2
Requires:       issue-generator
Requires:       sed
BuildArch:      noarch

%description
A script that displays current system information to help 
identify a host and its resources.
 
%prep
%setup -q

%build
gzip -9f man/*8

%install
pwd;ls -la
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_docdir}/%{name}
install -m 644 conf/hostinfo.conf %{buildroot}%{_sysconfdir}
install -m 644 conf/91-hostinfo.rules %{buildroot}%{_udevrulesdir}/91-hostinfo.rules
install -D -m 644 conf/hostinfo.service %{buildroot}%{_unitdir}/hostinfo.service
install -D -m 644 conf/hostinfo.timer %{buildroot}%{_unitdir}/hostinfo.timer
install -m 755 bin/hostinfo %{buildroot}%{_sbindir}
install -m 444 man/COPYING.GPLv2 %{buildroot}%{_docdir}/%{name}
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8
ln -sf service %{buildroot}%{_sbindir}/rchostinfo

%files
%defattr(-,root,root)
%{_sbindir}/hostinfo
%{_sbindir}/rchostinfo
%{_unitdir}/hostinfo.service
%{_unitdir}/hostinfo.timer
%{_udevrulesdir}/91-hostinfo.rules
%config %{_sysconfdir}/hostinfo.conf
%{_mandir}/man8/*
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%pre
%service_add_pre hostinfo.service hosinfo.timer

%post
%service_add_post hostinfo.service hostinfo.timer

%preun
%service_del_preun hostinfo.service hostinfo.timer
/usr/sbin/hostinfo Uninstalled

%postun
%service_del_postun hostinfo.service hostinfo.timer

%changelog
