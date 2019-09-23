#
# spec file for package sca-server-report
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
%define sca_config scatool
%define libbase /usr/lib/%{sca_common}
%define sca_python %{libbase}/python

Name:           sca-server-report
Version:        1.0
Release:        0
Summary:        Supportconfig Analysis Server Report
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/g23guy/sca-server-report
Source:         %{name}-%{version}.tar.gz
Requires:       python
Requires:       sca-patterns-base
Requires:       w3m
BuildArch:      noarch

%description
A tool that primarily analyzes the local server, but can analyze other 
supportconfigs that have been copied to the server. It uses the 
Supportconfig Analysis patterns to perform the analysis.

See %{_docdir}/sca-patterns-base/COPYING.GPLv2

%prep
%setup -q

%build
gzip -9f man/*5
gzip -9f man/*8

%install
pwd;ls -la
install -d %{buildroot}%{_sysconfdir}/%{sca_config}
install -d %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{sca_python}
mkdir -p %{buildroot}%{_sbindir}
install -m 544 bin/scatool %{buildroot}%{_sbindir}
install -m 644 bin/scatool.py %{buildroot}/%{sca_python}
install -m 644 config/scatool.conf %{buildroot}%{_sysconfdir}/%{sca_config}
install -m 644 man/*.5.gz %{buildroot}%{_mandir}/man5
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%{_sbindir}/scatool
%dir %{libbase}
%dir %{sca_python}
%{sca_python}/*
%dir %{_sysconfdir}/%{sca_config}
%config %{_sysconfdir}/%{sca_config}/*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man8/*

%changelog
