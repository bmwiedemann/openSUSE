#
# spec file for package phpPgAdmin
#
# Copyright (c) 2020 SUSE LLC
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


Name:           phpPgAdmin

%define lc_name phppgadmin
%define apxs %{_sbindir}/apxs2
%define ap_sysconfdir %(%{apxs} -q SYSCONFDIR)
%define ap_serverroot %(%{apxs} -q PREFIX)
%define ap_docroot %(%{apxs} -q PREFIX)/htdocs
%define ppa_config %{_sysconfdir}/%{name}/config.inc.php

Summary:        Administration of PostgreSQL over the web
License:        GPL-2.0-or-later
Group:          Productivity/Databases/Tools
Version:        7.12.1
Release:        0
#define rel_version %(/usr/bin/sed -e "s/\./-/g" <<<%{version})
%define rel_version REL_7-12-1
URL:            http://phppgadmin.sourceforge.net
Source0:        https://github.com/%{lc_name}/%{lc_name}/releases/download/%{rel_version}/%{name}-%{version}.tar.bz2
Source1:        %{name}.http
Patch0:         %{name}-config.inc.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  apache2-devel
Requires:       mod_php_any
Requires:       php >= 7.1
Requires:       php-pgsql

%description
phpPgAdmin is a web-based administration tool for PostgreSQL. It is
perfect for PostgreSQL DBAs, newbies and hosting services.

Features

* Administer multiple servers
* Support for PostgreSQL 9.x.x, 10.x, 11.x, 12.x
* Manage all aspects of:
	o Users & groups
	o Databases
	o Schemas
	o Tables, indexes, constraints, triggers, rules & privileges
	o Views, sequences & functions
	o Advanced objects
	o Reports
* Easy data manipulation:
	o Browse tables, views & reports
	o Execute arbitrary SQL
	o Select, insert, update and delete
* Dump table data in a variety of formats: SQL, COPY, XML, XHTML, CSV, Tabbed, pg_dump
* Import SQL scripts, COPY data, XML, CSV and Tabbed
* Supports the Slony master-slave replication engine
* Excellent language support:
	o Available in 27 languages
	o No encoding conflicts. Edit Russian data using a Japanese interface!
* Easy to install and configure

%prep
%setup -q
%patch0

%build

%install
%{__install} -d %{buildroot}%{ap_docroot}/%{name}
%{__cp} -dR *.php *.js classes help images lang libraries plugins themes xloadtree \
%{buildroot}%{ap_docroot}/%{name}

# install config to config dir
%{__install} -D -m0640 conf/config.inc.php-dist \
%{buildroot}%{ppa_config}

# install config for apache
%{__install} -D -m0644 %{S:1} %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.conf

# fix paths in http config
%{__sed} -i -e "s,@ap_docroot@,%{ap_docroot},g" -e "s,@name@,%{name},g" \
-e "s,@docdir@,%{_docdir},g" %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.conf

# remove not needed files from lang/
for i in Makefile convert.awk langcheck php2po po2php synch; do
%{__rm} -f %{buildroot}%{ap_docroot}/%{name}/lang/${i}
done

%postun
%restart_on_update apache2

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%if 0%{?suse_version} >= 1500
%license LICENSE
%else
%doc LICENSE
%endif
%doc CREDITS DEVELOPERS FAQ HISTORY TODO TRANSLATORS
%{ap_docroot}/%{name}
%config(noreplace) %{ap_sysconfdir}/conf.d/%{name}.conf
%dir %attr(0750,wwwrun,root) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,root,www) %{ppa_config}

%changelog
