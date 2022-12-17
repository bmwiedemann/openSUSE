#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global upstream_name   httpd
%global testsuite_name  %{upstream_name}-framework
%global tversion        svn1901574
%global flavor          @BUILD_FLAVOR@%{nil}
%define mpm             %{nil}
%if "%{flavor}" == "prefork" || "%{flavor}" == "test_prefork"
%define mpm             prefork
%endif
%if "%{flavor}" == "worker" || "%{flavor}" == "test_worker"
%define mpm             worker
%endif
%if "%{flavor}" == "event" || "%{flavor}" == "test_event"
%define mpm             event
%endif
%define test            0
%define unittest        0
%if "%{flavor}" == "test_prefork" || "%{flavor}" == "test_worker" || "%{flavor}" == "test_event" || "%{flavor}" == "test_devel" || "%{flavor}" == "test_main"
%define test            1
%if "%{flavor}" == "test_prefork" || "%{flavor}" == "test_worker" || "%{flavor}" == "test_event"
%define unittest        1
%endif
%endif
%if "%{mpm}" == "prefork"
%define mpm_alt_prio    10
%endif
%if "%{mpm}" == "worker"
%define mpm_alt_prio    20
%endif
%if "%{mpm}" == "event"
%define mpm_alt_prio    30
%endif
%define default_mpm     prefork
%define suse_maintenance_mmn  0
%define apache_mmn      %(test -s %{SOURCE0} && \
                          { echo -n apache_mmn_; bzcat %{SOURCE0} | \
                            awk '/^#define MODULE_MAGIC_NUMBER_MAJOR/ {printf "%d", $3}'; } || \
                          echo apache_mmn_notfound)
%define static_modules  unixd systemd
%define dynamic_modules authz_core access_compat actions alias allowmethods asis auth_basic auth_digest \\\
                        auth_form authn_anon authn_core authn_dbd authn_dbm authn_file authn_socache authnz_ldap \\\
                        authnz_fcgi authz_core authz_dbd authz_dbm authz_groupfile authz_host authz_owner authz_user \\\
                        autoindex bucketeer buffer cache cache_disk cache_socache case_filter case_filter_in cgid cgi \\\
                        charset_lite data dav dav_fs dav_lock dbd deflate brotli dialup dir dumpio echo env expires \\\
                        ext_filter file_cache filter headers heartmonitor http2 imagemap include info lbmethod_bybusyness \\\
                        lbmethod_byrequests lbmethod_bytraffic lbmethod_heartbeat ldap log_config log_debug log_forensic \\\
                        logio lua macro mime mime_magic negotiation optional_fn_export optional_fn_import \\\
                        optional_hook_export optional_hook_import proxy proxy_ajp proxy_balancer proxy_connect \\\
                        proxy_express proxy_fcgi proxy_fdpass proxy_ftp proxy_hcheck proxy_html proxy_http proxy_http2 \\\
                        proxy_scgi proxy_uwsgi proxy_wstunnel ratelimit reflector remoteip reqtimeout request rewrite \\\
                        sed session session_cookie session_crypto session_dbd setenvif slotmem_plain slotmem_shm \\\
                        socache_dbm socache_memcache socache_redis socache_shmcb speling ssl status substitute suexec \\\
                        unique_id userdir usertrack version vhost_alias watchdog xml2enc
%define support_bin     ab check_forensic dbmmanage find_directives gensslcert htdbm htdigest htpasswd httxt2dbm \\\
                        log_server_status logresolve split-logfile
%define support_sbin    apachectl htcacheclean fcgistarter logresolve.pl rotatelogs

%define platform_string Linux/SUSE
%define httpduser       wwwrun
%define httpdgroup      www

%define datadir         /srv/www
%define htdocsdir       %{datadir}/htdocs
%define manualdir       %{_datadir}/apache2/manual
%define errordir        %{_datadir}/apache2/error
%define iconsdir        %{_datadir}/apache2/icons
%define cgidir          %{datadir}/cgi-bin
%define localstatedir   %{_localstatedir}/lib/apache2
%define runtimedir      /run
%define proxycachedir   %{_localstatedir}/cache/apache2
%define logfiledir      %{_localstatedir}/log/apache2
%define sysconfdir      %{_sysconfdir}/apache2
%define includedir      %{_includedir}/apache2
%if "%{mpm}" != ""
%define libexecdir      %{_libdir}/apache2-%{mpm}
%else
%define libexecdir      %{_libdir}/apache2
%endif
%define installbuilddir %{_datadir}/apache2/build
%define userdir         public_html

%define suexec_safepath %{_prefix}/local/bin:%{_prefix}/bin:/bin

%define psuffix       %{nil}
%if "%{flavor}" != ""
%define psuffix      -%{flavor}
%endif

%define use_firewalld 1
%define build_http2 1

Name:           apache2%{psuffix}
Version:        2.4.54
Release:        0
Summary:        The Apache HTTPD Server
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://httpd.apache.org/
# essential sources
Source0:        https://www.apache.org/dist/httpd/%{upstream_name}-%{version}.tar.bz2
Source1:        https://www.apache.org/dist/httpd/%{upstream_name}-%{version}.tar.bz2.asc
Source2:        apache2.keyring
Source3:        apache2.service
Source4:        apache2@.service
Source5:        apache2.target
# Add file to take mtime from it in prep section
Source6:        apache2.changes
Source10:       apache2-ssl-dirs.tar.bz2
# test
# svn checkout http://svn.apache.org/repos/asf/httpd/test/framework/trunk/ httpd-framework
Source20:       %{testsuite_name}-%{tversion}.tar.bz2
Source21:       apache2-mod_example.c
# integration settings
Source30:       sysconfig.apache2
Source31:       logrotate.apache2
Source32:       permissions.apache2
Source33:       firewalld.apache2
Source34:       firewalld-ssl.apache2
Source35:       susefirewall.apache2
Source36:       susefirewall-ssl.apache2
# scripts
Source100:      apache2-a2enmod
Source101:      apache2-a2enflag
Source102:      apache2-systemd-ask-pass
Source103:      apache2-start_apache2
Source104:      apache2-script-helpers
# additional support
Source130:      apache2-gensslcert
Source131:      apache2-check_forensic
Source132:      apache2-find_directives
# configuration
Source150:      apache2-httpd.conf
Source151:      apache2-errors.conf
Source152:      apache2-default-server.conf
Source153:      apache2-listen.conf
Source154:      apache2-manual.conf
Source155:      apache2-mod_autoindex-defaults.conf
Source156:      apache2-mod_info.conf
Source157:      apache2-mod_log_config.conf
Source158:      apache2-mod_mime-defaults.conf
Source159:      apache2-mod_status.conf
Source160:      apache2-mod_userdir.conf
Source161:      apache2-server-tuning.conf
Source163:      apache2-ssl-global.conf
Source164:      apache2-mod_usertrack.conf
Source165:      apache2-mod_reqtimeout.conf
Source166:      apache2-loadmodule.conf
Source167:      apache2-global.conf
Source168:      apache2-mod_cgid-timeout.conf
Source169:      apache2-protocols.conf
Source190:      apache2-vhost.template
Source191:      apache2-vhost-ssl.template
# READMEs and other documentation
Source200:      apache2-README-access_compat.txt
Source201:      apache2-README-instances.txt
Source202:      apache2-README-configuration.txt
# layout of system dirs configuration, may be upstreamed
Patch0:         apache2-system-dirs-layout.patch
# apachectl is frontend for start_apache2, suse specific
Patch1:         apache2-apachectl.patch
# [bnc#210904] perhaps to be upstreamed
Patch2:         apache2-logresolve-tmp-security.patch
# [bnc#690734] TODO, to be upstreamed
Patch3:         apache2-LimitRequestFieldSize-limits-headers.patch
# [fate317766] backport of an upstream commit
Patch4:         apache2-HttpContentLengthHeadZero-HttpExpectStrict.patch
# PATCH:  https://marc.info/?l=apache-httpd-users&m=147448312531134&w=2
Patch100:       apache-test-application-xml-type.patch
# PATCH:  /test_ssl_var_lookup?SSL_SERVER_SAN_DNS_0 returns <build-host-name>
#         /test_ssl_var_lookup?SSL_SERVER_SAN_OTHER_dnsSRV_0 _https.<build-host-name>
# but Apache::Test::vars()->{servername} returns 'localhost' instead of <build-host-name>
# (see $san_dns and $san_dnssrv variables in t/ssl/varlookup.t)
# even if in live system I do not experience this inconsistency, let's turn off
# these variables from the test
Patch101:       apache-test-turn-off-variables-in-ssl-var-lookup.patch
BuildRequires:  apache-rpm-macros-control
#Since 2.4.7 the event MPM requires apr 1.5.0 or later.
BuildRequires:  apr-devel >= 1.5.0
BuildRequires:  apr-util-devel
BuildRequires:  automake
# for basic testing
BuildRequires:  curl
BuildRequires:  db-devel
%if %{use_firewalld}
BuildRequires:  firewall-macros
%endif
BuildRequires:  libbrotli-devel
%if %{build_http2}
BuildRequires:  pkgconfig(libnghttp2) >= 1.2.1
%endif
BuildRequires:  libcap-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel >= 0.9.8a
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
# SECTION test requirements
%if %{test}
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2
BuildRequires:  apache2-devel
BuildRequires:  apache2-manual
BuildRequires:  apache2-utils
%endif
%if "%{flavor}" == "test_prefork"
BuildRequires:  apache2-prefork
%endif
%if "%{flavor}" == "test_worker"
BuildRequires:  apache2-worker
%endif
%if "%{flavor}" == "test_event"
BuildRequires:  apache2-event
%endif
%if %{unittest}
# perl-doc is assumed by t/filter/case.t (/usr/lib/perl5/*/pod/perlsub.pod)
BuildRequires:  perl-doc
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Devel::CoreStack)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTTP::DAV)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::Cmd)
BuildRequires:  perl(URI)
%if %{build_http2}
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Protocol::HTTP2::Client)
%endif
BuildRequires:  netcfg
%endif
# /SECTION
%if "%{mpm}" != ""
Provides:       apache2-MPM
%endif
%if "%{flavor}" == ""
Requires:       %{_sysconfdir}/mime.types
Requires:       apache2-MPM
Suggests:       apache2-%{default_mpm}
Recommends:     apache2-utils
Requires:       logrotate
Provides:       %{apache_mmn}
Provides:       http_daemon
Provides:       httpd
Provides:       suse_maintenance_mmn_%{suse_maintenance_mmn}
Obsoletes:      apache2-example-pages
Requires(pre):  group(www)
Requires(pre):  user(wwwrun)
%{?systemd_ordering}
%endif
%if "%{flavor}" == "utils"
Requires:       /usr/bin/which
Recommends:     w3m
%endif
%if "%{flavor}" == "devel"
Requires:       apache2 = %{version}
Requires:       apr-devel
Requires:       apr-util-devel
Requires:       gcc
Provides:       httpd-devel = %{version}
%endif
%if "%{flavor}" == "manual"
Provides:       apache2-doc = %{version}
Obsoletes:      apache2-doc <= %{version}
%endif
%if "%{mpm}" != ""
Requires(pre):  permissions
Requires(post): %fillup_prereq
Requires(post): grep
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%if %{test} || "%{flavor}" == "manual"
BuildArch:      noarch
%endif

%description
The Apache HTTP Server Project is an effort to develop and
maintain an open-source HTTP server for modern operating
systems including UNIX and Windows. The goal of this project
is to provide a secure, efficient and extensible server that
provides HTTP services in sync with the current HTTP standards.

%prep
%setup -q -n %{upstream_name}-%{version} -a20
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch100 -p1
%patch101 -p1

#
# BUILD
#

%if ! %{test} && "%{flavor}" != "manual"
%build
echo "================== BUILDING [%{flavor}] flavor"
# configuration (autoreconf, configure) common for all flavors,
# except test and manual

autoreconf --force --install --verbose

# replace PLATFORM string that's seen in the "Server:" header
sed -i -e 's,(" PLATFORM "),(%{platform_string}),' server/core.c
# use mtime of .changes for build time
CHANGES_MTIME=`stat --format="%%y" %{SOURCE6}`
sed -i -e "s/__DATE__ \" \" __TIME__;/\"$CHANGES_MTIME\";/" server/buildmark.c

export CFLAGS="%{optflags} -fPIC -Wall
               -DLDAP_DEPRECATED -DDEFAULT_LISTENBACKLOG=APR_INT32_MAX -DDEFAULT_ERRORLOG='\"%{logfiledir}/error_log\"'"
export CPPFLAGS="%{optflags} -DSSL_EXPERIMENTAL_ENGINE -DMAX_SERVER_LIMIT=200000 -DLDAP_DEPRECATED -DMAXLINE=4096"
cat > config.layout <<-EOF
# SUSE Layout
<Layout SUSE>
Prefix:         %{datadir}
    exec_prefix:   %{_prefix}
    bindir:        %{_bindir}
    sbindir:       %{_sbindir}
    libdir:        %{_libdir}
    libexecdir:    %{libexecdir}
    mandir:        %{_mandir}
    sysconfdir:    %{sysconfdir}
    datadir:       %{datadir}
    installbuilddir: %{installbuilddir}
    errordir:      %{errordir}
    iconsdir:      %{iconsdir}
    htdocsdir:     %{htdocsdir}
    manualdir:     %{manualdir}
    cgidir:        %{cgidir}
    includedir:    %{includedir}
    localstatedir: %{localstatedir}
    runtimedir:    %{runtimedir}
    logfiledir:    %{logfiledir}
    proxycachedir: %{proxycachedir}
</Layout>
EOF
# %%configure (e. g --libexecdir) switches override
# layout paths (use layout because some of variables
# there does not exist as configure switches), so
# override them back
%configure \
        --prefix=%{datadir} \
        --libexecdir=%{libexecdir} \
        --includedir=%{includedir} \
        --sysconfdir=%{sysconfdir} \
        --enable-layout=SUSE \
        --libexecdir=%{libexecdir} \
%if "%{mpm}" != ""
        --with-program-name=httpd-%{mpm} \
%endif
        --with-apr=%{_bindir}/apr-1-config \
        --with-apr-util=%{_bindir}/apu-1-config \
%if "%{mpm}" != ""
        --with-mpm="%{mpm}" \
%endif
%if "%{mpm}" == "worker" || "%{mpm}" == "event"
%ifarch %ix86
%ifnarch i386
                --enable-nonportable-atomics=yes \
%endif
%endif
%endif
        --enable-exception-hook \
        --with-pcre \
        --enable-pie \
        --enable-mods-shared=all \
        --enable-mods-static="%{static_modules}" \
        --enable-ssl=shared \
        --disable-isapi \
        --enable-deflate \
        --enable-brotli \
        --enable-echo \
        --enable-filter \
        --enable-ext-filter \
        --enable-charset-lite \
        --enable-file-cache \
        --enable-logio \
        --enable-dumpio \
        --enable-bucketeer \
        --enable-case_filter \
        --enable-case_filter_in \
        --enable-imagemap \
%if %{build_http2}
        --enable-http2 \
%endif
        --with-ldap \
        --enable-ldap \
        --enable-authnz_ldap \
        --enable-authnz-fcgi \
        --enable-proxy \
        --enable-proxy-connect \
        --enable-proxy-ftp \
        --enable-proxy-http \
%if %{build_http2}
        --enable-proxy-http2 \
%endif
        --enable-proxy-fdpass \
        --enable-cache \
        --enable-disk-cache \
        --enable-mem-cache \
        --enable-version \
        --enable-dav-lock \
        --enable-authn-alias \
        --enable-optional-hook-export \
        --enable-optional-hook-import \
        --enable-optional-fn-import \
        --enable-optional-fn-export \
        --enable-suexec \
        --with-suexec-bin=%{_sbindir}/suexec \
        --with-suexec-caller=%{httpduser} \
        --with-suexec-docroot=%{datadir} \
        --with-suexec-logfile=%{logfiledir}/suexec.log \
        --with-suexec-userdir=%{userdir} \
        --with-suexec-uidmin=96 \
        --with-suexec-gidmin=96 \
        --with-suexec-safepath=%{suexec_safepath} \
        --disable-heartbeat

# MPMs build
%if "%{mpm}" != ""
# adjust SERVER_CONFIG_FILE
sed -i "s:httpd-%{mpm}.conf:httpd.conf:" include/ap_config_auto.h
make %{?_smp_mflags}
%endif

# main package build
%if "%{flavor}" == ""
pushd support
make %{?_smp_flags} suexec
popd
%endif

# utils build
%if "%{flavor}" == "utils"
pushd support
make %{?_smp_mflags}
cp %{SOURCE130} gensslcert
cp %{SOURCE131} check_forensic
cp %{SOURCE132} find_directives
popd
%endif
%endif

#
# INSTALL
#

%if ! %{test}
%install
echo "================== INSTALLING [%{flavor}] flavor"

# MPMs install
%if "%{mpm}" != ""
# install httpd binary
make DESTDIR=%{buildroot} program-install
# install modules
pushd modules
make DESTDIR=%{buildroot} install -j1
popd
# install alternative links (httpd binary, modules)
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/httpd %{buildroot}%{_sbindir}/httpd
mkdir -p %{buildroot}%{_libdir}/apache2/
for module in %{dynamic_modules}; do
  if [ -e %{buildroot}%{libexecdir}/mod_$module.so ]; then
    ln -sf %{_sysconfdir}/alternatives/mod_$module.so %{buildroot}%{_libdir}/apache2/mod_$module.so
  fi
done
%endif

# main packge install
%if "%{flavor}" == ""
mkdir -p %{buildroot}%{logfiledir} \
         %{buildroot}%{proxycachedir} \
         %{buildroot}%{localstatedir} \
         %{buildroot}%{libexecdir}

# save MODULE_MAGIC_NUMBER
mkdir -p %{buildroot}/%{_libexecdir}
cat > %{buildroot}/%{_libexecdir}/apache2_MMN <<-EOF
#!/bin/sh
echo %{apache_mmn}
EOF

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -m 644 %{SOURCE31} %{buildroot}/%{_distconfdir}/logrotate.d/apache2
%else
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE31} %{buildroot}/%{_sysconfdir}/logrotate.d/apache2
%endif

make DESTDIR=%{buildroot} install-suexec -j1

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/apache2.service
install -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/apache2@.service
install -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/apache2.target
ln -sf service %{buildroot}/%{_sbindir}/rcapache2

install -m 700 %{SOURCE102} %{buildroot}%{_sbindir}/apache2-systemd-ask-pass

install -m 755 %{SOURCE100} %{buildroot}%{_sbindir}/a2enmod
ln -s a2enmod %{buildroot}%{_sbindir}/a2dismod
install -m 755 %{SOURCE101} %{buildroot}%{_sbindir}/a2enflag
ln -s a2enflag %{buildroot}%{_sbindir}/a2disflag
install -m 744 %{SOURCE103} %{buildroot}%{_sbindir}/start_apache2
mkdir -p %{buildroot}/%{_datadir}/apache2/
install -m 644 %{SOURCE104} %{buildroot}/%{_datadir}/apache2/script-helpers

%if %{use_firewalld}
install -D -m 644 %{SOURCE33} %{buildroot}%{_prefix}/lib/firewalld/services/apache2.xml
install -D -m 644 %{SOURCE34} %{buildroot}%{_prefix}/lib/firewalld/services/apache2-ssl.xml
%else
install -d %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/
install -m 644 %{SOURCE35} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/apache2
install -m 644 %{SOURCE36} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/apache2-ssl
%endif

mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/apache2/sysconfig.d

mkdir -p %{buildroot}/%{_fillupdir}
install -m 644 %{SOURCE30} %{buildroot}%{_fillupdir}/sysconfig.apache2

mkdir -p %{buildroot}%{sysconfdir}
mkdir -p %{buildroot}%{sysconfdir}/conf.d
for c in default-server.conf \
         errors.conf \
         global.conf \
         httpd.conf \
         listen.conf \
         loadmodule.conf \
         mod_autoindex-defaults.conf \
         mod_info.conf \
         mod_log_config.conf \
         mod_mime-defaults.conf \
         mod_status.conf \
         mod_userdir.conf \
         mod_usertrack.conf \
         server-tuning.conf \
         mod_reqtimeout.conf \
         mod_cgid-timeout.conf \
         ssl-global.conf \
         protocols.conf
do
        install -m 644 %{_sourcedir}/apache2-$c %{buildroot}/%{sysconfdir}/$c
done
cat > %{buildroot}/%{sysconfdir}/uid.conf <<-EOF
        User %{httpduser}
        Group %{httpdgroup}
EOF
tar -xjf %{SOURCE10} -C %{buildroot}/%{sysconfdir}
# fixup libdir
%if "%{_lib}" != "lib64"
sed -e 's/lib64/%{_lib}/' -i \
  %{buildroot}/%{sysconfdir}/loadmodule.conf \
  %{buildroot}/%{_fillupdir}/sysconfig.apache2
%endif
mkdir %{buildroot}/%{sysconfdir}/vhosts.d
install -m 644 %{SOURCE190} %{buildroot}/%{sysconfdir}/vhosts.d/vhost.template
install -m 644 %{SOURCE191} %{buildroot}/%{sysconfdir}/vhosts.d/vhost-ssl.template
install -m 644 docs/conf/charset.conv %{buildroot}/%{sysconfdir}/
install -m 644 docs/conf/magic %{buildroot}/%{sysconfdir}/
ln -sf ../mime.types %{buildroot}/%{sysconfdir}/mime.types

make DESTDIR=%{buildroot} install-icons
make DESTDIR=%{buildroot} install-error
make DESTDIR=%{buildroot} sysconfdir=%{_docdir}/apache2/conf install-conf

cp -r docs/server-status %{buildroot}%{_datadir}/apache2/lua-server-status

mkdir -p %{buildroot}%{_mandir}/man8/
install -D -m 644 docs/man/suexec.8 %{buildroot}%{_mandir}/man8/
install -D -m 644 docs/man/httpd.8 %{buildroot}%{_mandir}/man8/

cp %{SOURCE200} README-access_compat.txt
cp %{SOURCE201} README-instances.txt
cp %{SOURCE202} README-configuration.txt
%endif

# utils install
%if "%{flavor}" == "utils"
> utils-filelist
for utility in %{support_bin}; do
  install -D -m 755 support/$utility %{buildroot}%{_bindir}/$utility
  echo %{_bindir}/$utility >> utils-filelist
  if [ -f docs/man/$utility.1 ]; then
    install -D -m 644 docs/man/$utility.1 %{buildroot}%{_mandir}/man1/$utility.1
    echo %{_mandir}/man1/$utility.1.* >> utils-filelist
  fi
done
for utility in %{support_sbin}; do
  install -D -m 755 support/$utility %{buildroot}%{_sbindir}/$utility
  echo %{_sbindir}/$utility >> utils-filelist
  if [ -f docs/man/$utility.8 ]; then
    install -D -m 644 docs/man/$utility.8 %{buildroot}%{_mandir}/man8/$utility.8
    echo %{_mandir}/man8/$utility.8.* >> utils-filelist
  fi
done
%endif

# devel install
%if "%{flavor}" == "devel"
mkdir -p %{buildroot}/%{_bindir}
install -D -m 755 support/apxs %{buildroot}%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1/
install -D -m 644 docs/man/apxs.1 %{buildroot}%{_mandir}/man1/
make DESTDIR=%{buildroot} install-build -j1
make DESTDIR=%{buildroot} install-include -j1
%endif

# manual install
%if "%{flavor}" == "manual"
mkdir -p %{buildroot}%{manualdir}
cp -ra docs/manual/* %{buildroot}%{manualdir}
mkdir -p %{buildroot}/%{sysconfdir}/conf.d/
install -m 644 %{SOURCE154} %{buildroot}/%{sysconfdir}/conf.d/manual.conf
%endif

%endif

#
# CHECK
#

%check
# test basic function of just built MPMs
%if ! %{test} && "%{mpm}" != ""
echo "Testing ./httpd-%{mpm}"
test_dir="$PWD/my-test-%{mpm}"
mkdir $test_dir
cat > $test_dir/httpd.conf << EOF
ServerName my_test
ErrorLog $test_dir/error_log
PidFile $test_dir/httpd.pid
User $(id -un)
Group $(id -gn)
Listen 60080
DocumentRoot $test_dir
LoadModule authz_core_module $PWD/modules/aaa/.libs/mod_authz_core.so
EOF
exit_code=0
./httpd-%{mpm} -k start -f $test_dir/httpd.conf
sleep 2
echo 'HTTPD HELLO' > $test_dir/hello.html
curl -s http://localhost:60080/hello.html | grep 'HTTPD HELLO' || exit_code=1
./httpd-%{mpm} -k stop -f $test_dir/httpd.conf
sleep 1
# do not continue %%check phase
exit $exit_code
%endif

# test just built utils
%if "%{flavor}" == "utils"
# htpasswd
echo "Testing htpasswd"
exit_code=0
support/htpasswd -bc htpasswd foo_user foo_password
support/htpasswd -bv htpasswd foo_user foo_password || exit_code=1
# htpasswd
echo "Testing htpasswd"
exit_code=0
support/htdbm -bc htpasswd bar_user bar_password
support/htdbm -bv htpasswd bar_user bar_password || exit_code=2
# do not continue %%check phase
exit $exit_code
%endif

# test _installed_ packages (via test_* flavors)
%if %{test}

%if "%{flavor}" == "test_main"
exit_code=0
# create test configuration, based on default distro one
# with minimum changes to see it is working
mkdir -p $PWD{%{_sysconfdir}/sysconfig,%{localstatedir},%{runtimedir},%{logfiledir}}
# adjust sysconfig file
cp %{_sysconfdir}/sysconfig/apache2 $PWD%{_sysconfdir}/sysconfig/
sed -i -e "s:\(APACHE_HTTPD_CONF=\).*:\1$PWD%{sysconfdir}/httpd.conf:" \
       -e "s:\(%{_localstatedir}\):$PWD\1:" $PWD%{_sysconfdir}/sysconfig/apache2
sed -i 's:\(APACHE_MPM=\).*:\1"prefork":' $PWD%{_sysconfdir}/sysconfig/apache2
# copy and adjust configuration (paths and Listen)
cp -r %{_sysconfdir}/apache2/ %{_sysconfdir}/mime.types etc 2>/dev/null || true
find etc/apache2 -name *.conf | xargs sed -i "s:\(%{_localstatedir}\):$PWD\1:"
find etc/apache2 -name *.conf | xargs sed -i "s:/etc:$PWD/etc:"
sed -i -e 's:80:60080:' -e 's:443:60443:' etc/apache2/listen.conf
# /usr/sbin/start_apache2 is 744
cp %{_sbindir}/start_apache2 .
export START_APACHE_SYSCONFIG_FILE=$PWD/etc/sysconfig/apache2
export START_APACHE_RUN_DIR=$PWD/run
./start_apache2 -k start
sleep 2
curl -s http://localhost:60080/manual/ | grep 'Apache.*HTTP Server.*Documentation' || exit_code=1
curl -s http://localhost:60080/manual/de/ | grep 'Neue Funktionen' || exit_code=2
./start_apache2 -k stop
sleep 1
# do not continue %%check phase
exit $exit_code
%endif

# test of devel package
%if "%{flavor}" == "test_devel"
# apxs test
echo "Testing apxs, compiling example module"
apxs -q CFLAGS | grep "\\%{optflags}"
cp %{SOURCE21} mod_example.c
apxs -c mod_example.c
test_dir="$PWD/my-test-devel"
echo "Try to load example module"
mkdir $test_dir
cat > $test_dir/httpd.conf << EOF
ServerName my_test
ErrorLog $test_dir/error_log
PidFile $test_dir/httpd.pid
User $(id -un)
Group $(id -gn)
Listen 60080
DocumentRoot $test_dir
LoadModule authz_core_module %{libexecdir}-%{default_mpm}/mod_authz_core.so
LoadModule example_module $PWD/.libs/mod_example.so
<Location /hello>
  SetHandler example-handler
</Location>
EOF
exit_code=0
%{_sbindir}/httpd-%{default_mpm} -k start -f $test_dir/httpd.conf
sleep 2
echo "Use example module"
curl -s http://localhost:60080/hello | grep 'Hello, world!' || exit_code=1
%{_sbindir}/httpd-%{default_mpm} -k stop -f $test_dir/httpd.conf
sleep 1
# do not continue %%check phase
exit $exit_code
%endif

# unittest run in test_$MPM flavors
echo "Run httpd-framework unittests"
cd httpd-framework
perl Makefile.PL -apxs %{apache_apxs}
function dep()
{
  dependee="$1"
  requirement="$2"
  # requirement has to be loaded before dependee;
  # there can be duplicite entries in $modules
  # string, will be added only once
  # in load-all-modules.conf
  if echo "$modules" | grep -q "$dependee"; then
    modules="$requirement $modules"
  fi
}
# create a conf loading all MPM's modules
echo >  $PWD/load-all-modules.conf
# hack: sort -u to load mod_proxy before mod_proxy_http, mod_cache before mod_cache_disk, etc.
modules=$(find %{_libdir}/apache2-%{mpm}/ %{_libdir}/apache2/ -name *.so | sed 's:.*/mod_\(.*\).so:\1:' | sort -u)
# fix up dependencies
dep "lbmethod_bybusyness" "proxy"
dep "lbmethod_byrequests" "proxy"
dep "lbmethod_bytraffic"  "proxy"
dep "lbmethod_heartbeat"  "proxy"
for m in $modules; do
  path=$(find %{_libdir}/apache2-%{mpm}/ %{_libdir}/apache2/ -name mod_$m.so | head -n 1)
  if ! grep -q "mod_$m.c" $PWD/load-all-modules.conf; then
    echo "<IfModule !mod_$m.c>"           >> $PWD/load-all-modules.conf
    echo "  LoadModule ${m}_module $path" >> $PWD/load-all-modules.conf
    echo "</IfModule>"                    >> $PWD/load-all-modules.conf
  fi
done
# run the testsuite
echo '#####################################################'
echo "# TESTING %{mpm}"
echo '#'
exit_code=0
t/TEST -clean
t/TEST -httpd /usr/sbin/httpd-%{mpm} -httpd_conf $PWD/load-all-modules.conf -start
t/TEST -run-tests || exit_code=1
t/TEST -stop
exit $exit_code

# end of installed packages test
%endif
exit 0

#
# FILES
#

# MPMs files
%if ! %{test} && "%{mpm}" != ""
%files
%{_sbindir}/httpd
%{_sbindir}/httpd-%{mpm}
%ghost %{_sysconfdir}/alternatives/httpd
# %%ghost %%{_sysconfdir}/alternatives/mod_*.so does not work
%(for module in %{dynamic_modules}; do echo "%ghost %{_sysconfdir}/alternatives/mod_$module.so"; done)
%dir %{_libdir}/apache2-%{mpm}
%dir %{_libdir}/apache2
%{_libdir}/apache2/*.so
%{libexecdir}/mod_*.so
%endif

# main package files
%if "%{flavor}" == ""
%files
%doc INSTALL READM* ABOUT_APACHE CHANGES
%license LICENSE
%attr(750,root,root) %dir %{logfiledir}
%attr(750,%{httpduser},root) %dir %{proxycachedir}
%attr(750,%{httpduser},root) %dir %{localstatedir}
%dir %{libexecdir}
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/apache2_MMN
%dir %{sysconfdir}
%config %{sysconfdir}/magic
%config %{sysconfdir}/mime.types
%config (noreplace) %{sysconfdir}/*.conf
%config (noreplace) %{sysconfdir}/charset.conv
%{sysconfdir}/vhosts.d/*.template
%dir %{sysconfdir}/ssl.crl
%dir %{sysconfdir}/ssl.crt
%dir %{sysconfdir}/ssl.csr
%dir %attr(700,root,root) %{sysconfdir}/ssl.key
%dir %{sysconfdir}/ssl.prm
%{sysconfdir}/ssl.*/README*
%dir %{sysconfdir}/conf.d
%dir %{sysconfdir}/vhosts.d
%{_fillupdir}/sysconfig.apache2
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/apache2
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/apache2
%endif
%{_unitdir}/apache2.service
%{_unitdir}/apache2@.service
%{_unitdir}/apache2.target
%{_sbindir}/apache2-systemd-ask-pass
%{_sbindir}/a2enflag
%{_sbindir}/a2enmod
%{_sbindir}/a2disflag
%{_sbindir}/a2dismod
%{_sbindir}/start_apache2
%{_sbindir}/rcapache2
%{_datadir}/apache2/script-helpers
%verify(not mode) %attr(0755,root,root) %{_sbindir}/suexec
%if %{use_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/apache2.xml
%{_prefix}/lib/firewalld/services/apache2-ssl.xml
%else
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/apache2
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/apache2-ssl
%endif
%{_datadir}/apache2
%{iconsdir}
%{errordir}
%{_mandir}/man8/httpd.8.*
%{_mandir}/man8/suexec.8.*
%doc support/SHA1
%{_docdir}/apache2/conf
%endif

# utils files
%if "%{flavor}" == "utils"
%files -f utils-filelist
%endif

# devel files
%if "%{flavor}" == "devel"
%files
%{_bindir}/apxs
%{_mandir}/man1/apxs.1.*
%{_datadir}/apache2
%{installbuilddir}
%{includedir}
%endif

# manual files
%if "%{flavor}" == "manual"
%files
%dir %{_datadir}/apache2
%{manualdir}
%dir %{sysconfdir}
%dir %{sysconfdir}/conf.d/
%config %{sysconfdir}/conf.d/manual.conf
%endif

#
# SCRIPTLETS
#

# MPMs scriptlets
%if ! %{test} && "%{mpm}" != ""
%post
%{_sbindir}/update-alternatives --quiet --force \
    --install %{_sbindir}/httpd httpd %{_sbindir}/httpd-%{mpm} %{mpm_alt_prio}
for module in %{dynamic_modules}; do
  if [ -e %{libexecdir}/mod_$module.so ]; then
    %{_sbindir}/update-alternatives --quiet --force \
        --install %{_libdir}/apache2/mod_$module.so mod_$module.so %{libexecdir}/mod_$module.so %{mpm_alt_prio}
  fi
done
exit 0

%postun
if [ "$1" = 1 ]; then
  %apache_request_restart
fi
if [ "$1" = 0 ]; then
  %{_sbindir}/update-alternatives --quiet --force --remove httpd %{_sbindir}/httpd
  for module in %{dynamic_modules}; do
    %{_sbindir}/update-alternatives --quiet --force --remove mod_$module.so %{_libdir}/apache2/mod_$module.so
  done
fi
exit 0

%posttrans
%apache_restart_if_needed
exit 0
%endif

# main package scriptlets
%if "%{flavor}" == ""
%pre
%service_add_pre apache2.service apache2.target
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/apache2 ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif
exit 0

%post
# wwwadmin group existed in past remove after openSUSE-13.2 out of support scope
if grep -q "^wwwadmin:" %{_sysconfdir}/group; then
        groupmod -n www wwwadmin 2>/dev/null ||:
        usermod -g %{httpdgroup} %{httpduser} 2>/dev/null ||:
        usermod -s /bin/false %{httpduser} 2>/dev/null ||:
fi
%service_add_post apache2.service apache2.target
%set_permissions %{_sbindir}/suexec || \
  echo "Please check %{_sysconfdir}/permissions.local for settings of %{_sbindir}/suexec ."
%{fillup_only apache2}
%if %{use_firewalld}
%firewalld_reload
%endif
exit 0

%posttrans
%apache_restart_if_needed
%if 0%{?suse_version} > 1500
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/apache2 ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%verifyscript
%verify_permissions -e %{_sbindir}/suexec

%preun
%service_del_preun apache2.service apache2.target
exit 0

%postun
%if %{defined service_del_postun_without_restart}
%service_del_postun_without_restart apache2.service apache2.target
%else
DISABLE_RESTART_ON_UPDATE='yes'
%service_del_postun apache2.service apache2.target
%endif
if [ "$1" = 1 ]; then
  %apache_request_restart
fi
%endif

%changelog
