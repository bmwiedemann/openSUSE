#
# spec file for package grommunio-dav
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?rhel} || 0%{?fedora_version}
%global __brp_mangle_shebangs_exclude_from sabredav|vobject|generate_vcards
%endif

Name:           grommunio-dav
Version:        1.5
%define scmver 1.5.0.800a8a8
Release:        0
Summary:        CalDAV and CardDAV implementation for grommunio
License:        AGPL-3.0-only
Group:          Productivity/Networking/Email/Clients
URL:            https://github.com/grommunio-dev/grommunio-dav
Source:         https://github.com/grommunio/grommunio-dav/releases/download/%version/grommunio-dav-%scmver.tar.xz
Source2:        https://github.com/grommunio/grommunio-dav/releases/download/%version/grommunio-dav-%scmver.tar.asc
Source3:        version.php.in
Source8:        %name.keyring
%if 0%{?suse_version} >= 1540 || 0%{?sle_version} >= 150400
%define fpmdir /etc/php8/fpm/php-fpm.d
%endif
%if 0%{?sle_version} && 0%{?sle_version} < 150400
%define fpmdir /etc/php7/fpm/php-fpm.d
%endif
%if 0%{?rhel} || 0%{?fedora_version}
%define fpmdir /etc/php-fpm.d
%endif

BuildArch:      noarch
%if 0%{?suse_version} >= 1540 || 0%{?sle_version} >= 150400
Requires:       php8-ctype
Requires:       php8-curl
Requires:       php8-dom
Requires:       php8-iconv
Requires:       php8-mbstring
Requires:       php8-sqlite
Requires:       php8-xmlreader
Requires:       php8-xmlwriter
%endif
%if 0%{?sle_version} && 0%{?sle_version} < 150400
Requires:       php7-ctype
Requires:       php7-curl
Requires:       php7-dom
Requires:       php7-iconv
Requires:       php7-mbstring
Requires:       php7-sqlite
Requires:       php7-xmlreader
Requires:       php7-xmlwriter
%endif
%if 0%{?rhel} || 0%{?fedora_version}
Requires:       php-ctype
Requires:       php-curl
Requires:       php-dom
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-sqlite
Requires:       php-xml
Requires:       php-xmlreader
Requires:       php-xmlwriter
%endif

Requires:       gromox >= 1.27
BuildRequires:  mapi-header-php
Requires:       mapi-header-php >= 1.5
%if 0%{?suse_version} >= 1500
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  %_sbindir/groupadd
Requires(pre):  %_sbindir/useradd
%endif
Provides:       system-user-grodav
Obsoletes:      system-user-grodav

%description
grommunio-dav is a CalDAV and CardDAV implementation for grommunio.

%define data_dir %_datadir/grommunio-dav
%define conf_dir %_sysconfdir/grommunio-dav

%prep
%autosetup -p1 -n %name-%scmver

%build
# Let the DEVELOPER_MODE be enabled for now, otherwise files will not work.
# sed -i "s;'DEVELOPER_MODE', true;'DEVELOPER_MODE', false;" config.php
sed -i 's;level = TRACE;level = INFO;' glogger.ini

>user.pre
%if 0%{?suse_version} >= 1500
%sysusers_generate_pre build/sysuser.conf user grommunio-dav.conf
%endif

%install
b="%buildroot"
cdir="$b/%conf_dir"
ddir="$b/%data_dir"
rm -fv "$b/%_datadir/%name/user.pre"

mkdir -p "$ddir"
cp -ar lib/ "$ddir/"
cp -ar vendor/ "$ddir/"
cp -a server.php "$ddir/"

mkdir -p "$cdir"
cp -a "config.php" "$cdir/"
cp -a "glogger.ini" "$cdir/"
ln -s "%conf_dir/config.php" "$ddir/config.php"
ln -s "%conf_dir/glogger.ini" "$ddir/glogger.ini"

# Nginx conf
mkdir -pv "$b/usr/share/grommunio-common/nginx/locations.d"
install -Dpvm 644 build/grommunio-dav.conf "$b/usr/share/grommunio-common/nginx/locations.d/"
mkdir -pv "$b/usr/share/grommunio-common/nginx/upstreams.d"
install -Dpvm 644 build/grommunio-dav-upstream.conf "$b/usr/share/grommunio-common/nginx/upstreams.d/grommunio-dav.conf"

# PHP-FPM
mkdir -pv "$b/%fpmdir" "$b/%_sysusersdir"
install -Dpvm 644 build/pool-grommunio-dav.conf "$b/%fpmdir/pool-grommunio-dav.conf"
install -m 0644 "build/sysuser.conf" "%buildroot/%_sysusersdir/grommunio-dav.conf"

mkdir -pv "$b/%_localstatedir/lib/grommunio-dav/"
mkdir -pv "$b/%_localstatedir/log/grommunio-dav/"

# set version number
sed -s "s/@VERSION@/%version/" %{SOURCE3} > "$ddir/version.php"

mkdir -p "%buildroot/%_sysusersdir"
install -m 0644 "build/sysuser.conf" "%buildroot/%_sysusersdir/grommunio-dav.conf"

%pre -f user.pre
%if !0%{?suse_version}
getent group grodav >/dev/null || %_sbindir/groupadd -r grodav
getent passwd grodav >/dev/null || %_sbindir/useradd -g grodav -s /bin/false \
        -r -c "user for %name" -d "%_localstatedir/lib/grodav" grodav
%endif

%post
# reload nginx and restart fpm as this package ships config snippets
# reloading is not sufficient especially for php-fpm as it does not
# create the socket with the appropriate permissions
/usr/bin/systemctl try-restart php-fpm.service 2>/dev/null || :
/usr/bin/systemctl reload nginx.service 2>/dev/null || :

%files
%doc LICENSE
%_sysconfdir/php*
%data_dir/
%dir %_sysconfdir/grommunio-dav
%config(noreplace) %attr(0644,root,root) %conf_dir/config.php
%config(noreplace) %attr(0644,root,root) %conf_dir/glogger.ini
%_datadir/grommunio-common/
%_sysusersdir/*.conf
%attr(0770,grodav,root) %dir %_localstatedir/lib/grommunio-dav/
%attr(0770,grodav,root) %dir %_localstatedir/log/grommunio-dav/

%changelog
