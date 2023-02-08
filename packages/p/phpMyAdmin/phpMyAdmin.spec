#
# spec file for package phpMyAdmin
#
# Copyright (c) 2023 SUSE LLC
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


%define ap_docroot_old  /srv/www/htdocs
%define ap_docroot      %{_datadir}
%define ap_tmpdir       %{_localstatedir}/cache/%{name}
%define pma_config      %{_sysconfdir}/%{name}/config.inc.php
%if !0%{?suse_version}
%define apache_user     nobody
%define apache_group    nogroup
%endif
Name:           phpMyAdmin
Version:        5.2.1
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
BuildRequires:  apache-rpm-macros
BuildRequires:  fdupes
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
Recommends:     php-curl
Recommends:     php-zip
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

%package apache
Summary:        Apache configuration for %{name}
Group:          Productivity/Networking/Web/Utilities
BuildRequires:  apache-rpm-macros-control
BuildRequires:  apache2
Requires:       %{name}
Requires:       apache2
Requires(post): %{_sbindir}/a2enmod
Requires(post): %{_sbindir}/a2enflag
Requires(post): php
Requires(postun):%{_sbindir}/a2enflag
Recommends:     mod_php_any >= 7.4
Supplements:    packageand(apache2:%name)

%description apache
This subpackage contains the Apache configuration files

%lang_package

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

# permissions
find . -type d -exec chmod 755 {} \;
find . ! -name '*.sh' ! -name '*-query' -type f -exec chmod 644 {} \;

%build

%install
#%%{__install} -d -m0750 $RPM_BUILD_ROOT%%{_sysconfdir}/%%{name}
install -d -m0755 %{buildroot}%{ap_docroot}/%{name}
cp -dR *.php *.ico *.txt js libraries locale themes templates vendor \
  %{buildroot}%{ap_docroot}/%{name}
# install config to config dir
install -D -m0640 %{buildroot}%{ap_docroot}/%{name}/config.sample.inc.php \
 %{buildroot}%{_sysconfdir}/%{name}/config.inc.php
# install TempDir (now in cache)
install -d -m0770 %{buildroot}%{ap_tmpdir}

# fix libraries/vendor_config.php
sed -i -e "s,@docdir@,%{_docdir}/%{name},g" -e "s,@sysconfdir@,%{_sysconfdir}/%{name},g" -e "s,@tmpdir@,%{ap_tmpdir},g" \
  %{buildroot}%{ap_docroot}/%{name}/libraries/vendor_config.php
# fix libraries/common.inc.php
#%%{__sed} -i -e "s,@PMA_Config@,%%{_sysconfdir}/%%{name}/config.inc.php,g" \
#  $RPM_BUILD_ROOT%%{ap_docroot}/%%{name}/libraries/common.inc.php

# generate file list
find %{buildroot}%{ap_docroot}/%{name} -mindepth 1 -maxdepth 1 -type d | sed -e "s@$RPM_BUILD_ROOT@@" > FILELIST
find %{buildroot}%{ap_docroot}/%{name} -maxdepth 1 -type f | grep -v 'config.inc.php' | sed -e "s@$RPM_BUILD_ROOT@@" >> FILELIST
install -D -m0644 %{SOURCE3} %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf
install -D -m0644 %{SOURCE4} %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.inc
# fix paths in http config
sed -i -e "s,@ap_docroot@,%{ap_docroot},g" -e "s,@name@,%{name},g" \
 -e "s,@docdir@,%{_docdir},g" -e "s,@ap_sysconfdir@,%{apache_sysconfdir},g" -e "s,@ap_tmpdir@,%{ap_tmpdir},g" %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf

# rpmlint stuff
%fdupes %{buildroot}%{ap_docroot}/%{name}

# find language files
%find_lang %{name} --all-name

%post
# generate blowfish secret only on install, not on upgrade
if [ $1 -eq 1 ]; then
  sed -i -e "s|^\(\$cfg\['blowfish_secret'\] = '\)\(';\).*|\1$(head -c 32 /dev/urandom | base64)\2|" %{pma_config}
fi

%preun
# only on uninstall, not on upgrade
if [ $1 -eq 0 ]; then
  echo "info: empty %{ap_tmpdir}/* for clean uninstall"
  rm -rf %{ap_tmpdir}/* || :
fi

%postun
# only on upgrade, not on install
if [ $1 -ge 1 ]; then
  echo "info: empty %{ap_tmpdir}/* for clean upgrade"
  rm -rf %{ap_tmpdir}/* || :
fi

%post apache
# only do on install, not on upgrade
if [ $1 -eq 1 ]; then
  # enable required apache modules
  a2enmod version >/dev/null || :

  # enable mod_php if preform MPM is used
  if start_apache2 -V | grep -q prefork; then
    mod_php=$(php -r "echo 'php' . PHP_MAJOR_VERSION;")
    echo "info: adding ${mod_php} to APACHE_MODULES"
    a2enmod ${mod_php} >/dev/null || :
  fi

  # enable phpMyAdmin flag
  echo "info: adding %{name} to APACHE_SERVER_FLAGS"
  a2enflag %{name} >/dev/null || :
fi
# on upgrade, check if new cache directory is in config
if [ $1 -gt 1 ] && ! grep -q %{ap_tmpdir} %{apache_sysconfdir}/conf.d/%{name}.conf; then
  # not found, create backup first
  cp --backup=t --preserve %{apache_sysconfdir}/conf.d/%{name}.conf{,.bak}

  # add cache directory /var/cache/phpMyAdmin
  echo "info: new cache directory added to %{apache_sysconfdir}/conf.d/%{name}.conf"
  sed -i "s|\(php_admin_value open_basedir[^:]*\)|\1:%{ap_tmpdir}|" %{apache_sysconfdir}/conf.d/%{name}.conf
  cat >> %{apache_sysconfdir}/conf.d/%{name}.conf << EOF

<Directory %{ap_tmpdir}>

    <IfVersion < 2.4>
        Order allow,deny
        Deny from all
    </IfVersion>

    <IfVersion >= 2.4>
        <IfModule !mod_access_compat.c>
            Require all denied
        </IfModule>
        <IfModule mod_access_compat.c>
            Order deny,allow
            Deny from all
        </IfModule>
    </IfVersion>

</Directory>
EOF

  # boo#1092345: change ap_docroot from /srv/www/htdocs to /usr/share
  if grep -q %{ap_docroot_old} %{apache_sysconfdir}/conf.d/%{name}.conf; then
    echo "info: changed %{ap_docroot_old} to %{ap_docroot} in %{apache_sysconfdir}/conf.d/%{name}.conf"
    sed -i "s|%{ap_docroot_old}|%{ap_docroot}|g" %{apache_sysconfdir}/conf.d/%{name}.conf
  fi
fi

%postun apache
# only do on uninstall, not on upgrade
if [ $1 -eq 0 ]; then
  # disable phpMyAdmin flag
  echo "info: removing %{name} from APACHE_SERVER_FLAGS"
  a2enflag -d %{name} >/dev/null || :
fi
%apache_request_restart

%posttrans apache
# restart apache instances after zypper or rpm transaction, if not have restarted already
%apache_restart_if_needed

%files -f FILELIST
%defattr(644,root,root,755)
%doc ChangeLog
%license LICENSE
%doc README RELEASE-DATE*
%doc examples doc sql
%dir %attr(0750,root,%{apache_group}) %{_sysconfdir}/%{name}
%dir %attr(0770,root,%{apache_group}) %{ap_tmpdir}
%config(noreplace) %{_sysconfdir}/%{name}/config.inc.php
%dir %{ap_docroot}/%{name}
%exclude %{ap_docroot}/%{name}/locale/*/LC_MESSAGES/phpmyadmin.mo
%exclude %{ap_docroot}/%{name}/vendor/phpmyadmin/sql-parser/locale/*/LC_MESSAGES/sqlparser.mo

%files apache
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.conf
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.inc

%files lang -f %{name}.lang

%changelog
