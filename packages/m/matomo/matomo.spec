#
# spec file for package matomo
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

%{!?_tmpfilesdir:%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d}

Name:           matomo
Version:        4.13.0
Release:        0
Summary:        Web analytics platform
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            http://matomo.org/
Source0:        http://builds.matomo.org/%{name}-%{version}.tar.gz
Source2:        %{name}.conf
Source3:        %{name}.logrotate
Source4:        %{name}-README.SUSE
Source10:       %{name}-archive.cron
Source11:       %{name}-archive.service
Source12:       %{name}-archive.timer
Source13:       %{name}.my.cnf
Source14:       %{name}-tmpfile.conf
Source99:       %{name}.rpmlintrc
# PATCH-FIX-OPENSUSE: Don't show wrong message with wrong owner of %%{apache_serverroot}/%%{name} when disable enable_auto_update through package installation.
Patch1:         %{name}-package_update.patch
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires(pre):  user(wwwrun)
Requires(pre):  group(www)
%else
Requires(pre):  aaa_base
%endif
BuildRequires:  apache-rpm-macros
BuildRequires:  cron
BuildRequires:  fdupes
BuildRequires:  logrotate
BuildRequires:  mariadb
BuildRequires:  unzip
BuildRequires:  pkgconfig(systemd)
Requires:       nodejs
Requires:       python3
Requires:       logrotate
Requires:       php-ctype
Requires:       php-curl
Requires:       php-dom
Requires:       php-gd
Requires:       php-iconv
# for the upgrade process:
Requires(pre):  php-json
Requires:       php-json
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-pdo
#Requires:       php-sqlite
Requires:       php-tokenizer
Requires:       php-xmlreader
Requires:       php-xmlwriter
Requires:       php-zlib
Requires(pre):  php
%{?systemd_requires}
Recommends:     php-geoip
Recommends:     php-openssl
Recommends:     mariadb
Recommends:     cron
Conflicts:      piwik

%description
Matomo, formerly Piwik, is a web analytics platform that gives
insights into a website's visitors and marketing campaigns, so the
strategy and online experience of visitors may be optimized.

%package apache
Summary:        Apache configuration for %{name}
Group:          Productivity/Networking/Web/Utilities
BuildRequires:  apache2
Requires:       apache2
Requires:       mod_php_any >= 7.2.5
Recommends:     apache2-mod_geoip
Supplements:    packageand(apache2:%name)

%description apache
This subpackage contains the Apache configuration files

%prep
%setup -q -n %{name}
%patch1 -p1
install -m644 %{SOURCE4} README.SUSE
# remove unwanted files
find . -type f "(" -name .htaccess -o -name .travis.sh -o -name .gitkeep ")" -delete
#find . -name ".git*" -exec rm -Rf "{}" "+"
find . -type f "(" -name "*.c" -o -name "*.h" -o -name "*.js.orig" ")" -delete
# env-script-interpreter
find . -type f -exec sed -i -e 's|\/usr\/bin\/env php|\/usr\/bin\/php|g' {} +
find . -type f -name "*.sh" -exec sed -i -e 's|\/usr\/bin\/env bash|\/bin\/bash|g' {} +
sed -i 's|python$|python3|' misc/log-analytics/import_logs.py

#
# disable the auto updater, it can't work properly with the new, more secure permissions and is a bad idea on a RPM based setup anyways.
#
sed -i '/enable_auto_update/s/1$/0/' config/global.ini.php

#
# Fix integrity check triggered from fix of rpmlint errors.
# Drop moved files
for i in CHANGELOG.md CONTRIBUTING.md PRIVACY.md README.md SECURITY.md LEGALNOTICE LICENSE 'misc\/cron\/.htaccess' 'misc\/How to install Matomo.html' 'vendor\/tecnickcom\/tcpdf\/tools\/.htaccess' 'vendor\/twig\/twig\/ext\/twig\/php_twig.h' 'vendor\/twig\/twig\/ext\/twig\/twig.c' 'js\/piwik.js.orig' '.eslintignore' '.eslintrc.js' '.browserslistrc' 'vendor\/lox\/xhprof\/extension\/php_xhprof.h' 'vendor\/lox\/xhprof\/extension\/xhprof.c'
do
  sed -i "/\W\"${i}\"\W/d" config/manifest.inc.php
done
# Insert new hashes for chanded files
for file in console 'vendor/tecnickcom/tcpdf/tools/tcpdf_addfont.php' 'config/global.ini.php' 'core/CliMulti/Output.php' 'plugins/CoreUpdater/Commands/Update.php' 'vendor/matomo/matomo-php-tracker/run_tests.sh' 'vendor/wikimedia/less.php/bin/lessc' 'misc/log-analytics/import_logs.py' 'core/CliMulti.php'
do
  size=$(ls -l $file | awk '{ print $5 }')
  checksum=$(md5sum $file  | awk '{ print $1 }')
  file2=$(echo "$file" | sed 's/\//\\\//g')
  sed -i "/\W\"$file2\"\W/c \"$file\" => array(\"$size\", \"$checksum\")," config/manifest.inc.php
done

%build
# nothing to build

%install
# make directories
install -d -m0755 %{buildroot}/%{apache_serverroot}/%{name}
install -d -m0755 %{buildroot}/%{apache_serverroot}/%{name}/tmp
install -d -m0755 %{buildroot}/%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}/%{_defaultdocdir}/%{name}
# copy src from build to buildroot
mv *SUSE %{buildroot}/%{_defaultdocdir}/%{name}
mv LEGALNOTICE %{buildroot}/%{_defaultdocdir}/%{name}
mv LICENSE %{buildroot}/%{_defaultdocdir}/%{name}
mv "misc/How to install Matomo.html" %{buildroot}/%{_defaultdocdir}/%{name}
mv *md %{buildroot}/%{_defaultdocdir}/%{name}
cp -dR * %{buildroot}/%{apache_serverroot}/%{name}
# install matomo.conf to apache conf.d
mkdir -p %{buildroot}/%{apache_sysconfdir}/conf.d
sed -e 's|__matomo_web__|%{apache_serverroot}/%{name}|g' \
	-e 's|__matomo_conf__|%{_sysconfdir}/%{name}|g' \
	-e 's|__matomo_log__|/var/log/%{name}|g' \
	%{SOURCE2} > %{buildroot}/%{apache_sysconfdir}/conf.d/%{name}.conf
# install logrotate
install -D -m0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
sed -i -e 's|@APACHE_USER@|%{apache_user}|g' %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
sed -i -e 's|@APACHE_GROUP@|%{apache_group}|g' %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
# move config to etc/matomo and make symlink
mv %{buildroot}/%{apache_serverroot}/%{name}/config/* \
   %{buildroot}/%{_sysconfdir}/%{name}
rm -d %{buildroot}/%{apache_serverroot}/%{name}/config
ln -s %{_sysconfdir}/%{name} %{buildroot}/%{apache_serverroot}/%{name}/config
# install cronscript and systemd-timer
install -d -m 0755 %{buildroot}/%{_sysconfdir}/cron.d
install -d -m 0755 %{buildroot}/var/log/%{name}
install -D -m 0644 %{SOURCE10} %{buildroot}/%{_sysconfdir}/cron.d/%{name}-archive
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}-archive.service
install -D -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/%{name}-archive.timer
install -D -m 0644 %{SOURCE14} %{buildroot}%{_tmpfilesdir}/%{name}.conf
sed -i -e 's|@APACHE_USER@|%{apache_user}|g' %{buildroot}%{_sysconfdir}/cron.d/%{name}-archive
sed -i -e 's|@APACHE_SERVERROOT@|%{apache_serverroot}|g' %{buildroot}%{_sysconfdir}/cron.d/%{name}-archive
sed -i -e 's|@APACHE_USER@|%{apache_user}|g' %{buildroot}%{_unitdir}/%{name}-archive.service
sed -i -e 's|@APACHE_GROUP@|%{apache_group}|g' %{buildroot}%{_unitdir}/%{name}-archive.service
sed -i -e 's|@APACHE_SERVERROOT@|%{apache_serverroot}|g' %{buildroot}%{_unitdir}/%{name}-archive.service
# install changes for mariadb
install -D -m0644 %{SOURCE13} %{buildroot}/%{_sysconfdir}/my.cnf.d/%{name}.my.cnf

%fdupes %{buildroot}/%{_prefix}
%fdupes %{buildroot}/srv

%pre
%service_add_pre matomo-archive.timer matomo-archive.service

%post
# BSC#1154324
# # # chown -R %{apache_user}:%{apache_group} %{apache_serverroot}/%{name}
%service_add_post matomo-archive.timer matomo-archive.service apache2.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
if [ $1 -gt 1 ]; then
  # Update matomo if this is an upgrade $1 == 2
  echo "matomo: Update matomo:core..."
  su %{apache_user} -s /bin/sh -c "%{_bindir}/php %{apache_serverroot}/%{name}/console config:set 'Tracker.record_statistics="0"'" || :
  su %{apache_user} -s /bin/sh -c "%{_bindir}/php %{apache_serverroot}/%{name}/console config:set 'General.maintenance_mode="1"'" || :
  su %{apache_user} -s /bin/sh -c "%{_bindir}/php %{apache_serverroot}/%{name}/console core:update --yes" || :
  su %{apache_user} -s /bin/sh -c "%{_bindir}/php %{apache_serverroot}/%{name}/console config:set 'General.maintenance_mode="0"'" || :
  su %{apache_user} -s /bin/sh -c "%{_bindir}/php %{apache_serverroot}/%{name}/console config:set 'Tracker.record_statistics="1"'" || :
  :
fi

%preun
%service_del_preun matomo-archive.timer matomo-archive.service

%postun
%service_del_postun matomo-archive.timer matomo-archive.service apache2.service

%files
%defattr(-,root,root,-)
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}-archive
%config(noreplace) %{_sysconfdir}/my.cnf.d/%{name}.my.cnf
%{_unitdir}/%{name}-archive.service
%{_unitdir}/%{name}-archive.timer
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0750,%{apache_user},%{apache_group}) %{_sysconfdir}/%{name}
%dir %attr(0750,%{apache_user},%{apache_group}) %{_sysconfdir}/%{name}/environment
%attr(0640,%{apache_user},%{apache_group}) %{_sysconfdir}/%{name}/*.php
%attr(0640,%{apache_user},%{apache_group}) %{_sysconfdir}/%{name}/environment/*.php
%ghost %attr(0750,%{apache_user},%{apache_group}) /run/%{name}_sessions
%defattr(644,root,root,755)
%dir %{apache_serverroot}/%{name}
%dir %attr(0750,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/js
%dir %attr(0750,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/misc
%dir %attr(0750,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/plugins
%dir %attr(0750,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/tmp
%dir %attr(0750,%{apache_user},%{apache_group}) /var/log/%{name}
%config(noreplace)  %attr(600,%{apache_user},%{apache_group}) %{_sysconfdir}/%{name}/*php
%{_sysconfdir}/%{name}/environment/*php
%attr(0644,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/matomo.js
%attr(0644,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/piwik.js
%attr(0644,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/js/piwik.min.js
%attr(0770,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/console
%attr(0770,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/misc/cron/archive.sh
%attr(0770,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/misc/log-analytics/import_logs.py
%attr(0770,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/vendor/pear/archive_tar/sync-php4
%attr(0770,%{apache_user},%{apache_group}) %{apache_serverroot}/%{name}/vendor/wikimedia/less.php/bin/lessc
%{apache_serverroot}/%{name}/*

%files apache
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.conf

%changelog
