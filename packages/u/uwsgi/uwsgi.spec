#
# spec file for package uwsgi
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


%define with_php 1
%if 0%{?suse_version} > 1320
%if 0%{?suse_version} >= 1550
%define php  php8
%else
%define php  php7
%endif
%else
%define with_php 0
%endif

%{?!python_module:%define python_module() python3-%{**}}
Name:           uwsgi
Version:        2.0.20
Release:        0
Summary:        Application Container Server for Networked/Clustered Web Applications
License:        Apache-2.0 AND GPL-2.0-only WITH GCC-exception-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://uwsgi-docs.readthedocs.io/en/latest/
Source:         https://projects.unbit.it/downloads/uwsgi-%{version}.tar.gz
Source1:        opensuse.ini.in
Source2:        uwsgi.service
Source3:        django.ini.example
Source4:        rails.yml.example
Source5:        trac.ini.example
Source6:        werkzeug.xml.example
Source7:        README.openSUSE
Source8:        uwsgi.ini
Source9:        uwsgi.tmpfiles.d
# PATCH-FIX-OPENSUSE uwsgi-1.9.17-plugin_build_path.patch - Don't attempt to install plugins to target dest during build
Patch0:         uwsgi-1.9.17-plugin_build_path.patch
# PATCH-FIX-OPENSUSE uwsgi-1.9.17-no-LD_RUN_PATH.patch - Disable invalid rpath in plugins
Patch1:         uwsgi-2.0.12-no-LD_RUN_PATH.patch
# PATCH-FIX-OPENSUSE uwsgi-1.9.13-objc_gc-no-fobjc-gc.patch - No -fobjc-gc in CFLAGS, which is incorrect in GNU
Patch2:         uwsgi-1.9.13-objc_gc-no-fobjc-gc.patch
# PATCH-FIX-OPENSUSE uwsgi-1.9.11-systemd_logger-old_systemd.patch - Older systemd in 12.2 does not implicity include syslog.h
Patch3:         uwsgi-1.9.11-systemd_logger-old_systemd.patch
# PATCH-FIX-OPENSUSE uwsgi-2.0.18-postgresql-config.patch - Use pkg-config instead of pg_config
Patch4:         uwsgi-2.0.18-postgresql-config.patch
# PATCH-FIX-UPSTREAM uwsgi-ld-noexecstack.patch - Do not create executable stack
Patch5:         uwsgi-ld-noexecstack.patch
BuildRequires:  apache-rpm-macros
%if 0%{suse_version} < 1500
BuildRequires:  apache2-devel
%else
BuildRequires:  apache2-devel >= 2.4.33
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  argon2-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  gcc-objc
%if 0%{?suse_version} > 1220
BuildRequires:  glusterfs-devel
%endif
#BuildRequires:  go
BuildRequires:  java-devel
#BuildRequires:  krb5-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libffi-devel
%if 0%{?suse_version} > 1210
BuildRequires:  libjansson-devel
%endif
#BuildRequires:  libmono-2_0-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libyaml-devel
%if 0%{?suse_version} > 1210
BuildRequires:  lua51-devel
%else
BuildRequires:  lua-devel
%endif
#BuildRequires:  mono-web
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre-devel
%if %{with_php}
BuildRequires:  %{php}-devel
BuildRequires:  %{php}-embed
%endif
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module greenlet-devel}
BuildRequires:  pkg-config
BuildRequires:  postgresql-devel
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} <= 1310
BuildRequires:  ruby19-devel
%endif
BuildRequires:  sqlite3-devel
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libsystemd)
%ifarch %{ix86} x86_64 %{arm}
%if 0%{?suse_version} < 1310
BuildRequires:  v8-devel
%endif
%endif
BuildRequires:  zeromq-devel
BuildRequires:  zlib-devel
%{?systemd_requires}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       uwsgi-carbon = %{version}
Obsoletes:      uwsgi-carbon < 1.9.11
Provides:       uwsgi-cgi = %{version}
Obsoletes:      uwsgi-cgi < 1.9.11
Provides:       uwsgi-fastrouter = %{version}
Obsoletes:      uwsgi-fastrouter < 1.9.11
Provides:       uwsgi-graylog2 = %{version}
Obsoletes:      uwsgi-graylog2 < 1.9.11
Provides:       uwsgi-http = %{version}
Obsoletes:      uwsgi-http < 1.9.11
Provides:       uwsgi-logsocket = %{version}
Obsoletes:      uwsgi-logsocket < 1.9.11
Provides:       uwsgi-nagios = %{version}
Obsoletes:      uwsgi-nagios < 1.9.11
Provides:       uwsgi-probepg = %{version}
Obsoletes:      uwsgi-probepg < 1.9.11
Provides:       uwsgi-redislog = %{version}
Obsoletes:      uwsgi-redislog < 1.9.11
Provides:       uwsgi-rrdtool = %{version}
Obsoletes:      uwsgi-rrdtool < 1.9.11
Provides:       uwsgi-rsyslog = %{version}
Obsoletes:      uwsgi-rsyslog < 1.9.11
Provides:       uwsgi-syslog = %{version}
Obsoletes:      uwsgi-syslog < 1.9.11
Provides:       uwsgi-ugreen = %{version}
Obsoletes:      uwsgi-ugreen < 1.9.11
Provides:       uwsgi-zergpool = %{version}
Obsoletes:      uwsgi-zergpool < 1.9.11
%if 0%{?suse_version} >= 1550
# these must be the last directives before the description
%define python_subpackage_only 1
%python_subpackages
%endif

%description
uWSGI is a self-healing application container server coded in pure C.

It is a WSGI server with a stack for networked/clustered web applications,
implementing message/object passing, caching, RPC and process management.

It uses the uwsgi protocol for all the networking/interprocess communications,
but it can speak other protocols as well (http, fastcgi, mongrel2...)

It can be run in preforking mode, threaded, asynchronous/evented and supports
various forms of green threads/coroutines (such as uGreen, Greenlet, Stackless,
Gevent and Fiber).

Different plugins can be used in order to add compatibility with
different technology on top of the same core.


# This is part of the apache2 package now
%if 0%{suse_version} < 1500
%package -n apache2-mod_proxy_uwsgi
Summary:        uWSGI Proxy Module for Apache 2.0
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description -n apache2-mod_proxy_uwsgi
uWSGI is a self-healing application container server coded in pure C.

This package contains an Apache 2.0 proxy module for uWSGI.
%endif

%package -n apache2-mod_uwsgi
Summary:        uWSGI Module for Apache 2.0
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description -n apache2-mod_uwsgi
uWSGI is a self-healing application container server coded in pure C.

This package contains an Apache 2.0 module for uWSGI.

%package emperor_pg
Summary:        PostgreSQL Emperor Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description emperor_pg
uWSGI is a self-healing application container server coded in pure C.

This package contains an emperor plugin allowing for configuration of
applications (vassals) in a PostgreSQL database.

%package emperor_zeromq
Summary:        ZeroMQ Emperor Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description emperor_zeromq
uWSGI is a self-healing application container server coded in pure C.

This package contains an emperor plugin allowing for configuration of
applications (vassals) via ZeroMQ.

%package gevent
Summary:        Gevent Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Requires:       %{name}-python3 = %{version}

%description gevent
uWSGI is a self-healing application container server coded in pure C.

This package contains support for Python Gevent, which is a non-blocking
networking framework.


%if 0%{?suse_version} > 1220
%package glusterfs
Summary:        GlusterFS Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description glusterfs
uWSGI is a self-healing application container server coded in pure C.

This package contains support for returning objects directly from a GlusterFS
filesystem
%endif

%package greenlet
Summary:        Greenlet Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Requires:       %{name}-python3 = %{version}

%description greenlet
uWSGI is a self-healing application container server coded in pure C.

This package contains support for the Python Greenlet non-blocking network
framework.

%package jvm
Summary:        JVM Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Provides:       uwsgi-jwsgi = %{version}
Obsoletes:      uwsgi-jwsgi < 1.9.11

%description jvm
uWSGI is a self-healing application container server coded in pure C.

This package contains support for embedding a Java virtual machine in uWSGI.

%package ldap
Summary:        LDAP Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description ldap
uWSGI is a self-healing application container server coded in pure C.

This package contains support for configuring uWSGI via LDAP.

%package libffi
Summary:        Plugin libffi for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description libffi
uWSGI is a self-healing application container server coded in pure C.

This package contains support for libffi.

%package logzmq
Summary:        ZMQ Logger for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description logzmq
uWSGI is a self-healing application container server coded in pure C.

This package contains support for ZMQ logging.

%package lua
Summary:        Lua Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description lua
uWSGI is a self-healing application container server coded in pure C.

This package contains support for Lua applications via the wsapi interface.

%package pam
Summary:        PAM Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description pam
uWSGI is a self-healing application container server coded in pure C.

This package contains support for PAM authentication.

%package psgi
Summary:        PSGI Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
%{?libperl_requires}

%description psgi
uWSGI is a self-healing application container server coded in pure C.

This package contains the PSGI plugin for running Perl applications that
support the PSGI protocol.

%package pypy
Summary:        PyPy Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description pypy
uWSGI is a self-healing application container server coded in pure C.

This package contains support for Python applications using PyPy.

%if 0%{suse_version} < 1550

%package python3
Summary:        Python 3 Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Requires:       python3-base >= 3.6
Provides:       python3-uwsgi-python3 = %{version}-%{release}

%description python3
uWSGI is a self-healing application container server coded in pure C.

This package contains support for Python 3 applications via the WSGI protocol.

%else

%package -n python-uwsgi-python3
Summary:        Python %{python_version} Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
%if "%{python_provides}" == "python3"
Provides:       uwsgi-python3 = %{version}-%{release}
Obsoletes:      uwsgi-python3 < %{version}-%{release}
%endif
# the plugin is linked to the python library, no reason the state -base explicitly

%description -n python-uwsgi-python3
uWSGI is a self-healing application container server coded in pure C.

This package contains support for Python %{python_version} applications via the WSGI protocol.

%endif

%if 0%{?suse_version} <= 1310
%package ruby
Summary:        Ruby Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Requires:       ruby19
Provides:       uwsgi-fiber = %{version}
Obsoletes:      uwsgi-fiber < 1.9.11

%description ruby
uWSGI is a self-healing application container server coded in pure C.

This package contains support for Ruby applications.
%endif

%package sqlite3
Summary:        SQLite3 Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description sqlite3
uWSGI is a self-healing application container server coded in pure C.

This package contains support for storing application configuration in SQLite3
databases.

%package v8
Summary:        V8 JavaScript Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description v8
uWSGI is a self-healing application container server coded in pure C.

This package contains support for JavaScript using V8.

%package xslt
Summary:        XSLT Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}

%description xslt
uWSGI is a self-healing application container server coded in pure C.

This package contains support for rendering XML content using XSLT.

%if %{with_php}
%package %{php}
Summary:        PHP7 Plugin for uWSGI
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Requires:       %{php}-embed

%description %{php}
uWSGI is a self-healing application container server coded in pure C.

This package contains support for PHP version 7.
%endif

%prep
%setup -q -n uwsgi-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# Generate a config that builds all plugins except for examples and stuff we
# can't satisfy the requirements for or are just broken
excluded_plugins=""

# Still no mongodb in Factory
excluded_plugins="$excluded_plugins stats_pusher_mongodb emperor_mongodb mongodb mongodblog gridfs"

# Mono plugin builds private key during build. It would not be a good idea to
# distribute the same key to multiple systems
excluded_plugins="$excluded_plugins mono"

# Only for OSX
excluded_plugins="$excluded_plugins alarm_speech"

%if 0%{?suse_version} <= 1320
# No php[57]-embed on openSUSE Leap for some reason
excluded_plugins="$excluded_plugins php"
%endif

# No stackless in openSUSE
excluded_plugins="$excluded_plugins stackless"

# No perl-Coro in Factory (there is a broken unmaintained one under d:l:perl:CPAN-C)
excluded_plugins="$excluded_plugins coroae"

# Requires libgloox, which is not in Factory
excluded_plugins="$excluded_plugins alarm_xmpp"

# No gccgo in openSUSE yet
excluded_plugins="$excluded_plugins gccgo"

# This plugin require a libuwsgi, which appears to conflict with core...
excluded_plugins="$excluded_plugins pyuwsgi"

# The SPNEGO router is not complete
excluded_plugins="$excluded_plugins router_spnego"

# These are example plugins and shouldn't be distributed
excluded_plugins="$excluded_plugins cplusplus dummy example"

# Ceph/RADOS not yet in Factory
excluded_plugins="$excluded_plugins rados"

# libtcc not yet in Factory
excluded_plugins="$excluded_plugins libtcc"

# matheval is deprecated
excluded_plugins="$excluded_plugins matheval"

# bsc#1156199 - python-txtorcon: GeoIP support is discontinued
excluded_plugins="$excluded_plugins geoip"

# V8 is not yet available on all platforms and is broken in the v8 versions in
# 13.1+
%if 0%{?suse_version} >= 1310
excluded_plugins="$excluded_plugins v8"
%else
%ifnarch %{ix86} x86_64 %{arm}
excluded_plugins="$excluded_plugins v8"
%endif
%endif

# python3 modules are built separately
excluded_plugins="$excluded_plugins python"

# Ruby 1.9 is no longer available after 13.1
%if 0%{?suse_version} > 1310
excluded_plugins="$excluded_plugins fiber mongrel2 rack rbthreads ruby19"
%endif

%if 0%{?suse_version} <= 1220
# Requirements missing on openSUSE <= 12.2
excluded_plugins="$excluded_plugins glusterfs"
%endif

plugins=$(python3 -c "import sys, os; print(', '.join([p for p in sorted(os.listdir('plugins')) if p not in sys.argv[1:]]))" $excluded_plugins)
sed -e "s#@@LIBDIR@@#%{_libdir}#" -e "s#@@PLUGINS@@#$plugins#" %{SOURCE1} > buildconf/opensuse.ini

# README.openSUSE
cp %{SOURCE7} .

%build
# Find correct location for libjvm
export UWSGICONFIG_JVM_LIBPATH=$(dirname $(find %{_jvmdir}/java/jre/lib -name "libjvm.so" | grep server))
export UWSGICONFIG_JVM_INCPATH="%{_jvmdir}/java/include"
export UWSGICONFIG_LUALIB="lua"
export UWSGICONFIG_LUAPC="lua"
export UWSGICONFIG_RUBYPATH="ruby1.9"
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations -I%{_includedir}/glusterfs -I$(echo %{_libdir}/erlang/lib/erl_interface-*/include) -I%{_jvmdir}/java/include/linux -L$UWSGICONFIG_JVM_LIBPATH/jli"
%{?jobs:export CPUCOUNT=%jobs}
python3 uwsgiconfig.py --build opensuse

# Build python3 plugins
%if 0%{?suse_version} < 1550
python3 uwsgiconfig.py --plugin plugins/python opensuse python3
%else
# https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html#bonus-multiple-python-versions-for-the-same-uwsgi-binary
%python_expand PYTHON=$python $python uwsgiconfig.py --plugin plugins/python opensuse ${python_flavor}
%endif

# Build Apache modules
%if 0%{suse_version} < 1500
%{apache_apxs} -c apache2/mod_proxy_uwsgi.c
%endif
%{apache_apxs} -c apache2/mod_uwsgi.c

# Build php plugin
%if %{with_php}
python3 uwsgiconfig.py --plugin plugins/php opensuse %{php}
%endif

%install
install -D -m 0755 uwsgi %{buildroot}%{_sbindir}/uwsgi
install -d -m 0755 %{buildroot}%{_libdir}/uwsgi
install -m 0755 *_plugin.so %{buildroot}%{_libdir}/uwsgi
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/uwsgi.service
install -d -m 0755 %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -D -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/uwsgi/uwsgi.ini
install -m 0644 %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -m 0644 vassals/broodlord.ini %{buildroot}%{_sysconfdir}/uwsgi/vassals/broodlord.ini.example
install -m 0644 vassals/cc.ini %{buildroot}%{_sysconfdir}/uwsgi/vassals/cc.ini.example
install -m 0644 vassals/multi.xml %{buildroot}%{_sysconfdir}/uwsgi/vassals/multi.xml.example
%if 0%{suse_version} < 1550
install -D -m 0644 uwsgidecorators.py %{buildroot}%{python3_sitelib}/uwsgidecorators.py
%else
%{python_expand #
install -D -m 0644 uwsgidecorators.py %{buildroot}%{$python_sitelib}/uwsgidecorators.py
if [ "%{$python_provides}" == "python3" ]; then
  ln -s  ${python_flavor}_plugin.so %{buildroot}%{_libdir}/uwsgi/python3_plugin.so
fi
}
%endif
install -D plugins/jvm/uwsgi.jar %{buildroot}%{_javadir}/uwsgi.jar
install -d -m 0755 %{buildroot}/%{apache_libexecdir}
install -m 0755 apache2/.libs/*.so %{buildroot}/%{apache_libexecdir}
%if 0%{?suse_version} > 1220
ln -sf /usr/sbin/service %{buildroot}%{_sbindir}/rcuwsgi
%endif

install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE9} %{buildroot}/%{_tmpfilesdir}/uwsgi.conf

%pre
%service_add_pre uwsgi.service

%post
%service_add_post uwsgi.service
%tmpfiles_create %{_tmpfilesdir}/uwsgi.conf

%preun
%service_del_preun uwsgi.service

%postun
%service_del_postun uwsgi.service

%files
%defattr(-,root,root,-)
%license LICENSE
%doc CONTRIBUTORS README contrib examples README.openSUSE
%{_sbindir}/uwsgi
%dir %{_sysconfdir}/uwsgi/
%config(noreplace) %{_sysconfdir}/uwsgi/uwsgi.ini
%dir %{_sysconfdir}/uwsgi/vassals
%config %{_sysconfdir}/uwsgi/vassals/*
%dir %{_libdir}/uwsgi
%ghost %dir %attr(711,root,root) /run/uwsgi
%{_unitdir}/uwsgi.service
%{_tmpfilesdir}/uwsgi.conf
%if 0%{?suse_version} > 1220
%{_sbindir}/rcuwsgi
%endif
%{_libdir}/uwsgi/airbrake_plugin.so
%{_libdir}/uwsgi/alarm_curl_plugin.so
%{_libdir}/uwsgi/asyncio_plugin.so
%{_libdir}/uwsgi/cache_plugin.so
%{_libdir}/uwsgi/carbon_plugin.so
%{_libdir}/uwsgi/cgi_plugin.so
%{_libdir}/uwsgi/cheaper_backlog2_plugin.so
%{_libdir}/uwsgi/cheaper_busyness_plugin.so
%{_libdir}/uwsgi/clock_monotonic_plugin.so
%{_libdir}/uwsgi/clock_realtime_plugin.so
%{_libdir}/uwsgi/corerouter_plugin.so
%{_libdir}/uwsgi/curl_cron_plugin.so
%{_libdir}/uwsgi/dumbloop_plugin.so
%{_libdir}/uwsgi/emperor_amqp_plugin.so
%{_libdir}/uwsgi/exception_log_plugin.so
%{_libdir}/uwsgi/fastrouter_plugin.so
%{_libdir}/uwsgi/forkptyrouter_plugin.so
%{_libdir}/uwsgi/echo_plugin.so
%{_libdir}/uwsgi/graylog2_plugin.so
%{_libdir}/uwsgi/http_plugin.so
%{_libdir}/uwsgi/legion_cache_fetch_plugin.so
%{_libdir}/uwsgi/logcrypto_plugin.so
%{_libdir}/uwsgi/logfile_plugin.so
%{_libdir}/uwsgi/logpipe_plugin.so
%{_libdir}/uwsgi/logsocket_plugin.so
%{_libdir}/uwsgi/nagios_plugin.so
%{_libdir}/uwsgi/objc_gc_plugin.so
%{_libdir}/uwsgi/msgpack_plugin.so
%{_libdir}/uwsgi/notfound_plugin.so
%{_libdir}/uwsgi/ping_plugin.so
%{_libdir}/uwsgi/pty_plugin.so
%{_libdir}/uwsgi/rawrouter_plugin.so
%{_libdir}/uwsgi/redislog_plugin.so
%{_libdir}/uwsgi/router_access_plugin.so
%{_libdir}/uwsgi/router_basicauth_plugin.so
%{_libdir}/uwsgi/router_cache_plugin.so
%{_libdir}/uwsgi/router_expires_plugin.so
%{_libdir}/uwsgi/router_hash_plugin.so
%{_libdir}/uwsgi/router_http_plugin.so
%{_libdir}/uwsgi/router_memcached_plugin.so
%{_libdir}/uwsgi/router_metrics_plugin.so
%{_libdir}/uwsgi/router_radius_plugin.so
%{_libdir}/uwsgi/router_redirect_plugin.so
%{_libdir}/uwsgi/router_redis_plugin.so
%{_libdir}/uwsgi/router_rewrite_plugin.so
%{_libdir}/uwsgi/router_static_plugin.so
%{_libdir}/uwsgi/router_uwsgi_plugin.so
%{_libdir}/uwsgi/router_xmldir_plugin.so
%{_libdir}/uwsgi/rpc_plugin.so
%{_libdir}/uwsgi/rrdtool_plugin.so
%{_libdir}/uwsgi/rsyslog_plugin.so
%{_libdir}/uwsgi/signal_plugin.so
%{_libdir}/uwsgi/spooler_plugin.so
%{_libdir}/uwsgi/ssi_plugin.so
%{_libdir}/uwsgi/sslrouter_plugin.so
%{_libdir}/uwsgi/stats_pusher_file_plugin.so
%{_libdir}/uwsgi/stats_pusher_socket_plugin.so
%{_libdir}/uwsgi/stats_pusher_statsd_plugin.so
%{_libdir}/uwsgi/symcall_plugin.so
%{_libdir}/uwsgi/syslog_plugin.so
%{_libdir}/uwsgi/systemd_logger_plugin.so
%{_libdir}/uwsgi/tornado_plugin.so
%{_libdir}/uwsgi/transformation_chunked_plugin.so
%{_libdir}/uwsgi/transformation_gzip_plugin.so
%{_libdir}/uwsgi/transformation_offload_plugin.so
%{_libdir}/uwsgi/transformation_template_plugin.so
%{_libdir}/uwsgi/transformation_tofile_plugin.so
%{_libdir}/uwsgi/transformation_toupper_plugin.so
%{_libdir}/uwsgi/tuntap_plugin.so
%{_libdir}/uwsgi/ugreen_plugin.so
%{_libdir}/uwsgi/webdav_plugin.so
%{_libdir}/uwsgi/xattr_plugin.so
%{_libdir}/uwsgi/zabbix_plugin.so
%{_libdir}/uwsgi/zergpool_plugin.so

%if 0%{suse_version} < 1500
%files -n apache2-mod_proxy_uwsgi
%defattr(-,root,root,-)
%{apache_libexecdir}/mod_proxy_uwsgi.so
%endif

%files -n apache2-mod_uwsgi
%defattr(-,root,root,-)
%{apache_libexecdir}/mod_uwsgi.so

%files emperor_pg
%defattr(-,root,root,-)
%{_libdir}/uwsgi/emperor_pg_plugin.so

%files emperor_zeromq
%defattr(-,root,root,-)
%{_libdir}/uwsgi/emperor_zeromq_plugin.so

%files gevent
%defattr(-,root,root,-)
%{_libdir}/uwsgi/gevent_plugin.so

%files greenlet
%defattr(-,root,root,-)
%{_libdir}/uwsgi/greenlet_plugin.so

%if 0%{?suse_version} > 1220
%files glusterfs
%defattr(-,root,root,-)
%{_libdir}/uwsgi/glusterfs_plugin.so
%endif

%files jvm
%defattr(-,root,root,-)
%{_libdir}/uwsgi/jvm_plugin.so
%{_libdir}/uwsgi/jwsgi_plugin.so
%{_libdir}/uwsgi/ring_plugin.so
%{_libdir}/uwsgi/servlet_plugin.so
%{_javadir}/uwsgi.jar

%files ldap
%defattr(-,root,root,-)
%{_libdir}/uwsgi/ldap_plugin.so

%files libffi
%defattr(-,root,root,-)
%{_libdir}/uwsgi/libffi_plugin.so

%files logzmq
%defattr(-,root,root,-)
%{_libdir}/uwsgi/logzmq_plugin.so

%files lua
%defattr(-,root,root,-)
%{_libdir}/uwsgi/lua_plugin.so

%files pam
%defattr(-,root,root,-)
%{_libdir}/uwsgi/pam_plugin.so

%files psgi
%defattr(-,root,root,-)
%{_libdir}/uwsgi/psgi_plugin.so

%files pypy
%defattr(-,root,root,-)
%{_libdir}/uwsgi/pypy_plugin.so

%if 0%{suse_version} < 1550

%files python3
%defattr(-,root,root,-)
%{_libdir}/uwsgi/python3_plugin.so
%{python3_sitelib}/uwsgidecorators.py*

%else

%files %{python_files uwsgi-python3}
%defattr(-,root,root,-)
%{_libdir}/uwsgi/%{python_flavor}_plugin.so
%if "%{python_provides}" == "python3"
%{_libdir}/uwsgi/python3_plugin.so
%endif
%{python_sitelib}/uwsgidecorators.py*

%endif

%if 0%{?suse_version} <= 1310
%files ruby
%defattr(-,root,root,-)
%{_libdir}/uwsgi/fiber_plugin.so
%{_libdir}/uwsgi/mongrel2_plugin.so
%{_libdir}/uwsgi/rack_plugin.so
%{_libdir}/uwsgi/rbthreads_plugin.so
%{_libdir}/uwsgi/ruby19_plugin.so
%endif

%files sqlite3
%defattr(-,root,root,-)
%{_libdir}/uwsgi/sqlite3_plugin.so

%ifarch %{ix86} x86_64 %{arm}
%if 0%{?suse_version} < 1310
%files v8
%defattr(-,root,root,-)
%{_libdir}/uwsgi/v8_plugin.so
%endif
%endif

%files xslt
%defattr(-,root,root,-)
%{_libdir}/uwsgi/xslt_plugin.so

%if 0%{?suse_version} > 1320
%files %{php}
%defattr(-,root,root,-)
%{_libdir}/uwsgi/php*_plugin.so
%endif

%changelog
