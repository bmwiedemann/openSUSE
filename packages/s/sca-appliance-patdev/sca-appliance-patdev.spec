# 
# spec file for package sca-appliance-patdev
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define sca_common sca
%define sca_webdir /srv/www/htdocs/%{sca_common}
%define sca_configdir %{_sysconfdir}/%{sca_common}

Name:         sca-appliance-patdev
Version:      1.3
Release:      0
Summary:      Supportconfig Analysis Appliance Pattern Development
License:      GPL-2.0
URL:          https://github.com/g23guy/sca-appliance-patdev
Group:        System/Monitoring
Source:       %{name}-%{version}.tar.gz
Requires:     sca-appliance-common
Requires:     sca-patterns-base
Buildarch:    noarch

%description
The SCA Appliance allows for adding custom patterns. This package
provides a database used to create pattern templates, speeding up
custom pattern development.

See %{_docdir}/sca-appliance-common/COPYING.GPLv2

%prep
%setup -q

%build
gzip -9f man/*1
gzip -9f man/*5
gzip -9f man/*8

%install
pwd;ls -la
mkdir -p %{buildroot}%{sca_configdir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_bindir}
install -d %{buildroot}%{sca_webdir}/docs-python
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_docdir}/%{name}
install -m 644 config/*.conf %{buildroot}%{sca_configdir}
install -m 644 config/* %{buildroot}%{_docdir}/%{name}
install -m 555 bin/pat %{buildroot}%{_bindir}
install -m 544 bin/sdpdb %{buildroot}%{_sbindir}
install -m 544 bin/setup-sdp %{buildroot}%{_sbindir}
install -m 644 docs-python/* %{buildroot}%{sca_webdir}/docs-python
install -m 644 websdp/* %{buildroot}%{sca_webdir}
install -m 400 websdp/sdp-config.php %{buildroot}%{sca_webdir}
install -m 644 schema/* %{buildroot}%{_docdir}/%{name}
install -m 644 docs/README* %{buildroot}%{_docdir}/%{name}
install -m 644 man/*.1.gz %{buildroot}%{_mandir}/man1
install -m 644 man/*.5.gz %{buildroot}%{_mandir}/man5
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%dir %attr(-,wwwrun,www) %{sca_webdir}
%dir %attr(-,wwwrun,www) %{sca_webdir}/docs-python
%dir %{sca_configdir}
%{_sbindir}/sdpdb
%{_sbindir}/setup-sdp
%{_bindir}/pat
%config %{sca_configdir}/sdp.conf
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man8/*
%attr(-,wwwrun,www) %{sca_webdir}/*
%doc %{_docdir}/%{name}/*

%changelog

