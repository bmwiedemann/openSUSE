#
# spec file for package roundcubemail
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


%define apache_serverroot %(%{_sbindir}/apxs2 -q DATADIR)
%define apache_sysconfdir %(%{_sbindir}/apxs2 -q SYSCONFDIR)
%define roundcubepath %{apache_serverroot}/%{name}
%define roundcubeconfigpath %{_sysconfdir}/%{name}
%define php_major_version       %(php -r "echo PHP_MAJOR_VERSION;")
Name:           roundcubemail
Version:        1.4.9
Release:        0
Summary:        A browser-based multilingual IMAP client
License:        GPL-3.0-or-later AND GPL-2.0-only AND BSD-3-Clause
Group:          Productivity/Networking/Email/Clients
URL:            https://www.roundcube.net/
Source0:        https://github.com/roundcube/%{name}/releases/download/%{version}/%{name}-%{version}-complete.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        %{name}-httpd.conf
Source3:        %{name}-httpd.inc
Source4:        README.openSUSE
Source5:        %{name}.logrotate
Source6:        https://roundcube.net/download/pubkey.asc#/%{name}.keyring
Source7:        https://github.com/roundcube/%{name}/releases/download/%{version}/%{name}-%{version}-complete.tar.gz.asc
Source8:        robots.txt
# PATCH-FIX-OPENSUSE roundcubemail-config_dir.patch -- use the general config directory /etc
Patch0:         %{name}-config_dir.patch
BuildRequires:  apache2-devel
BuildRequires:  pcre-devel
BuildRequires:  php
Requires:       http_daemon
Requires:       mod_php_any >= 5.4
Requires:       php-dom
Requires:       php-exif
Requires:       php-gettext
Requires:       php-iconv
Requires:       php-json
Requires:       php-mbstring
Requires:       php-openssl
## Requires: for upstream dep package
Requires:       php-pear-Auth_SASL >= 1.0.6
Requires:       php-pear-MDB2_Driver_mysqli
Requires:       php-pear-Mail_Mime >= 1.10.0
Requires:       php-pear-Net_IDNA2 >= 0.1.1
Requires:       php-pear-Net_LDAP2
Requires:       php-pear-Net_SMTP >= 1.8.1
Requires:       php-pear-Net_Sieve >= 1.4.3
Requires:       php-pear-Net_Socket >= 1.0.12
Requires:       php-session
Requires:       php-sockets
Requires:       php_any_db
Recommends:     logrotate
Recommends:     php-fileinfo
Recommends:     php-intl
Recommends:     php-imagick
Recommends:     php-mysql
Recommends:     php-pear-Crypt_GPG >= 1.6.3
Recommends:     php-zip
Suggests:       apache2
Conflicts:      roundcube-framework
Provides:       roundcube_framework = %{version}
BuildArch:      noarch
%if 0%{?suse_version} >= 1100
BuildRequires:  fdupes
%endif

%description
Roundcube Webmail is a browser-based multilingual IMAP client with an
application-like user interface. It provides MIME support, address
book, folder manipulation, message searching and spell checking.

Roundcube Webmail is written in PHP and requires a MySQL database.
The user interface is skinnable using XHTML and CSS 2.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE4} .
# remove cruft from source archive:
# .arcconfig       => file for phabricator.uri
# .gitignore       => git config file
# .php_cs.dist     => PhpCsFixer
# .scrutinizer.yml => PHP mess detector
# .travis.yml      => Travis CI descriptions
for file in .arcconfig .gitignore .php_cs.dist .scrutinizer.yml .travis.yml ; do
	find . -name "$file" -delete
done
# remove php documentor script
rm vendor/pear/net_smtp/phpdoc.sh
# remove 0-byte files
find . -size 0 -delete
# no need to check .htaccess each time, the apache config takes care of the restrictions
find . -name ".htaccess" -delete
# remove travis files
find vendor/ -name ".travis.yml" -delete

# remove obscure sub-directory
#rm -rf roundcubemail-git composer.json.rej
# remove mssql scripts (not needed on openSUSE)
rm -rf \
    SQL/mssql/ \
    SQL/mssql.*.sql
# remove shebang from chpass-wrapper
sed -i '1d' plugins/password/helpers/chpass-wrapper.py
# remove INSTALL doc
rm INSTALL
# fix interpreter for shell scripts
sed -e 's|%{_bindir}/env php|%{_bindir}/php|' -i bin/*.sh 
sed -e 's|%{_bindir}/env php|%{_bindir}/php|' -i vendor/pear/crypt_gpg/scripts/crypt-gpg-pinentry vendor/roundcube/plugin-installer/src/bin/rcubeinitdb.sh

%build

%install
# install roundcubemail.logrotate
install -d -m 0755 %{buildroot}/%{_sysconfdir}/logrotate.d
install %{SOURCE5} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

# extract roundcube-framework
install -d -m 0755 %{buildroot}/%{_datadir}/php%{php_major_version}
mv program/lib/Roundcube %{buildroot}%{_datadir}/php%{php_major_version}/Roundcube

# install roundcubemail
install -d -m 0755 %{buildroot}/%{roundcubepath}
cp -a * %{buildroot}%{roundcubepath}/
cp %{SOURCE8} %{buildroot}%{roundcubepath}/
ln -s %{roundcubepath}/installer %{buildroot}/%{roundcubepath}/public_html/installer

# install config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp config/* %{buildroot}%{roundcubeconfigpath}/
install %{buildroot}/%{roundcubeconfigpath}/config.inc.php.sample %{buildroot}/%{roundcubeconfigpath}/config.inc.php
rm -rf %{buildroot}/%{roundcubepath}/config
ln -s %{roundcubeconfigpath} %{buildroot}/%{roundcubepath}/config

# logs + temp go into /var/
rm -rf %{buildroot}/%{roundcubepath}/logs \
       %{buildroot}%{roundcubepath}/temp
install -d %{buildroot}/%{_localstatedir}/log/%{name} \
         %{buildroot}%{_localstatedir}/lib/%{name}
ln -s %{_localstatedir}/log/%{name}/ %{buildroot}/%{roundcubepath}/logs
ln -s %{_localstatedir}/lib/%{name}/ %{buildroot}/%{roundcubepath}/temp

# move some plugin configs to /etc/roundcubemail
for PLUGIN in acl managesieve password; do
    if [ -f %{buildroot}/%{roundcubepath}/plugins/$PLUGIN/config.inc.php.dist ]; then
        mv %{buildroot}%{roundcubepath}/plugins/$PLUGIN/config.inc.php.dist %{buildroot}%{roundcubeconfigpath}/$PLUGIN.inc.php
        ln -s %{roundcubeconfigpath}/$PLUGIN.inc.php %{buildroot}/%{roundcubepath}/plugins/$PLUGIN/config.inc.php
    fi
done

# skins have some configurable files in their directories
mkdir -p %{buildroot}%{roundcubeconfigpath}/skins/elastic/styles
for file in _styles.less _variables.less ; do
        mv %{buildroot}%{roundcubepath}/skins/elastic/styles/$file %{buildroot}%{roundcubeconfigpath}/skins/elastic/styles/
        ln -s %{roundcubeconfigpath}/skins/elastic/styles/$file %{buildroot}%{roundcubepath}/skins/elastic/styles/
done

# install httpd.conf file and adapt the configuration
install -D -m0644 %{SOURCE3} %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.inc
# fix paths in http config
sed -e "s#__ROUNDCUBEPATH__#%{roundcubepath}#g" \
 -e "s,@apache_sysconfdir@,%{apache_sysconfdir},g" \
 -e "s,@name@,%{name},g" \
%{SOURCE2} > %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf

# install docs
install -d -m 0755 %{buildroot}/%{_defaultdocdir}/%{name}
%if 0%{?suse_version} >= 1500
TXT="CHANGELOG UPGRADING README.md README.openSUSE SQL"
rm %{buildroot}%{roundcubepath}/LICENSE
%else
TXT="CHANGELOG UPGRADING README.md README.openSUSE SQL LICENSE"
%endif
for i in $TXT; do
    mv -v %{buildroot}%{roundcubepath}/$i %{buildroot}%{_defaultdocdir}/%{name}/
done

# move Readme files to docdir
for file in LICENSE README README.rst *.md ; do
	for i in $(find %{buildroot}%{roundcubepath}/vendor -type f -name "$file"); do
		BASEDIR=$(echo "$i" | sed -e "s|%{buildroot}%{roundcubepath}/vendor||g")
		BASEDIR=$(dirname "$BASEDIR")
		mkdir -p "%{buildroot}%{_defaultdocdir}/%{name}/$BASEDIR"
		mv "$i" "%{buildroot}%{_defaultdocdir}/%{name}/$BASEDIR"
	done
done

# create a link for SQL
ln -s %{_defaultdocdir}/%{name}/SQL %{buildroot}/%{roundcubepath}/SQL

# Make ghost files
mkdir %{buildroot}%{roundcubepath}/migrated
mkdir %{buildroot}%{roundcubepath}/migration

# fdupes
%if 0%{?suse_version} >= 1100
%fdupes %{buildroot}%{roundcubepath}
%fdupes %{buildroot}%{_defaultdocdir}/%{name}
%endif

%pre
# backup logs, temp and config for migration
if [ ! -h %{roundcubepath}/logs ] && [ -d %{roundcubepath}/logs ]; then
        mkdir -p %{roundcubepath}/migration
        mv %{roundcubepath}/logs %{roundcubepath}/migration/.
fi
if [ ! -h %{roundcubepath}/temp ] && [ -d %{roundcubepath}/temp ]; then
        mkdir -p %{roundcubepath}/migration
        mv %{roundcubepath}/temp %{roundcubepath}/migration/.
fi
if [ ! -h %{roundcubepath}/SQL ] && [ -d %{roundcubepath}/SQL ]; then
        mkdir -p %{roundcubepath}/migration
        mv %{roundcubepath}/SQL %{roundcubepath}/migration/.
fi

for PLUGIN in acl managesieve password; do
    if [ ! -h %{roundcubepath}/plugins/$PLUGIN/config.inc.php ] && [ -f %{roundcubepath}/plugins/$PLUGIN/config.inc.php ]; then
            mv %{roundcubepath}/plugins/$PLUGIN/config.inc.php %{roundcubepath}/migration/$PLUGIN.inc.php
    fi
done

%post
# replace default des string in config file for better security
makedesstr() {
	local chars="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	local max=${#chars}
	for i in $(seq 1 24); do
		echo "$chars" | dd bs=1 skip=$(($(od -An -d -N2 /dev/urandom) % $max)) count=1 2>/dev/null
	done
	echo
}

sed -i "s/rcmail-\!24ByteDESkey\*Str/`makedesstr`/" %{roundcubeconfigpath}/defaults.inc.php || : &> /dev/null

# Update ?
if [ ${1:-0} -eq 1 ]; then
  if [ -x %{_sbindir}/a2enmod ]; then
  # enable required apache modules
  %if 0%{?suse_version} > 01500
    if ! grep -q php %{_sysconfdir}/sysconfig/apache2 1>&2 2>/dev/null; then
      %{_sbindir}/a2enmod -q php7    || %{_sbindir}/a2enmod php7
    fi
  %endif
    for module in alias brotli deflate expires filter headers rewrite setenvif version ; do
      %{_sbindir}/a2enmod -q $module || %{_sbindir}/a2enmod $module
    done
  fi
fi

# restore backed up logs, temp and config
if [ -h %{roundcubepath}/logs ] && [ -d %{roundcubepath}/migration/logs ]; then
        mkdir -p %{roundcubepath}/migrated
        cp %{roundcubepath}/migration/logs/* %{roundcubepath}/logs/.
        mv %{roundcubepath}/migration/logs %{roundcubepath}/migrated/.
fi
if [ -h %{roundcubepath}/temp ] && [ -d %{roundcubepath}/migration/temp ]; then
        mkdir -p %{roundcubepath}/migrated
        cp %{roundcubepath}/migration/temp/* %{roundcubepath}/temp/.
        mv %{roundcubepath}/migration/temp %{roundcubepath}/migrated/.
fi
if [ -h %{roundcubepath}/SQL ] && [ -d %{roundcubepath}/migration/SQL ]; then
        rm -r %{roundcubepath}/migration/SQL
fi
for PLUGIN in acl managesieve password; do
    if [ -f %{roundcubepath}/migration/$PLUGIN.inc.php ] && [ -h %{roundcubepath}/plugins/$PLUGIN/config.inc.php ]; then
            cp %{roundcubepath}/migration/$PLUGIN.inc.php %{roundcubeconfigpath}/.
            mv %{roundcubepath}/migration/$PLUGIN.inc.php %{roundcubepath}/migrated/$PLUGIN.inc.php
    fi
done
for MIGDIR in migration migrated; do
    if [ -d %{roundcubepath}/$MIGDIR ]; then
        find %{roundcubepath}/$MIGDIR -empty -delete
    fi
    if [ -d %{roundcubepath}/$MIGDIR ]; then
        echo "Found %{roundcubepath}/$MIGDIR! Make sure you delete this folder after checking the migration!"
    fi
done

# update/make new config
if [ ! -f %{roundcubeconfigpath}/config.inc.php ]; then
  if [ -f %{roundcubeconfigpath}/main.inc.php ] && [ -f %{roundcubeconfigpath}/db.inc.php ]; then
    %{roundcubepath}/bin/update.sh \
        --version '?' \
        --accept
  else
    cp %{roundcubeconfigpath}/config.inc.php.sample %{roundcubeconfigpath}/config.inc.php
  fi
fi

exit 0

%files
%defattr(0644, root, root,0755)
%doc CHANGELOG
%if 0%{?suse_version} >= 1500
%license LICENSE
%else 
%doc LICENSE
%endif
%doc README.md
%doc README.openSUSE
%doc UPGRADING
%doc SQL/
%doc %{_defaultdocdir}/%{name}/*
%dir %{roundcubepath}
%dir %{roundcubeconfigpath}
%dir %{roundcubeconfigpath}/skins
%dir %{roundcubeconfigpath}/skins/elastic
%dir %{roundcubeconfigpath}/skins/elastic/styles/
%ghost %config(noreplace) %{roundcubeconfigpath}/config.inc.php
%config(noreplace) %{roundcubeconfigpath}/acl.inc.php
%config(noreplace) %{roundcubeconfigpath}/managesieve.inc.php
%config(noreplace) %{roundcubeconfigpath}/password.inc.php
%config %{roundcubeconfigpath}/config.inc.php.sample
%config %{roundcubeconfigpath}/defaults.inc.php
%config %{roundcubeconfigpath}/mimetypes.php
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.conf
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.inc
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{roundcubeconfigpath}/skins/elastic/styles/_styles.less 
%config(noreplace) %{roundcubeconfigpath}/skins/elastic/styles/_variables.less
%{roundcubepath}/composer.json-dist
%{roundcubepath}/composer.json
%{roundcubepath}/composer.lock
%{roundcubepath}/config
%{roundcubepath}/index.php
%{roundcubepath}/robots.txt
%dir %{roundcubepath}/bin
%attr(0755,root,root) %{roundcubepath}/bin/*.sh
%attr(0755,root,root) %{roundcubepath}/vendor/roundcube/plugin-installer/src/bin/rcubeinitdb.sh
%attr(0755,root,root) %{roundcubepath}/plugins/password/helpers/change_ldap_pass.pl 
%attr(0755,root,root) %{roundcubepath}/vendor/pear/crypt_gpg/scripts/crypt-gpg-pinentry
%{roundcubepath}/installer/
%{roundcubepath}/logs
%ghost %{roundcubepath}/migrated/
%ghost %{roundcubepath}/migration/
%{roundcubepath}/public_html/
%{roundcubepath}/plugins/
%{roundcubepath}/program/
%{roundcubepath}/skins/
%{roundcubepath}/SQL
%{roundcubepath}/temp
%{roundcubepath}/vendor/
%dir %{_datadir}/php%{php_major_version}
%{_datadir}/php%{php_major_version}/Roundcube/
%attr(-, wwwrun, root) %{_localstatedir}/log/%{name}
%attr(-, wwwrun, root) %{_localstatedir}/lib/%{name}

%changelog
