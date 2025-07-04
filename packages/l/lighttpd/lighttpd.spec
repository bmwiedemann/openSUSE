#
# spec file for package lighttpd
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define pkg_home %{_localstatedir}/lib/%{name}
#
%define pkg_name %{name}
%define pkg_version %{version}
%define tarball_version %{version}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           lighttpd
Version:        1.4.79
Release:        0
Summary:        A Secure, Fast, Compliant, and Very Flexible Web Server
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
URL:            https://www.lighttpd.net/
Source:         https://download.lighttpd.net/lighttpd/releases-1.4.x/%{name}-%{version}.tar.xz
Source1:        https://download.lighttpd.net/lighttpd/releases-1.4.x/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.sysconfig
Source3:        %{name}.keyring
Source7:        lighttpd.logrotate
BuildRequires:  autoconf
BuildRequires:  iputils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  shadow
BuildRequires:  perl(CGI)
BuildRequires:  pkgconfig(dbi)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Requires:       spawn-fcgi
Requires(post): %fillup_prereq
Requires(pre):  shadow
Recommends:     %{name}-mod_openssl = %{version}
Recommends:     logrotate
Provides:       http_daemon
Provides:       httpd
Provides:       group(%{name})
Provides:       user(%{name})
%{?systemd_requires}
%if 0%{?suse_version} <= 1600 && 0%{?is_opensuse}
BuildRequires:  libattr-devel
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
%else
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(mysqlclient)
BuildRequires:  pkgconfig(pam)
%endif
%if 0%{?suse_version} > 1500
# pg_config moved to postgresql-server-devel in postgresql11* packages boo#1153722
BuildRequires:  postgresql-server-devel
%endif

%description
Lighttpd is a secure, fast, compliant, and very flexible Web server
that has been optimized for high-performance environments. It has a
very low memory footprint compared to other Web servers and takes care
of CPU load. Its advanced feature set (FastCGI, CGI, Auth,
Output-Compression, URL-Rewriting, and more) makes lighttpd the perfect
Web server software for every server that is suffering load problems.

%package mod_magnet
Summary:        A module to control the request handling in lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_magnet
A module to control the request handling in lighttpd.

It is the successor of mod_cml.

%package mod_vhostdb_dbi
Summary:        DBI based virtual hosts module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_vhostdb_dbi
With DBI based vhosting you can put the information where to look for
the document-root of a given host into any DBI supported database.

%package mod_vhostdb_ldap
Summary:        LDAP based virtual hosts module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_vhostdb_ldap
With LDAP based vhosting you can put the information where to look for
the document-root of a given host into an LDAP database.

%package mod_vhostdb_mysql
Summary:        MySQL based virtual hosts module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_vhostdb_mysql
With MySQL based vhosting you can put the information where to look for
the document-root of a given host into a MySQL database.

%package mod_vhostdb_pgsql
Summary:        PostgreSQL based virtual hosts module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_vhostdb_pgsql
With PostgreSQL based vhosting you can put the information where to look
for the document-root of a given host into a PostgreSQL database.

%package mod_rrdtool
Summary:        Lighttpd module to feed rrdtool databases
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Requires:       rrdtool

%description mod_rrdtool
RRD_tool is a system to store and display time-series data (i.e.
network bandwidth, machine-room temperature, server load average).

This module feeds an rrdtool database with the traffic stats from
lighttpd.

%package mod_maxminddb
Summary:        MaxMind GeoIP2 database support for Lighttp
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_maxminddb
This module supports fast ip/location lookups using MaxMind
GeoIP2 databases.

%package mod_webdav
Summary:        WebDAV module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_webdav
A WebDAV implementation designed to be fast and compliant to RFC 4918.

%package mod_authn_gssapi
Summary:        GSSAPI authentication in lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_authn_gssapi
A module to provide GSSAPI authentication in lighttpd.

%package mod_authn_ldap
Summary:        LDAP authentication in lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_authn_ldap
A module to provide LDAP authentication in lighttpd.

%package mod_authn_sasl
Summary:        SASL authentication in lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_authn_sasl
A module to provide SASL authentication in lighttpd.

%package mod_authn_pam
Summary:        PAM authentication in lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_authn_pam
A module to provide PAM authentication in lighttpd.

%prep
%autosetup -p1 -n %{pkg_name}-%{pkg_version}

%build
export CFLAGS="%{optflags} -W -Wmissing-prototypes -Wmissing-declarations -Wpointer-arith -Wchar-subscripts -Wformat=2 -Wbad-function-cast -std=gnu99 -fstack-protector"
autoreconf -fiv
%configure                      \
    --bindir=%{_sbindir}        \
    --libdir=%{_libdir}/%{name} \
    --enable-ipv6               \
    --with-ldap                 \
    --with-pam                  \
    --with-dbi                  \
    --with-pgsql                \
    --with-mysql                \
    --with-openssl              \
    --with-krb5                 \
    --with-lua                  \
    --with-zstd                 \
    --with-brotli               \
    --with-webdav-props         \
    --with-webdav-locks         \
    --with-maxminddb            \
    --with-sasl                 \
    --with-attr
%make_build

%check
%make_build check

%install
%make_install
install -d -m 0755                                 \
    %{buildroot}%{pkg_home}/sockets/               \
    %{buildroot}%{_var}/cache/%{name}/compress     \
    %{buildroot}%{_var}/log/%{name}                \
    %{buildroot}%{_sysconfdir}/%{name}
# systemd service
install -D -m 0644 doc/systemd/lighttpd.service %{buildroot}%{_unitdir}/%{name}.service
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
#
# sample config
#
perl -p -i.orig -e 's|^(server\.tag = ).*$|$1 "%{name} (%{version}/SuSE)"|' doc/config/lighttpd.conf
diff -ur doc/config/lighttpd.conf{.orig,} ||:
rm -vf doc/config/lighttpd.conf.orig ||:
cp -rv doc/config/* %{buildroot}%{_sysconfdir}/%{name}/
find %{buildroot}%{_sysconfdir}/%{name}/ -name Makefile\* -delete
#
# sysconfig template
#
install -D -m 0644 %{SOURCE2} \
    %{buildroot}%{_fillupdir}/sysconfig.%{name}
#
# logrotate config
#
install -D -m 0644 %{SOURCE7} \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
#
# remove the .la files. we dont need them.
#
find %{buildroot} -type f -name "*.la" -delete -print
# remove executable bit from doc scripts to avoid pulling dependencies
chmod -v -x doc/scripts/*.sh

%pre
%{_sbindir}/groupadd -r %{name} >/dev/null 2>&1 ||:
%{_sbindir}/useradd  -g %{name} -s /bin/false -r -c "user for %{name}" -d %{pkg_home} %{name} >/dev/null 2>&1 ||:
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%{_sbindir}/*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}/conf.d
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}/vhosts.d
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/lighttpd.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/lighttpd.annotated.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/modules.conf
# modules config
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/access_log.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/auth.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/cgi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/debug.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/deflate.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/dirlisting.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/evhost.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/expire.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/fastcgi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/mime.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/mod.template
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/proxy.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/scgi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/simple_vhost.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/ssi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/status.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/tls.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/userdir.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/vhosts.d/vhosts.template

# modules
%license COPYING
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/mod_accesslog.so
%{_libdir}/%{name}/mod_auth.so
%{_libdir}/%{name}/mod_authn_file.so
%{_libdir}/%{name}/mod_cgi.so
%{_libdir}/%{name}/mod_deflate.so
%{_libdir}/%{name}/mod_dirlisting.so
%{_libdir}/%{name}/mod_extforward.so
%{_libdir}/%{name}/mod_h2.so
%{_libdir}/%{name}/mod_openssl.so
%{_libdir}/%{name}/mod_proxy.so
%{_libdir}/%{name}/mod_ssi.so
%{_libdir}/%{name}/mod_sockproxy.so
%{_libdir}/%{name}/mod_status.so
%{_libdir}/%{name}/mod_userdir.so
%{_libdir}/%{name}/mod_vhostdb.so
%{_libdir}/%{name}/mod_wstunnel.so
%{_libdir}/%{name}/mod_authn_dbi.so
%{_libdir}/%{name}/mod_ajp13.so
%{_mandir}/man8/*.8%{?ext_man}
%doc AUTHORS NEWS README
#doc doc/*.dot
%doc doc/outdated/accesslog.txt
%doc doc/outdated/authentication.txt
%doc doc/outdated/cgi.txt
%doc doc/outdated/configuration.txt
%doc doc/outdated/fastcgi-state.txt
%doc doc/outdated/features.txt
%doc doc/outdated/performance.txt
%doc doc/outdated/plugins.txt
%doc doc/outdated/proxy.txt
%doc doc/outdated/security.txt
%doc doc/outdated/skeleton.txt
%doc doc/outdated/ssi.txt
%doc doc/outdated/ssl.txt
%doc doc/outdated/state.txt
%doc doc/outdated/status.txt
%doc doc/outdated/traffic-shaping.txt
%doc doc/outdated/userdir.txt
%{_fillupdir}/sysconfig.%{name}
%dir %attr(751,%{name},%{name}) %{pkg_home}/
%dir %attr(751,%{name},%{name}) %{pkg_home}/sockets/
%attr(751,%{name},%{name}) %{_var}/cache/%{name}/
%dir %attr(750,%{name},%{name}) %{_var}/log/%{name}/

%files mod_magnet
%license COPYING
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/magnet.conf
%{_libdir}/%{name}/mod_magnet.so
%doc doc/outdated/magnet.txt

%files mod_vhostdb_dbi
%license COPYING
%{_libdir}/%{name}/mod_vhostdb_dbi.so

%files mod_vhostdb_ldap
%license COPYING
%{_libdir}/%{name}/mod_vhostdb_ldap.so

%files mod_vhostdb_mysql
%license COPYING
%{_libdir}/%{name}/mod_vhostdb_mysql.so

%files mod_vhostdb_pgsql
%license COPYING
%{_libdir}/%{name}/mod_vhostdb_pgsql.so

%files mod_rrdtool
%license COPYING
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/rrdtool.conf
%doc doc/outdated/rrdtool.txt
%doc doc/scripts/rrdtool-graph.sh
%{_libdir}/%{name}/mod_rrdtool.so

%files mod_maxminddb
%license COPYING
%{_libdir}/%{name}/mod_maxminddb.so

%files mod_webdav
%license COPYING
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/webdav.conf
%{_libdir}/%{name}/mod_webdav.so
%doc doc/outdated/webdav.txt

%files mod_authn_gssapi
%license COPYING
%{_libdir}/%{name}/mod_authn_gssapi.so

%files mod_authn_ldap
%license COPYING
%{_libdir}/%{name}/mod_authn_ldap.so

%files mod_authn_sasl
%license COPYING
%{_libdir}/%{name}/mod_authn_sasl.so

%files mod_authn_pam
%license COPYING
%{_libdir}/%{name}/mod_authn_pam.so

%changelog
