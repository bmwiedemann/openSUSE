# 
# spec file for package sca-appliance-broker
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

Name:         sca-appliance-broker
Version:      1.3
Release:      0
Summary:      Supportconfig Analysis Appliance Broker
License:      GPL-2.0
URL:          https://github.com/g23guy/sca-appliance-broker
Group:        System/Monitoring
Source:       %{name}-%{version}.tar.gz
Requires:     sca-appliance-common
Buildarch:    noarch

%description
Monitors inbound supportconfig archives and is responsible for
assigning new and retry archives states for appropriate agent analysis. 

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
mkdir -p %{buildroot}%{sca_webdir}
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_docdir}/%{name}
install -m 644 config/*.conf %{buildroot}%{sca_configdir}
install -m 644 config/* %{buildroot}%{_docdir}/%{name}
install -m 644 websca/index.html %{buildroot}%{_docdir}/%{name}
install -m 640 websca/* %{buildroot}%{sca_webdir}
install -m 544 bin/* %{buildroot}%{_sbindir}
install -m 644 schema/* %{buildroot}%{_docdir}/%{name}
install -m 644 docs/* %{buildroot}%{_docdir}/%{name}
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8
install -m 644 man/*.5.gz %{buildroot}%{_mandir}/man5

%files
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%dir %attr(-,wwwrun,www) %{sca_webdir}
%dir %{sca_configdir}
%{_sbindir}/scadb
%{_sbindir}/sdbroker
%{_sbindir}/sdbroker-monitor
%{_sbindir}/setup-sca
%{_sbindir}/setup-sdagent
%{_sbindir}/setup-sdbroker
%attr(-,wwwrun,www) %{sca_webdir}/*
%config %{sca_configdir}/sdbroker.conf
%doc %{_mandir}/man8/*
%doc %{_mandir}/man5/*
%attr(-,wwwrun,www) %{_docdir}/%{name}/index.html
%doc %{_docdir}/%{name}/*

%post
if [[ -s /srv/www/htdocs/index.html ]]; then
	if grep -i '<html><body><h1>It works!</h1></body></html>' /srv/www/htdocs/index.html &>/dev/null; then
		mv /srv/www/htdocs/index.html /srv/www/htdocs/index.html.sca_orig
		cp -a %{_docdir}/%{name}/index.html /srv/www/htdocs/
	else
		echo
		echo "WARNING: File already exists: /srv/www/htdocs/index.html"
		echo " Redirector %{_docdir}/%{name}/index.html will not be installed."
		echo
	fi
else
	cp -a %{_docdir}/%{name}/index.html /srv/www/htdocs/
fi

%postun
if [[ -s /srv/www/htdocs/index.html.sca_orig ]]; then
	mv /srv/www/htdocs/index.html.sca_orig /srv/www/htdocs/index.html
elif grep -i 'sca/index.php' /srv/www/htdocs/index.html &>/dev/null; then
	mv /srv/www/htdocs/index.html /srv/www/htdocs/index.html.sca_redirector
fi

%changelog

