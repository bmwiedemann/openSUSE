#
# spec file for package phpMyAdmin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define apxs %{_sbindir}/apxs2
%define ap_sysconfdir %(%{apxs} -q SYSCONFDIR)
%define ap_serverroot %(%{apxs} -q PREFIX)
%define ap_docroot %(%{apxs} -q PREFIX)/htdocs
%define pma_config %{_sysconfdir}/%{name}/config.inc.php
%if 0%{?suse_version}
%define ap_usr wwwrun
%define ap_grp www
%else
%define ap_usr nobody
%define ap_grp nogroup
%endif
Name:           phpMyAdmin
Version:        4.9.0.1
Release:        0
Summary:        Administration of MySQL over the web
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Frontends
URL:            https://www.phpMyAdmin.net/
Source0:        https://files.phpmyadmin.net/phpMyAdmin/%{version}/%{name}-%{version}-all-languages.tar.xz
Source1:        https://files.phpmyadmin.net/phpMyAdmin/%{version}/%{name}-%{version}-all-languages.tar.xz.asc
# http://docs.phpmyadmin.net/en/latest/setup.html#verifying-phpmyadmin-releases
Source2:        https://files.phpmyadmin.net/phpmyadmin.keyring#/%{name}.keyring
Source3:        %{name}.http
Source4:        %{name}.http.inc
Source100:      %{name}-rpmlintrc
# Fix-SuSE: provide useful default config
Patch0:         %{name}-config.patch
# Fix-SUSE: auto config for pma storage
Patch1:         %{name}-pma.patch
BuildRequires:  apache2-devel
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  xz
#
Requires:       php-bz2
Requires:       php-ctype
Requires:       php-gd
Requires:       php-gettext
Requires:       php-iconv
Requires:       php-json
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-openssl
Requires:       php-session
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         coreutils
PreReq:         grep
PreReq:         pwgen
PreReq:         sed
Recommends:     mod_php_any >= 5.5
Recommends:     php-curl
Recommends:     php-zip
### will be removed with php >= 7.2
## boo#1050980
Suggests:       php-mcrypt
BuildArch:      noarch

%description
phpMyAdmin can manage a whole MySQL server (needs a super-user) as well as a
single database. To accomplish the latter you'll need a properly set up MySQL
user who can read/write only the desired database. It's up to you to look up
the appropriate part in the MySQL manual.

Currently phpMyAdmin can:

  * browse and drop databases, tables, views, fields and indexes
  * create, copy, drop, rename and alter databases, tables, fields and indexes
  * maintenance server, databases and tables, with proposals on server
    configuration
  * execute, edit and bookmark any SQL-statement, even batch-queries
  * load text files into tables
  * create^1 and read dumps of tables
  * export^1 data to various formats: CSV, XML, PDF, ISO/IEC 26300 -
    OpenDocument Text and Spreadsheet, Word, Excel and L^AT[E]X formats
  * import data and MySQL structures from Microsoft Excel and OpenDocument
    spreadsheets, as well as XML, CSV, and SQL files
  * administer multiple servers
  * manage MySQL users and privileges
  * check referential integrity in MyISAM tables
  * using Query-by-example (QBE), create complex queries automatically
    connecting required tables
  * create PDF graphics of your Database layout
  * search globally in a database or a subset of it
  * transform stored data into any format using a set of predefined functions,
    like displaying BLOB-data as image or download-link
  * track changes on databases, tables and views
  * support InnoDB tables and foreign keys (see FAQ 3.6)
  * support mysqli, the improved MySQL extension (see FAQ 1.17)
  * communicate in 57 different languages
  * synchronize two databases residing on the same as well as remote servers
    (see FAQ 9.1)

%prep
%setup -q -n %{name}-%{version}-all-languages
## rpmlint:
# wrong-file-end-of-line-encoding
perl -p -i -e 's|\r\n|\n|' examples/config.manyhosts.inc.php
%patch0
%patch1

# clean up
find . -name .github -type d -prune -exec rm -r {} \;
for file in *.orig .buildinfo .gitkeep .travis.yml .weblate .jshintrc .eslintrc.json \
.php_cs.dist .scrutinizer.yml .editorconfig php_twig.h twig.c; do
  find . -type f -name $file -delete
done

# set proper shebang
sed -i 's/env php/php/' vendor/phpmyadmin/sql-parser/bin/*-query

# permissions
find . -type d -exec chmod 755 {} \;
find . ! -name '*.sh' ! -name '*-query' -type f -exec chmod 644 {} \;

%build

%install
#%%{__install} -d -m0750 $RPM_BUILD_ROOT%%{_sysconfdir}/%%{name}
install -d -m0755 %{buildroot}%{ap_docroot}/%{name}
cp -dR *.css *.php *.ico js libraries locale themes templates vendor \
  %{buildroot}%{ap_docroot}/%{name}
# install config to config dir
install -D -m0640 %{buildroot}%{ap_docroot}/%{name}/config.sample.inc.php \
 %{buildroot}%{_sysconfdir}/%{name}/config.inc.php
# install TempDir
install -d -m0770 %{buildroot}%{ap_docroot}/%{name}/tmp

# fix libraries/vendor_config.php
sed -i -e "s,@docdir@,%{_docdir}/%{name},g" -e "s,@sysconfdir@,%{_sysconfdir}/%{name},g" \
  %{buildroot}%{ap_docroot}/%{name}/libraries/vendor_config.php
# fix libraries/common.inc.php
#%%{__sed} -i -e "s,@PMA_Config@,%%{_sysconfdir}/%%{name}/config.inc.php,g" \
#  $RPM_BUILD_ROOT%%{ap_docroot}/%%{name}/libraries/common.inc.php

# generate file list
find %{buildroot}%{ap_docroot}/%{name} -mindepth 1 -maxdepth 1 -type d | sed -e "s@$RPM_BUILD_ROOT@@" > FILELIST
find %{buildroot}%{ap_docroot}/%{name} -maxdepth 1 -type f | grep -v 'config.inc.php' | sed -e "s@$RPM_BUILD_ROOT@@" >> FILELIST
install -D -m0644 %{SOURCE3} %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.conf
install -D -m0644 %{SOURCE4} %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.inc
# fix paths in http config
sed -i -e "s,@ap_docroot@,%{ap_docroot},g" -e "s,@name@,%{name},g" \
 -e "s,@docdir@,%{_docdir},g" -e "s,@ap_sysconfdir@,%{ap_sysconfdir},g" %{buildroot}%{ap_sysconfdir}/conf.d/%{name}.conf

# rpmlint stuff
%fdupes %{buildroot}%{ap_docroot}/%{name}/libraries
%fdupes %{buildroot}%{ap_docroot}/%{name}/themes

%post
# on `rpm -ivh` PARAM is 1
# on `rpm -Uvh` PARAM is 2
# set PmaAbsoluteUri ### generate blowfish secret
sed -i -e "s,@FQDN@,$(cat %{_sysconfdir}/HOSTNAME)," \
 -e "s/\\\$cfg\['blowfish_secret'\] = ''/\$cfg['blowfish_secret'] = '`pwgen -s -1 46`'/" %{pma_config}
# enable required apache modules
if [ -x %{_sbindir}/a2enmod ]; then
  a2enmod -q version || a2enmod version
  # get installed php_version (5 or 7)
  php_version=$(php -v | sed -n 's/^PHP\ \([[:digit:]]\+\)\..*$/\1/p')
  if [[ -n ${php_version} ]] && start_apache2 -V | grep -q prefork; then
    a2enmod -q "php${php_version}" || a2enmod "php${php_version}"
  fi
fi
#systemctl try-restart apache2 &>/dev/null

#%%postun
#systemctl try-restart apache2 &>/dev/null

%files -f FILELIST
%defattr(644,root,root,755)
%doc ChangeLog
%license LICENSE
%doc README RELEASE-DATE*
%doc examples doc sql
%dir %attr(0750,root,%{ap_grp}) %{_sysconfdir}/%{name}
%dir %attr(0770,root,%{ap_grp}) %{ap_docroot}/%{name}/tmp
%config(noreplace) %{_sysconfdir}/%{name}/config.inc.php
%dir %{ap_docroot}/%{name}
%config(noreplace) %{ap_sysconfdir}/conf.d/%{name}.conf
%config(noreplace) %{ap_sysconfdir}/conf.d/%{name}.inc
%attr (755,root,root) %{ap_docroot}/%{name}/vendor/phpmyadmin/sql-parser/bin/*-query

%changelog
