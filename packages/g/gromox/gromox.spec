#
# spec file for package gromox
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


%define _libexecdir %_prefix/libexec

Name:           gromox
Version:        2.46
Release:        0
Summary:        Groupware server backend with RPC, IMAP,POP3, PHP-MAPI support
License:        AGPL-3.0-or-later AND GPL-2.0-only AND GPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://grommunio.com/
Source:         https://github.com/grommunio/gromox/releases/download/%name-%version/%name-%version.tar.zst
Source2:        https://github.com/grommunio/gromox/releases/download/%name-%version/%name-%version.tar.asc
Source8:        %name.keyring
BuildRequires:  fdupes
%if 0%{?suse_version} && 0%{?suse_version} < 1600
BuildRequires:  gcc14-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version}
BuildRequires:  libmysqlclient-devel >= 5.6
BuildRequires:  openldap2-devel
%else
BuildRequires:  mariadb-devel >= 5.6
BuildRequires:  openldap-devel
%endif
BuildRequires:  libtool >= 2
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkg-config
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  php8-devel
%else
BuildRequires:  php-devel >= 7
%endif
BuildRequires:  zstd
BuildRequires:  group(gromox)
BuildRequires:  pkgconfig(fmt) >= 8
BuildRequires:  pkgconfig(jsoncpp) >= 1.4.0
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(libHX) >= 4.27
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libesedb)
BuildRequires:  pkgconfig(libolecf)
BuildRequires:  pkgconfig(libpff)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(tinyxml2) >= 8
BuildRequires:  pkgconfig(wmime) >= 1
BuildRequires:  pkgconfig(zlib)
BuildRequires:  user(grommunio)
BuildRequires:  user(gromox)
%if 0%{?suse_version}
Requires:       glibc-locale-base
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
# Require php-cli/fpm (and modules) that have a chance of loading mapi.so
# which means same generation as the one we built with.
Requires:       php8-cli
Requires:       php8-fpm
Requires:       php8-mysql
Requires:       php8-posix
Requires:       php8-soap
%endif
%if 0%{?rhel} || 0%{?fedora_version}
Requires:       php-cli
Requires:       php-fpm
Requires:       php-mysqlnd
Requires:       php-posix
Requires:       php-soap
%endif
Requires:       w3m
Requires(pre):  user(grommunio)
Requires(pre):  user(gromox)
Requires(pre):  group(gromox)
Provides:       php-mapi-gromox = %version-%release
Conflicts:      grommunio-admin-api < 1.10.7
Recommends:     mapitags
%{?systemd_ordering}
%if !0%{?_pamdir:1}
%define _pamdir /%_lib/security
%endif

%description
Gromox is the central groupware server component of grommunio. It is
capable of serving as a replacement for Microsoft Exchange and
compatibles. Connectivity options include RPC/HTTP (Outlook
Anywhere), MAPI/HTTP, IMAP, POP3, an SMTP-speaking LDA, and a PHP
module with a Z-MAPI function subset.

Import is possible from PST/OST/MSG/CDFV2/TNEF, EML/ICAL/VCF, Kopano,
Zarafa, and via imapsync.

Gromox relies on other components to provide a sensibly complete mail
system, such as Postfix as a mail transfer agent, and grommunio-admin
for user management. A webmail client interface is available with
grommunio-web. The grommunio appliance ships these essentials and has a
ready-to-run installation of Gromox.

%prep
%autosetup -p1

%build
%configure \
%if 0%{?suse_version} && 0%{?suse_version} < 1600
	CC=gcc-14 CXX=g++-14 \
%endif
	%nil
%make_build V=1

%install
b="%buildroot"
%make_install
%if "%_pamdir" != "%_libdir/security"
# libtool gets confused if pamlibdir is not below prefix;
# as such we are not using `make install pamlibdir=...`
mkdir -pv "$b/%_pamdir"
mv "$b/%_libdir/security"/* "$b/%_pamdir/"
%endif
# done in system-user-gromox (which exists for ease of building for multiple distros)
rm -fv "%buildroot/%_sysusersdir/sysusers-gromox.conf"
for i in /var/lib/gromox /var/lib/gromox/domain \
    /var/lib/gromox/queue \
    /var/lib/gromox/queue/mess /var/lib/gromox/queue/save \
    /var/lib/gromox/queue/cache \
    /var/lib/gromox/queue/timer /var/lib/gromox/user \
    /var/log/gromox; do
	mkdir -p "$b/$i"
done

find "$b" -type f -name "*.la" -delete
rm -fv "$b/%_libdir"/*.so

mkdir -p "$b/%_sysconfdir/%name" "$b/%_datadir/%name"
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
mkdir -p "$b/etc/php8/fpm/php-fpm.d"
cp -a "$b/usr/share/gromox/fpm-gromox.conf.sample" "$b/etc/php8/fpm/php-fpm.d/gromox.conf"
%endif
%if 0%{?sle_version} && 0%{?sle_version} < 150400
mkdir -p "$b/etc/php7/fpm/php-fpm.d"
cp -a "$b/usr/share/gromox/fpm-gromox.conf.sample" "$b/etc/php7/fpm/php-fpm.d/gromox.conf"
%endif
%if 0%{?rhel} || 0%{?fedora_version}
mkdir -p "$b/etc/php-fpm.d"
cp -a "$b/usr/share/gromox/fpm-gromox.conf.sample" "$b/etc/php-fpm.d/gromox.conf"
%endif
perl -i -lpe 's{Type=simple}{Type=simple\nRestart=on-failure}' "$b/%_unitdir"/*.service
%fdupes %buildroot/%_prefix

%global services gromox-delivery.service gromox-delivery-queue.service gromox-event.service gromox-http.service gromox-imap.service gromox-midb.service gromox-pop3.service gromox-snapshot.service gromox-snapshot.timer gromox-timer.service gromox-zcore.service

%if 0%{?service_add_pre:1}
%pre
# User addition done a priori by system-user-gromox(!)
%service_add_pre %services
%endif

%post
/sbin/ldconfig
%tmpfiles_create tmpfiles-gromox.conf
%if 0%{?service_add_post:1}
%service_add_post %services
%else
%systemd_post %services
%endif
if ! test -x /usr/bin/systemctl; then
	exit 0
fi
# saslauthd re-opens pam_gromox.so everytime, however
# libgromox_common.so stays resident because of STB_UNIQUE symbols,
# therefore saslauthd can run into the problem that a new version of
# the pam module will be combined with a too old version of gromox
# libs. No good solution in sight..
/usr/bin/systemctl try-restart grommunio-chat.service php-fpm.service saslauthd.service 2>/dev/null || :
# Delete old service links
if /usr/bin/systemctl is-enabled gromox-exch.target >/dev/null 2>/dev/null; then
	echo Migrating gromox-exch.target
	/usr/bin/systemctl enable gromox-http.service gromox-midb.service gromox-zcore.service || :
	/usr/bin/systemctl disable gromox-exch.target || :
fi
if /usr/bin/systemctl is-enabled gromox-mra.target >/dev/null 2>/dev/null; then
	echo Migrating gromox-mra.target
	/usr/bin/systemctl enable gromox-imap.service gromox-pop3.service || :
	/usr/bin/systemctl disable gromox-mra.target || :
fi
if /usr/bin/systemctl is-enabled gromox-mta.target >/dev/null 2>/dev/null; then
	echo Migrating gromox-mta.target
	/usr/bin/systemctl enable gromox-delivery.service gromox-delivery-queue.service || :
	/usr/bin/systemctl disable gromox-mta.target || :
fi
if /usr/bin/systemctl is-enabled gromox-sa.target >/dev/null 2>/dev/null; then
	echo Migrating gromox-sa.target
	/usr/bin/systemctl enable gromox-event.service gromox-timer.service || :
	/usr/bin/systemctl disable gromox-sa.target || :
fi

%preun
%if 0%{?service_del_preun:1}
%service_del_preun %services
%else
%systemd_preun %services
%endif

%postun
%if 0%{?service_del_postun:1}
%service_del_postun %services
%else
%systemd_postun_with_restart %services
%endif
/sbin/ldconfig

%files
%_sysconfdir/php*
# "grommunio" permission is exercised by grommunio-admin-api.
# pam.cfg needs to be accessible by arbitrary programs (hence we need at least 0751).
%attr(0755,grommunio,gromoxcf) %dir %_sysconfdir/%name/
%_sbindir/gromox-*
%_libdir/*.so.*
%_libdir/php*/
%_libexecdir/%name/
%_pamdir/
%_datadir/%name/
%_mandir/man*/*.[0-9]*
%_tmpfilesdir/*.conf
%_unitdir/*
%attr(0770,gromox,gromox) /var/lib/gromox/
%attr(0770,gromox,gromox) /var/log/gromox/
%if 0%{?suse_version} >= 1500 && 0%{?suse_version} < 1550
%dir %_libexecdir
%endif
%license LICENSE.txt
%doc doc/changelog.rst

%changelog
