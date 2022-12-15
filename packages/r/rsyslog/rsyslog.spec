#
# spec file for package rsyslog
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# drop this with next release when doc tarball version lines up
%define rsyslog_major 8.2212
%define rsyslog_patch 0
Name:           rsyslog
Summary:        The enhanced syslogd for Linux and Unix
License:        Apache-2.0 AND GPL-3.0-or-later
Group:          System/Daemons
Version:        %{rsyslog_major}.%{rsyslog_patch}
Release:        0
%bcond_with     udpspoof
%bcond_with     dbi
%bcond_with     pkgconfig
%if 0%{?suse_version} > 1230
%bcond_without  journal
%else
%bcond_with     journal
%endif
%bcond_without  gssapi
%bcond_without  gnutls
%bcond_without  openssl
%bcond_without  gcrypt
%bcond_without  mysql
%bcond_without  pgsql
%bcond_without  relp
%bcond_without  rfc3195
%bcond_without  snmp
%bcond_without  diagtools
%bcond_without  mmnormalize
%bcond_without  elasticsearch
%bcond_without  omhttpfs
%bcond_without  omamqp1
%bcond_without  tcl
%bcond_without  kafka
# https://github.com/rsyslog/rsyslog/issues/1355
%bcond_with	maxminddb
# contributed modules not built for various reasons
# --enable-mmgrok - grok not in factory
# TODO: ... doesnt have a proper configure check but wants hdfs.h
%bcond_with     hdfs
%bcond_with     mongodb
%bcond_with     hiredis
%bcond_with     zeromq

%define         rsyslogdocdir               %{_docdir}/%{name}
%if %{defined _rundir}
%define         rsyslog_rundir              %{_rundir}/rsyslog
%else
%define         rsyslog_rundir              %{_localstatedir}/run/rsyslog
%endif
%define         rsyslog_sockets_cfg         %{rsyslog_rundir}/additional-log-sockets.conf
%define         rsyslog_module_dir_nodeps   %{_libdir}/rsyslog/
%define         rsyslog_module_dir_withdeps %{_libdir}/rsyslog/
URL:            http://www.rsyslog.com/
# Upstream library deprecated and we want to support migration
Obsoletes:      %{name}-module-guardtime <= 8.38.0
Provides:       syslog
Provides:       sysvinit(syslog)
Conflicts:      otherproviders(syslog)
Requires(pre):  %fillup_prereq
Requires(pre):  syslog-service >= 2.0
%{?systemd_ordering}
BuildRequires:  pkgconfig(systemd) >= 209
%if %{with journal}
BuildRequires:  pkgconfig(libsystemd) >= 234
%endif
# for patch1
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
#
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  flex
BuildRequires:  libzstd-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if %{with rfc3195}
%if %{with pkgconfig}
BuildRequires:  pkgconfig(liblogging-rfc3195) >= 1.0.1
%else
BuildRequires:  liblogging-devel
%endif
%endif
%if %{with pkgconfig}
BuildRequires:  pkgconfig(liblogging-stdlog) >= 1.0.1
%else
BuildRequires:  liblogging-devel
%endif
%if %{with omhttpfs}
BuildRequires:  curl-devel >= 7.0.0
%endif
%if %{with omamqp1}
%if %{with pkgconfig}
BuildRequires:  pkgconfig(libqpid-proton) >= 0.9
%else
BuildRequires:  qpid-proton-devel >= 0.9
%endif
%endif
%if %{with hiredis}
BuildRequires:  hiredis-devel >= 0.10.1
%endif
%if %{with mongodb}
# TODO: PKG_CHECK_MODULES(LIBMONGO_CLIENT, libmongo-client >= 0.1.4)
%endif
%if %{with zeromq}
BuildRequires:  czmq-devel >= 3.0.2
%endif
%if %{with kafka}
BuildRequires:  librdkafka-devel
Requires:       librdkafka1
%endif
%if %{with gssapi}
BuildRequires:  krb5-devel
%endif
%if %{with gnutls}
BuildRequires:  libgnutls-devel
%endif
%if %{with openssl}
BuildRequires:  pkgconfig(openssl)
%endif
%if %{with gcrypt}
BuildRequires:  libgcrypt-devel
%endif
%if %{with dbi}
BuildRequires:  libdbi-devel
%endif
%if %{with mysql}
BuildRequires:  mysql-devel
%endif
%if %{with snmp}
BuildRequires:  net-snmp-devel
%endif
%if %{with pgsql}
BuildRequires:  postgresql-devel
%endif
%if %{with relp}
# RELP support
%if %{with pkgconfig}
BuildRequires:  pkgconfig(relp) >= 1.2.14
%else
BuildRequires:  librelp-devel >= 1.2.14
%endif
%endif
%if %{with udpspoof}
# UDP spoof support
BuildRequires:  libnet-devel
%endif
%if %{with mmnormalize}
# mmnormalize support
%if %{with pkgconfig}
BuildRequires:  pkgconfig(lognorm) >= 2.0.3
%else
BuildRequires:  liblognorm-devel >= 2.0.3
%endif
%endif
%if %{with maxminddb}
BuildRequires:  pkgconfig(libmaxminddb)
%endif
#
# mmjsonparse needs liblognorm,
# but json check is unconditional
%if %{with pkgconfig}
BuildRequires:  pkgconfig(libestr) >= 0.1.9
BuildRequires:  pkgconfig(libfastjson) >= 0.99.8
BuildRequires:  pkgconfig(uuid) >= 2.21.0
%else
BuildRequires:  libestr-devel
BuildRequires:  libfastjson-devel >= 0.99.7
BuildRequires:  libuuid-devel
%endif
%if %{with tcl}
%if %{with pkgconfig}
BuildRequires:  pkgconfig(tcl)
%else
BuildRequires:  tcl-devel
%endif
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://www.rsyslog.com/files/download/%{name}/%{name}-%{version}.tar.gz
Source1:        rsyslog.sysconfig
Source2:        rsyslog.conf.in
Source3:        rsyslog.service
Source4:        rsyslog.d.remote.conf.in
Source5:        rsyslog-service-prepare.in
Source6:        usr.sbin.rsyslogd
Source7:        module-mysql
Source8:        module-snmp
Source9:        module-udpspoof
Source14:       https://www.rsyslog.com/files/download/rsyslog/rsyslog-doc-%{rsyslog_major}.0.tar.gz
Source16:       journald-rsyslog.conf
Source17:       acpid.frule
Source18:       firewall.frule
Source19:       NetworkManager.frule

# this is a dirty hack since % dir does only work for the specified directory and nothing above
# but I want to be able to switch this to /etc/apparmor.d once the profiles received more testing
%define APPARMOR_PROFILE_PATH /usr/share/apparmor/extra-profiles
%define APPARMOR_PROFILE_PATH_DIR_COMMANDS %dir /usr/share/apparmor \
                                           %dir /usr/share/apparmor/extra-profiles \
                                           %dir /usr/share/apparmor/extra-profiles/rsyslog.d

%description
Rsyslog is an enhanced multi-threaded syslogd supporting, among others,
MySQL, syslog/tcp, RFC 3195, permitted sender lists, filtering on any
message part, and fine grain output format control. It is quite
compatible to stock sysklogd and can be used as a drop-in replacement.
Its advanced features make it suitable for enterprise-class, encryption
protected syslog relay chains while at the same time being very easy to
setup for the novice user.

%package doc
Summary:        Additional documentation for rsyslog
Group:          System/Daemons

%description doc
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This package provides additional documentation for rsyslog.

%if %{with diagtools}

%package diag-tools
Requires:       %{name} = %{version}
Summary:        Diagnostic tools
Group:          System/Daemons

%description diag-tools
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This package provides additional diagnostic tools (small helpers,
usually not needed).

%endif

%if %{with gssapi}

%package module-gssapi
Requires:       %{name} = %{version}
Summary:        GSS-API support module for rsyslog
Group:          System/Daemons

%description module-gssapi
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides the support to receive syslog messages from the
network protected via Kerberos 5 encryption and authentication.

%endif

%if %{with mysql}

%package module-mysql
Requires:       %{name} = %{version}
Summary:        MySQL support module for rsyslog
Group:          System/Daemons

%description module-mysql
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This package provides a module with the support for logging into MySQL
databases.

%endif

%if %{with pgsql}

%package module-pgsql
Requires:       %{name} = %{version}
Summary:        PostgreSQL support module for rsyslog
Group:          System/Daemons

%description module-pgsql
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides the support for logging into PostgreSQL databases.

%endif

%if %{with dbi}

%package module-dbi
Requires:       %{name} = %{version}
Summary:        Database support via DBI
Group:          System/Daemons

%description module-dbi
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This package provides a module with the support for logging into DBI
supported databases.

%endif

%if %{with snmp}

%package module-snmp
Requires:       %{name} = %{version}
Summary:        SNMP support module for rsyslog
Group:          System/Daemons

%description module-snmp
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides the ability to send syslog messages as an SNMPv1 &
v2c traps.

%endif

%if %{with gnutls}

%package module-gtls
Requires:       %{name} = %{version}
Summary:        TLS encryption support module for rsyslog
Group:          System/Daemons

%description module-gtls
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides the ability for TLS encrypted TCP logging using
the GnuTLS library.
%endif

%if %{with openssl}

%package module-ossl
Requires:       %{name} = %{version}
Summary:        TLS encryption support module for rsyslog
Group:          System/Daemons

%description module-ossl
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides the ability for TLS encrypted TCP logging using
the OpenSSL library.
%endif

%if %{with gcrypt}

%package module-gcrypt
Requires:       %{name} = %{version}
Summary:        Libgcrypt log file encryption support module for rsyslog
Group:          System/Daemons

%description module-gcrypt
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides log file encryption support using libgcrypt and
a rsgtutil utility to manage the files.
%endif

%if %{with relp}

%package module-relp
Requires:       %{name} = %{version}
Summary:        RELP protocol support module for syslog
Group:          System/Daemons

%description module-relp
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides Reliable Event Logging Protocol support.

%endif

%if %{with mmnormalize}

%package module-mmnormalize
Requires:       %{name} = %{version}
Summary:        Contains the mmnormalize support module for syslog
Group:          System/Daemons

%description module-mmnormalize
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides log normalizing support.

%endif

%if %{with udpspoof}

%package module-udpspoof
Requires:       %{name} = %{version}
Summary:        UDP spoof support module for syslog
Group:          System/Daemons

%description module-udpspoof
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides a UDP forwarder that allows changing the sender address.

%endif

%if %{with elasticsearch}

%package module-elasticsearch
Requires:       %{name} = %{version}
Summary:        ElasticSearch output module for syslog
Group:          System/Daemons

%description module-elasticsearch
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support to output to an ElasticSearch database.

%endif

%if %{with omhttpfs}

%package module-omhttpfs
Requires:       %{name} = %{version}
Summary:        HDFS via HTTP output module for syslog
Group:          System/Daemons

%description module-omhttpfs
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support to output to HDFS via HTTP.

%endif

%if %{with hdfs}

%package module-hdfs
Requires:       %{name} = %{version}
Summary:        HDFS output module for syslog
Group:          System/Daemons

%description module-hdfs
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support to output to an HDFS database.

%endif

%if %{with mongodb}

%package module-mongodb
Requires:       %{name} = %{version}
Summary:        MongoDB output module for syslog
Group:          System/Daemons

%description module-mongodb
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support to output to a MongoDB database.

%endif

%if %{with hiredis}

%package module-hiredis
Requires:       %{name} = %{version}
Summary:        Redis output module for syslog
Group:          System/Daemons

%description module-hiredis
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support to output to a Redis database.

%endif

%if %{with zeromq}

%package module-zeromq
Requires:       %{name} = %{version}
Summary:        ZeroMQ support module for syslog
Group:          System/Daemons

%description module-zeromq
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support for ZeroMQ.

%endif

%if %{with kafka}

%package module-kafka
Requires:       %{name} = %{version}
Summary:        Kafka support module for syslog
Group:          System/Daemons

%description module-kafka
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support for Kafka.

%endif

%if %{with omamqp1}
%package module-omamqp1
Requires:       %{name} = %{version}
Summary:        AMQP support module for syslog
Group:          System/Daemons

%description module-omamqp1
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides support for AMQP.
%endif

%if %{with tcl}
%package module-omtcl
Requires:       %{name} = %{version}
Summary:        TCL output module for rsyslog
Group:          System/Daemons

%description module-omtcl
Rsyslog is an enhanced multi-threaded syslog daemon. See rsyslog
package.

This module provides an output module for TCL.
%endif

%prep
%setup -q -a 14
#
for file in rsyslog-service-prepare; do
	sed \
	-e 's;RUN_DIR;%{rsyslog_rundir};g' \
	-e 's;ADDITIONAL_SOCKETS;%{rsyslog_sockets_cfg};g' \
	"%{_sourcedir}/${file}.in" > "${file}"
done

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -W -Wall -I../grammar -I../../grammar"
# needs java
#        --enable-gui            \

# for patch1
autoreconf -fiv

%configure			\
	--with-moddirs=%{rsyslog_module_dir_withdeps} \
	--enable-option-checking	\
	--enable-largefile	\
	--enable-regexp		\
	--enable-klog		\
	--enable-kmsg		\
	--enable-inet		\
	--enable-unlimited-select	\
	--enable-rsyslogd	\
	--enable-liblogging-stdlog	\
%if %{with elasticsearch}
	--enable-elasticsearch	\
%endif
%if %{with kafka}
	--enable-imkafka		\
	--enable-omkafka		\
%endif
%if %{with omhttpfs}
	--enable-omhttpfs	\
%endif
%if %{with gnutls}
	--enable-gnutls		\
%endif
%if %{with openssl}
	--enable-openssl	\
%endif
%if %{with gssapi}
	--enable-gssapi-krb5	\
%endif
%if %{with dbi}
	--enable-libdbi		\
%endif
%if %{with mysql}
	--enable-mysql		\
%endif
%if %{with pgsql}
	--enable-pgsql		\
%endif
%if %{with relp}
	--enable-relp		\
%endif
%if %{with rfc3195}
        --enable-rfc3195        \
%endif
%if %{with snmp}
	--enable-snmp		\
	--enable-mmsnmptrapd	\
%endif
	--enable-mail		\
	--enable-imfile		\
	--enable-imptcp		\
	--enable-impstats	\
	--enable-omprog		\
	--enable-omuxsock	\
%if %{with udpspoof}
	--enable-omudpspoof	\
%endif
	--enable-omstdout	\
	--enable-pmlastmsg	\
	--enable-pmcisconames	\
	--enable-pmaixforwardedfrom	\
	--enable-pmsnare	\
	--enable-pmnull		\
	--enable-pmnormalize	\
	--enable-omruleset	\
	--enable-omhttp		\
%if %{with mmnormalize}
	--enable-mmnormalize \
	--enable-mmjsonparse	\
	--enable-mmaudit	\
%endif
%if %{with hdfs}
	--enable-omhdfs		\
%endif
%if %{with mongodb}
	--enable-ommongodb	\
%endif
%if %{with omamqp1}
	--enable-omamqp1	\
%endif
%if %{with hiredis}
	--enable-omhiredis	\
%endif
%if %{with zeromq}
	--enable-imzmq3		\
	--enable-omzmq3		\
%endif
%if %{with diagtools}
	--enable-imdiag		\
	--enable-diagtools	\
%endif
%if %{with journal}
	--enable-imjournal	\
	--enable-omjournal	\
%endif
	--enable-mmanon		\
	--enable-mmaudit	\
	--enable-mmkubernetes 	\
	--enable-mmjsonparse	\
	--enable-mmutf8fix	\
	--enable-mmcount	\
	--enable-mmsequence	\
	--enable-mmfields	\
	--enable-mmpstrucdata	\
	--enable-mmrfc5424addhmac \
	--enable-mmrm1stspace	\
	--enable-pmciscoios \
	--enable-pmpanngfw	\
%if %{with gcrypt}
	--enable-libgcrypt	\
%else
	--disable-libgcrypt	\
%endif
%if %{with tcl}
	--enable-omtcl		\
%endif
%if %{with maxminddb}
	--enable-mmdblookup	\
%endif
	--enable-usertools	\
	--disable-static

make %{?_smp_mflags:%{_smp_mflags}} V=1

%install
make install DESTDIR="%{buildroot}"  V=1
#
rm -f %{buildroot}%{rsyslog_module_dir_nodeps}/*.la
#
# move all modules linking libraries in /usr to /usr/lib[64]
# the user has to specify them with full path then...
install -d -m0755 %{buildroot}%{rsyslog_module_dir_withdeps}
if test "%{rsyslog_module_dir_nodeps}" != "%{rsyslog_module_dir_withdeps}" ; then
	for mod in  \
%if %{with gnutls}
		lmnsd_gtls.so \
%endif
%if %{with openssl}
		lmnsd_ossl.so \
%endif
%if %{with gcrypt}
		lmcry_gcry.so \
%endif
%if %{with gssapi}
		omgssapi.so imgssapi.so lmgssutil.so \
%endif
%if %{with dbi}
		omlibdbi.so \
%endif
%if %{with mysql}
		ommysql.so \
%endif
%if %{with pgsql}
		ompgsql.so \
%endif
%if %{with relp}
		imrelp.so omrelp.so \
%endif
%if %{with snmp}
		omsnmp.so \
%endif
%if %{with mmnormalize}
		mmnormalize.so  \
		mmjsonparse.so \
		mmaudit.so \
%endif
%if %{with elasticsearch}
		omelasticsearch.so \
%endif
%if %{with omhttpfs}
		omhttpfs.so \
%endif
%if %{with kafka}
		imkafka.so \
		omkafka.so \
%endif
	; do
		mv -f %{buildroot}%{rsyslog_module_dir_nodeps}/$mod \
		      %{buildroot}%{rsyslog_module_dir_withdeps}
	done
fi
%if !0%{?usrmerged}
	install -d -m0755 %{buildroot}/sbin
	ln -sf %{_sbindir}/rsyslogd $RPM_BUILD_ROOT/sbin/rsyslogd
%endif
# it is simply broken (bnc#890228)
rm -f $RPM_BUILD_ROOT%{_sbindir}/zpipe
#
install -m755 rsyslog-service-prepare %{buildroot}%{_sbindir}/
ln -svf service %buildroot/%{_sbindir}/rc%{name}
#
install -d -m0755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -d -m0755 %{buildroot}%{_localstatedir}/run/rsyslog
install -d -m0755 %{buildroot}%{_localstatedir}/spool/rsyslog
for file in rsyslog.conf rsyslog.d.remote.conf ; do
	sed \
%ifarch s390 s390x
	-e 's;tty10;console;g' \
%endif
	-e 's;ADDITIONAL_SOCKETS;%{rsyslog_sockets_cfg};g' \
	-e 's;ETC_RSYSLOG_CONF;%{_sysconfdir}/rsyslog.conf;g' \
	-e 's;ETC_RSYSLOG_D_DIR;%{_sysconfdir}/rsyslog.d;g' \
	-e 's;ETC_RSYSLOG_D_GLOB;%{_sysconfdir}/rsyslog.d/*.conf;g' \
	-e 's;RSYSLOG_SPOOL_DIR;%{_localstatedir}/spool/rsyslog;g' \
	%{_sourcedir}/${file}.in > ${file}.$$
done
install    -m0600 rsyslog.conf.$$ \
                  %{buildroot}%{_sysconfdir}/rsyslog.conf
install    -m0600 rsyslog.d.remote.conf.$$ \
                  %{buildroot}%{_sysconfdir}/rsyslog.d/remote.conf
#
install -d -m0755 %{buildroot}%{_fillupdir}
install    -m0600 %{_sourcedir}/rsyslog.sysconfig \
                  %{buildroot}%{_fillupdir}/sysconfig.syslog-rsyslog
#
rm -f doc/Makefile*
install -d -m0755 %{buildroot}%{rsyslogdocdir}/html/
find ChangeLog README AUTHORS \
	\( -type d -exec install -m755 -d   %{buildroot}%{rsyslogdocdir}/\{\} \; \) \
     -o \( -type f -exec install -m644 \{\} %{buildroot}%{rsyslogdocdir}/\{\} \; \)
cp -av build/* %{buildroot}%{rsyslogdocdir}/html/
#
%if %{with mysql}
install -m644 plugins/ommysql/createDB.sql \
	%{buildroot}%{rsyslogdocdir}/mysql-createDB.sql
%endif
%if %{with pgsql}
install -m644 plugins/ompgsql/createDB.sql \
	%{buildroot}%{rsyslogdocdir}/pgsql-createDB.sql
%endif
install -d -m0755 %{buildroot}%{_unitdir}
install -m644 %{SOURCE3} %{buildroot}%{_unitdir}/
install -d -m0755 %{buildroot}%{_prefix}/lib/systemd/journald.conf.d
install -m644 %{SOURCE16} %{buildroot}%{_prefix}/lib/systemd/journald.conf.d/30-rsyslog.conf
# create ghosts
install -d -m0755 %{buildroot}%{rsyslog_rundir}
touch %{buildroot}%{rsyslog_sockets_cfg}
chmod 644 %{buildroot}%{rsyslog_sockets_cfg}
mkdir -p %{buildroot}%{APPARMOR_PROFILE_PATH}/rsyslog.d/
install -m0640 %{SOURCE6} %{buildroot}%{APPARMOR_PROFILE_PATH}/
install -m0600 %{SOURCE17} %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m0600 %{SOURCE18} %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m0600 %{SOURCE19} %{buildroot}%{_sysconfdir}/rsyslog.d/

%if %{with mysql}
  install -m0640 %{SOURCE7} %{buildroot}%{APPARMOR_PROFILE_PATH}/rsyslog.d/
%endif
%if %{with snmp}
  install -m0640 %{SOURCE8} %{buildroot}%{APPARMOR_PROFILE_PATH}/rsyslog.d/
%endif
%if %{with udpspoof}
  install -m0640 %{SOURCE9} %{buildroot}%{APPARMOR_PROFILE_PATH}/rsyslog.d/
%endif

%clean
if [ -n "%{buildroot}" ] && [ "%{buildroot}" != "/" ] ; then
	rm -rf "%{buildroot}"
fi

%pre
%{service_add_pre rsyslog.service}

%post
#
# update linker caches
#
/sbin/ldconfig
#
# remove obsolete variables
#
%{remove_and_set -n syslog SYSLOG_DAEMON SYSLOG_REQUIRES_NETWORK}
%{remove_and_set -n syslog RSYSLOGD_COMPAT_VERSION RSYSLOGD_NATIVE_VERSION}
#
# add RSYSLOGD_* variables
#
%{fillup_only -ns syslog rsyslog}
#
# Do not use multiple facilities with the same priority pattern.
# It causes start failure since rsyslog-6.4.x (bnc#780607).
#
# FIXME: it seems to be a valid syntax -> rsyslog bug?
#
if grep -qs '^local[0246],' etc/rsyslog.conf ; then
   sed -i -e 's/^local\([0246]\),/local\1.*;/g' etc/rsyslog.conf
fi
#
# create dirs, touch log default files
#
if [ "$1" = "1" ] ; then  # first install
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
# touch the additional log sockets config file
#
mkdir -p -m750 ".%{rsyslog_rundir}"
touch ".%{rsyslog_sockets_cfg}"
chmod 640 ".%{rsyslog_sockets_cfg}"
fi # first install
#
# Enable the rsyslogservice to be started by systemd
#
# This macro enables based on a systemctl preset config file only
%{service_add_post rsyslog.service}
# But we want to enable a syslog-daemon regardless of the preset;
# force the creation of a syslog.service alias link (bnc#790805).
# We do not check the obsolete SYSLOG_DAEMON variable as we want
# to switch when installing it and there is a provider conflict.
/usr/bin/systemctl -f enable rsyslog.service >/dev/null 2>&1 || :

%preun
#
# stop the rsyslogd daemon when it is running
#
%{service_del_preun syslog.socket}
%{service_del_preun rsyslog.service}

%postun
#
# update linker caches
#
/sbin/ldconfig
#
# cleanup init scripts
#
%{service_del_postun rsyslog.service}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/rsyslog.d
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/rsyslog.d/remote.conf
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/rsyslog.d/*.frule
%{_sbindir}/rsyslogd
%if !0%{?usrmerged}
/sbin/rsyslogd
%endif
%dir %{rsyslog_module_dir_nodeps}
%{rsyslog_module_dir_nodeps}/fmhash.so
%{rsyslog_module_dir_nodeps}/fmhttp.so
%{rsyslog_module_dir_nodeps}/imfile.so
%{rsyslog_module_dir_nodeps}/imklog.so
%{rsyslog_module_dir_nodeps}/imkmsg.so
%{rsyslog_module_dir_nodeps}/immark.so
%{rsyslog_module_dir_nodeps}/impstats.so
%{rsyslog_module_dir_nodeps}/imtcp.so
%{rsyslog_module_dir_nodeps}/imudp.so
%{rsyslog_module_dir_nodeps}/imuxsock.so
%{rsyslog_module_dir_nodeps}/lmnet.so
%{rsyslog_module_dir_nodeps}/lmnetstrms.so
%{rsyslog_module_dir_nodeps}/lmnsd_ptcp.so
%{rsyslog_module_dir_nodeps}/imptcp.so
%{rsyslog_module_dir_nodeps}/lmregexp.so
%{rsyslog_module_dir_nodeps}/lmtcpclt.so
%{rsyslog_module_dir_nodeps}/lmtcpsrv.so
%{rsyslog_module_dir_nodeps}/lmzlibw.so
%{rsyslog_module_dir_nodeps}/mmanon.so
%{rsyslog_module_dir_nodeps}/mmcount.so
%{rsyslog_module_dir_nodeps}/mmexternal.so
%{rsyslog_module_dir_nodeps}/mmfields.so
%{rsyslog_module_dir_nodeps}/mmkubernetes.so
%{rsyslog_module_dir_nodeps}/mmpstrucdata.so
%{rsyslog_module_dir_nodeps}/mmrfc5424addhmac.so
%{rsyslog_module_dir_nodeps}/mmsequence.so
%{rsyslog_module_dir_nodeps}/mmutf8fix.so
%{rsyslog_module_dir_nodeps}/mmrm1stspace.so
%{rsyslog_module_dir_nodeps}/ommail.so
%{rsyslog_module_dir_nodeps}/omhttp.so
%{rsyslog_module_dir_nodeps}/omprog.so
%{rsyslog_module_dir_nodeps}/omruleset.so
%{rsyslog_module_dir_nodeps}/omstdout.so
%{rsyslog_module_dir_nodeps}/omtesting.so
%{rsyslog_module_dir_nodeps}/omuxsock.so
%{rsyslog_module_dir_nodeps}/pmlastmsg.so
%{rsyslog_module_dir_nodeps}/pmaixforwardedfrom.so
%{rsyslog_module_dir_nodeps}/pmcisconames.so
%{rsyslog_module_dir_nodeps}/pmciscoios.so
%{rsyslog_module_dir_nodeps}/pmsnare.so
%{rsyslog_module_dir_nodeps}/pmnull.so
%{rsyslog_module_dir_nodeps}/pmnormalize.so
%{rsyslog_module_dir_nodeps}/pmpanngfw.so
%if %{with rfc3195}
%{rsyslog_module_dir_nodeps}/im3195.so
%endif
%if %{with journal}
%{rsyslog_module_dir_nodeps}/imjournal.so
%{rsyslog_module_dir_nodeps}/omjournal.so
%dir %{_prefix}/lib/systemd/journald.conf.d/
%{_prefix}/lib/systemd/journald.conf.d/30-rsyslog.conf
%endif
%dir %{rsyslog_module_dir_withdeps}
%{_mandir}/man5/rsyslog.conf.5*
%{_mandir}/man8/rsyslogd.8*
%license COPYING COPYING.ASL20 COPYING.LESSER
%dir %{rsyslogdocdir}
%doc %{rsyslogdocdir}/ChangeLog
%doc %{rsyslogdocdir}/README
%doc %{rsyslogdocdir}/AUTHORS
%dir %{_localstatedir}/spool/rsyslog
%{_fillupdir}/sysconfig.syslog-rsyslog
%attr(0755,root,root) %dir %ghost %{rsyslog_rundir}
%attr(0644,root,root) %ghost %{rsyslog_sockets_cfg}
%{_sbindir}/rsyslog-service-prepare
%{_unitdir}/rsyslog.service
%{_sbindir}/rc%{name}
%{APPARMOR_PROFILE_PATH_DIR_COMMANDS}
%config %{APPARMOR_PROFILE_PATH}/usr.sbin.rsyslogd

%files doc
%defattr(-,root,root)
%dir %{rsyslogdocdir}/
%doc %{rsyslogdocdir}/html/

%if %{with diagtools}

%files diag-tools
%defattr(-,root,root)
%{_sbindir}/msggen
%{_sbindir}/rsyslog_diag_hostname
%{rsyslog_module_dir_nodeps}/imdiag.so
%endif

%if %{with gssapi}

%files module-gssapi
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omgssapi.so
%{rsyslog_module_dir_withdeps}/imgssapi.so
%{rsyslog_module_dir_withdeps}/lmgssutil.so
%endif

%if %{with mysql}

%files module-mysql
%defattr(-,root,root)
%doc %{rsyslogdocdir}/mysql-createDB.sql
%{rsyslog_module_dir_withdeps}/ommysql.so
%config %{APPARMOR_PROFILE_PATH}/rsyslog.d/module-mysql
%endif

%if %{with pgsql}

%files module-pgsql
%defattr(-,root,root)
%doc %{rsyslogdocdir}/pgsql-createDB.sql
%{rsyslog_module_dir_withdeps}/ompgsql.so
%endif

%if %{with dbi}

%files module-dbi
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omlibdbi.so
%endif

%if %{with snmp}

%files module-snmp
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omsnmp.so
%{rsyslog_module_dir_nodeps}/mmsnmptrapd.so
%config %{APPARMOR_PROFILE_PATH}/rsyslog.d/module-snmp
%endif

%if %{with gnutls}

%files module-gtls
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/lmnsd_gtls.so
%endif

%if %{with openssl}

%files module-ossl
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/lmnsd_ossl.so
%endif

%if %{with relp}

%files module-relp
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/imrelp.so
%{rsyslog_module_dir_withdeps}/omrelp.so
%endif

%if %{with mmnormalize}

%files module-mmnormalize
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/mmnormalize.so
%{rsyslog_module_dir_withdeps}/mmjsonparse.so
%{rsyslog_module_dir_withdeps}/mmaudit.so
%endif

%if %{with udpspoof}

%files module-udpspoof
%defattr(-,root,root)
%{rsyslog_module_dir_nodeps}/omudpspoof.so
%config %{APPARMOR_PROFILE_PATH}/rsyslog.d/module-udpspoof
%endif

%if %{with elasticsearch}

%files module-elasticsearch
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omelasticsearch.so
%endif

%if %{with omhttpfs}

%files module-omhttpfs
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omhttpfs.so
%endif

%if %{with hdfs}

%files module-hdfs
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omhdfs.so
%endif

%if %{with mongodb}

%files module-mongodb
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/ommongodb.so
%endif

%if %{with hiredis}

%files module-hiredis
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omhiredis.so
%endif

%if %{with zeromq}

%files module-zeromq
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/imzmq3.so
%{rsyslog_module_dir_withdeps}/omzmq3.so
%endif

%if %{with kafka}

%files module-kafka
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/imkafka.so
%{rsyslog_module_dir_withdeps}/omkafka.so
%endif

%if %{with omamqp1}
%files module-omamqp1
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omamqp1.so
%endif

%if %{with gcrypt}

%files module-gcrypt
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/lmcry_gcry.so
%{_bindir}/rscryutil
%endif

%if %{with tcl}
%files module-omtcl
%defattr(-,root,root)
%{rsyslog_module_dir_withdeps}/omtcl.so*
%endif

%changelog
