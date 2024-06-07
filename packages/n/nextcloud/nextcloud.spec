#
# spec file for package nextcloud
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


#
%if 0%{?suse_version}
%define apache_myserverroot %{apache_serverroot}/htdocs
%define apache_confdir %{apache_sysconfdir}/conf.d
%define apache_docdir /usr/share/doc/packages
%else
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
%define apache_serverroot /var/www/html
%define apache_confdir /etc/httpd/conf.d
%define apache_user apache
%define apache_group apache
%define __jar_repack 0
%else
%define apache_serverroot /var/www
%define apache_confdir /etc/httpd/conf.d
%define apache_user www
%define apache_group www
%endif
%endif

%define nc_user     %{apache_user}
%define nc_dir      %{apache_myserverroot}/%{name}
%define ocphp_bin   /usr/bin

%if 0%{?rhel} == 600 || 0%{?rhel_version} == 600 || 0%{?centos_version} == 600
%define statedir    /var/run
%else
%define statedir    /run
%endif

Name:           nextcloud
Version:        29.0.2
Release:        0
Summary:        File hosting service
License:        AGPL-3.0-only
Group:          Productivity/Networking/Web/Utilities
URL:            https://nextcloud.com
Source0:        https://download.nextcloud.com/server/releases/%{name}-%{version}.tar.bz2
Source1:        apache_secure_data
Source2:        README
Source3:        README.SELinux
Source4:        README.SUSE
Source5:        robots.txt
Source10:       %{name}-cron
Source11:       %{name}-cron.service
Source12:       %{name}-cron.timer
Source99:       %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  apache-rpm-macros
BuildRequires:  cron
BuildRequires:  fdupes
BuildRequires:  unzip
#
Requires:       cron
Requires:       curl
Requires:       libxml2-2
Requires:       mariadb >= 10.3
Requires:       php-bz2
Requires:       php-dom
Requires:       php-gd
Requires:       php-intl
Requires:       php-json
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-posix
Requires:       php-zip
#
%if 0%{?fedora_version} || 0%{?rhel} || 0%{?rhel_version} || 0%{?centos_version}
Requires:       php < 8.4.0
Requires:       php >= 8.1.0
Requires:       php-process
Requires:       php-xml
Recommends:     sqlite
%endif
#
%if 0%{?suse_version}
Requires:       php-ctype
Requires:       php-curl
# SUSE does not include the fileinfo module in php-common.
Requires:       php-fileinfo
Requires:       php-iconv
Requires:       php-opcache
Requires:       php-openssl
Requires:       php-pear
Requires:       php-xmlreader
Requires:       php-xmlwriter
Requires:       php-zip
Requires:       php-zlib
Recommends:     sqlite3
%{?systemd_requires}
%endif
Recommends:     php-sysvsem
# Database connectors:
Recommends:     php-sqlite
#Recommends:     php-pgsql
# Require for specific apps:
Requires:       php-ftp
Requires:       php-ldap
#Requires:       php-imap
#Requires:       php-smbclient
# Recommend for specific apps:
Recommends:     php-exif
Recommends:     php-gmp
# For enhanced server performance:
Recommends:     php-APCu
Recommends:     php-bcmath
# For preview generation:
Recommends:     php-imagick
Recommends:     php-ffmpeg
#Recommends:     libreoffice
# For command line processing:
Recommends:     php-pcntl

%description
Nextcloud is a suite of client-server software for creating file
hosting services and using them.

%package apache
Summary:        Apache configuration for %{name}
Group:          Productivity/Networking/Web/Utilities
BuildRequires:  apache2 >= 2.4
Requires:       %{name} = %{version}
Requires:       apache2
Requires:       mod_php_any < 8.4.0
Requires:       mod_php_any >= 8.1.0
Supplements:    packageand(apache2:%name)

%description apache
This subpackage contains the Apache configuration files

%prep
%setup -q -n %{name}
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .
### Don't remove git files!!
### git files should not be removed, otherwise nextcloud rise up integrity check failure in some situations.
###
## delete unneeded gitfiles
#rm -r `find . -name ".gitignore" -or -name ".gitkeep" -or -name ".github"`
## remove entries in signature.json to prevent integrity check failure
#find . -iname signature.json \
#    -exec sed -i "/\/.gitignore\": ./d" "{}" \;  \
#    -exec sed -i "/\/.gitkeep\": ./d" "{}" \; \
#    -exec sed -i "/\/.github\": ./d" "{}" \;
#rm -f 3rdparty/symfony/debug/Resources/ext/*.{c,h}

%build

%install
# no server side java code contained, alarm is false
idir=$RPM_BUILD_ROOT/%{apache_myserverroot}/%{name}
mkdir -p $idir
mkdir -p $idir/data
mkdir -p $idir/search
cp -aRf * $idir
cp -aRf .htaccess $idir
cp -aRf .user.ini $idir
# $idir/l10n to disappear in future
#rm -f $idir/l10n/l10n.pl

if [ ! -f $idir/robots.txt ]; then
  install -p -D -m 644 %{SOURCE5} $idir/robots.txt
fi

# create the AllowOverride directive
install -p -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{apache_confdir}/nextcloud.conf
ocpath="%{apache_myserverroot}/%{name}"
sed -i -e"s|@DATAPATH@|${ocpath}|g" $RPM_BUILD_ROOT/%{apache_confdir}/nextcloud.conf

# not needed for distro packages
rm -f ${idir}/indie.json

%if 0%{?suse_version}
# link duplicate doc files
%fdupes -s $RPM_BUILD_ROOT/%{apache_myserverroot}/%{name}
%endif

# CronJob
install -d -m 0755 %{buildroot}%{_sysconfdir}/cron.d
install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}-cron.service
install -D -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/%{name}-cron.timer
sed -i -e"s|@APACHE_USER@|%{apache_user}|g" %{buildroot}%{_sysconfdir}/cron.d/%{name}
sed -i -e"s|@APACHE_MYSERVERROOT@|%{apache_myserverroot}|g" %{buildroot}%{_sysconfdir}/cron.d/%{name}
sed -i -e"s|@APACHE_USER@|%{apache_user}|g" %{buildroot}%{_unitdir}/%{name}-cron.service
sed -i -e"s|@APACHE_MYSERVERROOT@|%{apache_myserverroot}|g" %{buildroot}%{_unitdir}/%{name}-cron.service
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-cron

%pre
%service_add_pre %{name}-cron.timer %{name}-cron.service

# avoid fatal php errors, while we are changing files
# https://github.com/nextcloud
#
# We don't do this for new installs. Only for updates.
# If the first argument to pre is 1, the RPM operation is an initial installation. If the argument is 2,
# the operation is an upgrade from an existing version to a new one.
if [ $1 -gt 1 -a ! -s %{statedir}/apache_stopped_during_nextcloud_install ]; then
  echo "o %{name} pre-install: Checking for running Apache"
  # FIXME: this above should make it idempotent -- a requirement with openSUSE.
  # it does not work.
%if 0%{?suse_version} && 0
  service apache2 status | grep running > %{statedir}/apache_stopped_during_nextcloud_install
  service apache2 stop
%endif
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
  service httpd status | grep running > %{statedir}/apache_stopped_during_nextcloud_install
  service httpd stop
%endif
fi
if [ -s %{statedir}/apache_stopped_during_nextcloud_install ]; then
  echo "o %{name} pre-install: Stopping Apache"
fi

if [ $1 -eq 1 ]; then
  echo "o %{name} pre-install: First install starting"
else
  echo "o %{name} pre-install: Upgrade starting ..."
fi
# https://github.com/nextcloud
if [ -x %{ocphp_bin}/php -a -f %{nc_dir}/occ ]; then
  echo "o %{name} pre-install: occ maintenance:mode --on"
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ maintenance:mode --on" || true
  echo yes > %{statedir}/occ_maintenance_mode_during_nextcloud_install
fi

%post
%service_add_post %{name}-cron.timer %{name}-cron.service

if [ $1 -eq 1 ]; then
%if 0%{?suse_version}
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} > 1500
a2enmod php8
%else
a2enmod php7
%endif
%endif
fi

if [ -s %{statedir}/apache_stopped_during_nextcloud_install ]; then
  echo "o %{name} post-install: Restarting Apache"
  ## If we stopped apache in pre section, we now should restart. -- but *ONLY* then!
  ## Maybe delegate that task to occ upgrade? They also need to handle this, somehow.
%if 0%{?suse_version}
  service apache2 start
%endif
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
  service httpd start
%endif
fi

if [ -s %{statedir}/occ_maintenance_mode_during_nextcloud_install ]; then
  echo "o %{name} post-install: occ maintenance:repair (fix possible errors)"
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ maintenance:repair" || true
  echo "o %{name} post-install: occ db:add-missing-* (add missing db things)"
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ maintenance:mimetype:update-db" || true
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ db:add-missing-columns" || true
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ db:add-missing-indices" || true
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ db:add-missing-primary-keys" || true
  echo "o %{name} post-install: occ update apps"
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ app:update --all" || true
  echo "o %{name} post-install: occ upgrade"
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ upgrade" || true
  echo "o %{name} post-install: occ maintenance:mode --off"
  su %{nc_user} -s /bin/sh -c "cd %{nc_dir}; PATH=%{ocphp_bin}:$PATH php ./occ maintenance:mode --off" || true
fi

rm -f %{statedir}/apache_stopped_during_nextcloud_install
rm -f %{statedir}/occ_maintenance_mode_during_nextcloud_install

if [ $1 -eq 1 ]; then
  echo "o %{name} post-install: First install complete"
else
  echo "o %{name} post-install: Upgrade complete"
fi

%preun
%service_del_preun %{name}-cron.timer %{name}-cron.service

%postun
%service_del_postun %{name}-cron.timer %{name}-cron.service

%files
%defattr(644,root,root,755)
%exclude %{apache_myserverroot}/%{name}/README
%exclude %{apache_myserverroot}/%{name}/README.SUSE
%exclude %{apache_myserverroot}/%{name}/README.SELinux
%doc README README.SUSE README.SELinux
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_sbindir}/rc%{name}-cron
%{_unitdir}/%{name}-cron.service
%{_unitdir}/%{name}-cron.timer
%{apache_myserverroot}/%{name}
%attr(-,%{apache_user},%{apache_group}) %{apache_myserverroot}/%{name}/occ
%config(noreplace) %{apache_myserverroot}/%{name}/.user.ini
%defattr(664,%{apache_user},%{apache_group},775)
%{apache_myserverroot}/%{name}/apps
%{apache_myserverroot}/%{name}/core/js/mimetypelist.js
%dir %{apache_myserverroot}/%{name}/core/img/filetypes
%{apache_myserverroot}/%{name}/core/img/filetypes/*
%defattr(660,%{apache_user},%{apache_group},770)
%{apache_myserverroot}/%{name}/config
%{apache_myserverroot}/%{name}/data

%files apache
%config(noreplace) %{apache_confdir}/nextcloud.conf

%changelog
