#
# spec file for package cacti
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define datadir /srv/www
%define cacti_dir %{datadir}/cacti

Name:           cacti
Version:        1.2.31+git14.396480d3
%global base_version %(echo %{version} | sed 's/+[^+]*//')
%global next_base_version %(echo %{base_version} | awk -F. -v OFS=. '{$NF++; print}')
Release:        0
Summary:        Web Front-End to Monitor System Data via RRDtool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://www.cacti.net/
Source0:        %{name}-%{version}.tar
Source1:        %{name}.txt
Source3:        %{name}.logrotate
Source4:        %{name}-httpd.conf.default
Source10:       cacti-rpmlintrc
# PATCH-FIX-UPSTREAM cacti-config.patch
Patch0:         %{name}-config-dist.patch
Patch1:         cactid_service.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  fdupes
BuildRequires:  systemd-rpm-macros
Requires:       apache2
Requires:       logrotate
Requires:       mariadb
Requires:       mod_php_any >= 8.1
Requires:       net-snmp
Requires:       php-ctype
Requires:       php-gd
Requires:       php-gmp
Requires:       php-intl
Requires:       php-json
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-mysql >= 8.1
Requires:       php-openssl
Requires:       php-posix
Requires:       php-snmp >= 8.1
Requires:       php-sockets >= 8.1
Requires:       php-zlib
Requires:       rrdtool
Recommends:     php-gettext
Recommends:     php-pcntl
Recommends:     mariadb-tools
Conflicts:      cacti-spine < %{base_version}
Conflicts:      cacti-spine >= %{next_base_version}
Provides:       cacti-system = %{base_version}-%{release}
Obsoletes:      cacti-PA < %{base_version}-%{release}
Provides:       cacti-PA = %{base_version}-%{release}
BuildArch:      noarch
%{?systemd_requires}

%description
Cacti is a complete front-end to RRDtool: it stores all necessary
information for creating graphs and populates them with data from a
MySQL database. The front-end is completely PHP driven. Along with
being able to maintain graphs, data sources, and round robin archives
in a database, Cacti also handles data gathering. There exists an SNMP
support for those accustomed to creating traffic graphs with MRTG as
well.

%prep
%autosetup -p1

%build
cat %{SOURCE1} > quickstart.txt
# rename patched config file
mv include/config.php.dist include/config.php

#delete some files
find . -type f -name "*\.orig" -delete
find . -type f -name .gitignore -delete
find . -type f -name .gitattributes -delete
find . -type f -name .htaccess -delete
find locales -type f -name "*.sh" -delete

# fix env interpreter lines
sed -i 's|%{_bindir}/env perl|%{_bindir}/perl|g' $(find * -name "*.pl")
sed -i 's|%{_bindir}/env php|%{_bindir}/php|g' include/vendor/cldr-to-gettext-plural-rules/bin/export-plural-rules
sed -i 's|%{_bindir}/env bash|%{_bindir}/bash|g' $(find * -name "*.sh")
sed -i 's|/usr/local/spine/bin/spine|%{_bindir}/spine|' install/functions.php

#nothing to build

%install
install -d -m 0755 %{buildroot}%{cacti_dir}
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}

cp *.php        %{buildroot}%{cacti_dir}
cp -pr cache    %{buildroot}%{cacti_dir}
cp -pr cli      %{buildroot}%{cacti_dir}
cp -pr formats  %{buildroot}%{cacti_dir}
cp -pr images   %{buildroot}%{cacti_dir}
cp -pr include  %{buildroot}%{cacti_dir}
cp -pr install  %{buildroot}%{cacti_dir}
cp -pr lib      %{buildroot}%{cacti_dir}
cp -pr locales  %{buildroot}%{cacti_dir}
cp -pr mibs     %{buildroot}%{cacti_dir}
cp -pr plugins  %{buildroot}%{cacti_dir}
cp -pr resource %{buildroot}%{cacti_dir}
cp -pr rra      %{buildroot}%{cacti_dir}
cp -pr scripts  %{buildroot}%{cacti_dir}

install -d -m 0755 scripts %{buildroot}%{cacti_dir}/scripts
install -m 0755 scripts/* %{buildroot}%{cacti_dir}/scripts
install -d -m 0755 cli %{buildroot}%{cacti_dir}/cli
install -m 0755 cli/* %{buildroot}%{cacti_dir}/cli
install -m 0644 *.sql %{buildroot}%{cacti_dir}

sed -i \
    -e "s;__CACTIDIR__;%{cacti_dir};g" \
    -e "s;__APACHEUSER__;%{apache_user};g" \
    -e "s;__APACHEGROUP__;%{apache_group};g" \
    service/cactid.service
install -Dm644 service/cactid.service %{buildroot}%{_unitdir}/cactid.service

# apache2 config
install -d -m 0755 %{buildroot}%{apache_sysconfdir}/conf.d
sed -e "s;__CACTIDIR__;%{cacti_dir};g" %{SOURCE4} > %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf
install -d -m 0755 %{buildroot}%{apache_sysconfdir}/vhosts.d/conf.d
sed -e "s;__CACTIDIR__;%{cacti_dir};g" -e "s;<IfDefine CACTI>;<IfDefine CACTIVHOST>;g" \
    %{SOURCE4} > %{buildroot}%{apache_sysconfdir}/vhosts.d/conf.d/%{name}.conf

# logrotate config
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
sed -e "s;__APACHEUSER__;%{apache_user};g" -e "s;__APACHEGROUP__;%{apache_group};g" \
    %{SOURCE3} > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

ln -sfr %{buildroot}%{_localstatedir}/log/%{name} %{buildroot}%{cacti_dir}/log

# Set the correct permissions for pl and sh files
#find %%{buildroot}%%{cacti_dir} -type f -name "*.sh" -o -name "*.pl" -exec chmod ugo+x {} \;
# Make a list of directories, files, and permissions to set. any remaining are owned by root:root
(
find %{buildroot}%{cacti_dir} -type d|sed -e '
s|%{buildroot}%{cacti_dir}/cache/boost|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/cache/boost|
s|%{buildroot}%{cacti_dir}/cache/mibcache|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/cache/mibcache|
s|%{buildroot}%{cacti_dir}/cache/realtime|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/cache/realtime|
s|%{buildroot}%{cacti_dir}/cache/spikekill|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/cache/spikekill|
s|%{buildroot}%{cacti_dir}/include/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/include/vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer|
s|%{buildroot}%{cacti_dir}/resource/snmp_queries|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/resource/snmp_queries|
s|%{buildroot}%{cacti_dir}/resource/script_server|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/resource/script_server|
s|%{buildroot}%{cacti_dir}/resource/script_queries|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/resource/script_queries|
s|%{buildroot}%{cacti_dir}/rra|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/rra|
s|%{buildroot}%{cacti_dir}/scripts|%%dir %%attr(00755,%{apache_user},%{apache_group}) %{cacti_dir}/scripts|
s|%{buildroot}|%%dir %%attr(-,root,root) |
'
find %{buildroot}%{cacti_dir} -type f|sed -e '
s|%{buildroot}%{cacti_dir}/include/config.php||
s|%{buildroot}%{cacti_dir}/include/vendor/csrf/csrf-secret.php||
s|%{buildroot}%{cacti_dir}/scripts/\(.*\)\.pl|%%attr(0755,root,root) %{cacti_dir}/scripts/\1.pl|
s|%{buildroot}%{cacti_dir}/scripts/\(.*\)\.sh|%%attr(0755,root,root) %{cacti_dir}/scripts/\1.sh|
s|%{buildroot}|%%attr(-,root,root) |
'
)|sort -u|tee %{name}.list

%fdupes %{buildroot}

%post
%service_add_post cactid.service

%pre
%service_add_pre cactid.service
#attempt to remove old way & exit with 0 status if fails
systemctl --quiet stop %{name}-cron.timer || :
systemctl --quiet disable %{name}-cron.timer || :
systemctl --quiet stop %{name}-cron.service || :
systemctl --quiet disable %{name}-cron.service || :

%preun
%service_del_preun cactid.service

%postun
%service_del_postun  cactid.service

%files -f %{name}.list
%dir %{datadir}
%dir %{cacti_dir}
%license LICENSE
%doc README.md
%doc quickstart.txt
%attr(-,%{apache_user},%{apache_group}) %dir %{_localstatedir}/lib/%{name}
%attr(-,%{apache_user},%{apache_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{apache_user},%{apache_group}) %{cacti_dir}/include/vendor/csrf/csrf-secret.php
%attr(-,%{apache_user},%{apache_group}) %{cacti_dir}/log
%{cacti_dir}/log
%config(noreplace) %{cacti_dir}/include/config.php
%{_unitdir}/cactid.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{apache_sysconfdir}/conf.d
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.conf
%dir %{apache_sysconfdir}/vhosts.d/conf.d
%config(noreplace) %{apache_sysconfdir}/vhosts.d/conf.d/%{name}.conf

%changelog
