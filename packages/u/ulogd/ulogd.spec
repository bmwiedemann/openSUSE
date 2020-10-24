#
# spec file for package ulogd
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


Name:           ulogd
Version:        2.0.7
Release:        0
Summary:        Userspace logging for Netfilter
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            http://netfilter.org/projects/ulogd/

#Git-Clone:	git://git.netfilter.org/ulogd2
#DL-URL:	http://netfilter.org/projects/ulogd/files/
Source:         http://netfilter.org/projects/ulogd/files/%name-%version.tar.bz2
Source2:        http://netfilter.org/projects/ulogd/files/%name-%version.tar.bz2.sig
Source4:        ulogd.service
Source5:        ulogd.conf
Patch1:         0001-build-adjust-configure-for-postgresql-10-11.patch
Patch4:         ulogd-conf.diff

BuildRequires:  autoconf >= 2.50
BuildRequires:  automake >= 1.11
BuildRequires:  libmysqlclient-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.21
BuildRequires:  sqlite3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libmnl) >= 1.0.3
BuildRequires:  pkgconfig(libnetfilter_acct) >= 1.0.1
BuildRequires:  pkgconfig(libnetfilter_conntrack) >= 1.0.2
BuildRequires:  pkgconfig(libnetfilter_log) >= 1.0.0
BuildRequires:  pkgconfig(libnfnetlink) >= 1.0.1
BuildRequires:  pkgconfig(libpq)
%sysusers_requires

%description
ulogd is a userspace logging daemon for netfilter/iptables related
logging. This includes per-packet logging of security violations,
per-packet logging for accounting purpose as well as per-flow
logging.

%package mysql
Summary:        MySQL output target for ulogd
Group:          Productivity/Networking/Security
Requires:       %name = %version-%release

%description mysql
MySQL output target for ulogd.

%package pcap
Summary:        pcap output target for ulogd
Group:          Productivity/Networking/Security
Requires:       %name = %version-%release

%description pcap
pcap output target for ulogd.

%package pgsql
Summary:        PostgreSQL output target for ulogd
Group:          Productivity/Networking/Security
Requires:       %name = %version-%release

%description pgsql
PostgreSQL output target for ulogd.

%package sqlite3
Summary:        SQLite3 output target for ulogd
Group:          Productivity/Networking/Security
Requires:       %name = %version-%release

%description sqlite3
SQLite3 output target for ulogd.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
%make_build
%sysusers_generate_pre %{SOURCE5} ulogd

%install
%make_install
b="%buildroot"
find "$b" -type f -iname "*.la" -delete
mkdir -p "$b/var/log/ulogd"
mkdir -p "$b/%_sysconfdir"
install -pm0644 ulogd.conf "$b/%_sysconfdir/"
mkdir -p "$b/%_unitdir"
install -pm0644 "%{S:4}" "$b/%_unitdir"
ln -s /sbin/service "$b/%_sbindir/rc%name"
mkdir -p "$b/%_sysusersdir"
install -m 644 %{SOURCE5} "$b/%_sysusersdir/"

%pre -f ulogd.pre
%service_add_pre ulogd.service

%post
%service_add_post ulogd.service

%preun
%service_del_preun ulogd.service

%postun
%service_del_postun ulogd.service

%files
%config(noreplace) %_sysconfdir/ulogd.conf
%_sbindir/ulogd
%dir %_libdir/%name
%_libdir/%name/ulogd_[fir]*.so*
%_libdir/%name/ulogd_output_GRAPHITE.so*
%_libdir/%name/ulogd_output_GPRINT.so*
%_libdir/%name/ulogd_output_LOGEMU.so*
%_libdir/%name/ulogd_output_NACCT.so*
%_libdir/%name/ulogd_output_OPRINT.so*
%_libdir/%name/ulogd_output_SYSLOG.so*
%_libdir/%name/ulogd_output_XML.so*
%_mandir/*/*
%attr(0750,ulogd,root) /var/log/ulogd
%_sysusersdir/ulogd.conf
%_unitdir/ulogd.service
%_sbindir/rc%name

# These are the dependency-heavy things:

%files mysql
%_libdir/%name/ulogd_output_MYSQL.so*

%files pcap
%_libdir/%name/ulogd_output_PCAP.so*

%files pgsql
%_libdir/%name/ulogd_output_PGSQL.so*

%files sqlite3
%_libdir/%name/ulogd_output_SQLITE3.so*

%changelog
