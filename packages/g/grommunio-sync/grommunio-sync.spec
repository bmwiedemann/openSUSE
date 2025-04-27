#
# spec file for package grommunio-sync
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


Name:           grommunio-sync
Version:        2.2
Release:        0
Summary:        An implementation of Exchange ActiveSync protocol
Group:          Productivity/Networking/Email/Utilities
License:        AGPL-3.0-only
BuildArch:      noarch
URL:            https://grommunio.com/
Source:         https://github.com/grommunio/grommunio-sync/releases/download/%version/grommunio-sync-%version.tar.zst
Source2:        https://github.com/grommunio/grommunio-sync/releases/download/%version/grommunio-sync-%version.tar.asc

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%define phpdir /etc/php8
%else
%define phpdir /etc/php7
%endif
BuildRequires:  zstd
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       php8-mbstring
Requires:       php8-mysql
Requires:       php8-pcntl
Requires:       php8-pdo
Requires:       php8-posix
Requires:       php8-redis
Requires:       php8-soap
%endif
%if 0%{?sle_version} && 0%{?sle_version} < 150400
Requires:       php7-mbstring
Requires:       php7-mysql
Requires:       php7-pcntl
Requires:       php7-pdo
Requires:       php7-posix
Requires:       php7-redis
Requires:       php7-soap
%endif
%if 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora_version}
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-pcntl
Requires:       php-pdo
Requires:       php-posix
Requires:       php-redis
Requires:       php-soap
%endif
Requires:       gromox
BuildRequires:  mapi-header-php
Requires:       mapi-header-php
%if 0%{?suse_version} >= 1500
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  %_sbindir/groupadd
Requires(pre):  %_sbindir/useradd
%endif
Provides:       system-user-grosync
Obsoletes:      system-user-grosync

%define gsync_dir %_datadir/%name

%description
grommunio-sync is an implementation of the ActiveSync protocol which is
used "over-the-air" for multi-platform ActiveSync devices. Devices
supported are including Windows Mobile, Android, iPhone, and Nokia.
With grommunio-sync, many groupware servers can be connected and synced
with these devices.

%prep
%autosetup

%build
%if 0%{?suse_version} >= 1500
%sysusers_generate_pre %_sourcedir/system-user-grosync.conf user grommunio-sync.conf
%else
: >>"user.pre"
%endif

%install
b="%buildroot"

cdir="$b/%_sysconfdir/grommunio-sync"
mkdir -pv "$b/%gsync_dir"
cp -av * "$b/%gsync_dir/"
rm -fv "$b/%gsync_dir/"{INSTALL,LICENSE,DEVELOPMENT}
rm -frv "$b/%gsync_dir/build"

sed -s "s/__VERSION__/%version/" build/version.php.in > "$b/%gsync_dir/version.php"

mkdir -pv "$b/%_sysconfdir/grommunio-sync"

mv -v "$b/%gsync_dir/config.php" "$cdir/grommunio-sync.conf.php"
ln -sv "%_sysconfdir/grommunio-sync/grommunio-sync.conf.php" "$b/%gsync_dir/config.php"

mkdir -pv "$b/%_sbindir"
ln -sv "%gsync_dir/grommunio-sync-top.php" "$b/%_sbindir/grommunio-sync-top"

mkdir -pv "$b/var/log/grommunio" "$b/%_localstatedir/log/grommunio-sync"
mkdir -pv "$b/%_sysconfdir/logrotate.d"
install -Dpm 644 build/grommunio-sync.lr \
    "$b/%_sysconfdir/logrotate.d/grommunio-sync.lr"

# NGINX
mkdir -pv "$b/usr/share/grommunio-common/nginx/locations.d"
install -Dpm 644 build/grommunio-sync.conf "$b/usr/share/grommunio-common/nginx/locations.d/grommunio-sync.conf"
mkdir -pv "$b/usr/share/grommunio-common/nginx/upstreams.d"
install -Dpm 644 build/grommunio-sync-upstream.conf "$b/usr/share/grommunio-common/nginx/upstreams.d/grommunio-sync.conf"

# PHP-FPM
mkdir -pv "$b/%phpdir/fpm/php-fpm.d/"
install -Dpm 644 build/pool-grommunio-sync.conf "$b/%phpdir/fpm/php-fpm.d/pool-grommunio-sync.conf"

mkdir -p "%buildroot/%_sysusersdir"
install -m 0644 "build/sysuser.conf" "%buildroot/%_sysusersdir/grommunio-sync.conf"

%pre -f user.pre
%if !0%{?suse_version}
getent group grosync >/dev/null || %_sbindir/groupadd -r grosync
getent passwd grosync >/dev/null || %_sbindir/useradd -g grosync -s /bin/false \
        -r -c "user for %name" -d "%_localstatedir/lib/grosync" grosync
%endif

%files
%doc LICENSE
%dir %_sysconfdir/grommunio-sync
%config(noreplace) %attr(0640,root,grosync) %_sysconfdir/grommunio-sync/grommunio-sync.conf.php
%config(noreplace) %attr(0640,root,root) %_sysconfdir/logrotate.d/grommunio-sync.lr
%dir %phpdir
%dir %phpdir/fpm
%dir %phpdir/fpm/php-fpm.d/
%attr(0640,root,root) %phpdir/fpm/php-fpm.d/pool-grommunio-sync.conf
%_sbindir/grommunio-sync-top
%_datadir/grommunio-common/
%gsync_dir/
%_sysusersdir/*.conf
%attr(750,root,root) /var/log/grommunio/
%attr(770,root,grosync) %dir %_localstatedir/log/grommunio-sync

%changelog
