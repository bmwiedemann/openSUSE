#
# spec file for package zabbix
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


# backport...
%{!?_initddir: %{expand: %%global _initddir %{_initrddir}}}
%{!?_rundir: %{expand: %%global _rundir %{_localstatedir}/run}}

%define server_user  zabbixs
%define server_group zabbixs
# keep zabbix user for backwards compatibility of agent
%define agent_user   zabbix
%define agent_group  zabbix

%if 0%{suse_version} > 1310
%define bashcompletiondir /usr/share/bash-completion/completions/
%else
%define bashcompletiondir /etc/bash_completion.d/
%endif

%define basic_configuration --enable-proxy --enable-server --enable-agent  --sysconfdir=%{_sysconfdir}/zabbix
# globally defined configure variables
%define _with_openipmi --with-openipmi
%define _with_java --enable-java
%define _with_ipv6 --enable-ipv6
%define _with_ssh2 --with-ssh2
%define _with_ldap --with-ldap
%define _with_libcurl --with-libcurl
%define _with_openipmi --with-openipmi
%define _with_net_snmp --with-net-snmp 
%define _with_odbc --with-unixodbc
%define _with_net_snmp --with-net-snmp
%define _with_libxml2 --with-libxml2
%define _with_openssl --with-openssl

# sle 10 and RHEL4 does not have new enough java sdk... (must be separated sle 10 rpm is a bit picky...)
%if 0%{?sles_version} && 0%{?sles_version} <= 10
%undefine _with_java
%endif
%if 0%{?rhel_version} && 0%{?rhel_version} <= 406
%undefine _with_java
%endif
%if 0%{?suse_version}
%define apache2_sysconfdir %(%{_sbindir}/apxs2 -q SYSCONFDIR)
%else
# this should be rhel compatible
%define apache2_sysconfdir %(%{_sbindir}/apxs -q SYSCONFDIR)
%endif

%if 0%{?sles_version} == 11
%define php_version 53
%else
%if 0%{?suse_version} > 150
%define php_version 7
%else
%define php_version 5
%endif
%endif
%define SuSeFirewall_services_dir /etc/sysconfig/SuSEfirewall2.d/services

# SLE 11 has old openssl...
%if 0%{?suse_version} <= 1210
%undefine _with_openssl
%endif

Name:           zabbix
Version:        3.0.28
Release:        0

%define bcversion 3.0-1.0

Url:            http://www.zabbix.com
Source0:        http://sourceforge.net/projects/zabbix/files/ZABBIX%20Latest%20Stable/%{version}/zabbix-%{version}.tar.gz
Source1:        zabbix-rpmlintrc
Source2:        zabbix-agentd.init.d
Source3:        zabbix-server.init.d
Source4:        zabbix-proxy.init.d
Source5:        apache2-zabbix.conf
Source6:        README.SUSE
Source7:        zabbix-agentd.firewall
Source8:        zabbix-server.firewall
Source9:        zabbix-java-gateway.firewall
Source10:       zabbix-java-gateway.init.d
Source11:       zabbix-server.service
Source12:       zabbix-agentd.service
Source13:       zabbix-proxy.service
Source14:       zabbix-java-gateway.service
Source15:       rn3.0.0.html
Source16:       zabbix-tmpfiles.conf
Source17:       zabbix-java-gateway.sh
Source18:       zabbix-proxy.firewall
Source19:       https://github.com/zabbix/zabbix-bash-completion/archive/%{bcversion}/zabbix-bash-completion-%{bcversion}.tar.gz
# PATCH-FIX-UPSTREAM zabbix-3.0.20-jsLoader-fix.patch bnc#1105278
Patch0:         zabbix-3.0.20-jsLoader-fix.patch
# PATCH-FIX-UPSTREAM zabbix-3.0.25-new-m4-pgsql.patch fix for opensuse issue caused/solved by bnc#1120035
Patch1:         zabbix-3.0.25-new-m4-pgsql.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?_with_openipmi:1}
BuildRequires:  OpenIPMI-devel
%endif
%if 0%{?suse_version}
BuildRequires:  apache2-devel
%else
BuildRequires:  httpd-devel
%endif
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?suse_version}
BuildRequires:  help2man
%endif
%if 0%{?_with_ssh2:1}
BuildRequires:  libssh2-devel
%endif
BuildRequires:  libtool
%if 0%{?_with_net_snmp:1}
BuildRequires:  net-snmp-devel
%endif
%if 0%{?_with_ldap:1}
BuildRequires:  openldap2-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  postgresql-devel
BuildRequires:  sqlite-devel
%if 0%{?_with_java:1}
BuildRequires:  java-devel >= 1.6
%endif
%if 0%{?_with_odbc:1}
BuildRequires:  unixODBC-devel
%endif
%if 0%{?suse_version} < 1020
BuildRequires:  curl-devel
BuildRequires:  mysql-devel
BuildRequires:  tcpd-devel
%else
BuildRequires:  fdupes
BuildRequires:  libcurl-devel
BuildRequires:  libmysqlclient-devel
%endif
BuildRequires:  libxml2-devel
BuildRequires:  update-alternatives

Summary:        Distributed monitoring system
License:        GPL-2.0-or-later
Group:          System/Monitoring

%description
Zabbix is a distributed monitoring system.


%package agent
Requires(pre):  pwdutils %insserv_prereq %fillup_prereq
Summary:        Local resource monitor agent for Zabbix
Group:          System/Monitoring

%description agent
The Zabbix agent monitors local resources and relays information to the server.


%package server
Requires:       zabbix_server_binary = %{version}-%{release}
Requires(pre):  pwdutils %insserv_prereq %fillup_prereq
Summary:        System files for the Zabbix server
Group:          System/Monitoring

%description server
The Zabbix server component.


%package proxy
Requires:       zabbix_proxy_binary = %{version}-%{release}
Requires(pre):  pwdutils %insserv_prereq %fillup_prereq
Summary:        System files for the Zabbix proxy
Group:          System/Monitoring

%description proxy
The Zabbix proxy component.


%package phpfrontend
Requires:       php%{php_version}
Requires:       php%{php_version}-bcmath
Requires:       php%{php_version}-ctype
Requires:       php%{php_version}-gd
Requires:       php%{php_version}-ldap
Requires:       php%{php_version}-mbstring
Requires:       php%{php_version}-sockets
Summary:        Zabbix web frontend (php)
Group:          Productivity/Networking/Web/Frontends

%description phpfrontend
The Zabbix PHP frontend allows access via standard web browsers.

NOTE: You still have to install the PHP package which contains your db driver!


%package server-mysql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_server_binary = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Summary:        Zabbix server with MySQL support
Group:          System/Monitoring

%description server-mysql
The Zabbix server compiled with MySQL support.


%package server-postgresql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_server_binary = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Summary:        Zabbix server with PostgreSQL support
Group:          System/Monitoring

%description server-postgresql
The Zabbix server compiled with PostgreSQL support.


%package server-sqlite
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_server_binary = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Summary:        Zabbix server with SQLite support
Group:          System/Monitoring

%description server-sqlite
The Zabbix server compiled with SQLite support.


%package proxy-mysql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_proxy_binary = %{version}-%{release}
Requires:       %{name}-proxy = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Summary:        Zabbix proxy with MySQL support
Group:          System/Monitoring

%description proxy-mysql
The Zabbix proxy compiled with MySQL support.


%package proxy-postgresql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_proxy_binary = %{version}-%{release}
Requires:       %{name}-proxy = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Summary:        Zabbix proxy with PostgreSQL support
Group:          System/Monitoring

%description proxy-postgresql
The Zabbix proxy compiled with PostgreSQL support.


%package proxy-sqlite
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_proxy_binary = %{version}-%{release}
Requires:       %{name}-proxy = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Summary:        Zabbix proxy with SQLite support
Group:          System/Monitoring

%description proxy-sqlite
The Zabbix proxy compiled with SQLite support.

%package java-gateway
Provides:       %{name} = %{version}-%{release}
Requires:       jre
Summary:        Zabbix Java gateway
Group:          System/Monitoring

%description java-gateway
JMX monitoring can be used to monitor JMX counters of a Java
application. To retrieve the value of a particular JMX counter on a
host, the Zabbix server queries the Zabbix Java gateway, which in
turn uses the JMX management API to query the application of interest
remotely.

%package bash-completion
Provides:       %{name} = %{version}-%{release}
Requires:       awk
Requires:       bash-completion
Requires:       iproute2
Summary:        Zabbix bash completion
Group:          System/Shells
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description bash-completion
Bash completion for Zabbix daemons and utilities

%prep
%setup -q -n zabbix-%{version}%{?rclevel} -a 19
%patch0
# as SLE 11 is "too old" we do not patch it with postgresql separation logic...
%if 0%{?suse_version} > 1110
%patch1
%endif
cp %{S:6} .
# fix source & config files to respect adapted names
for file in src/zabbix_java/settings.sh src/zabbix_java/lib/logback.xml %{SOURCE17} conf/*.conf  misc/init.d/suse/*/zabbix_* src/zabbix_server/server.c \
	src/zabbix_server/alerter/alerter.c src/zabbix_agent/zbxconf.c src/zabbix_agent/zabbix_agentd.c src/zabbix_proxy/proxy.c ChangeLog; do
	sed -i -e "s@/home/zabbix/bin@%{_bindir}@g" \
		-e "s@^[# ]*PidFile=/tmp/zabbix_@PidFile=%{_rundir}/%{agent_user}/zabbix-@g" \
		-e "s@^[# ]*LogFile=/tmp/zabbix_@LogFile=%{_localstatedir}/log/%{agent_user}/zabbix-@g" \
		-e "s@^[# ]*DBSocket=/tmp/mysql.sock@DBSocket=%{_rundir}/mysql/mysql.sock@g" \
		-e "s@DBUser=root@DBUser=zabbix@g" \
		-e "s@^[# ]*DBPassword=.*@DBPassword=zabbix@g" \
		-e "s@zabbix_agentd.userparams.conf@zabbix-agentd.userparams.conf@g" \
		-e "s@zabbix_agentd.conf@zabbix-agentd.conf@g" \
		-e "s@zabbix_server.conf@zabbix-server.conf@g" \
		-e "s@zabbix_proxy.conf@zabbix-proxy.conf@g" \
		-e 's@PID_FILE="/tmp/zabbix_@PID_FILE="%{_rundir}/%{agent_user}/zabbix-@g' \
		-e "s@Hostname=Zabbix Server@Hostname=Zabbix_Server@" \
		-e "s@<file>/tmp/zabbix_@<file>%{_localstatedir}/log/%{server_user}/zabbix-@g" \
		-e "s@ttern>/tmp/zabbix_@ttern>%{_localstatedir}/log/%{server_user}/zabbix-@g" \
		-e "s@GW_PID:=/var/run/zabbix/zabbix-java-gateway.pid@GW_PID:=%{_rundir}/%{server_user}/zabbix-java-gateway.pid@g" \
		-e "s@GW_LOGFILE:=/var/log/zabbix/zabbix-java-gateway.log@GW_LOGFILE:=%{_localstatedir}/log/%{server_user}/zabbix-java-gateway.log@g" $file
done

# change bash completion files to use adapted names

for file in zabbix-bash-completion-%{bcversion}/*completion; do
	sed -i -e "s#zabbix_get#zabbix-get#g" \
		-e "s#zabbix_sender#zabbix-sender#g" \
		-e "s#zabbix_agentd#zabbix-agentd#g" \
		-e "s#zabbix_server#zabbix-server#g" \
		-e "s#zabbix_proxy#zabbix-proxy#g" $file
done

# fix server, java and proxy (again) config for log and run location...
for file in src/zabbix_java/settings.sh conf/zabbix_proxy.conf conf/zabbix_server.conf ; do
	sed -i -e "s#^[# ]*LogFile=/var/log/.*/zabbix-#LogFile=%{_localstatedir}/log/%{server_user}/zabbix-#g" \
		-e "s#^[# ]*PidFile=%{_rundir}/.*/zabbix-#PidFile=%{_rundir}/%{server_user}/zabbix-#g" \
		-e 's#PID_FILE="%{_rundir}/.*/zabbix-#PID_FILE="%{_rundir}/%{server_user}/zabbix-#g' $file
done

# fix db content to respect adapted names and suse naming conventions
for file in database/*/data.sql; do
	sed -i -e "s#syslogd#syslog-ng#g" \
		-e "s#Syslogd#Syslog-ng#g" \
		-e "s#Zabbix_agent#Zabbix-agent#g" \
		-e "s#zabbix_agent#zabbix-agent#g" \
		-e "s#Zabbix_server#Zabbix-server#g" \
		-e "s#zabbix_server#zabbix-server#g" \
		-e "s#Zabbix_proxy#Zabbix-proxy#g" \
		-e "s#zabbix_proxy#zabbix-proxy#g" \
		-e "s#httpd#httpd2-prefork#g" $file
done
##### Fix for date time macros
REF_DATE=$(LANG=C date -r configure +"%%b %%d %%Y")
REF_TIME=$(LANG=C date -r configure +"%%H:%%M:%%S")
sed -i -e "s/__DATE__/\"${REF_DATE}\"/g" -e "s/__TIME__/\"${REF_TIME}\"/g" src/libs/zbxcommon/str.c
#####
##### Fix location of zabbix java gateway location
sed -ri 's@^(ZABBIX_JAVA_CONF=.\{ZABBIX_JAVA_CONF:=).*@\1%{_sysconfdir}/zabbix/zabbix-java-gateway.conf}@g' %{S:17}

%if 0%{?suse_version} < 1110
######### Fix building on SLE 10 #############
sed -ri 's/(_full_libnetsnmp_libs=).*/\1"`$_libnetsnmp_config --libs` -lcrypto"/' configure
##############################################
%endif

%build

# autoreconf not needed anymore
autoreconf -i
ZABBIX_BASIC_CONFIG="%{expand:%{basic_configuration}}  %{?_with_openipmi}  %{?_with_java}  %{?_with_ipv6}  %{?_with_ssh2} %{?_with_ldap} %{?_with_odbc}"
ZABBIX_BASIC_CONFIG="$ZABBIX_BASIC_CONFIG %{?_with_libcurl} %{?_with_openipmi} %{?_with_net_snmp} %{?_with_libxml2} %{?_with_openssl}"

# build MySQL binaries
# only sle care about 1.5 level of java bytecode others do not
%if 0%{?_with_java:1} && 0%{?sles_version}
JAVAC="javac -source 1.5 -target 1.5"
%else
JAVAC=javac
%endif
export JAVAC
CFLAGS="%optflags"
export CFLAGS

%configure $ZABBIX_BASIC_CONFIG --with-mysql --without-postgresql
make %{?_smp_mflags} JAVAC="$JAVAC"
cp src/zabbix_server/zabbix_server zabbix-server-mysql
cp src/zabbix_proxy/zabbix_proxy zabbix-proxy-mysql

# build PostgreSQL binaries
make clean
%configure $ZABBIX_BASIC_CONFIG --with-postgresql
make %{?_smp_mflags} JAVAC="$JAVAC"
cp src/zabbix_server/zabbix_server zabbix-server-postgresql
cp src/zabbix_proxy/zabbix_proxy zabbix-proxy-postgresql

# build SQLite binaries
make clean
%configure $ZABBIX_BASIC_CONFIG --with-sqlite3 --without-postgresql
make %{?_smp_mflags} JAVAC="$JAVAC"
cp src/zabbix_server/zabbix_server zabbix-server-sqlite
cp src/zabbix_proxy/zabbix_proxy zabbix-proxy-sqlite
cp src/zabbix_get/zabbix_get zabbix-get
# looks removed from source...
#cp src/zabbix_agent/zabbix_agent zabbix-agent
cp src/zabbix_agent/zabbix_agentd zabbix-agentd
cp src/zabbix_sender/zabbix_sender zabbix-sender

# generate man pages
# looks removed from loop bellow zabbix-agent
for prog in zabbix-server-mysql zabbix-proxy-mysql zabbix-server-postgresql \
            zabbix-proxy-postgresql zabbix-server-sqlite zabbix-proxy-sqlite \
            zabbix-get zabbix-agentd zabbix-sender ; do
# workaround should be uncommented if removed patch for compilation..
#	echo "#!/bin/sh" >> ${prog}.sh
#	echo "./${prog} \$* | sed -e '/Compilation time/d'" >> ${prog}.sh
#	chmod 755 ${prog}.sh
#	help2man -N -o ${prog}.1 ./${prog}.sh
	help2man -N -o ${prog}.1 ./${prog}
done

%install
# SLE 11 does not like new java bytecode so just ignore that check
export NO_BRP_CHECK_BYTECODE_VERSION=true
# install the binaries
# server
install -Dm 0755 zabbix-server-mysql %{buildroot}/%{_sbindir}/zabbix-server-mysql
install -Dm 0755 zabbix-server-postgresql %{buildroot}/%{_sbindir}/zabbix-server-postgresql
install -Dm 0755 zabbix-server-sqlite %{buildroot}/%{_sbindir}/zabbix-server-sqlite
install -Dm 0755 src/zabbix_get/zabbix_get %{buildroot}/%{_bindir}/zabbix-get

# proxy
install -Dm 0755 zabbix-proxy-mysql %{buildroot}/%{_sbindir}/zabbix-proxy-mysql
install -Dm 0755 zabbix-proxy-postgresql %{buildroot}/%{_sbindir}/zabbix-proxy-postgresql
install -Dm 0755 zabbix-proxy-sqlite %{buildroot}/%{_sbindir}/zabbix-proxy-sqlite

# agents
install -Dm 0755 src/zabbix_agent/zabbix_agentd %{buildroot}/%{_sbindir}/zabbix-agentd
install -Dm 0755 src/zabbix_sender/zabbix_sender %{buildroot}/%{_sbindir}/zabbix-sender

# Manual pages
install -Dm 0644 zabbix-agentd.1 %{buildroot}/%{_mandir}/man1/zabbix-agentd.1
install -Dm 0644 zabbix-get.1 %{buildroot}/%{_mandir}/man1/zabbix-get.1
install -Dm 0644 zabbix-proxy-mysql.1 %{buildroot}/%{_mandir}/man1/zabbix-proxy-mysql.1
install -Dm 0644 zabbix-proxy-postgresql.1 %{buildroot}/%{_mandir}/man1/zabbix-proxy-postgresql.1
install -Dm 0644 zabbix-proxy-sqlite.1 %{buildroot}/%{_mandir}/man1/zabbix-proxy-sqlite.1
install -Dm 0644 zabbix-sender.1 %{buildroot}/%{_mandir}/man1/zabbix-sender.1
install -Dm 0644 zabbix-server-mysql.1 %{buildroot}/%{_mandir}/man1/zabbix-server-mysql.1
install -Dm 0644 zabbix-server-postgresql.1 %{buildroot}/%{_mandir}/man1/zabbix-server-postgresql.1
install -Dm 0644 zabbix-server-sqlite.1 %{buildroot}/%{_mandir}/man1/zabbix-server-sqlite.1

# Bash completion
install -Dm 0644 zabbix-bash-completion-%{bcversion}/zabbix-daemons-completion %{buildroot}/%{bashcompletiondir}/zabbix-daemons-completion
install -Dm 0644 zabbix-bash-completion-%{bcversion}/zabbix_get-completion %{buildroot}/%{bashcompletiondir}/zabbix-get-completion
install -Dm 0644 zabbix-bash-completion-%{bcversion}/zabbix_sender-completion %{buildroot}/%{bashcompletiondir}/zabbix-sender-completion
install -Dm 0644 zabbix-bash-completion-%{bcversion}/zabbix_agentd-completion %{buildroot}/%{bashcompletiondir}/zabbix-agentd-completion
install -Dm 0644 zabbix-bash-completion-%{bcversion}/zabbix_server-completion %{buildroot}/%{bashcompletiondir}/zabbix-server-completion
install -Dm 0644 zabbix-bash-completion-%{bcversion}/zabbix_proxy-completion %{buildroot}/%{bashcompletiondir}/zabbix-proxy-completion

# update-alternatives handling for manual pages
install -d -m 0755 %{buildroot}/%{_sysconfdir}/alternatives
touch -r /bin/true %{buildroot}%{_sysconfdir}/alternatives/zabbix-server
touch -r /bin/true %{buildroot}%{_sysconfdir}/alternatives/zabbix-proxy 
touch -r /etc/passwd %{buildroot}%{_sysconfdir}/alternatives/zabbix-server.1%{?ext_man}
touch -r /etc/passwd %{buildroot}%{_sysconfdir}/alternatives/zabbix-proxy.1%{?ext_man} 
ln -s %{_sysconfdir}/alternatives/zabbix-server.1 %{buildroot}%{_mandir}/man1/zabbix-server.1
ln -s %{_sysconfdir}/alternatives/zabbix-proxy.1 %{buildroot}%{_mandir}/man1/zabbix-proxy.1

# install the php frontend
mkdir -p %{buildroot}/%{_datadir}/zabbix
cp -r frontends/php/* %{buildroot}/%{_datadir}/zabbix
install -Dm 0644 %{S:5} %{buildroot}/%{apache2_sysconfdir}/conf.d/zabbix.conf

# remove .htaccess files as access rules are moved to zabbix.conf
find %{buildroot}/%{_datadir}/zabbix -name .htaccess -print -delete

# create directory structure
install -d %{buildroot}/%{_localstatedir}/log/%{server_user}
install -d %{buildroot}/%{_localstatedir}/log/%{agent_user}
install -d %{buildroot}/%{_rundir}/%{server_user}
install -d %{buildroot}/%{_rundir}/%{agent_user}

# install the config files
install -Dm 0640 conf/zabbix_agentd.conf %{buildroot}/%{_sysconfdir}/zabbix/zabbix-agentd.conf
install -Dm 0640 conf/zabbix_server.conf %{buildroot}/%{_sysconfdir}/zabbix/zabbix-server.conf
install -Dm 0640 conf/zabbix_proxy.conf %{buildroot}/%{_sysconfdir}/zabbix/zabbix-proxy.conf

# set the rc sym links
%if 0%{?suse_version} >= 1210
ln -s /usr/sbin/service %{buildroot}/%{_sbindir}/rczabbix-agentd
ln -s /usr/sbin/service %{buildroot}/%{_sbindir}/rczabbix-server
ln -s /usr/sbin/service %{buildroot}/%{_sbindir}/rczabbix-proxy
%if 0%{?_with_java:1}
ln -s /usr/sbin/service %{buildroot}/%{_sbindir}/rczabbix-java-gateway
%endif
%else
ln -s %{_initddir}/zabbix-agentd %{buildroot}/%{_sbindir}/rczabbix-agentd
ln -s %{_initddir}/zabbix-server %{buildroot}/%{_sbindir}/rczabbix-server
ln -s %{_initddir}/zabbix-proxy %{buildroot}/%{_sbindir}/rczabbix-proxy
%if 0%{?_with_java:1}
ln -s %{_initddir}/zabbix-java-gateway %{buildroot}/%{_sbindir}/rczabbix-java-gateway
%endif
%endif

%if 0%{?suse_version} <= 1220
# install the init.d scripts
install -Dm 0755 %{S:2} %{buildroot}/%{_initddir}/zabbix-agentd
install -Dm 0755 %{S:3} %{buildroot}/%{_initddir}/zabbix-server
install -Dm 0755 %{S:4} %{buildroot}/%{_initddir}/zabbix-proxy
 %if 0%{?_with_java:1}
install -Dm 0755 %{S:10}  %{buildroot}/%{_initddir}/zabbix-java-gateway
 %endif
%endif

# install firewall description files
install -d 0755 %{buildroot}/%{SuSeFirewall_services_dir}
%if 0%{?suse_version} > 1020
install -m 0644 %{S:7} %{buildroot}/%{SuSeFirewall_services_dir}/zabbix-agentd
install -m 0644 %{S:8} %{buildroot}/%{SuSeFirewall_services_dir}/zabbix-server
install -m 0644 %{S:18} %{buildroot}/%{SuSeFirewall_services_dir}/zabbix-proxy
%if 0%{?_with_java:1}
install -m 0644 %{S:9} %{buildroot}/%{SuSeFirewall_services_dir}/zabbix-java-gateway
%endif
%endif

ln -s %{_sysconfdir}/alternatives/zabbix-proxy %{buildroot}%{_sbindir}/zabbix-proxy
ln -s %{_sysconfdir}/alternatives/zabbix-server %{buildroot}%{_sbindir}/zabbix-server
touch -r /bin/true %{buildroot}%{_sysconfdir}/alternatives/zabbix-server
touch -r /bin/true %{buildroot}%{_sysconfdir}/alternatives/zabbix-proxy 

%if 0%{?_with_java:1}
# install java gateway files
install -dm 0755 %{buildroot}/%{_prefix}/lib/zabbix-java-gateway
cp -r src/zabbix_java/lib/*.jar %{buildroot}/%{_prefix}/lib/zabbix-java-gateway
install -Dm 0644 src/zabbix_java/bin/zabbix-java-gateway-%{version}%{?rclevel}.jar %{buildroot}/%{_prefix}/lib/zabbix-java-gateway/zabbix-java-gateway-%{version}%{?rclevel}.jar
install -m 0644 src/zabbix_java/settings.sh %{buildroot}/%{_sysconfdir}/zabbix/zabbix-java-gateway.conf
install -m 0644 src/zabbix_java/lib/logback.xml %{buildroot}/%{_sysconfdir}/zabbix/zabbix-java-gateway-log.xml
install -m 0755 %{S:17} %{buildroot}/%{_bindir}/zabbix-java-gateway
%endif

%if 0%{?suse_version} > 1020
%fdupes %{buildroot}/%{_prefix}
%endif

# install systemd unit files
%if 0%{?suse_version} >= 1210
install -Dm 0644 %{SOURCE11} %{buildroot}/%{_unitdir}/zabbix-server.service
install -Dm 0644 %{SOURCE12} %{buildroot}/%{_unitdir}/zabbix-agentd.service
install -Dm 0644 %{SOURCE13} %{buildroot}/%{_unitdir}/zabbix-proxy.service
install -dm 0755 %{buildroot}/%{_unitdir}/zabbix-server.service.requires
install -dm 0755 %{buildroot}/%{_unitdir}/zabbix-proxy.service.requires
%if 0%{?_with_java:1}
install -Dm 0644 %{SOURCE14} %{buildroot}/%{_unitdir}/zabbix-java-gateway.service
%endif
# this stupidity is required because i do not wanna create separate zabbix-common
# in case i ever do it will put it under one scope...
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
sed -e 's@/var/run/zabbix@%{_rundir}/%{server_user}@g; s/root zabbix/root %{server_group}/g' %{SOURCE16} > %{buildroot}%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
sed -e 's@/var/run/zabbix@%{_rundir}/%{server_user}@g; s/root zabbix/root %{server_group}/g' %{SOURCE16} > %{buildroot}%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
sed -e 's@/var/run/zabbix@%{_rundir}/%{agent_user}@g; s/root zabbix/root %{agent_group}/g' %{SOURCE16} > %{buildroot}%{_prefix}/lib/tmpfiles.d/zabbix-agentd.conf
%if 0%{?_with_java:1}
sed -e 's@/var/run/zabbix@%{_rundir}/%{server_user}@g; s/root zabbix/root %{server_group}/g' %{SOURCE16} > %{buildroot}%{_prefix}/lib/tmpfiles.d/zabbix-java-gateway.conf
%endif
%endif
###################################################################################
# Release Notes...
cp %{SOURCE15} .

%pre server
%if 0%{?suse_version} >= 1210
%service_add_pre zabbix-server.service
%endif
%{_bindir}/getent group %{server_group} >/dev/null || %{_sbindir}/groupadd -r %{server_group}
%{_bindir}/getent passwd %{server_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{server_user} -s /bin/false -c "Zabbix Server Daemon" -g %{server_group} %{server_user}

%pre proxy
%if 0%{?suse_version} >= 1210
%service_add_pre zabbix-proxy.service
%endif
%{_bindir}/getent group %{server_group} >/dev/null || %{_sbindir}/groupadd -r %{server_group}
%{_bindir}/getent passwd %{server_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{server_user} -s /bin/false -c "Zabbix Proxy Daemon" -g %{server_group} %{server_user}

%pre agent
%if 0%{?suse_version} >= 1210
%service_add_pre zabbix-agentd.service
%endif
%{_bindir}/getent group %{agent_group} >/dev/null || %{_sbindir}/groupadd -r %{agent_group}
%{_bindir}/getent passwd %{agent_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{agent_user} -s /bin/false -c "Zabbix Agent Daemon" -g %{agent_group} %{agent_user}

%if 0%{?_with_java:1}
%pre java-gateway
%if 0%{?suse_version} >= 1210
%service_add_pre zabbix-java-gateway.service
%endif
%{_bindir}/getent group %{server_group} >/dev/null || %{_sbindir}/groupadd -r %{server_group}
%{_bindir}/getent passwd %{server_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{server_user} -s /bin/false -c "Zabbix Java Daemon" -g %{server_group} %{server_user}
%endif

%post server
if [ "$1" -gt 1 ]; then
	chown root:%{server_group} %{_sysconfdir}/zabbix/zabbix-server.conf
	chmod 0640 %{_sysconfdir}/zabbix/zabbix-server.conf
	chown -R root:%{server_group} %{_rundir}/%{server_user} || :
	chown -R root:%{server_group} %{_localstatedir}/log/%{server_user} || :
	if [ $(stat -c '%a' %{_rundir}/%{server_user}) -ne '770' ]; then
		chmod 0770 %{_rundir}/%{server_user}
		chmod 0770 %{_localstatedir}/log/%{server_user}
	fi
fi
%if 0%{?suse_version} >= 1210
%service_add_post zabbix-server.service
systemd-tmpfiles --create /usr/lib/tmpfiles.d/zabbix-server.conf
%else
%fillup_and_insserv -f zabbix-server
%endif

%post proxy
if [ "$1" -gt 1 ]; then
	chown root:%{server_group} %{_sysconfdir}/zabbix/zabbix-proxy.conf
	chmod 0640 %{_sysconfdir}/zabbix/zabbix-proxy.conf
	chown -R root:%{server_group} %{_rundir}/%{server_user} || :
	chown -R root:%{server_group} %{_localstatedir}/log/%{server_user} || :
	if [ $(stat -c '%a' %{_rundir}/%{server_user}) -ne '770' ]; then
		chmod 0770 %{_rundir}/%{server_user}
		chmod 0770 %{_localstatedir}/log/%{server_user}
	fi
fi
%if 0%{?suse_version} >= 1210
%service_add_post zabbix-proxy.service
systemd-tmpfiles --create /usr/lib/tmpfiles.d/zabbix-proxy.conf
%else
%fillup_and_insserv -f zabbix-proxy
%endif

%if 0%{?_with_java:1}
%post java-gateway
if [ "$1" -gt 1 ]; then
	chown root:%{server_group} %{_sysconfdir}/zabbix/zabbix-java-gateway.conf
	chmod 0640 %{_sysconfdir}/zabbix/zabbix-java-gateway.conf
	chown -R root:%{server_group} %{_rundir}/%{server_user} || :
	chown -R root:%{server_group} %{_localstatedir}/log/%{server_user} || :
	if [ $(stat -c '%a' %{_rundir}/%{server_user}) -ne '770' ]; then
		chmod 0770 %{_rundir}/%{server_user}
		chmod 0770 %{_localstatedir}/log/%{server_user}
	fi
fi
 %if 0%{?suse_version} >= 1210
%service_add_post zabbix-java-gateway.service
systemd-tmpfiles --create /usr/lib/tmpfiles.d/zabbix-java-gateway.conf
 %else
%fillup_and_insserv -f zabbix-java-gateway
 %endif
%endif

%post agent
if [ "$1" -gt 1 ]; then
	chown root:%{agent_group} %{_sysconfdir}/zabbix/zabbix-agent*.conf
	chmod 0640 %{_sysconfdir}/zabbix/zabbix-agent*.conf
	chown -R root:%{agent_group} %{_rundir}/%{agent_user} || :
	chown -R root:%{agent_group} %{_localstatedir}/log/%{agent_user} || :
	if [ $(stat -c '%a' %{_rundir}/%{agent_user}) -ne '770' ]; then
		chmod 0770 %{_rundir}/%{agent_user}
		chmod 0770 %{_localstatedir}/log/%{agent_user}
	fi
fi
%if 0%{?suse_version} >= 1210
%service_add_post zabbix-agentd.service
systemd-tmpfiles --create /usr/lib/tmpfiles.d/zabbix-agentd.conf
%else
%fillup_and_insserv -f zabbix-agentd
%endif

%post server-mysql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix-server zabbix-server %{_sbindir}/zabbix-server-mysql 11 \
	--slave %{_mandir}/man1/zabbix-server.1%{?ext_man} zabbix-server.1%{?ext_man} %{_mandir}/man1/zabbix-server-mysql.1%{?ext_man}

%post server-postgresql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix-server zabbix-server %{_sbindir}/zabbix-server-postgresql 11 \
	--slave %{_mandir}/man1/zabbix-server.1%{?ext_man} zabbix-server.1%{?ext_man} %{_mandir}/man1/zabbix-server-postgresql.1%{?ext_man}

%post server-sqlite
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix-server zabbix-server %{_sbindir}/zabbix-server-sqlite 10 \
	--slave %{_mandir}/man1/zabbix-server.1%{?ext_man} zabbix-server.1%{?ext_man} %{_mandir}/man1/zabbix-server-sqlite.1%{?ext_man}

%post proxy-mysql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix-proxy zabbix-proxy %{_sbindir}/zabbix-proxy-mysql 11 \
	--slave %{_mandir}/man1/zabbix-proxy.1%{?ext_man} zabbix-proxy.1%{?ext_man} %{_mandir}/man1/zabbix-proxy-mysql.1%{?ext_man}

%post proxy-postgresql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix-proxy zabbix-proxy %{_sbindir}/zabbix-proxy-postgresql 11 \
	--slave %{_mandir}/man1/zabbix-proxy.1%{?ext_man} zabbix-proxy.1%{?ext_man} %{_mandir}/man1/zabbix-proxy-postgresql.1%{?ext_man}

%post proxy-sqlite
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix-proxy zabbix-proxy %{_sbindir}/zabbix-proxy-sqlite 10 \
	--slave %{_mandir}/man1/zabbix-proxy.1%{?ext_man} zabbix-proxy.1%{?ext_man} %{_mandir}/man1/zabbix-proxy-sqlite.1%{?ext_man}

%preun server
%if 0%{?suse_version} >= 1220
%service_del_preun zabbix-server.service
%else
%stop_on_removal zabbix-server
%endif

%preun proxy
%if 0%{?suse_version} >= 1220
%service_del_preun zabbix-proxy.service
%else
%stop_on_removal zabbix-proxy
%endif

%if 0%{?_with_java:1}
%preun java-gateway
 %if 0%{?suse_version} >= 1220
%service_del_preun zabbix-java-gateway.service
 %else
%stop_on_removal zabbix-java-gateway
 %endif
%endif

%preun agent
%if 0%{?suse_version} >= 1220
%service_del_preun zabbix-agentd.service
%else
%stop_on_removal zabbix-agentd
%endif

%preun server-mysql
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove zabbix-server %{_sbindir}/zabbix-server-mysql
fi

%preun server-postgresql
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove zabbix-server %{_sbindir}/zabbix-server-postgresql
fi

%preun server-sqlite
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove zabbix-server %{_sbindir}/zabbix-server-sqlite
fi

%preun proxy-mysql
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix-proxy-mysql
fi

%preun proxy-postgresql
if [ "$1" = 0 ] ; then
        %{_sbindir}/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix-proxy-postgresql
fi

%preun proxy-sqlite
if [ "$1" = 0 ] ; then
        %{_sbindir}/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix-proxy-sqlite
fi

%postun server
%if 0%{?suse_version} >= 1220
%service_del_postun zabbix-server.service
%else
%restart_on_update zabbix-server
%insserv_cleanup
%endif

%postun proxy
%if 0%{?suse_version} >= 1220
%service_del_postun zabbix-proxy.service
%else
%restart_on_update zabbix-proxy
%insserv_cleanup
%endif

%if 0%{?_with_java:1}
%postun java-gateway
 %if 0%{?suse_version} >= 1220
%service_del_postun zabbix-java-gateway.service
 %else
%restart_on_update zabbix-java-gateway
%insserv_cleanup
 %endif
%endif

%postun agent
%if 0%{?suse_version} >= 1220
%service_del_postun zabbix-agentd.service
%else
%restart_on_update zabbix-agentd
%insserv_cleanup
%endif

%files server
%defattr(-,root,root)
%doc AUTHORS ChangeLog database/ibm_db2 database/mysql  database/oracle database/postgresql database/sqlite3 upgrades/dbpatches rn3.0.0.html
# release notes are hardcoded on full release
#rn%%{version}%%{?rclevel}.html
%if 0%{?suse_version} <= 1220
%{_initddir}/zabbix-server
%endif
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix-server.conf
%if 0%{?suse_version} && 0%{?suse_version} > 1020
%config %{SuSeFirewall_services_dir}/zabbix-server
%endif
%{_bindir}/zabbix-get
%{_sbindir}/zabbix-server
%{_sbindir}/rczabbix-server
%attr(0770,root,%{server_group}) %dir %{_localstatedir}/log/%{server_user}
%ghost %attr(0770,root,%{server_group}) %dir %{_rundir}/%{server_user}
%{_mandir}/man1/zabbix-get.1*
%{_mandir}/man1/zabbix-server.1%{?ext_man}
%if 0%{?suse_version} >= 1220
%{_unitdir}/zabbix-server.service
%{_unitdir}/zabbix-server.service.requires
%{_prefix}/lib/tmpfiles.d/zabbix-server.conf
%endif
%ghost %{_sysconfdir}/alternatives/zabbix-server
%ghost %{_sysconfdir}/alternatives/zabbix-server.1%{?ext_man}

%files proxy
%defattr(-,root,root)
%if 0%{?suse_version} <= 1220
%{_initddir}/zabbix-proxy
%endif
%{_sbindir}/zabbix-proxy
%{_sbindir}/rczabbix-proxy
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix-proxy.conf
%if 0%{?suse_version} && 0%{?suse_version} > 1020
%config %{SuSeFirewall_services_dir}/zabbix-proxy
%endif
%attr(0770,root,%{server_group}) %dir %{_localstatedir}/log/%{server_user}
%ghost %attr(0770,root,%{server_group}) %dir %{_rundir}/%{server_user}
%{_mandir}/man1/zabbix-proxy.1%{?ext_man}
%if 0%{?suse_version} >= 1220
%{_unitdir}/zabbix-proxy.service
%{_unitdir}/zabbix-proxy.service.requires
%{_prefix}/lib/tmpfiles.d/zabbix-proxy.conf
%endif
%ghost %{_sysconfdir}/alternatives/zabbix-proxy
%ghost %{_sysconfdir}/alternatives/zabbix-proxy.1%{?ext_man}

%files agent
%defattr(-,root,root)
%if 0%{?suse_version} <= 1220
%{_initddir}/zabbix-agentd
%endif
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{agent_group}) %{_sysconfdir}/zabbix/zabbix-agent*.conf
%if 0%{?suse_version} && 0%{?suse_version} > 1020
%config %{SuSeFirewall_services_dir}/zabbix-agentd
%endif
%{_sbindir}/rczabbix-agentd
%{_sbindir}/zabbix-agentd
%{_sbindir}/zabbix-sender
%attr(0770,root,%{agent_group}) %dir %{_localstatedir}/log/%{agent_user}
%ghost %attr(0770,root,%{agent_group}) %dir %{_rundir}/%{agent_user}
%{_mandir}/man1/zabbix-agentd.1%{?ext_man}
%{_mandir}/man1/zabbix-sender.1%{?ext_man}
%if 0%{?suse_version} >= 1220
%{_unitdir}/zabbix-agentd.service
%{_prefix}/lib/tmpfiles.d/zabbix-agentd.conf
%endif

%files phpfrontend
%defattr(-,root,root)
%doc README.SUSE
%dir %{apache2_sysconfdir}
%dir %{apache2_sysconfdir}/conf.d
%config(noreplace) %{apache2_sysconfdir}/conf.d/zabbix.conf
%{_datadir}/zabbix

%files server-mysql
%defattr(-,root,root)
%{_sbindir}/zabbix-server-mysql
%if 0%{?suse_version} >= 1130
%ghost %_sysconfdir/alternatives/zabbix-server
%ghost %_sysconfdir/alternatives/zabbix-server.1%{?ext_man}
%endif
%{_mandir}/man1/zabbix-server-mysql.1%{?ext_man}

%files server-postgresql
%defattr(-,root,root)
%{_sbindir}/zabbix-server-postgresql
%if 0%{?suse_version} >= 1130
%ghost %_sysconfdir/alternatives/zabbix-server
%ghost %_sysconfdir/alternatives/zabbix-server.1%{?ext_man}
%endif
%{_mandir}/man1/zabbix-server-postgresql.1%{?ext_man}

%files server-sqlite
%defattr(-,root,root)
%{_sbindir}/zabbix-server-sqlite
%if 0%{?suse_version} >= 1130
%ghost %_sysconfdir/alternatives/zabbix-server
%ghost %_sysconfdir/alternatives/zabbix-server.1%{?ext_man}
%endif
%{_mandir}/man1/zabbix-server-sqlite.1%{?ext_man}

%files proxy-mysql
%defattr(-,root,root)
%{_sbindir}/zabbix-proxy-mysql
%if 0%{?suse_version} >= 1130
%ghost %_sysconfdir/alternatives/zabbix-proxy
%ghost %_sysconfdir/alternatives/zabbix-proxy.1%{?ext_man}
%endif
%{_mandir}/man1/zabbix-proxy-mysql.1%{?ext_man}

%files proxy-postgresql
%defattr(-,root,root)
%{_sbindir}/zabbix-proxy-postgresql
%if 0%{?suse_version} >= 1130
%ghost %_sysconfdir/alternatives/zabbix-proxy
%ghost %_sysconfdir/alternatives/zabbix-proxy.1%{?ext_man}
%endif
%{_mandir}/man1/zabbix-proxy-postgresql.1%{?ext_man}

%files proxy-sqlite
%defattr(-,root,root)
%{_sbindir}/zabbix-proxy-sqlite
%if 0%{?suse_version} >= 1130
%ghost %_sysconfdir/alternatives/zabbix-proxy
%ghost %_sysconfdir/alternatives/zabbix-proxy.1%{?ext_man}
%endif
%{_mandir}/man1/zabbix-proxy-sqlite.1%{?ext_man}

%if 0%{?_with_java:1}
%files java-gateway
%defattr(-,root,root)
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix-java-gateway.conf
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix-java-gateway-log.xml
%dir %{_prefix}/lib/zabbix-java-gateway
%{_bindir}/zabbix-java-gateway
%{_prefix}/lib/zabbix-java-gateway/zabbix-java-gateway-%{version}%{?rclevel}.jar
%{_prefix}/lib/zabbix-java-gateway/android-json-4.3_r3.1.jar
%{_prefix}/lib/zabbix-java-gateway/slf4j-api-1.6.1.jar
%{_prefix}/lib/zabbix-java-gateway/logback-core-0.9.27.jar
%{_prefix}/lib/zabbix-java-gateway/logback-classic-0.9.27.jar
%if 0%{?suse_version} <= 1220
%{_initddir}/zabbix-java-gateway
%endif
%{_sbindir}/rczabbix-java-gateway
%attr(0770,root,%{server_group}) %dir %{_localstatedir}/log/%{server_user}
%ghost %attr(0770,root,%{server_group}) %dir %{_rundir}/%{server_user}
%if 0%{?suse_version} > 1020
%config %{SuSeFirewall_services_dir}/zabbix-java-gateway
%endif
%if 0%{?suse_version} >= 1220
%{_unitdir}/zabbix-java-gateway.service
%{_prefix}/lib/tmpfiles.d/zabbix-java-gateway.conf
%endif
%endif

%files bash-completion
%defattr(-,root,root)
%{bashcompletiondir}/zabbix-daemons-completion
%{bashcompletiondir}/zabbix-get-completion
%{bashcompletiondir}/zabbix-sender-completion
%{bashcompletiondir}/zabbix-agentd-completion
%{bashcompletiondir}/zabbix-server-completion
%{bashcompletiondir}/zabbix-proxy-completion

%changelog
