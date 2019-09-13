#
# spec file for package ganglia-web
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


%define web_prefixdir /srv/www/htdocs/ganglia-web

Name:           ganglia-web
Version:        3.7.2
Release:        0
Summary:        Ganglia web frontend
License:        BSD-3-Clause
Group:          System/Monitoring
Url:            http://ganglia.info/
Source0:        https://downloads.sourceforge.net/project/ganglia/ganglia-web/3.7.2/ganglia-web-3.7.2.tar.gz
Source1:        ganglia-httpd24.conf.d
Source2:        README.SUSE
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
%setup -q
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
install %SOURCE1 %{buildroot}/etc/apache2/conf.d/%{name}.conf

%fdupes %{buildroot}%{web_prefixdir}
%fdupes %{buildroot}%{_localstatedir}/lib/ganglia-web

%files
%defattr(-,root,root)
%doc AUTHORS COPYING TODO README README.SUSE
%dir %{web_prefixdir}/
%dir %{web_prefixdir}/dwoo
%{web_prefixdir}/*
%config(noreplace) %{web_prefixdir}/conf_default.php
%config(noreplace) /etc/apache2/conf.d/%{name}.conf
%dir %{_localstatedir}/lib/ganglia-web
%{_localstatedir}/lib/ganglia-web/conf
%attr(0755,wwwrun,www)%{_localstatedir}/lib/%{name}/dwoo
%attr(0755,wwwrun,www)%{_localstatedir}/lib/%{name}/dwoo/compiled
%attr(0755,wwwrun,www)%{_localstatedir}/lib/%{name}/dwoo/cache

%changelog
