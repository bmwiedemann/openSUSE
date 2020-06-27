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
%define ap_docroot_old %(%{apxs} -q PREFIX)/htdocs
%define ap_docroot %{_datadir}
%define ppa_config %{_sysconfdir}/%{name}/config.inc.php

Summary:        Administration of PostgreSQL over the web
License:        GPL-2.0-or-later
Group:          Productivity/Databases/Tools
Version:        7.12.1
Release:        0
%define rel_version REL_7-12-1
URL:            http://phppgadmin.sourceforge.net
Source0:        https://github.com/%{lc_name}/%{lc_name}/releases/download/%{rel_version}/%{name}-%{version}.tar.bz2
Source1:        %{name}.http
Source2:        %{name}.http.inc
Patch0:         %{name}-config.inc.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  apache2-devel
BuildRequires:  fdupes
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

### remove not needed files
pushd lang
rm -f README langcheck synch
popd

%build

%install
%{__install} -d %{buildroot}%{ap_docroot}/%{name}
%{__cp} -dR *.php *.js classes help images js lang libraries plugins themes xloadtree \
%{buildroot}%{ap_docroot}/%{name}

# install config to config dir
%{__install} -D -m0640 conf/config.inc.php-dist \
%{buildroot}%{ppa_config}

# generate file list
find %{buildroot}%{ap_docroot}/%{name} -mindepth 1 -maxdepth 1 -type d | grep -v 'conf' | sed -e "s@$RPM_BUILD_ROOT@@" > FILELIST
find %{buildroot}%{ap_docroot}/%{name} -maxdepth 1 -type f | grep -v 'config.inc.php-dist' | sed -e "s@$RPM_BUILD_ROOT@@" >> FILELIST

# install config for apache
%{__install} -D -m0644 %{S:1} %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.conf
%{__install} -D -m0644 %{S:2} %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.inc

# fix paths in http config
%{__sed} -i -e "s,@ap_docroot@,%{ap_docroot},g" -e "s,@name@,%{name},g" \
-e "s,@docdir@,%{_docdir},g" -e "s,@ap_sysconfdir@,%{ap_sysconfdir},g" %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.conf

# rpmlint stuff
%fdupes %{buildroot}%{ap_docroot}/%{name}

%post
# enable phpPgAdmin flag
if [ -x %{_sbindir}/a2enflag ]; then
  flag_find=$(grep -cw /etc/sysconfig/apache2 -e "^APACHE_SERVER_FLAGS=.*%{name}.*")
  if [ $flag_find -eq 0 ]; then
    echo "info: adding %{name} to APACHE_SERVER_FLAGS"
    a2enflag %{name}
  fi
fi
# We changed ap_docroot from {ap_docroot_old} to {ap_docroot} (/srv/www/htdocs to /usr/share)
# If someone did 'manually' change the config file it won't be replaced by rpm
# Hence we backup the existing and place the new one
find=0
find=$(grep -cw %{ap_sysconfdir}/conf.d/%{name}.conf -e "%{ap_docroot_old}/%{name}") || :
if [ $find -gt 0 ]; then
  ap_date="$(date '+%Y%m%d-%H%M')"
  echo "creating backup of %{ap_sysconfdir}/conf.d/%{name}.conf to %{ap_sysconfdir}/conf.d/%{name}.conf.backup-${ap_date}"
  cp -a %{ap_sysconfdir}/conf.d/%{name}.conf %{ap_sysconfdir}/conf.d/%{name}.conf.backup-${ap_date}
  echo "copying %{ap_sysconfdir}/conf.d/%{name}.conf.rpmnew to %{ap_sysconfdir}/conf.d/%{name}.conf"
  cp -a %{ap_sysconfdir}/conf.d/%{name}.conf.rpmnew %{ap_sysconfdir}/conf.d/%{name}.conf
fi
%restart_on_update apache2

%postun
# only do on uninstall, not on update
if [ $1 -eq 0 ]; then
  # disable phpPgAdmin flag
  if [ -x %{_sbindir}/a2enflag ]; then
    flag_find=$(grep -cw /etc/sysconfig/apache2 -e "^APACHE_SERVER_FLAGS=.*%{name}.*")
    if [ $flag_find -eq 1 ]; then
      echo "info: removing %{name} from APACHE_SERVER_FLAGS"
      a2enflag -d %{name}
    fi
  fi
fi
%restart_on_update apache2

%files -f FILELIST
%defattr(0644,root,root,0755)
%doc CREDITS DEVELOPERS FAQ HISTORY TODO TRANSLATORS
%license LICENSE
%dir %{ap_docroot}/%{name}
%config(noreplace) %{ap_sysconfdir}/conf.d/%{name}.conf
%config(noreplace) %{ap_sysconfdir}/conf.d/%{name}.inc
%dir %attr(0750,wwwrun,root) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,root,www) %{ppa_config}

%changelog
