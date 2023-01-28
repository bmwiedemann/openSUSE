#
# spec file for package zabbix
#
# Copyright (c) 2023 SUSE LLC
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


%define server_user  zabbixs
%define server_group zabbixs
# keep zabbix user for backwards compatibility of agent
%define agent_user   zabbix
%define agent_group  zabbix
%define SUSEfirewall_services_dir %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services
Name:           zabbix
Version:        6.0.12
Release:        0
Summary:        Distributed monitoring system
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://www.zabbix.com
Source0:        https://cdn.zabbix.com/zabbix/sources/stable/6.0/zabbix-%{version}.tar.gz
Source1:        rn6.0.0.html
Source2:        zabbix-tmpfiles.conf
Source3:        zabbix-java-gateway.sh
Source4:        zabbix-logrotate.in
Source5:        apache2-zabbix.conf
Source6:        README.SUSE
Source7:        zabbix-server.firewall
Source8:        zabbix-agentd.firewall
Source9:        zabbix-proxy.firewall
Source10:       zabbix-java-gateway.firewall
Source11:       zabbix-proxy.service
Source12:       zabbix-agentd.service
Source13:       zabbix-server.service
Source14:       zabbix-java-gateway.service
Source15:       README-SSL.SUSE
# PATCH-FIX-UPSTREAM zabbix-6.0.12-new-m4-pgsql.patch fix for opensuse issue caused/solved by bnc#1120035
Patch0:         zabbix-6.0.12-new-m4-pgsql.patch
# PATCH-FIX-UPSTREAN  zabbix-6.0.12-curl-fixes.patch fix for curl specific issue https://git.zabbix.com/projects/ZBX/repos/zabbix/pull-requests/4946/commits/f462538f52a1fba52fdd4010e40fe7281044f6b1?since=52c6b9703eacf3252ec66117a8cff094624b9217#include/common/zbxsysinc.h
Patch2:         zabbix-6.0.12-curl-fixes.patch
# PATCH-FIX-OPENSUSE  zabbix-6.0.12-netsnmp-fixes.patch fix for removed md5 auth protocol
Patch3:         zabbix-6.0.12-netsnmp-fixes.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  java-devel >= 1.6
BuildRequires:  libmysqlclient-devel
BuildRequires:  libtool
BuildRequires:  logrotate
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  unixODBC-devel
BuildRequires:  update-alternatives
BuildRequires:  pkgconfig(OpenIPMI)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
%{?systemd_requires}

%description
Zabbix is a distributed monitoring system.

Zabbix is software that monitors numerous parameters of a network and the
health and integrity of servers. Zabbix uses a flexible notification mechanism
that allows users to configure e-mail based alerts for virtually any event.
This allows a fast reaction to server problems. Zabbix offers excellent
reporting and data visualisation features based on the stored data. This makes
Zabbix ideal for capacity planning.

Zabbix supports both polling and trapping. All Zabbix reports and statistics,
as well as configuration parameters, are accessed through a web-based frontend.
A web-based frontend ensures that the status of your network and the health of
your servers can be assessed from any location. Properly configured, Zabbix can
play an important role in monitoring IT infrastructure. This is equally true
for small organisations with a few servers and for large companies with a
multitude of servers.

%package agent
Summary:        Local resource monitor agent for Zabbix
Group:          System/Monitoring
Requires:       logrotate
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Conflicts:      zabbix-agent

%description agent
The Zabbix agent monitors local resources and relays information to the server.

%package server
Summary:        System files for the Zabbix server
Group:          System/Monitoring
Requires:       fping
Requires:       logrotate
Requires:       update-alternatives
Requires:       zabbix_server_binary = %{version}-%{release}
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Conflicts:      zabbix-server

%description server
The Zabbix server component.

%package proxy
Summary:        System files for the Zabbix proxy
Group:          System/Monitoring
Requires:       fping
Requires:       logrotate
Requires:       update-alternatives
Requires:       zabbix_proxy_binary = %{version}-%{release}
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Conflicts:      zabbix-proxy

%description proxy
The Zabbix proxy component.

%package ui
Summary:        Zabbix web frontend (php)
Group:          Productivity/Networking/Web/Frontends
Requires:       apache2
Requires:       php8
Requires:       php8-bcmath
Requires:       php8-ctype
Requires:       php8-gd
Requires:       php8-gettext
Requires:       php8-ldap
Requires:       php8-mbstring
Requires:       php8-sockets
Requires:       php8-xmlreader
Requires:       php8-xmlwriter
Suggests:       php8-mysqli
Suggests:       php8-pgsql
Conflicts:      zabbix-phpfrontend
Obsoletes:      zabbix-phpfrontend < 6.0.0

%description ui
The Zabbix PHP frontend allows access via standard web browsers.

NOTE: You still have to install the PHP package which contains your db driver!

%package server-mysql
Summary:        Zabbix server with MySQL support
Group:          System/Monitoring
Requires:       %{name}-server = %{version}-%{release}
Requires:       mariadb
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      zabbix-server-mysql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_server_binary = %{version}-%{release}

%description server-mysql
The Zabbix server compiled with MySQL support.

%package server-postgresql
Summary:        Zabbix server with PostgreSQL support
Group:          System/Monitoring
Requires:       %{name}-server = %{version}-%{release}
Requires:       postgresql
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      zabbix-server-postgresql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_server_binary = %{version}-%{release}

%description server-postgresql
The Zabbix server compiled with PostgreSQL support.

%package proxy-mysql
Summary:        Zabbix proxy with MySQL support
Group:          System/Monitoring
Requires:       %{name}-proxy = %{version}-%{release}
Requires:       mariadb
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      zabbix-proxy-mysql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_proxy_binary = %{version}-%{release}

%description proxy-mysql
The Zabbix proxy compiled with MySQL support.

%package proxy-postgresql
Summary:        Zabbix proxy with PostgreSQL support
Group:          System/Monitoring
Requires:       %{name}-proxy = %{version}-%{release}
Requires:       postgresql
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      zabbix-proxy-postgresql
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_proxy_binary = %{version}-%{release}

%description proxy-postgresql
The Zabbix proxy compiled with PostgreSQL support.

%package proxy-sqlite
Summary:        Zabbix proxy with SQLite support
Group:          System/Monitoring
Requires:       %{name}-proxy = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      zabbix-proxy-sqlite
Provides:       %{name} = %{version}-%{release}
Provides:       zabbix_proxy_binary = %{version}-%{release}

%description proxy-sqlite
The Zabbix proxy compiled with SQLite support.

%package java-gateway
Summary:        Zabbix Java gateway
Group:          System/Monitoring
Requires:       jre
Requires(pre):  shadow
Conflicts:      zabbix-java-gateway
Provides:       %{name} = %{version}-%{release}

%description java-gateway
JMX monitoring can be used to monitor JMX counters of a Java
application. To retrieve the value of a particular JMX counter on a
host, the Zabbix server queries the Zabbix Java gateway, which in
turn uses the JMX management API to query the application of interest
remotely.

%prep
%setup -q -n zabbix-%{version}
%patch0
#%%patch1
%patch2
%patch3

cp %{SOURCE6} .
# fix source & config files to respect adapted names
for file in src/zabbix_java/settings.sh src/zabbix_java/lib/logback.xml %{SOURCE3} conf/*.conf  misc/init.d/suse/*/zabbix_* src/zabbix_server/server.c \
	src/zabbix_server/alerter/alerter.c src/zabbix_agent/zbxconf.c src/zabbix_agent/zabbix_agentd.c src/zabbix_proxy/proxy.c ChangeLog; do
	sed -i -e "s@/home/zabbix/bin@%{_bindir}@g" \
		-e "s@^[# ]*PidFile=/tmp/zabbix_@PidFile=%{_rundir}/%{agent_user}/zabbix_@g" \
		-e "s@^[# ]*LogFile=/tmp/zabbix_@LogFile=%{_localstatedir}/log/%{agent_user}/zabbix_@g" \
		-e "s@^[# ]*DBSocket=/tmp/mysql.sock@DBSocket=%{_rundir}/mysql/mysql.sock@g" \
		-e "s@^[# ]*SocketDir=/tmp@SocketDir=%{_rundir}/%{agent_user}@g" \
		-e "s@DBUser=root@DBUser=zabbix@g" \
		-e "s@^[# ]*DBPassword=.*@DBPassword=zabbix@g" \
		-e "s@Hostname=Zabbix Server@Hostname=Zabbix_Server@" \
		-e "s@GW_PID:=%{_localstatedir}/run/zabbix/zabbix-java-gateway.pid@GW_PID:=%{_rundir}/%{server_user}/zabbix-java-gateway.pid@g" \
		-e "s@GW_LOGFILE:=%{_localstatedir}/log/zabbix/zabbix-java-gateway.log@GW_LOGFILE:=%{_localstatedir}/log/%{server_user}/zabbix-java-gateway.log@g" $file
done

# fix server, java and proxy (again) config for log and run location...
for file in src/zabbix_java/settings.sh conf/zabbix_proxy.conf conf/zabbix_server.conf ; do
	sed -i -e "s#^[# ]*LogFile=%{_localstatedir}/log/.*/zabbix_#LogFile=%{_localstatedir}/log/%{server_user}/zabbix_#g" \
		-e "s#^[# ]*PidFile=%{_rundir}/.*/zabbix_#PidFile=%{_rundir}/%{server_user}/zabbix_#g" \
		-e "s#^[# ]*SocketDir=%{_rundir}/%{agent_user}#SocketDir=%{_rundir}/%{server_user}#g" \
		-e 's#PID_FILE="%{_rundir}/.*/zabbix_#PID_FILE="%{_rundir}/%{server_user}/zabbix_#g' $file
done

# fix db content to respect adapted names and suse naming conventions
for file in database/*/data.sql; do
	sed -i -e "s#syslogd#syslog-ng#g" \
		-e "s#Syslogd#Syslog-ng#g" \
		-e "s#httpd#httpd2-prefork#g" $file
done
##### Fix for date time macros
REF_DATE=$(LANG=C date -r configure +"%%b %%d %%Y")
REF_TIME=$(LANG=C date -r configure +"%%H:%%M:%%S")
sed -i -e "s/__DATE__/\"${REF_DATE}\"/g" -e "s/__TIME__/\"${REF_TIME}\"/g" src/libs/zbxcommon/str.c
#####
##### Fix location of zabbix java gateway location
sed -ri 's@^(ZABBIX_JAVA_CONF=.\{ZABBIX_JAVA_CONF:=).*@\1%{_sysconfdir}/zabbix/zabbix-java-gateway.conf}@g' %{SOURCE3}

# Remove prebuilt Windows binaries
rm -rf bin

#make separate directories for each config
cd ..
cp -r zabbix-%{version} zabbix-%{version}-postgresql
cp -r zabbix-%{version} zabbix-%{version}-sqlite
cd -

%build
ZABBIX_BASIC_CONFIG="--enable-proxy --enable-server --enable-agent  --sysconfdir=%{_sysconfdir}/zabbix \
                     --with-openipmi --enable-java --enable-ipv6 --with-ssh2 --with-ldap --with-unixodbc \
                     --with-libcurl --with-net-snmp --with-libxml2 --with-openssl --with-libpcre --with-libevent"

# configure MySQL repo (here)
autoreconf -fvi
%configure $ZABBIX_BASIC_CONFIG --with-mysql --without-postgresql --without-sqlite3
make %{?_smp_mflags}

# configure PostgreSQL repo
cd ../zabbix-%{version}-postgresql
autoreconf -fvi
%configure $ZABBIX_BASIC_CONFIG --with-postgresql --without-mysql --without-sqlite3
make %{?_smp_mflags}
cd -

# configure SQLite repo
cd ../zabbix-%{version}-sqlite
autoreconf -fvi
%configure $ZABBIX_BASIC_CONFIG --disable-server --enable-proxy --with-sqlite3 --without-postgresql --without-mysql
make %{?_smp_mflags}
cd -

%install
# install the binaries

%make_install -C ../zabbix-%{version}-sqlite
mv %{buildroot}%{_sbindir}/zabbix_proxy %{buildroot}%{_sbindir}/zabbix_proxy-sqlite

%make_install -C ../zabbix-%{version}-postgresql
mv %{buildroot}%{_sbindir}/zabbix_server %{buildroot}%{_sbindir}/zabbix_server-postgresql
mv %{buildroot}%{_sbindir}/zabbix_proxy %{buildroot}%{_sbindir}/zabbix_proxy-postgresql

%make_install
mv %{buildroot}%{_sbindir}/zabbix_server %{buildroot}%{_sbindir}/zabbix_server-mysql
mv %{buildroot}%{_sbindir}/zabbix_proxy %{buildroot}%{_sbindir}/zabbix_proxy-mysql

mv %{buildroot}%{_bindir}/zabbix_sender %{buildroot}%{_sbindir}/zabbix_sender

# create directory structure
install -d %{buildroot}%{_localstatedir}/log/%{server_user}
install -d %{buildroot}%{_localstatedir}/log/%{agent_user}

# move java gateway files
mkdir -p %{buildroot}/%{_prefix}/lib/zabbix-java-gateway
mv %{buildroot}%{_sbindir}/zabbix_java/lib/*.jar %{buildroot}%{_prefix}/lib/zabbix-java-gateway
mv %{buildroot}%{_sbindir}/zabbix_java/bin/*.jar %{buildroot}%{_prefix}/lib/zabbix-java-gateway
mv %{buildroot}%{_sbindir}/zabbix_java/settings.sh %{buildroot}%{_sysconfdir}/zabbix/zabbix-java-gateway.conf
mv %{buildroot}%{_sbindir}/zabbix_java/lib/logback.xml %{buildroot}%{_sysconfdir}/zabbix/zabbix-java-gateway-log.xml
install -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/zabbix-java-gateway
# we do not need the rest
rm -r %{buildroot}%{_sbindir}/zabbix_java

# install the php frontend
mkdir -p %{buildroot}%{_datadir}/zabbix
cp -r ui/* %{buildroot}%{_datadir}/zabbix
install -Dm 0644 %{SOURCE5} %{buildroot}%{apache_sysconfdir}/conf.d/zabbix.conf
# remove .htaccess files as access rules are moved to zabbix.conf
find %{buildroot}%{_datadir}/zabbix -name .htaccess -exec rm -v {} \;

# Install log rotation
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
sed -e 's|COMPONENT|agentd|g; s|USER|zabbix|g' %{SOURCE4} > \
     %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-agent
sed -e 's|COMPONENT|server|g; s|USER|zabbixs|g' %{SOURCE4} > \
     %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-server
sed -e 's|COMPONENT|proxy|g; s|USER|zabbixs|g' %{SOURCE4} > \
     %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-proxy

%fdupes %{buildroot}

# install firewall description files for SLE 12 / Leap 42
%if 0%{?suse_version} < 1500
install -Dm 0644 %{SOURCE7} %{buildroot}%{SUSEfirewall_services_dir}/zabbix_server
install -Dm 0644 %{SOURCE8} %{buildroot}%{SUSEfirewall_services_dir}/zabbix_agentd
install -Dm 0644 %{SOURCE9} %{buildroot}%{SUSEfirewall_services_dir}/zabbix_proxy
install -Dm 0644 %{SOURCE10} %{buildroot}%{SUSEfirewall_services_dir}/zabbix-java-gateway
%endif

# install systemd unit files
install -Dm 0644 %{SOURCE11} %{buildroot}%{_unitdir}/zabbix_proxy.service
install -Dm 0644 %{SOURCE12} %{buildroot}%{_unitdir}/zabbix_agentd.service
install -Dm 0644 %{SOURCE13} %{buildroot}%{_unitdir}/zabbix_server.service
install -Dm 0644 %{SOURCE14} %{buildroot}%{_unitdir}/zabbix-java-gateway.service
install -dm 0755 %{buildroot}/%{_unitdir}/zabbix_server.service.requires
install -dm 0755 %{buildroot}/%{_unitdir}/zabbix_proxy.service.requires

# set the rc sym links
ln -s service %{buildroot}%{_sbindir}/rczabbix_agentd
ln -s service %{buildroot}%{_sbindir}/rczabbix_server
ln -s service %{buildroot}%{_sbindir}/rczabbix_proxy
ln -s service %{buildroot}%{_sbindir}/rczabbix-java-gateway

# this stupidity is required because i do not wanna create separate zabbix-common
# in case i ever do it will put it under one scope...
install -Dm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/zabbix_agentd.conf
# here I suppose server_user==server_group (and agent_user==agent_group, which is for compatibility reasons)
sed -i 's@%{agent_user}@%{server_user}@g' %{SOURCE2}
install -Dm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/zabbix_server.conf
install -Dm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/zabbix_proxy.conf
install -Dm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/zabbix-java-gateway.conf
###################################################################################

# update-alternatives
install -d -m 0755 %{buildroot}%{_sysconfdir}/alternatives
touch -r /bin/true %{buildroot}%{_sysconfdir}/alternatives/zabbix_server
touch -r /bin/true %{buildroot}%{_sysconfdir}/alternatives/zabbix_proxy
ln -s %{_sysconfdir}/alternatives/zabbix_server %{buildroot}%{_sbindir}/zabbix_server
ln -s %{_sysconfdir}/alternatives/zabbix_proxy %{buildroot}%{_sbindir}/zabbix_proxy

# set links zabbix-* -> zabbix_* (to avoid confusion among users)
ln -s %{_sbindir}/zabbix_server %{buildroot}%{_sbindir}/zabbix-server
ln -s %{_sbindir}/zabbix_server %{buildroot}%{_sbindir}/zabbix-proxy
ln -s %{_sbindir}/zabbix_agentd %{buildroot}%{_sbindir}/zabbix-agentd
ln -s %{_sbindir}/zabbix_sender %{buildroot}%{_sbindir}/zabbix-sender
ln -s %{_bindir}/zabbix_get %{buildroot}%{_bindir}/zabbix-get

# Remove Makefiles from database directories so they don't get picked up by %%doc
rm database/*/Makefile*

# Release Notes - what has changed against Zabbix 3.x
cp %{SOURCE1} .

# SSL README
cp %{SOURCE15} .

%pre server
# Server daemon
%{_bindir}/getent group %{server_group} >/dev/null || %{_sbindir}/groupadd -r %{server_group}
%{_bindir}/getent passwd %{server_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{server_user} -s /bin/false -c "Zabbix Server Daemon" -g %{server_group} %{server_user}
%service_add_pre zabbix_server.service
exit 0

%pre proxy
# Proxy daemon
%{_bindir}/getent group %{server_group} >/dev/null || %{_sbindir}/groupadd -r %{server_group}
%{_bindir}/getent passwd %{server_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{server_user} -s /bin/false -c "Zabbix Proxy Daemon" -g %{server_group} %{server_user}
%service_add_pre zabbix_proxy.service
exit 0

%pre agent
# Agent daemon
%{_bindir}/getent group %{agent_group} >/dev/null || %{_sbindir}/groupadd -r %{agent_group}
%{_bindir}/getent passwd %{agent_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{agent_user} -s /bin/false -c "Zabbix Agent Daemon" -g %{agent_group} %{agent_user}
%service_add_pre zabbix_agentd.service
exit 0

%pre java-gateway
# Java daemon
%{_bindir}/getent group %{server_group} >/dev/null || %{_sbindir}/groupadd -r %{server_group}
%{_bindir}/getent passwd %{server_user} >/dev/null || %{_sbindir}/useradd -r -d %{_localstatedir}/lib/%{server_user} -s /bin/false -c "Zabbix Java Daemon" -g %{server_group} %{server_user}
%service_add_pre zabbix-java-gateway.service
exit 0

%post server
%service_add_post zabbix_server.service
%tmpfiles_create %{_tmpfilesdir}/zabbix_server.conf
echo "Please read %{_docdir}/%{name}-server/README-SSL.SUSE to set up SSL on Zabbix server."

%post proxy
%service_add_post zabbix_proxy.service
%tmpfiles_create %{_tmpfilesdir}/zabbix_proxy.conf
echo "Please read %{_docdir}/%{name}-proxy/README-SSL.SUSE to set up SSL on Zabbix proxy."

%post java-gateway
%service_add_post zabbix-java-gateway.service
%tmpfiles_create %{_tmpfilesdir}/zabbix-java-gateway.conf

%post agent
%service_add_post zabbix_agentd.service
%tmpfiles_create %{_tmpfilesdir}/zabbix_agentd.conf
echo "Please read %{_docdir}/%{name}-agent/README-SSL.SUSE to set up SSL on Zabbix agent."

%post server-mysql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix_server zabbix_server %{_sbindir}/zabbix_server-mysql 12

%post server-postgresql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix_server zabbix_server %{_sbindir}/zabbix_server-postgresql 11

%post proxy-mysql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix_proxy %{_sbindir}/zabbix_proxy-mysql 12

%post proxy-postgresql
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix_proxy %{_sbindir}/zabbix_proxy-postgresql 11

%post proxy-sqlite
%{_sbindir}/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix_proxy %{_sbindir}/zabbix_proxy-sqlite 10

%preun server
%service_del_preun zabbix_server.service

%preun proxy
%service_del_preun zabbix_proxy.service

%preun java-gateway
%service_del_preun zabbix-java-gateway.service

%preun agent
%service_del_preun zabbix_agentd.service

%postun server
%service_del_postun zabbix_server.service

%postun proxy
%service_del_postun zabbix_proxy.service

%postun java-gateway
%service_del_postun zabbix-java-gateway.service

%postun agent
%service_del_postun zabbix_agentd.service

%postun server-mysql
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove zabbix_server %{_sbindir}/zabbix_server-mysql
fi

%postun server-postgresql
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove zabbix_server %{_sbindir}/zabbix_server-postgresql
fi

%postun proxy-mysql
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove zabbix_proxy %{_sbindir}/zabbix_proxy-mysql
fi

%postun proxy-postgresql
if [ "$1" = 0 ] ; then
        %{_sbindir}/update-alternatives --remove zabbix_proxy %{_sbindir}/zabbix_proxy-postgresql
fi

%postun proxy-sqlite
if [ "$1" = 0 ] ; then
        %{_sbindir}/update-alternatives --remove zabbix_proxy %{_sbindir}/zabbix_proxy-sqlite
fi

%files server
%doc AUTHORS ChangeLog database/mysql database/oracle database/postgresql database/sqlite3 rn6.0.0.html README-SSL.SUSE
%if 0%{?suse_version} < 1500
%config %{SUSEfirewall_services_dir}/zabbix_server
%endif
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix_server.conf
%{_bindir}/zabbix_get
%{_bindir}/zabbix-get
%{_bindir}/zabbix_js
%{_sbindir}/zabbix_server
%{_sbindir}/zabbix-server
%{_sbindir}/rczabbix_server
%attr(0770,root,%{server_group}) %dir %{_localstatedir}/log/%{server_user}
%ghost %attr(0770,root,%{server_group}) %dir %{_rundir}/%{server_user}
%{_mandir}/man1/zabbix_get.1%{?ext_man}
%{_mandir}/man8/zabbix_server.8%{?ext_man}
%{_unitdir}/zabbix_server.service
%{_unitdir}/zabbix_server.service.requires
%{_tmpfilesdir}/zabbix_server.conf
%ghost %{_sysconfdir}/alternatives/zabbix_server
%ghost %{_sysconfdir}/alternatives/zabbix_server.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server

%files proxy
%doc README-SSL.SUSE
%if 0%{?suse_version} < 1500
%config %{SUSEfirewall_services_dir}/zabbix_proxy
%endif
%{_sbindir}/zabbix_proxy
%{_sbindir}/zabbix-proxy
%{_sbindir}/rczabbix_proxy
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%attr(0770,root,%{server_group}) %dir %{_localstatedir}/log/%{server_user}
%ghost %attr(0770,root,%{server_group}) %dir %{_rundir}/%{server_user}
%{_mandir}/man8/zabbix_proxy.8%{?ext_man}
%{_unitdir}/zabbix_proxy.service
%{_unitdir}/zabbix_proxy.service.requires
%{_tmpfilesdir}/zabbix_proxy.conf
%ghost %{_sysconfdir}/alternatives/zabbix_proxy
%ghost %{_sysconfdir}/alternatives/zabbix_proxy.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-proxy

%files agent
%doc README-SSL.SUSE
%if 0%{?suse_version} < 1500
%config %{SUSEfirewall_services_dir}/zabbix_agentd
%endif
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{agent_group}) %{_sysconfdir}/zabbix/zabbix_agent*.conf
%{_sbindir}/rczabbix_agentd
%{_sbindir}/zabbix_agentd
%{_sbindir}/zabbix-agentd
%{_sbindir}/zabbix_sender
%{_sbindir}/zabbix-sender
%attr(0770,root,%{agent_group}) %dir %{_localstatedir}/log/%{agent_user}
%ghost %attr(0770,root,%{agent_group}) %dir %{_rundir}/%{agent_user}
%{_mandir}/man8/zabbix_agentd.8%{?ext_man}
%{_mandir}/man1/zabbix_sender.1%{?ext_man}
%{_unitdir}/zabbix_agentd.service
%{_tmpfilesdir}/zabbix_agentd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-agent

%files ui
%doc README.SUSE
%dir %{apache_sysconfdir}
%dir %{apache_sysconfdir}/conf.d
%config(noreplace) %{apache_sysconfdir}/conf.d/zabbix.conf
%{_datadir}/zabbix

%files server-mysql
%{_sbindir}/zabbix_server-mysql
%{_sbindir}/zabbix_server
%ghost %{_sysconfdir}/alternatives/zabbix_server

%files server-postgresql
%{_sbindir}/zabbix_server-postgresql
%{_sbindir}/zabbix_server
%ghost %{_sysconfdir}/alternatives/zabbix_server

%files proxy-mysql
%{_sbindir}/zabbix_proxy-mysql
%{_sbindir}/zabbix_proxy
%ghost %{_sysconfdir}/alternatives/zabbix_proxy

%files proxy-postgresql
%{_sbindir}/zabbix_proxy-postgresql
%{_sbindir}/zabbix_proxy
%ghost %{_sysconfdir}/alternatives/zabbix_proxy

%files proxy-sqlite
%{_sbindir}/zabbix_proxy-sqlite
%{_sbindir}/zabbix_proxy
%ghost %{_sysconfdir}/alternatives/zabbix_proxy

%files java-gateway
%if 0%{?suse_version} < 1500
%config %{SUSEfirewall_services_dir}/zabbix-java-gateway
%endif
%dir %{_sysconfdir}/zabbix
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix-java-gateway.conf
%config(noreplace) %attr(0640, root, %{server_group}) %{_sysconfdir}/zabbix/zabbix-java-gateway-log.xml
%dir %{_prefix}/lib/zabbix-java-gateway
%{_bindir}/zabbix-java-gateway
%{_prefix}/lib/zabbix-java-gateway/zabbix-java-gateway-%{version}%{?rclevel}.jar
%{_prefix}/lib/zabbix-java-gateway/android-json-4.3_r3.1.jar
%{_prefix}/lib/zabbix-java-gateway/slf4j-api-1.7.32.jar
%{_prefix}/lib/zabbix-java-gateway/logback-core-1.2.9.jar
%{_prefix}/lib/zabbix-java-gateway/logback-classic-1.2.9.jar
%{_sbindir}/rczabbix-java-gateway
%attr(0770,root,%{server_group}) %dir %{_localstatedir}/log/%{server_user}
%ghost %attr(0770,root,%{server_group}) %dir %{_rundir}/%{server_user}
%{_unitdir}/zabbix-java-gateway.service
%{_tmpfilesdir}/zabbix-java-gateway.conf

%changelog
