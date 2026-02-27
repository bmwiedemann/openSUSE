#
# spec file for package syslog-ng
#
# Copyright (c) 2026 SUSE LLC
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


%define         __provides_exclude_from ^%{_libdir}/syslog-ng/
%define         syslog_ng_sockets_cfg	%{syslog_ng_rundir}/additional-log-sockets.conf
%global		py_ver	 %(rpm -qf %{_bindir}/python3 --qf "%%{version}" | awk -F. '{print $1"."$2}')

#redis only in openSUSE
%if !0%{?is_opensuse}
%bcond_with	redis
%else
%bcond_without	redis
%endif

# mqtt only in Tumbleweed
%if 0%{?suse_version} > 1600
%bcond_without	mqtt
%else
%bcond_with	mqtt
%endif

# GRPC and BPF dependencies only in TW
%if 0%{?suse_version} > 1500
%bcond_without  grpc
%bcond_without	bpf
%else
%bcond_with     grpc
%bcond_with	bpf
%endif

# CloudAuth needs 15+
%if 0%{?suse_version} >= 1500
%bcond_without  cloudauth
%else
%bcond_with     cloudauth
%endif

%if %{with grpc}
BuildRequires:  grpc-devel
BuildRequires:  protobuf-devel
%endif

# missing dependencies on SLES 15
%if 0%{?sle_version} >= 150000 && !0%{?is_opensuse}
%bcond_with	dbi
%bcond_with	java
%bcond_with	geoip
%else
%bcond_without  dbi
%ifarch armv7l armv7hl
%bcond_with	java
%else
%bcond_without	java
%endif
%bcond_without	geoip
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if %{defined _rundir}
%define         syslog_ng_rundir        %{_rundir}/syslog-ng
%else
%define         syslog_ng_rundir	%{_localstatedir}/run/syslog-ng
%endif
# turn features on and off
%bcond_without	python
%bcond_without	http
%bcond_without	smtp
# mongodb & amqp C clients are no more bundled with syslog-ng sources
# and not yet available in openSUSE
# leaving here for future usage
%bcond_with	mongodb
%bcond_with	amqp
# prepaing for Leap 16.0
%if 0%{?suse_version} == 1600
%bcond_with	pythondeps
%else
%bcond_without	pythondeps
%endif
%bcond_without	snmp
Name:           syslog-ng
Version:        4.11.0
Release:        0
Summary:        Enhanced system logging daemon
License:        GPL-2.0-only
Group:          System/Daemons
URL:            https://syslog-ng.org/
Source0:        https://github.com/balabit/syslog-ng/releases/download/syslog-ng-%{version}/%{name}-%{version}.tar.gz
Source1:        syslog-ng.sysconfig
Source2:        syslog-ng.conf.default
Source3:        syslog-ng.service
Source4:        syslog-ng-service-prepare
Patch0:         syslog-ng-reproducible-jar-mtime.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libcap-devel
BuildRequires:  libjson-devel
BuildRequires:  libnet-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
%if %{with snmp}
BuildRequires:  net-snmp-devel
%endif
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libsystemd)
#!BuildIgnore:  rsyslog
Requires(pre):  %fillup_prereq
Requires(pre):  syslog-service >= 2.0
Conflicts:      syslog
Provides:       syslog
Provides:       sysvinit(syslog)
%if %{with mqtt}
BuildRequires:  libpaho-mqtt-devel
%endif
%if %{with smtp}
BuildRequires:  libesmtp-devel
%endif
%if %{with http}
BuildRequires:  libcurl-devel
%endif
%if %{with geoip}
BuildRequires:  libmaxminddb-devel
%endif
%if %{with redis}
BuildRequires:  hiredis-devel
%endif
%if %{with dbi}
BuildRequires:  libdbi-devel
%endif
%if %{with java}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  java-devel >= 1.8
BuildRequires:  libtool
%endif
%if %{with pythondeps}
BuildRequires:  python3-PyYAML
BuildRequires:  python3-cachetools
BuildRequires:  python3-certifi
BuildRequires:  python3-charset-normalizer
BuildRequires:  python3-google-auth
BuildRequires:  python3-idna
BuildRequires:  python3-kubernetes
BuildRequires:  python3-oauthlib
BuildRequires:  python3-pip
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-requests
BuildRequires:  python3-requests-oauthlib
BuildRequires:  python3-rsa
BuildRequires:  python3-six
BuildRequires:  python3-urllib3
BuildRequires:  python3-websocket-client
%endif

%if %{with bpf}
BuildRequires:  bpftool
BuildRequires:  clang
BuildRequires:  libbpf-devel
%endif

%description
syslog-ng is an enhanced log daemon, supporting a wide range of input and
output methods: syslog, unstructured text, message queues, databases (SQL
and NoSQL alike) and more.

Key features:

 * receive and send RFC3164 and RFC5424 style syslog messages
 * work with any kind of unstructured data
 * receive and send JSON formatted messages
 * classify and structure logs with builtin parsers (csv-parser(),
   db-parser(), ...)
 * normalize, crunch and process logs as they flow through the system
 * hand on messages for further processing using message queues (like
   AMQP), files or databases (like PostgreSQL or MongoDB).

%package -n libevtlog-4_11-0
Summary:        Syslog-ng event logger library runtime
Group:          System/Libraries

%description -n libevtlog-4_11-0
The EventLog library provides an alternative to the simple syslog()
API provided on UNIX systems. Compared to syslog, EventLog adds
structured messages.

EventLog provides an interface to build, format and output an event
record. The exact format and output method can be customized by the
administrator via a configuration file.

This package is now merged into syslog-ng.

%package http
Summary:        HTTP destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}
Obsoletes:      syslog-ng-curl <= 4.8.1
Provides:       syslog-ng-curl = %{version}

%description http
This package provides HTTP destination support for syslog-ng by means
of libcurl.

%package java
Summary:        Java destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description java
This package provides Java destination support for syslog-ng.

%package sql
Summary:        SQL support using DBI for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description sql
This package provides the libafsql module providing support for
logging into a SQL database using DBI.

%package smtp
Summary:        SMTP output support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description smtp
This package provides the afsmtp module providing support for
logging into SMTP.

%package geoip
Summary:        GeoIP (MaxMindDB) support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description geoip
This package provides GeoIP (MaxMindDB) modules providing support for
logging geo-location information.

%package redis
Summary:        Redis destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description redis
This package provides the libredis module providing support for
logging to a redis destination.

%package bpf
Summary:        Faster UDP log collection for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description bpf
This package provides faster UDP log collection for syslog-ng using bpf

%package python
Summary:        Python destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description python
This package provides Python destination support for syslog-ng.

%package python-modules
Summary:        Python modules for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-python
%if %{with pythondeps}
Requires:       python3-PyYAML
Requires:       python3-cachetools
Requires:       python3-certifi
Requires:       python3-charset-normalizer
Requires:       python3-google-auth
Requires:       python3-idna
Requires:       python3-kubernetes
Requires:       python3-pip
Requires:       python3-pyasn1
Requires:       python3-pyasn1-modules
Requires:       python3-python-dateutil
Requires:       python3-requests
Requires:       python3-rsa
Requires:       python3-six
Requires:       python3-websocket-client
%endif

%description python-modules
This package provides python modules for syslog-ng, for
Kubernetes log enrichment, Hypr support, etc.

%package devel
Summary:        Development files for syslog-ng
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Provides:       libevtlog-devel = %{version}
Obsoletes:      libevtlog-devel <= 0.2.13

%description devel
This package provides files necessary for syslog-ng development.

%package snmp
Summary:        SNMP support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description snmp
This package provides SNMP support for syslog-ng

%package mqtt
Summary:        MQTT support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%package grpc
Summary:        Common files for grpc-based syslog-ng drivers
Group:          System/Daemons
Requires:       %{name} = %{version}

%description grpc
This package provides provides common files for grpc-based syslog-ng drivers

%package opentelemetry
Summary:        OpenTelemetry support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-grpc

%description opentelemetry
This package provides OpenTelemetry support for syslog-ng

%package loki
Summary:        Loki destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-grpc

%description loki
This package provides Loki destination support for syslog-ng

%package bigquery
Summary:        Google BigQuery destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-grpc

%description bigquery
This package provides Google BigQuery destination support for syslog-ng

%package clickhouse
Summary:        Clickhouse destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-grpc

%description clickhouse
This package provides Clickhouse destination support for syslog-ng

%package pubsub
Summary:        Google PubSub destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-grpc

%description pubsub
This package provides Google PubSub destination support for syslog-ng

%package cloudauth
Summary:        Cloud Authentication support for syslog-ng: pubsub
Group:          System/Daemons
Requires:       %{name} = %{version}

%description cloudauth
This package provides Cloud Authentication support for syslog-ng,
currently used for Google PubSub

%description mqtt
This package provides MQTT support for syslog-ng

%prep
%setup -q -n syslog-ng-%{version}
%if %{with java}
# The "--date" option was added into jar in OpenJDK 17
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
%patch -P 0 -p1
%endif
%endif
# fill out placeholders in the config,
# systemd service and prepare script.
for file in \
	syslog-ng.conf.default \
	syslog-ng.service \
	syslog-ng-service-prepare \
; do
	sed \
	-e 's;@sbindir@;%{_sbindir};g' \
	-e 's;RUN_DIR;%{syslog_ng_rundir};g' \
	-e 's;ADDITIONAL_SOCKETS;%{syslog_ng_sockets_cfg};g' \
	"%{_sourcedir}/${file}" > "${file}"
done
%ifarch s390 s390x
    sed -i -e 's/tty10/console/g' syslog-ng.conf.default
%endif

# fix python
sed -i 's|^#\s*!%{_bindir}/env python3|#!%{_bindir}/python3|' lib/merge-grammar.py
touch -r lib/cfg-grammar.y lib/merge-grammar.py

%build
%if %{with java}
autoreconf -fi
%endif
##
## build ####################################################
##
export CFLAGS="%{optflags}"

export AM_YFLAGS=-d

export BPFTOOL=/usr/sbin/bpftool

%configure \
	--prefix=%{_prefix}			\
	--enable-ipv6				\
	--enable-manpages			\
	--enable-tcp-wrapper			\
	--enable-spoof-source			\
	--sysconfdir=%{_sysconfdir}/syslog-ng		\
	--localstatedir=%{_localstatedir}/lib/syslog-ng	\
	--with-pidfile-dir=%{_localstatedir}/run	\
	--with-module-dir="%{_libdir}/syslog-ng"	\
	--with-default-modules="affile,afprog,afsocket,afuser,basicfuncs,csvparser,dbparser,syslogformat"	\
	--datadir="%{_datadir}"	\
	--without-compile-date			\
	--enable-ssl				\
%if %{with grpc}
        --enable-cpp                            \
        --enable-grpc                           \
%endif
%if %{with cloudauth}
        --enable-cloud-auth                     \
%else
        --disable-cloud-auth                    \
%endif
%if %{with snmp}
        --enable-afsnmp                         \
%else
        --disable-afsnmp                         \
%endif
%if %{with bpf}
        --enable-ebpf                           \
%endif
	--disable-native			\
%if %{with mqtt}
	--enable-mqtt				\
%endif
%if %{with smtp}
        --with-libesmtp=%{_prefix}/lib                \
%endif
	--enable-systemd			\
	--with-systemd-journal=system		\
%if %{with dbi}
	--enable-sql				\
%endif
        --enable-json                           \
	--enable-capabilities			\
%if %{with amqp}
        --enable-amqp                        \
%else
        --disable-amqp                       \
%endif
%if %{with mongodb}
        --enable-mongodb                        \
%else
        --disable-mongodb                       \
%endif
%if %{with redis}
	--enable-redis				\
%endif
%if %{with java}
       --enable-java                           \
%else
       --disable-java                          \
%endif
       --disable-java-modules                  \
%if %{with python}
	--enable-python				\
	--with-python=%{py_ver}			\
        --with-python-packages=none           \
%else
	--disable-python			\
%endif
        --enable-dynamic-linking

#
# - build syslog-ng
#
%make_build

%install
##
## install ##################################################
##
for dir in /sbin \
           %{_sysconfdir}/syslog-ng \
           %{_localstatedir}/lib/syslog-ng \
           %{_localstatedir}/run/syslog-ng \
%if 0%{?suse_version} >= 1500
           %{_fillupdir} ;
%else
           %{_localstatedir}/adm/fillup-templates ;
%endif
do
	test -d %{buildroot}/${dir} || \
	install -d -m755 %{buildroot}/${dir}
done
#
%make_install
#
install -d -m755 %{buildroot}%{_unitdir}/
install -c -m644 syslog-ng.service         %{buildroot}%{_unitdir}/
install -c -m755 syslog-ng-service-prepare %{buildroot}%{_sbindir}/

# install config.h (bnc#982487)
install -p -m644 config.h %{buildroot}%{_includedir}/%{name}

# install configs
install -m644 syslog-ng.conf.default \
              %{buildroot}/%{_sysconfdir}/syslog-ng/syslog-ng.conf
install -m644 %{_sourcedir}/syslog-ng.sysconfig \
              %{buildroot}/%{_fillupdir}/sysconfig.syslog-ng
# create empty /etc/syslog-ng/conf.d/
install -d -m755 %{buildroot}%{_sysconfdir}/syslog-ng/conf.d/

%if 0%{?suse_version} < 1550
# create a compatibility link in /sbin
ln -sf %{_sbindir}/syslog-ng %{buildroot}/sbin/
%endif

# don't package update-patterndb now
rm %{buildroot}%{_bindir}/update-patterndb

# delete java destination related files
rm -fr %{buildroot}%{_datadir}/syslog-ng/include/scl/elasticsearch/plugin.conf
rm -fr %{buildroot}%{_datadir}/syslog-ng/include/scl/elasticsearch/elastic-java.conf
rm -fr %{buildroot}%{_datadir}/syslog-ng/include/scl/hdfs/
rm -fr %{buildroot}%{_datadir}/syslog-ng/include/scl/kafka/

# create ghosts
install -d -m755 %{buildroot}%{syslog_ng_rundir}
touch            %{buildroot}%{syslog_ng_sockets_cfg}
chmod 644        %{buildroot}%{syslog_ng_sockets_cfg}

%pre
%{service_add_pre syslog-ng.service}

%post
##
## post install #############################################
##
/sbin/ldconfig
#
# remove obsolete variables
#
%{remove_and_set -n syslog SYSLOG_DAEMON SYSLOG_REQUIRES_NETWORK}
#
# add SYSLOG_NG_* variables if needed
#
%{fillup_only -ans syslog ng}
#
# create dirs, touch log default files
#
mkdir -p var/log
touch var/log/messages;  chmod 640 var/log/messages
touch var/log/mail;      chmod 640 var/log/mail
touch var/log/mail.info; chmod 640 var/log/mail.info
touch var/log/mail.warn; chmod 640 var/log/mail.warn
touch var/log/mail.err;  chmod 640 var/log/mail.err
#
# touch the additional log files we are using
#
touch var/log/acpid;            chmod 640 var/log/acpid
touch var/log/firewall;         chmod 640 var/log/firewall
touch var/log/NetworkManager;   chmod 640 var/log/NetworkManager
#
# generate empty additional-log-sockets.conf file
# see also syslog-ng.conf.default in pkg src dir.
#
additional_sockets="%{syslog_ng_sockets_cfg}"
install -d -m750 ${additional_sockets%/*}
cat >$additional_sockets <<EOF
source chroots { };
EOF
chmod 640 "${additional_sockets#/}"
#
# Enable the syslog-ng systemd service
#
# This macro enables based on a systemctl preset config file only
%{service_add_post syslog-ng.service}
# But we want to enable a syslog-daemon regardless of the preset;
# force the creation of a syslog.service alias link (bnc#790805).
# We do not check the obsolete SYSLOG_DAEMON variable as we want
# to switch when installing it and there is a provider conflict.
%{_bindir}/systemctl -f enable syslog-ng.service >/dev/null 2>&1 || :

%preun
##
## pre uninstall ############################################
##
%{service_del_preun syslog.socket}
%{service_del_preun syslog-ng.service}

%postun
##
## post uninstall ###########################################
##
#
# update linker caches
#
/sbin/ldconfig
#
# cleanup init scripts
#
%{service_del_postun syslog-ng.service}

%post -n libevtlog-4_11-0 -p /sbin/ldconfig
%postun -n libevtlog-4_11-0 -p /sbin/ldconfig

%post -n syslog-ng-grpc -p /sbin/ldconfig
%postun -n syslog-ng-grpc -p /sbin/ldconfig

%files
##
## file list ################################################
##
%license COPYING
%doc AUTHORS NEWS.md
%doc syslog-ng.conf.default
%if 0%{?suse_version} < 1550
/sbin/syslog-ng
%endif
%attr(755,root,root) %{_sbindir}/syslog-ng
%attr(755,root,root) %{_sbindir}/syslog-ng-ctl
%attr(755,root,root) %{_sbindir}/syslog-ng-debun
%attr(755,root,root) %{_sbindir}/syslog-ng-service-prepare
%attr(755,root,root) %{_bindir}/loggen
%attr(755,root,root) %{_bindir}/pdbtool
%attr(755,root,root) %{_bindir}/dqtool
%attr(755,root,root) %{_bindir}/persist-tool
%attr(755,root,root) %{_bindir}/slogencrypt
%attr(755,root,root) %{_bindir}/slogkey
%attr(755,root,root) %{_bindir}/slogverify
%attr(755,root,root) %{_bindir}/syslog-ng-update-virtualenv
%{_mandir}/man5/syslog-ng.conf.5%{?ext_man}
%{_mandir}/man8/syslog-ng.8%{?ext_man}
%{_mandir}/man1/pdbtool.1%{?ext_man}
%{_mandir}/man1/loggen.1%{?ext_man}
%{_mandir}/man1/syslog-ng-ctl.1%{?ext_man}
%{_mandir}/man1/dqtool.1%{?ext_man}
%{_mandir}/man1/syslog-ng-debun.1%{?ext_man}
%{_mandir}/man1/persist-tool.1.gz
%{_mandir}/man1/slogencrypt.1*
%{_mandir}/man1/slogkey.1*
%{_mandir}/man1/slogverify.1*
%{_mandir}/man7/secure-logging.7*
%dir %{_libdir}/syslog-ng
%dir %{_libdir}/syslog-ng/loggen
%dir %{_datadir}/syslog-ng
%dir %{_datadir}/syslog-ng/include
%dir %{_datadir}/syslog-ng/include/scl
%dir %{_datadir}/syslog-ng/include/scl/graphite
%dir %{_datadir}/syslog-ng/include/scl/nodejs
%dir %{_datadir}/syslog-ng/include/scl/pacct
%dir %{_datadir}/syslog-ng/include/scl/rewrite
%dir %{_datadir}/syslog-ng/include/scl/syslogconf
%dir %{_datadir}/syslog-ng/include/scl/system
%dir %{_datadir}/syslog-ng/include/scl/solaris
%dir %{_datadir}/syslog-ng/include/scl/mbox/
%dir %{_datadir}/syslog-ng/include/scl/apache/
%dir %{_datadir}/syslog-ng/include/scl/loggly/
%dir %{_datadir}/syslog-ng/include/scl/logmatic/
%dir %{_datadir}/syslog-ng/include/scl/cisco/
%dir %{_datadir}/syslog-ng/include/scl/snmptrap/
%dir %{_datadir}/syslog-ng/include/scl/osquery/
%dir %{_datadir}/syslog-ng/include/scl/windowseventlog/
%dir %{_datadir}/syslog-ng/include/scl/loadbalancer/
%dir %{_datadir}/syslog-ng/include/scl/cim/
%dir %{_datadir}/syslog-ng/include/scl/default-network-drivers/
%dir %{_datadir}/syslog-ng/include/scl/ewmm/
%dir %{_datadir}/syslog-ng/include/scl/iptables/
%dir %{_datadir}/syslog-ng/include/scl/sudo/
%dir %{_datadir}/syslog-ng/include/scl/graylog2/
%dir %{_datadir}/syslog-ng/include/scl/linux-audit/
%dir %{_datadir}/syslog-ng/include/scl/websense/
%dir %{_datadir}/syslog-ng/include/scl/collectd/
%dir %{_datadir}/syslog-ng/include/scl/netskope/
%dir %{_datadir}/syslog-ng/include/scl/junos/
%dir %{_datadir}/syslog-ng/include/scl/checkpoint/
%dir %{_datadir}/syslog-ng/include/scl/paloalto/
%dir %{_datadir}/syslog-ng/include/scl/sumologic/
%dir %{_datadir}/syslog-ng/include/scl/cee/
%dir %{_datadir}/syslog-ng/include/scl/discord/
%dir %{_datadir}/syslog-ng/include/scl/fortigate/
%dir %{_datadir}/syslog-ng/include/scl/mariadb/
%dir %{_datadir}/syslog-ng/include/scl/python/
%dir %{_datadir}/syslog-ng/include/scl/splunk/
%dir %{_datadir}/syslog-ng/include/scl/logscale/
%dir %{_datadir}/syslog-ng/include/scl/opensearch/
%dir %{_datadir}/syslog-ng/include/scl/google/
%dir %{_datadir}/syslog-ng/include/scl/openobserve/
%dir %{_datadir}/syslog-ng/include/scl/pgsql/
%dir %{_datadir}/syslog-ng/include/scl/pihole/
%dir %{_datadir}/syslog-ng/include/scl/qbittorrent/
%dir %{_datadir}/syslog-ng/include/scl/darwinosl/
%dir %{_datadir}/syslog-ng/include/scl/arr/
%dir %{_datadir}/syslog-ng/include/scl/jellyfin/
%dir %{_datadir}/syslog-ng/include/scl/azure/
%dir %{_datadir}/syslog-ng/include/scl/freebsd-audit/
%dir %{_datadir}/syslog-ng/include/scl/stats-exporter/
%dir %{_datadir}/syslog-ng/xsd
%dir %{_sysconfdir}/syslog-ng
%dir %{_sysconfdir}/syslog-ng/conf.d
%config(noreplace) %{_sysconfdir}/syslog-ng/syslog-ng.conf
%{_unitdir}/syslog-ng.service
%dir %{_localstatedir}/lib/syslog-ng
%attr(0755,root,root) %dir %ghost %{syslog_ng_rundir}
%attr(0644,root,root) %ghost %{syslog_ng_sockets_cfg}
%if 0%{?suse_version} >= 1500
%{_fillupdir}/sysconfig.syslog-ng
%else
%{_localstatedir}/adm/fillup-templates/sysconfig.syslog-ng
%endif
%{_libdir}/libsyslog-ng-*.so.*
%{_libdir}/libsecret-storage.so.*
%{_libdir}/libloggen_helper-*.so.*
%{_libdir}/libloggen_plugin-*.so.*
%attr(755,root,root) %{_libdir}/syslog-ng/libadd-contextual-data.so
%attr(755,root,root) %{_libdir}/syslog-ng/libsecure-logging.so
%if %{with amqp}
%attr(755,root,root) %{_libdir}/syslog-ng/libafamqp.so
%endif
%attr(755,root,root) %{_libdir}/syslog-ng/libaffile.so
%attr(755,root,root) %{_libdir}/syslog-ng/libafprog.so
%attr(755,root,root) %{_libdir}/syslog-ng/libappmodel.so
%if %{with mongodb}
%attr(755,root,root) %{_libdir}/syslog-ng/libafmongodb.so
%endif
%attr(755,root,root) %{_libdir}/syslog-ng/libafsocket.so
%attr(755,root,root) %{_libdir}/syslog-ng/libafstomp.so
%attr(755,root,root) %{_libdir}/syslog-ng/libafuser.so
%attr(755,root,root) %{_libdir}/syslog-ng/libbasicfuncs.so
%attr(755,root,root) %{_libdir}/syslog-ng/libconfgen.so
%attr(755,root,root) %{_libdir}/syslog-ng/libcsvparser.so
%attr(755,root,root) %{_libdir}/syslog-ng/libcryptofuncs.so
%attr(755,root,root) %{_libdir}/syslog-ng/libexamples.so
%attr(755,root,root) %{_libdir}/syslog-ng/libgraphite.so
%attr(755,root,root) %{_libdir}/syslog-ng/libjson-plugin.so
%attr(755,root,root) %{_libdir}/syslog-ng/libkvformat.so
%attr(755,root,root) %{_libdir}/syslog-ng/liblinux-kmsg-format.so
%attr(755,root,root) %{_libdir}/syslog-ng/libpseudofile.so
%attr(755,root,root) %{_libdir}/syslog-ng/libcef.so
%attr(755,root,root) %{_libdir}/syslog-ng/libtimestamp.so
%attr(755,root,root) %{_libdir}/syslog-ng/libdisk-buffer.so
%attr(755,root,root) %{_libdir}/syslog-ng/libtfgetent.so
%attr(755,root,root) %{_libdir}/syslog-ng/libmap-value-pairs.so
%attr(755,root,root) %{_libdir}/syslog-ng/libtags-parser.so
%attr(755,root,root) %{_libdir}/syslog-ng/libxml.so
%attr(755,root,root) %{_libdir}/syslog-ng/libsdjournal.so
%attr(755,root,root) %{_libdir}/syslog-ng/libsyslogformat.so
%attr(755,root,root) %{_libdir}/syslog-ng/libstardate.so
%attr(755,root,root) %{_libdir}/syslog-ng/libsystem-source.so
%attr(755,root,root) %{_libdir}/syslog-ng/libhook-commands.so
%attr(755,root,root) %{_libdir}/syslog-ng/loggen/libloggen_socket_plugin.so
%attr(755,root,root) %{_libdir}/syslog-ng/loggen/libloggen_ssl_plugin.so
%attr(755,root,root) %{_libdir}/syslog-ng/libazure-auth-header.so
%attr(755,root,root) %{_libdir}/syslog-ng/libregexp-parser.so
%attr(755,root,root) %{_libdir}/syslog-ng/librate-limit-filter.so
%attr(755,root,root) %{_libdir}/syslog-ng/libcorrelation.so
%attr(755,root,root) %{_libdir}/syslog-ng/libmetrics-probe.so
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/graphite/README
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/graphite/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/nodejs/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/pacct/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/rewrite/cc-mask.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/system/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/syslogconf/README
%attr(755,root,root) %{_datadir}/syslog-ng/include/scl/syslogconf/convert-syslogconf.awk
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/syslogconf/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/cim/template.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/solaris/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/mbox/mbox.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/apache/apache.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/loggly/loggly.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/logmatic/logmatic.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/cisco/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/snmptrap/snmptrapd-source.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/osquery/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/windowseventlog/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/windowseventlog/windowseventlog.xml
%attr(755,root,root) %{_datadir}/syslog-ng/include/scl/loadbalancer/gen-loadbalancer.sh
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/loadbalancer/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/cim/adapter.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/default-network-drivers/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/ewmm/ewmm.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/iptables/iptables.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/sudo/sudo.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/graylog2/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/linux-audit/linux-audit.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/websense/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/collectd/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/netskope/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/junos/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/checkpoint/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/paloalto/panos.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/sumologic/sumologic.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/cee/adapter.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/discord/discord.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/fortigate/fortigate.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/mariadb/audit.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/python/python-modules.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/splunk/splunk.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/logscale/logscale.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/opensearch/opensearch.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/google/google-pubsub.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/openobserve/openobserve.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/pgsql/pgsql.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/pihole/pihole.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/qbittorrent/qbittorrent.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/darwinosl/darwinosl-metadata-db.csv
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/darwinosl/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/arr/arr.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/jellyfin/jellyfin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/azure/azure-monitor.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/freebsd-audit/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/stats-exporter/plugin.conf
%attr(644,root,root) %{_datadir}/syslog-ng/smart-multi-line.fsm
%attr(644,root,root) %{_datadir}/syslog-ng/xsd/*
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl.conf

%files -n libevtlog-4_11-0
%{_libdir}/libevtlog-*.so.*

%if %{with snmp}
%files snmp
%attr(755,root,root) %{_libdir}/syslog-ng/libafsnmp.so
%endif

%if %{with http}
%files http
%attr(755,root,root) %{_libdir}/syslog-ng/libhttp.so
%dir %{_datadir}/syslog-ng/include/scl/telegram/
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/telegram/telegram.conf
%dir %{_datadir}/syslog-ng/include/scl/slack/
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/slack/slack.conf
%dir %{_datadir}/syslog-ng/include/scl/elasticsearch/
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/elasticsearch/elastic-http.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/elasticsearch/elastic-datastream.conf

%endif

%if %{with dbi}
%files sql
%dir %{_libdir}/syslog-ng
%attr(755,root,root) %{_libdir}/syslog-ng/libafsql.so

%endif

%if %{with grpc}

%files grpc
%attr(755,root,root) %{_libdir}/libgrpc-protos.so.*

%files opentelemetry
%attr(755,root,root) %{_libdir}/syslog-ng/libotel.so

%files loki
%attr(755,root,root) %{_libdir}/syslog-ng/libloki.so

%files bigquery
%attr(755,root,root) %{_libdir}/syslog-ng/libbigquery.so

%files clickhouse
%attr(755,root,root) %{_libdir}/syslog-ng/libclickhouse.so

%files pubsub
%attr(755,root,root) %{_libdir}/syslog-ng/libpubsub.so

%endif

%if %{with cloudauth}

%files cloudauth
%attr(755,root,root) %{_libdir}/syslog-ng/libcloud_auth.so

%endif

%if %{with bpf}

%files bpf
%attr(755,root,root) %{_libdir}/syslog-ng/libebpf.so

%endif

%files devel
%if %{with grpc}
%attr(644,root,root) %{_libdir}/libgrpc-protos.la
%{_libdir}/libgrpc-protos.so
%endif
%attr(644,root,root) %{_libdir}/libsyslog-ng.la
%attr(644,root,root) %{_libdir}/libevtlog.la
%attr(644,root,root) %{_libdir}/libsecret-storage.la
%attr(644,root,root) %{_libdir}/libloggen_helper.la
%attr(644,root,root) %{_libdir}/libloggen_plugin.la
%attr(644,root,root) %{_libdir}/syslog-ng/*.la
%attr(755,root,root) %{_libdir}/syslog-ng/loggen/libloggen_socket_plugin.la
%attr(755,root,root) %{_libdir}/syslog-ng/loggen/libloggen_ssl_plugin.la
%{_libdir}/libsyslog-ng.so
%{_libdir}/libevtlog.so
%{_libdir}/libsecret-storage.so
%{_libdir}/libloggen_helper.so
%{_libdir}/libloggen_plugin.so
%attr(644,root,root) %{_libdir}/pkgconfig/syslog-ng.pc
%dir %{_includedir}/syslog-ng
%attr(-,root,root) %{_includedir}/syslog-ng/*
%dir %{_datadir}/syslog-ng/tools
%attr(755,root,root) %{_datadir}/syslog-ng/tools/merge-grammar.py
%attr(644,root,root) %{_datadir}/syslog-ng/tools/cfg-grammar.y
%attr(644,root,root) %{_datadir}/syslog-ng/tools/lex-rules.am
%attr(755,root,root) %{_datadir}/syslog-ng/tools/system-expand.sh

%if %{with python}
%files python
%attr(755,root,root) %{_libdir}/syslog-ng/libmod-python.so
%defattr(-,root,root)
%{_libdir}/syslog-ng/python/syslogng-1.0-py%{py_ver}.egg-info
%dir %{_libdir}/syslog-ng/python
%dir %{_libdir}/syslog-ng/python/syslogng
%{_libdir}/syslog-ng/python/syslogng/*
%dir %{_sysconfdir}/syslog-ng/python/
%{_sysconfdir}/syslog-ng/python/README.md
%{_libdir}/syslog-ng/python/requirements.txt
%exclude %{_libdir}/syslog-ng/python/syslogng/modules/

%files python-modules
%dir %{_libdir}/syslog-ng/python/syslogng/modules/
%{_libdir}/syslog-ng/python/syslogng/modules/*

%endif

%if %{with java}
%files java
%attr(755,root,root) %{_libdir}/syslog-ng/libmod-java.so
%dir %{_libdir}/syslog-ng/java-modules
%attr(755,root,root) %{_libdir}/syslog-ng/java-modules/syslog-ng-core.jar

%endif

%if %{with smtp}
%files smtp
%dir %{_libdir}/syslog-ng
%attr(755,root,root) %{_libdir}/syslog-ng/libafsmtp.so

%endif

%if %{with geoip}
%files geoip
%dir %{_libdir}/syslog-ng
%attr(755,root,root) %{_libdir}/syslog-ng/libgeoip2-plugin.so

%endif

%if %{with redis}
%files redis
%dir %{_libdir}/syslog-ng
%attr(755,root,root) %{_libdir}/syslog-ng/libredis.so

%endif

%if %{with mqtt}

%files mqtt
%defattr(-,root,root)
%dir %{_libdir}/syslog-ng
%attr(755,root,root) %{_libdir}/syslog-ng/libmqtt.so

%endif

%changelog
