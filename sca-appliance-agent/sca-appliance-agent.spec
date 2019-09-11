#
# spec file for package sca-appliance-agent
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


%define sca_common sca
%define sca_libdir /usr/lib/%{sca_common}
%define sca_configdir %{_sysconfdir}/%{sca_common}

Name:           sca-appliance-agent
Version:        1.3
Release:        0
Summary:        Supportconfig Analysis Appliance Agent
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/g23guy/sca-appliance-agent
Source:         %{name}-%{version}.tar.gz
Requires:       sca-appliance-common
Requires:       sca-patterns-base
BuildArch:      noarch

%description
Analyzes supportconfig archives using the Supportconfig Analysis patterns. The results are
posted in a MySQL database and can be posted or emailed as an html report. 

See %{_docdir}/sca-appliance-common/COPYING.GPLv2

%prep
%setup -q

%build
gzip -9f man/*8
gzip -9f man/*5

%install
pwd;ls -la
mkdir -p %{buildroot}%{sca_configdir}
mkdir -p %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_docdir}/%{name}
install -d %{buildroot}%{sca_libdir}/php
install -m 644 config/*.conf %{buildroot}%{sca_configdir}
install -m 644 config/* %{buildroot}%{_docdir}/%{name}
install -m 544 bin/sdagent* %{buildroot}%{_sbindir}
install -m 640 bin/reportfull.php %{buildroot}%{sca_libdir}/php
install -m 644 docs/* %{buildroot}%{_docdir}/%{name}
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8
install -m 644 man/*.5.gz %{buildroot}%{_mandir}/man5

%files
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%dir %{sca_configdir}
%dir %{sca_libdir}
%dir %{sca_libdir}/php
%{sca_libdir}/php/*
%{_sbindir}/sdagent*
%config %{sca_configdir}/sdagent.conf
%config %{sca_configdir}/sdagent-patterns.conf
%config %{sca_configdir}/sdagent-supportconfig.conf
%doc %{_mandir}/man8/*
%doc %{_mandir}/man5/*
%doc %{_docdir}/%{name}/*

%changelog
