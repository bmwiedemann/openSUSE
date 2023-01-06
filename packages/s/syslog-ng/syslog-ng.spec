#
# spec file for package syslog-ng
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


%define         syslog_ng_sockets_cfg	%{syslog_ng_rundir}/additional-log-sockets.conf
%global		py_ver	 %(rpm -qf %{_bindir}/python3 --qf "%%{version}" | awk -F. '{print $1"."$2}')

#redis only in openSUSE
%if !0%{?is_opensuse}
%bcond_with	redis
%else
%bcond_without	redis
%endif

# mqtt only in Tumbleweed
%if 0%{?suse_version} > 1500
%bcond_without	mqtt
%else
%bcond_with	mqtt
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
%bcond_without	curl
%bcond_without	smtp
# mongodb & amqp C clients are no more bundled with syslog-ng sources
# and not yet available in openSUSE
# leaving here for future usage
%bcond_with	mongodb
%bcond_with	amqp
Name:           syslog-ng
Version:        3.37.1
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
Patch0:         syslog-ng-nojavah.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libcap-devel
BuildRequires:  libjson-devel
BuildRequires:  libnet-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  net-snmp-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libsystemd)
#!BuildIgnore:  rsyslog
Requires(pre):  %fillup_prereq
Requires(pre):  syslog-service >= 2.0
Conflicts:      syslog
Provides:       syslog
Provides:       sysvinit(syslog)
Obsoletes:      syslog-ng-json
%if %{with mqtt}
BuildRequires:  libpaho-mqtt-devel
%endif
%if %{with smtp}
BuildRequires:  libesmtp-devel
%endif
%if %{with curl}
BuildRequires:  libcurl-devel
%endif
%if %{with geoip}
%if 0%{?leap_version} >= 420200
BuildRequires:  libmaxminddb-devel
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  libmaxminddb-devel
%endif
%endif
%if %{with redis}
BuildRequires:  hiredis-devel
%endif
%if %{with dbi}
BuildRequires:  libdbi-devel
%endif
%if %{with java}
BuildRequires:  java-devel >= 1.8
%endif
%if %{with python}
BuildRequires:  python3-devel
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

%package -n libevtlog-3_37-0
Summary:        Syslog-ng event logger library runtime
Group:          System/Libraries

%description -n libevtlog-3_37-0
The EventLog library provides an alternative to the simple syslog()
API provided on UNIX systems. Compared to syslog, EventLog adds
structured messages.

EventLog provides an interface to build, format and output an event
record. The exact format and output method can be customized by the
administrator via a configuration file.

This package is now merged into syslog-ng.

%package curl
Summary:        HTTP destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description curl
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

%package python
Summary:        Python destination support for syslog-ng
Group:          System/Daemons
Requires:       %{name} = %{version}

%description python
This package provides Python destination support for syslog-ng.

%package devel
Summary:        Development files for syslog-ng
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Provides:       libevtlog-devel = 0.2.13
Obsoletes:      libevtlog-devel <= 0.2.13
Requires:       glib2-devel
Requires:       glibc-devel
Requires:       libcap-devel
Requires:       libopenssl-1_1-devel
Requires:       pcre-devel
Requires:       systemd-devel

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

%description mqtt
This package provides MQTT support for syslog-ng

%prep
%setup -q -n syslog-ng-%{version}
%patch0 -p1
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
# sed -i 's|^#\s*!%{_bindir}/env python|#!%{_bindir}/python3|' lib/merge-grammar.py
# touch -r lib/cfg-grammar.y lib/merge-grammar.py

%build
autoreconf -fi
##
## build ####################################################
##
export CFLAGS="%{optflags}"

export AM_YFLAGS=-d

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
        --enable-afsnmp                         \
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

%post -n libevtlog-3_37-0 -p /sbin/ldconfig
%postun -n libevtlog-3_37-0 -p /sbin/ldconfig

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
%dir %{_datadir}/syslog-ng/include/scl/kubernetes/
%dir %{_datadir}/syslog-ng/include/scl/mariadb/
%dir %{_datadir}/syslog-ng/xsd
%dir %{_sysconfdir}/syslog-ng
%dir %{_sysconfdir}/syslog-ng/conf.d
%config(noreplace) %{_sysconfdir}/syslog-ng/syslog-ng.conf
%config(noreplace) %{_sysconfdir}/syslog-ng/scl.conf
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
%attr(755,root,root) %{_libdir}/syslog-ng/libdbparser.so
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
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/loadbalancer/gen-loadbalancer.sh
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
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/kubernetes/kubernetes.conf
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/mariadb/audit.conf
%attr(644,root,root) %{_datadir}/syslog-ng/xsd/*

%files -n libevtlog-3_37-0
%{_libdir}/libevtlog-*.so.*

%files snmp
%attr(755,root,root) %{_libdir}/syslog-ng/libafsnmp.so

%if %{with curl}
%files curl
%attr(755,root,root) %{_libdir}/syslog-ng/libhttp.so
%dir %{_datadir}/syslog-ng/include/scl/telegram/
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/telegram/telegram.conf
%dir %{_datadir}/syslog-ng/include/scl/slack/
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/slack/slack.conf
%dir %{_datadir}/syslog-ng/include/scl/elasticsearch/
%attr(644,root,root) %{_datadir}/syslog-ng/include/scl/elasticsearch/elastic-http.conf

%endif

%if %{with dbi}
%files sql
%dir %{_libdir}/syslog-ng
%attr(755,root,root) %{_libdir}/syslog-ng/libafsql.so

%endif

%files devel
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
%attr(644,root,root) %{_datadir}/syslog-ng/tools/merge-grammar.py
%attr(644,root,root) %{_datadir}/syslog-ng/tools/cfg-grammar.y
%attr(644,root,root) %{_datadir}/syslog-ng/tools/lex-rules.am
%attr(644,root,root) %{_datadir}/syslog-ng/tools/system-expand.sh

%if %{with python}
%files python
%attr(755,root,root) %{_libdir}/syslog-ng/libmod-python.so
%{_libdir}/syslog-ng/python/syslogng-1.0-py%{py_ver}.egg-info
%dir %{_libdir}/syslog-ng/python
%dir %{_libdir}/syslog-ng/python/syslogng
%{_libdir}/syslog-ng/python/syslogng/*

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
%if 0%{?leap_version} >= 420200
%attr(755,root,root) %{_libdir}/syslog-ng/libgeoip2-plugin.so
%endif
%if 0%{?suse_version} > 1320
%attr(755,root,root) %{_libdir}/syslog-ng/libgeoip2-plugin.so
%endif

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
