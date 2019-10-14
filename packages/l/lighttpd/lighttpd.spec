#
# spec file for package lighttpd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define pkg_home %{_localstatedir}/lib/%{name}
Name:           lighttpd
Version:        1.4.54
Release:        0
#
%define pkg_name %{name}
%define pkg_version %{version}
%define tarball_version %{version}
#
Summary:        A Secure, Fast, Compliant, and Very Flexible Web Server
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
URL:            https://www.lighttpd.net/
Source:         https://download.lighttpd.net/lighttpd/releases-1.4.x/%{name}-%{version}.tar.xz
Source1:        https://download.lighttpd.net/lighttpd/releases-1.4.x/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.sysconfig
Source3:        %{name}.keyring
Source4:        lightytest.sh
Source5:        lighttpd.SuSEfirewall
Source6:        lighttpd-ssl.SuSEfirewall
Source7:        lighttpd.logrotate
BuildRequires:  FastCGI-devel
BuildRequires:  GeoIP-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gamin-devel
BuildRequires:  gdbm-devel
BuildRequires:  iputils
BuildRequires:  krb5-devel
BuildRequires:  libattr-devel
BuildRequires:  libbz2-devel
BuildRequires:  libdbi-devel
BuildRequires:  libmemcached-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lua51-devel
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
%if 0%{?suse_version} > 1500
# pg_config moved to postgresql-server-devel in postgresql11* packages boo#1153722
BuildRequires:  postgresql-server-devel
%endif 
BuildRequires:  pwdutils
BuildRequires:  sqlite-devel >= 3
BuildRequires:  zlib-devel
BuildRequires:  perl(CGI)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(systemd)
Requires:       spawn-fcgi
Requires(post): %fillup_prereq
Requires(pre):  shadow
Recommends:     %{name}-mod_openssl = %{version}
Recommends:     logrotate
Provides:       http_daemon
Provides:       httpd
%{?systemd_requires}
%if 0%{?suse_version} >= 1330
BuildRequires:  php7-fastcgi
%else
BuildRequires:  php5-fastcgi
%endif

%description
Lighttpd is a secure, fast, compliant, and very flexible Web server
that has been optimized for high-performance environments. It has a
very low memory footprint compared to other Web servers and takes care
of CPU load. Its advanced feature set (FastCGI, CGI, Auth,
Output-Compression, URL-Rewriting, and more) makes lighttpd the perfect
Web server software for every server that is suffering load problems.

%package mod_cml
Summary:        CML (Cache Meta Language) module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_cml
CML is a Meta language to describe the dependencies of a page at one
side and building a page from its fragments on the oth er side using
LUA.

CML (Cache Meta Language) wants to solves several problems:

* dynamic content needs caching to perform

* checking if the content is dirty inside of the application is
   usually more expensive than sending out the cached data

* a dynamic page is usually fragmented and the fragments have
   different livetimes

* the different fragements can be cached independently

%package mod_magnet
Summary:        A module to control the request handling in lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_magnet
A module to control the request handling in lighttpd.

It is the successor of mod_cml.

%package mod_mysql_vhost
Summary:        MySQL based virtual hosts (vhosts) module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_mysql_vhost
With MySQL based vhosting you can put the information where to look for
a document-root of a given host into a MySQL database.

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

%package mod_trigger_b4_dl
Summary:        Another anti hot-linking module for Lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_trigger_b4_dl
Anti Hotlinking:

* if user requests download-url directly the request is denied and
   he is redirected to ''deny-url'

* if user visits trigger-url before requesting download-url access
   is granted

* if user visits download-url again after trigger-timeout has run
   down to the request is denied and he is redirected  to deny-url

The storage for the trigger information is either stored locally in a
gdbm file or remotly in memcached.

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

%package mod_geoip
Summary:        GeoIP legacy database support for Lighttp
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_geoip
This module supports fast ip/location lookups using the legacy
MaxMind GeoIP / GeoCity databases. The databases were
discontinued 2 January 2019 and this module is deprecated.
See %{name}-mod_maxminddb which supports MaxMind GeoIP2.

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
The WebDAV module is a very minimalistic implementation of RFC 2518.
Minimalistic means that not all operations are implementated yet..

So far we have:
* PROPFIND
* OPTIONS
* MKCOL
* DELETE
* PUT
and the usual GET, POST, HEAD from HTTP/1.1..

So far mounting a webdav resource into Windows XP works and the basic
litmus tests are passed.

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

%package mod_authn_mysql
Summary:        MySQL authentication in lighttpd
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description mod_authn_mysql
A module to provide MySQL authentication in lighttpd.

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
%setup -q -n %{pkg_name}-%{pkg_version}

%build
export CFLAGS="%{optflags} -DLDAP_DEPRECATED -W -Wmissing-prototypes -Wmissing-declarations -Wpointer-arith -Wchar-subscripts -Wformat=2 -Wbad-function-cast -std=gnu99 -fstack-protector"
%configure                      \
    --bindir=%{_sbindir}        \
    --libdir=%{_libdir}/%{name} \
    --with-libev                \
    --enable-lfs                \
    --enable-ipv6               \
    --with-pcre                 \
    --with-ldap                 \
    --with-pam                  \
    --with-dbi                  \
    --with-pgsql                \
    --with-mysql                \
    --with-openssl              \
    --with-krb5                 \
    --with-gdbm                 \
    --with-lua                  \
    --with-memcached            \
    --with-bzip2                \
    --with-webdav-props         \
    --with-webdav-locks         \
    --with-fam                  \
    --with-geoip                \
    --with-maxminddb            \
    --with-sasl                 \
    --with-attr
make %{?_smp_mflags}

%check
%if 0%{?suse_version} > 1200
export PHP="/srv/www/cgi-bin/php"
%else
export PHP="/srv/www/cgi-bin/php5"
%endif
sh -x %{SOURCE4}

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
# as much as i would like to use -delete here. sles9 doesnt understand it.
find %{buildroot}%{_sysconfdir}/%{name}/ -name Makefile\* -print0 | xargs -r0 rm -fv
#
# sysconfig template
#
install -D -m 0644 %{SOURCE2} \
    %{buildroot}%{_fillupdir}/sysconfig.%{name}
#
# susefirewall config file
#
install -D -m 0644 %{SOURCE5} \
    %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/lighttpd
install -D -m 0644 %{SOURCE6} \
    %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/lighttpd-ssl
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
chmod -x doc/scripts/spawn-php.sh doc/scripts/rrdtool-graph.sh

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
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/lighttpd*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sbindir}/*
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}/conf.d
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}/vhosts.d
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/lighttpd.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/modules.conf
# modules config
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/access_log.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/auth.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/cgi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/compress.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/debug.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/dirlisting.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/evhost.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/expire.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/fastcgi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/mime.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/mod.template
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/proxy.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/scgi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/secdownload.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/simple_vhost.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/ssi.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/status.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/userdir.conf
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/vhosts.d/vhosts.template
# modules
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/mod_access.so
%{_libdir}/%{name}/mod_accesslog.so
%{_libdir}/%{name}/mod_alias.so
%{_libdir}/%{name}/mod_auth.so
%{_libdir}/%{name}/mod_authn_file.so
%{_libdir}/%{name}/mod_cgi.so
%{_libdir}/%{name}/mod_compress.so
%{_libdir}/%{name}/mod_deflate.so
%{_libdir}/%{name}/mod_dirlisting.so
%{_libdir}/%{name}/mod_evasive.so
%{_libdir}/%{name}/mod_evhost.so
%{_libdir}/%{name}/mod_expire.so
%{_libdir}/%{name}/mod_extforward.so
%{_libdir}/%{name}/mod_fastcgi.so
%{_libdir}/%{name}/mod_flv_streaming.so
%{_libdir}/%{name}/mod_indexfile.so
%{_libdir}/%{name}/mod_openssl.so
%{_libdir}/%{name}/mod_proxy.so
%{_libdir}/%{name}/mod_redirect.so
%{_libdir}/%{name}/mod_rewrite.so
%{_libdir}/%{name}/mod_scgi.so
%{_libdir}/%{name}/mod_secdownload.so
%{_libdir}/%{name}/mod_setenv.so
%{_libdir}/%{name}/mod_simple_vhost.so
%{_libdir}/%{name}/mod_ssi.so
%{_libdir}/%{name}/mod_staticfile.so
%{_libdir}/%{name}/mod_sockproxy.so
%{_libdir}/%{name}/mod_status.so
%{_libdir}/%{name}/mod_uploadprogress.so
%{_libdir}/%{name}/mod_userdir.so
%{_libdir}/%{name}/mod_usertrack.so
%{_libdir}/%{name}/mod_vhostdb.so
%{_libdir}/%{name}/mod_wstunnel.so
%{_mandir}/man8/*.8%{?ext_man}
%doc AUTHORS NEWS README
#doc doc/*.dot
%doc doc/scripts/spawn-php.sh
%doc doc/outdated/accesslog.txt
%doc doc/outdated/access.txt
%doc doc/outdated/alias.txt
%doc doc/outdated/authentication.txt
%doc doc/outdated/cgi.txt
%doc doc/outdated/compress.txt
%doc doc/outdated/configuration.txt
%doc doc/outdated/expire.txt
%doc doc/outdated/fastcgi-state.txt
%doc doc/outdated/fastcgi.txt
%doc doc/outdated/features.txt
%doc doc/outdated/performance.txt
%doc doc/outdated/plugins.txt
%doc doc/outdated/proxy.txt
%doc doc/outdated/redirect.txt
%doc doc/outdated/rewrite.txt
%doc doc/outdated/scgi.txt
%doc doc/outdated/secdownload.txt
%doc doc/outdated/security.txt
%doc doc/outdated/setenv.txt
%doc doc/outdated/simple-vhost.txt
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

%files mod_cml
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/cml.conf
%{_libdir}/%{name}/mod_cml.so
%doc doc/outdated/cml.txt

%files mod_magnet
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/magnet.conf
%{_libdir}/%{name}/mod_magnet.so
%doc doc/outdated/magnet.txt

%files mod_mysql_vhost
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/mysql_vhost.conf
%{_libdir}/%{name}/mod_mysql_vhost.so
%doc doc/outdated/mysqlvhost.txt

%files mod_vhostdb_dbi
%{_libdir}/%{name}/mod_vhostdb_dbi.so

%files mod_vhostdb_ldap
%{_libdir}/%{name}/mod_vhostdb_ldap.so

%files mod_vhostdb_mysql
%{_libdir}/%{name}/mod_vhostdb_mysql.so

%files mod_vhostdb_pgsql
%{_libdir}/%{name}/mod_vhostdb_pgsql.so

%files mod_trigger_b4_dl
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/trigger_b4_dl.conf
%{_libdir}/%{name}/mod_trigger_b4_dl.so
%doc doc/outdated/trigger_b4_dl.txt

%files mod_rrdtool
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/rrdtool.conf
%doc doc/outdated/rrdtool.txt
%doc doc/scripts/rrdtool-graph.sh
%{_libdir}/%{name}/mod_rrdtool.so

%files mod_geoip
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/geoip.conf
%{_libdir}/%{name}/mod_geoip.so

%files mod_maxminddb
%{_libdir}/%{name}/mod_maxminddb.so

%files mod_webdav
%config(noreplace) %attr(640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/webdav.conf
%{_libdir}/%{name}/mod_webdav.so
%doc doc/outdated/webdav.txt

%files mod_authn_gssapi
%{_libdir}/%{name}/mod_authn_gssapi.so

%files mod_authn_ldap
%{_libdir}/%{name}/mod_authn_ldap.so

%files mod_authn_mysql
%{_libdir}/%{name}/mod_authn_mysql.so

%files mod_authn_sasl
%{_libdir}/%{name}/mod_authn_sasl.so

%files mod_authn_pam
%{_libdir}/%{name}/mod_authn_pam.so

%changelog
