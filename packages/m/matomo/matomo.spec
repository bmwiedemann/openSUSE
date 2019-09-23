#
# spec file for package matomo
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

%define apxs %{_sbindir}/apxs2
%define ap_sysconfdir %(%{apxs} -q SYSCONFDIR)
%define ap_serverroot %(%{apxs} -q PREFIX)

%if 0%{?suse_version}
%define ap_usr wwwrun
%define ap_grp www
%else
%define ap_usr nobody
%define ap_grp nogroup
%endif

Name:           matomo
Version:        3.11.0
Release:        0
Summary:        Web analytics platform
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
Url:            http://matomo.org/
Source0:        http://builds.matomo.org/%{name}-%{version}.tar.gz
Source2:        %{name}.conf
Source3:        %{name}.logrotate
Source4:        %{name}-README.SUSE
Source10:       %{name}-archive.cron
Source11:       %{name}-archive.service
Source12:       %{name}-archive.timer
Source13:       %{name}.my.cnf
Source99:       %{name}.rpmlintrc
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires(pre):  user(%ap_usr)
Requires(pre):  group(%ap_grp)
%else
Requires(pre):  aaa_base
%endif
BuildRequires:  apache2-devel
BuildRequires:  cron
BuildRequires:  fdupes
BuildRequires:  logrotate
BuildRequires:  mariadb
#BuildRequires:  php-json
#BuildRequires:  php-mbstring
#BuildRequires:  php-pdo
BuildRequires:  systemd
BuildRequires:  unzip
Requires:       apache2
Requires:       cron
Requires:       logrotate
Requires:       mariadb
Requires:       mod_php_any >= 5.5.9
Requires:       php-curl
Requires:       php-gd
Requires:       php-json
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-pdo
%{?systemd_requires}
Recommends:     php-geoip
Recommends:     apache2-mod_geoip

Conflicts:      piwik

%description
Matomo, formerly Piwik, is a web analytics platform that gives
insights into a website's visitors and marketing campaigns, so the
strategy and online experience of visitors may be optimized.

%prep
%setup -q -n matomo
install -m644 %{SOURCE4} README.SUSE
# remove unwanted files
find . -type f "(" -name .htaccess -o -name .travis.sh ")" -delete
#find . -name ".git*" -exec rm -Rf "{}" "+"
find . -type f "(" -name "*.c" -o -name "*.h" -o -name "*.js.orig" ")" -delete
# env-script-interpreter
find . -type f -exec sed -i -e 's|\/usr\/bin\/env php|\/usr\/bin\/php|g' {} +
#
# Fix integrity check triggered from fix of rpmlint errors.
# Drop moved files
for i in CHANGELOG.md CONTRIBUTING.md PRIVACY.md README.md SECURITY.md LEGALNOTICE LICENSE 'misc\/cron\/.htaccess' 'misc\/How to install Matomo.html' 'vendor\/tecnickcom\/tcpdf\/tools\/.htaccess' 'vendor\/twig\/twig\/ext\/twig\/php_twig.h' 'vendor\/twig\/twig\/ext\/twig\/twig.c' 'js\/piwik.js.orig'
do
  sed -i "/\W\"${i}\"\W/d" config/manifest.inc.php
done
# Insert new hashes for chanded files
for file in console 'vendor/leafo/lessphp/plessc' 'vendor/tecnickcom/tcpdf/tools/tcpdf_addfont.php'
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
install -d -m0755 %{buildroot}/%{ap_serverroot}/%{name}
install -d -m0755 %{buildroot}/%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}/%{_defaultdocdir}/%{name}
# copy src from build to buildroot
mv *SUSE %{buildroot}/%{_defaultdocdir}/%{name}
mv LEGALNOTICE %{buildroot}/%{_defaultdocdir}/%{name}
mv LICENSE %{buildroot}/%{_defaultdocdir}/%{name}
mv "misc/How to install Matomo.html" %{buildroot}/%{_defaultdocdir}/%{name}
mv *md %{buildroot}/%{_defaultdocdir}/%{name}
cp -dR * %{buildroot}/%{ap_serverroot}/%{name}
# install matomo.conf to apache conf.d
install -D -m0640 %{SOURCE2} %{buildroot}/%{ap_sysconfdir}/conf.d/%{name}.conf
# install logrotate
install -D -m0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
# move config to etc/matomo and make symlink
mv %{buildroot}/%{ap_serverroot}/%{name}/config/* \
   %{buildroot}/%{_sysconfdir}/%{name}
rm -d %{buildroot}/%{ap_serverroot}/%{name}/config
ln -s %{_sysconfdir}/%{name} %{buildroot}/%{ap_serverroot}/%{name}/config
# install cronscript and systemd-timer
install -d -m 0755 %{buildroot}/%{_sysconfdir}/cron.d
install -d -m 0755 %{buildroot}/var/log/%{name}
install -D -m 0644 %{SOURCE10} %{buildroot}/%{_sysconfdir}/cron.d/%{name}-archive
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}-archive.service
install -D -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/%{name}-archive.timer
sed -i -e 's|@ap_serverroot@|%{ap_serverroot}|g' %{buildroot}%{_sysconfdir}/cron.d/%{name}-archive
sed -i -e 's|@ap_serverroot@|%{ap_serverroot}|g' %{buildroot}%{_unitdir}/%{name}-archive.service
# install changes for mariadb
install -D -m0644 %{SOURCE13} %{buildroot}/%{_sysconfdir}/my.cnf.d/%{name}.my.cnf

%fdupes %{buildroot}/%{_prefix}
%fdupes %{buildroot}/srv

%pre
%service_add_pre matomo-archive.timer matomo-archive.service

%post
chown -R %{ap_usr}:%{ap_grp} %{ap_serverroot}/%{name}
%service_add_post matomo-archive.timer matomo-archive.service apache2.service
# Update matomo if this is an upgrade $1 == 2
echo "matomo: Update matomo:core..."
if [ $1 -gt 1 ]; then
  su wwwrun -s /bin/sh -c "%{_bindir}/php %{ap_serverroot}/%{name}/console config:set 'Tracker.record_statistics="0"'" || :
  su wwwrun -s /bin/sh -c "%{_bindir}/php %{ap_serverroot}/%{name}/console config:set 'General.maintenance_mode="1"'" || :
  su wwwrun -s /bin/sh -c "%{_bindir}/php %{ap_serverroot}/%{name}/console core:update --yes" || :
  su wwwrun -s /bin/sh -c "%{_bindir}/php %{ap_serverroot}/%{name}/console config:set 'General.maintenance_mode="0"'" || :
  su wwwrun -s /bin/sh -c "%{_bindir}/php %{ap_serverroot}/%{name}/console config:set 'Tracker.record_statistics="1"'" || :
  :
fi

%preun
%service_del_preun matomo-archive.timer matomo-archive.service

%postun
%service_del_postun matomo-archive.timer matomo-archive.service apache2.service

%files
%defattr(-,root,root,-)
#%%doc README.SUSE CHANGELOG.md CONTRIBUTING.md LEGALNOTICE README.md SECURITY.md
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/*
%config(noreplace) %{ap_sysconfdir}/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}-archive
%config(noreplace) %{_sysconfdir}/my.cnf.d/%{name}.my.cnf
%{_unitdir}/%{name}-archive.service
%{_unitdir}/%{name}-archive.timer
%dir %attr(0750,%{ap_usr},%{ap_grp}) %{_sysconfdir}/%{name}
%dir %attr(0750,%{ap_usr},%{ap_grp}) %{_sysconfdir}/%{name}/environment
%defattr(640,%{ap_usr},%{ap_grp},750)
%dir %{ap_serverroot}/%{name}
%dir /var/log/%{name}
%config(noreplace)  %attr(600,%{ap_usr},%{ap_grp}) %{_sysconfdir}/%{name}/*php
%{_sysconfdir}/%{name}/environment/*php
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/console
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/misc/cron/archive.sh
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/misc/log-analytics/import_logs.py
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/misc/composer/clean-xhprof.sh
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/misc/composer/build-xhprof.sh
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/vendor/leafo/lessphp/package.sh
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/vendor/leafo/lessphp/lessify
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/vendor/leafo/lessphp/plessc
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/vendor/pear/archive_tar/sync-php4
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/vendor/szymach/c-pchart/coverage.sh
%attr(0770,%{ap_usr},%{ap_grp}) %{ap_serverroot}/%{name}/vendor/tecnickcom/tcpdf/tools/tcpdf_addfont.php
%{ap_serverroot}/%{name}/*

%changelog
