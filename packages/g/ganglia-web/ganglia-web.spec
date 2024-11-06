#
# spec file for package ganglia-web
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


%define web_prefixdir /srv/www/htdocs/ganglia-web
%define gittag f5bdfca75f9f5d701c8f8e9310f7801cd2e62799

Name:           ganglia-web
Version:        3.7.5
Release:        0
Summary:        Ganglia web frontend
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            http://ganglia.info/
Source0:        https://github.com/ganglia/ganglia-web/archive/%{gittag}.tar.gz#/ganglia-web-%{version}.tar.gz
Source1:        ganglia-httpd24.conf.d
Source2:        README.SUSE
Patch1:         0001-added-of-download_js.patch
Patch2:         0002-looking-for-systemwide-user-config.patch
BuildRequires:  apache2
BuildRequires:  fdupes
BuildRequires:  rsync
Requires:       apache2
Requires:       mod_php_any
Requires:       php
Requires:       php-gd
Requires:       php-xml
Requires:       rrdtool
Recommends:     ganglia-gmetad
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a web frontend to display the XML tree published by
ganglia, and to provide historical graphs of collected metrics. This website is
written in the PHP5/7 language and uses the Dwoo templating engine.

%prep
%setup -q -n %{name}-%{gittag}
%autopatch -p1

%build
cp %SOURCE2 .

%install
%{__sed} -i 's,www-data,abuild,' Makefile
%{__sed} -i 's,/usr/share/ganglia-webfrontend,%{buildroot}%{web_prefixdir},'  Makefile
%{__sed} -i 's,WEBPATH,%{web_prefixdir},' %SOURCE1
%{__sed} -i 's,/etc/ganglia-web,%{buildroot}/etc/apache2/conf.d,' Makefile
%{__sed} -i 's,/var/lib/ganglia,%{buildroot}/var/lib/ganglia,' Makefile

make install
install -d %{buildroot}/etc/apache2/conf.d
install -m 644 %SOURCE1 %{buildroot}/etc/apache2/conf.d/%{name}.conf
mkdir -pv %{buildroot}%{_docdir}/%{name}/
cp -v download_js.sh %{buildroot}%{_docdir}/%{name}/download_js.sh
# fix suprious buildroot in config
%{__sed} -i 's@%{buildroot}@@' %{buildroot}/%{web_prefixdir}/conf_default.php

%fdupes %{buildroot}%{web_prefixdir}
%fdupes %{buildroot}%{_localstatedir}/lib/ganglia-web

%files
%defattr(-,root,root)
%doc AUTHORS TODO README README.SUSE
%{_docdir}/%{name}/download_js.sh
%license COPYING
%dir /srv/www
%dir /srv/www/htdocs
%dir %{web_prefixdir}/
%dir %{web_prefixdir}/dwoo
%{web_prefixdir}/*
%config(noreplace) /etc/apache2/conf.d/%{name}.conf
%dir %{_localstatedir}/lib/ganglia-web
%{_localstatedir}/lib/ganglia-web/conf
%attr(0755,wwwrun,www)%{_localstatedir}/lib/%{name}/dwoo
%attr(0755,wwwrun,www)%{_localstatedir}/lib/%{name}/dwoo/compiled
%attr(0755,wwwrun,www)%{_localstatedir}/lib/%{name}/dwoo/cache

%changelog
