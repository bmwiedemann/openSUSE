#
# spec file for package monitoring-plugins
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


Name:           monitoring-plugins
Version:        2.3~alpha.20200520T233014.cadac85e
Release:        0
Summary:        The Monitoring Plug-Ins
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          System/Monitoring
URL:            http://monitoring-plugins.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source11:       %{name}-permissions
Source12:       %{name}-README.SUSE
Source13:       %{name}-README.SUSE-check_dhcp
Source14:       %{name}-README.SUSE-check_icmp
Source15:       %{name}-README.SUSE-check_ide_smart
Source16:       usr.lib.nagios.plugins.check_dhcp
Source17:       usr.lib.nagios.plugins.check_ntp_time
Source18:       %{name}.check_cups.sh
Source19:       usr.lib.nagios.plugins.check_cups
Source20:       %{name}-README.SUSE-check_cups
Source22:       usr.lib.nagios.plugins.check_ping
Source23:       usr.lib.nagios.plugins.check_icmp
Source24:       usr.lib.nagios.plugins.check_ide_smart
Source25:       usr.lib.nagios.plugins.check_ssh
Source26:       check_ircd_ssl
Source27:       %{name}-README-extra-opts
Source28:       %{name}-README.SUSE-check_ping
Source29:       %{name}-README.SUSE-check_ntp_time
Source30:       usr.lib.nagios.plugins.check_disk
Source31:       usr.lib.nagios.plugins.check_load
Source32:       usr.lib.nagios.plugins.check_procs
Source33:       usr.lib.nagios.plugins.check_swap
Source34:       usr.lib.nagios.plugins.check_users
Source35:       usr.lib.nagios.plugins.check_procs.sle15
Source50:       nrpe-check_mailq
Source51:       nrpe-check_load
Source52:       nrpe-check_ntp_time
Source53:       nrpe-check_swap
Source54:       nrpe-check_partition
Source55:       nrpe-check_proc_cron
Source56:       nrpe-check_total_procs
Source57:       nrpe-check_users
Source58:       nrpe-check_zombie_procs
Source59:       nrpe-check_mysql
Source60:       nrpe-check_ups
# PATCH-FIX-UPSTREAM Quote the options comming in from users (path names might contain whitespaces)
Patch1:         %{name}-2.1.1-check_logfile.patch
# PATCH-FIX-UPSTREAM Allow to ping IPv4 with check_ping again for dual stack hosts: https://github.com/monitoring-plugins/monitoring-plugins/issues/1550
Patch6:         %{name}-1.4.6-no_chown.patch
# PATCH-FIX-UPSTREAM Use correct pointer
Patch11:        %{name}.check_snmp.arrayaddress.patch
# PATCH-FIX-UPSTREAM print out all arguments out a Group if in verbose mode
Patch15:        %{name}-too_few_arguments_for_check_disk.patch
# PATCH-FIX-UPSTREAM port should be integer, not character
Patch118:       %{name}.check_hpjd.c-64bit-portability-issue.patch
# PATCH-FIX-UPSTREAM kstreitova@suse.com -- fix build with MariaDB 10.2
Patch119:       monitoring-plugins-2.2-mariadb_102_build_fix.patch
# PATCH-FIX-UPSTREAM see https://bugzilla.redhat.com/512559
Patch121:       %{name}-wrong_return_in_check_swap.patch
BuildRequires:  bind-utils
BuildRequires:  dhcp-devel
BuildRequires:  fping
%if 0%{?suse_version}
PreReq:         permissions
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  iputils
BuildRequires:  libdbi-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  nagios-rpm-macros
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssh
BuildRequires:  openssl-devel
%if 0%{?fedora_version} ||  0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  net-snmp-perl
BuildRequires:  net-snmp-utils
%else
BuildRequires:  perl-Net-SNMP
%endif
BuildRequires:  postfix
BuildRequires:  postgresql-devel
BuildRequires:  procps
BuildRequires:  python-devel
BuildRequires:  samba-client
%if 0%{?suse_version}
%if 0%{?suse_version} > 1020
BuildRequires:  freeradius-client-devel
BuildRequires:  rpcbind
%else
BuildRequires:  portmap
BuildRequires:  radiusclient
%endif
%if 0%{?suse_version} > 910
BuildRequires:  krb5-devel
%if 0%{?suse_version} > 1310
BuildRequires:  syslog
%else
BuildRequires:  syslog-ng
%endif
%else
BuildRequires:  heimdal-devel
%endif
%else
BuildRequires:  krb5-devel
%endif
# recommend the old, included checks to allow an easy update - but
# also allow users to deselect some of the new sub-packages
%if 0%{?suse_version}
Recommends:     %{name}-bgpstate
Recommends:     %{name}-breeze
Recommends:     %{name}-by_ssh
Recommends:     %{name}-cluster
Recommends:     %{name}-dhcp
Recommends:     %{name}-dig
Recommends:     %{name}-disk
Recommends:     %{name}-disk_smb
Recommends:     %{name}-dns
Recommends:     %{name}-dummy
Recommends:     %{name}-file_age
Recommends:     %{name}-flexlm
Recommends:     %{name}-http
Recommends:     %{name}-icmp
Recommends:     %{name}-ide_smart
Recommends:     %{name}-ifoperstatus
Recommends:     %{name}-ifstatus
Recommends:     %{name}-ircd
Recommends:     %{name}-linux_raid
Recommends:     %{name}-load
Recommends:     %{name}-log
Recommends:     %{name}-mailq
Recommends:     %{name}-mrtg
Recommends:     %{name}-mrtgtraf
Recommends:     %{name}-nt
Recommends:     %{name}-ntp_peer
Recommends:     %{name}-ntp_time
Recommends:     %{name}-nwstat
Recommends:     %{name}-oracle
Recommends:     %{name}-overcr
Recommends:     %{name}-ping
Recommends:     %{name}-procs
Recommends:     %{name}-real
Recommends:     %{name}-rpc
Suggests:       %{name}-nagios
%ifnarch ppc ppc64 sparc sparc64 s390 s390x
Recommends:     %{name}-sensors
%endif
Recommends:     %{name}-smtp
Recommends:     %{name}-ssh
Recommends:     %{name}-swap
Recommends:     %{name}-tcp
Recommends:     %{name}-time
Recommends:     %{name}-ups
Recommends:     %{name}-users
Recommends:     %{name}-wave
Suggests:       %{name}-cups
Obsoletes:      nagios-plugins <= %{version}
Provides:       nagios-plugins = 1.5
%endif
%define         apt_get_command %{_bindir}/apt-get
%define         qstat_command   %{_bindir}/qstat
%if ! 0%{?suse_version}
%define         _libexecdir     %{nagios_plugindir}
%endif

%description
The actual service checks on current monitoring solutions like Icinga,
Nagios or Shinken (just to name a few) are performed by separate
"plugin" programs which return the status of the checks to the
running daemon.

This package contains those plugins.

%package  extras
Summary:        Plug-Ins which depend on additional packages
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
%if 0%{?suse_version}
Recommends:     %{name}-fping
Recommends:     %{name}-hpjd
Recommends:     %{name}-ldap
Recommends:     %{name}-mysql
Recommends:     %{name}-pgsql
Recommends:     %{name}-snmp
Suggests:       %{name}-apt
Suggests:       %{name}-game
%endif
Provides:       nagios-plugins-extras = %{version}
Obsoletes:      nagios-plugins-extras <= 1.5

%description extras
These are additional monitoring checks that require additional packages
which have to be installed.

%package all
Summary:        All Monitoring-Plugin checks
Group:          System/Monitoring
%if 0%{?suse_version}
Recommends:     %{name}-apt
Recommends:     %{name}-bgpstate
Recommends:     %{name}-bind
Recommends:     %{name}-bonding
Recommends:     %{name}-breeze
Recommends:     %{name}-by_ssh
Recommends:     %{name}-clamav
Recommends:     %{name}-cluster
Recommends:     %{name}-contentage
Recommends:     %{name}-cups
Recommends:     %{name}-dbi-mysql
Recommends:     %{name}-dbi-pgsql
Recommends:     %{name}-dbi-sqlite3
Recommends:     %{name}-dhcp
Recommends:     %{name}-dig
Recommends:     %{name}-disk
Recommends:     %{name}-disk_smb
Recommends:     %{name}-diskio
Recommends:     %{name}-dns
Recommends:     %{name}-dummy
Recommends:     %{name}-file_age
Recommends:     %{name}-flexlm
Recommends:     %{name}-fping
Recommends:     %{name}-game
Recommends:     %{name}-hpasm
Recommends:     %{name}-hpjd
Recommends:     %{name}-http
Recommends:     %{name}-icmp
Recommends:     %{name}-ide_smart
Recommends:     %{name}-ifoperstatus
Recommends:     %{name}-ifstatus
Recommends:     %{name}-ipmi-sensor1
Recommends:     %{name}-ircd
Recommends:     %{name}-ldap
Recommends:     %{name}-linux_raid
Recommends:     %{name}-load
Recommends:     %{name}-log
Recommends:     %{name}-mailq
Recommends:     %{name}-maintenance
Recommends:     %{name}-mem
Recommends:     %{name}-mrtg
Recommends:     %{name}-mrtgtraf
Recommends:     %{name}-mysql
Recommends:     %{name}-mysql_health
Recommends:     %{name}-nagios
Recommends:     %{name}-nfsmounts
Recommends:     %{name}-nis
Recommends:     %{name}-nt
Recommends:     %{name}-ntp_peer
Recommends:     %{name}-ntp_time
Recommends:     %{name}-nwstat
Recommends:     %{name}-oracle
Recommends:     %{name}-overcr
Recommends:     %{name}-pgsql
Recommends:     %{name}-ping
Recommends:     %{name}-procs
Recommends:     %{name}-qlogic_sanbox
Recommends:     %{name}-radius
Recommends:     %{name}-real
Recommends:     %{name}-rpc
Recommends:     %{name}-rsync
%endif
Provides:       nagios-plugins-all = %{version}
Obsoletes:      nagios-plugins-all <= 1.5
%if 0%{?suse_version}
%ifnarch ppc ppc64 sparc sparc64 s390 s390x
Recommends:     %{name}-sensors
%endif
Recommends:     %{name}-smtp
Recommends:     %{name}-snmp
Recommends:     %{name}-ssh
Recommends:     %{name}-swap
Recommends:     %{name}-tcp
Recommends:     %{name}-time
Recommends:     %{name}-ups
Recommends:     %{name}-ups_alarm
Recommends:     %{name}-uptime
Recommends:     %{name}-users
Recommends:     %{name}-wave
Recommends:     %{name}-zypper
Recommends:     nagios-xen-host
%endif

%description all
This virtual package recommends all currently available, official
Monitoring plugins and additional packages that are available in
https://build.opensuse.org/project/show/server:monitoring

%if 0%{?suse_version} < 01310
%package apt
Summary:        Check for software updates via apt-get
Group:          System/Monitoring
Requires:       %{apt_get_command}
Provides:       nagios-plugins-apt = %{version}
Obsoletes:      nagios-plugins-apt <= 1.5

%description apt
This plugin checks for software updates on systems that use package management
systems based on the apt-get command found in Debian GNU/Linux or Ubuntu for
example.
%endif

%package breeze
Summary:        Monitor Breezecom wireless equipment
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       net-snmp
Requires:       perl
Provides:       nagios-plugins-breeze = %{version}
Obsoletes:      nagios-plugins-breeze <= 1.5

%description breeze
This plugin reports the signal strength of a Breezecom wireless equipment.

%package by_ssh
Summary:        Execute checks via SSH
Group:          System/Monitoring
Requires:       openssh
Provides:       nagios-plugins-by_ssh = %{version}
Obsoletes:      nagios-plugins-by_ssh <= 1.5

%description by_ssh
This plugin uses SSH to execute commands on a remote host.

The most common mode of use is to refer to a local identity file with
the '-i' option. In this mode, the identity pair should have a null
passphrase and the public key should be listed in the authorized_keys
file of the remote host. Usually the key will be restricted to running
only one command on the remote server. If the remote SSH server tracks
invocation arguments, the one remote program may be an agent that can
execute additional commands as proxy.

%package cluster
Summary:        Host/Service Cluster Plugin
Group:          System/Monitoring
Provides:       nagios-plugins-cluster = %{version}
Obsoletes:      nagios-plugins-cluster <= 1.5

%description cluster
Provides the check_cluster plugin to check Services and/or Hosts running
as a cluster.

Example:
  check_cluster -s -d 2,0,2,0 -c @3:
Will alert critical if there are 3 or more service data points in a non-OK
state.

%package common
Summary:        Libraries for Nagios plugins
Group:          System/Monitoring
Provides:       nagios-plugins-common = %{version}
Obsoletes:      nagios-plugins-common <= 1.5

%description common
This package includes the libraries (scripts) that are included by many
of the standard checks.

%package dbi
Summary:        Check databases using DBI
Group:          System/Monitoring
Requires:       %{name}-dbi_backend >= %{version}
Provides:       nagios-plugins-dbi = %{version}
Obsoletes:      nagios-plugins-dbi <= 1.5

%description dbi
This program connects to an (SQL) database using DBI and checks the
specified metric against threshold levels. The default metric is
the result of the specified query.

This package provides the check_dbi plugin.

%package dbi-mysql
Summary:        Check MySQL/MariaDB database using DBI
Group:          System/Monitoring
Requires:       %{name}-dbi >= %{version}
Requires:       libdbi-drivers-dbd-mysql
Provides:       nagios-plugins-dbi-mysql = %{version}
Obsoletes:      nagios-plugins-dbi-mysql <= 1.5
Provides:       %{name}-dbi_backend = %{version}

%description dbi-mysql
This program connects to an (SQL) database using DBI and checks the
specified metric against threshold levels. The default metric is
the result of the specified query.

This virtual package requires the needed libraries for check_dbi to work
with a MySQL/MariaDB database.

%package dbi-pgsql
Summary:        Check PostgreSQL database using DBI
Group:          System/Monitoring
Requires:       %{name}-dbi >= %{version}
Requires:       libdbi-drivers-dbd-pgsql
Provides:       nagios-plugins-dbi-pgsql = %{version}
Obsoletes:      nagios-plugins-dbi-pgsql <= 1.5
Provides:       %{name}-dbi_backend = %{version}

%description dbi-pgsql
This program connects to an (SQL) database using DBI and checks the
specified metric against threshold levels. The default metric is
the result of the specified query.

This virtual package requires the needed libraries for check_dbi to work
with a PostgreSQL database

%package dbi-sqlite3
Summary:        Check SQlite3 database using DBI
Group:          System/Monitoring
Requires:       %{name}-dbi >= %{version}
Requires:       libdbi-drivers-dbd-sqlite3
Provides:       nagios-plugins-dbi-sqlite3 = %{version}
Obsoletes:      nagios-plugins-dbi-sqlite3 <= 1.5
Provides:       %{name}-dbi_backend = %{version}

%description dbi-sqlite3
This program connects to an (SQL) database using DBI and checks the
specified metric against threshold levels. The default metric is
the result of the specified query.

This virtual package requires the needed libraries for check_dbi to work
with a SQlite database.

%package dhcp
Summary:        Check DHCP servers
Group:          System/Monitoring
Provides:       nagios-plugins-dhcp = %{version}
Obsoletes:      nagios-plugins-dhcp <= 1.5
%if 0%{?suse_version}
Recommends:     apparmor-parser
Recommends:     apparmor-profiles
%else
#Requires:       apparmor-parser
#Requires:       apparmor-profiles
%endif

%description dhcp
This plugin tests the availability of DHCP servers on a network.

Please read
/usr/share/doc/packages/monitoring-plugins-dhcp/README.SUSE-check_dhcp
for details how to setup this check.

%package dig
Summary:        Test DNS service via dig
Group:          System/Monitoring
Requires:       %{_bindir}/dig
Provides:       nagios-plugins-dig = %{version}
Obsoletes:      nagios-plugins-dig <= 1.5

%description dig
This plugin test the DNS service on the specified host using dig.

%package disk
Summary:        Check disk space
Group:          System/Monitoring
Provides:       nagios-plugins-disk = %{version}
Obsoletes:      nagios-plugins-disk <= 1.5

%description disk
This plugin checks the amount of used disk space on a mounted file system and
generates an alert if free space is less than one of the threshold values.

%package disk_smb
Summary:        Check SMB Disk
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       perl
Provides:       nagios-plugins-disk_smb = %{version}
Obsoletes:      nagios-plugins-disk_smb <= 1.5

%description disk_smb
Check the amount of used disk space on a remote Samba or Windows share and
generate an alert if free space is less than one of the threshold values.

%package dns
Summary:        Obtain the IP address for a given host/domain
Group:          System/Monitoring
Requires:       %{_bindir}/nslookup
Provides:       nagios-plugins-dns = %{version}
Obsoletes:      nagios-plugins-dns <= 1.5

%description dns
This plugin uses the nslookup program to obtain the IP address for the given
host/domain query.

An optional DNS server to use may be specified. If no DNS server is specified,
the default server(s) specified in /etc/resolv.conf will be used.

%package dummy
Summary:        Dummy check
Group:          System/Monitoring
Provides:       nagios-plugins-dummy = %{version}
Obsoletes:      nagios-plugins-dummy <= 1.5

%description dummy
This plugin will simply return the state corresponding to the numeric value of
the <state> argument with optional text.

%package file_age
Summary:        Check the age/size of files
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       perl
Provides:       nagios-plugins-file_age = %{version}
Obsoletes:      nagios-plugins-file_age <= 1.5

%description file_age
This plugin will check either the age of files or their size.

%package flexlm
Summary:        Check flexlm license managers
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       perl
Provides:       nagios-plugins-flexlm = %{version}
Obsoletes:      nagios-plugins-flexlm <= 1.5

%description flexlm
Flexlm license managers usually run as a single server or three servers and a
quorum is needed.  The plugin return OK if 1 (single) or 3 (triple) servers
are running, CRITICAL if 1(single) or 3 (triple) servers are down, and WARNING
if 1 or 2 of 3 servers are running.

%package fping
Summary:        Fast ping check
Group:          System/Monitoring
Requires:       fping
Provides:       nagios-plugins-fping = %{version}
Obsoletes:      nagios-plugins-fping <= 1.5

%description fping
This plugin will use the fping command to ping the specified host for
a fast check. Note that it is necessary to set the suid flag on fping.

%if 0%{?suse_version} < 01310
%package game
Summary:        Gameserver check
Group:          System/Monitoring
Requires:       %{qstat_command}
Provides:       nagios-plugins-game = %{version}
Obsoletes:      nagios-plugins-game <= 1.5

%description game
Check connections to game servers. This plugin uses the 'qstat' command, the
popular game server status query tool.
%endif

%package hpjd
Summary:        Check status of an HP printer
Group:          System/Monitoring
Requires:       net-snmp
Provides:       nagios-plugins-hpjd = %{version}
Obsoletes:      nagios-plugins-hpjd <= 1.5

%description hpjd
This plugin tests the STATUS of an HP printer with a JetDirect card.

%package http
Summary:        Test the HTTP service on the specified host
Group:          System/Monitoring
Provides:       nagios-plugins-http = %{version}
Obsoletes:      nagios-plugins-http <= 1.5

%description http
This plugin tests the HTTP service on the specified host. It can test
normal (http) and secure (https) servers, follow redirects, search for
strings and regular expressions, check connection times, and report on
certificate expiration times.

%package icmp
Summary:        Send ICMP packets to the specified host
Group:          System/Monitoring
Provides:       nagios-plugins-icmp = %{version}
Obsoletes:      nagios-plugins-icmp <= 1.5

%description icmp
This plugin sends ICMP (ping) packets to the specified host. You can
specify different RTA factors and acceptable packet loss.

Please read
/usr/share/doc/packages/monitoring-plugins-icmp/README.SUSE-check_icmp
for details how to setup this check.

%package ide_smart
Summary:        Check local hard drive
Group:          System/Monitoring
Provides:       nagios-plugins-ide_smart = %{version}
Obsoletes:      nagios-plugins-ide_smart <= 1.5

%description ide_smart
This plugin checks a local hard drive with the (Linux specific) SMART
interface.

Please read
/usr/share/doc/packages/monitoring-plugins-ide_smart/README.SUSE-check_ide_smart
for details how to setup this check.

%package ifoperstatus
Summary:        Monitor network interfaces
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
%if 0%{?fedora_version} ||  0%{?rhel_version} || 0%{?centos_version}
Requires:       net-snmp-perl
Requires:       net-snmp-utils
%else
Requires:       perl-Net-SNMP
%endif
Provides:       nagios-plugins-ifoperstatus = %{version}
Obsoletes:      nagios-plugins-ifoperstatus <= 1.5

%description ifoperstatus
This plugin monitors operational status of a particular network interface on
the target host.

%package ifstatus
Summary:        Monitor operational status network interfaces
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
%if 0%{?fedora_version} ||  0%{?rhel_version} || 0%{?centos_version}
Requires:       net-snmp-perl
Requires:       net-snmp-utils
%else
Requires:       perl-Net-SNMP
%endif
Provides:       nagios-plugins-ifstatus = %{version}
Obsoletes:      nagios-plugins-ifstatus <= 1.5

%description ifstatus
This plugin monitors operational status of each network interface on the target
host.

%package ircd
Summary:        Check an IRCd server
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       perl
Requires:       perl(IO::Socket::INET6)
Requires:       perl(IO::Socket::SSL)
Provides:       nagios-plugins-ircd = %{version}
Obsoletes:      nagios-plugins-ircd <= 1.5

%description ircd
Monitor the status of an Internet Relay Chat daemon (IRCd) with this check.

%package ldap
Summary:        Test a LDAP server
Group:          System/Monitoring
Provides:       nagios-plugins-ldap = %{version}
Obsoletes:      nagios-plugins-ldap <= 1.5

%description ldap
Monitor access to a Lightweight Directory Access Protocol (LDAP) server.

This package includes the 'check_ldap' and 'check_ldaps' plugins.

%package load
Summary:        Test the current system load average
Group:          System/Monitoring
Provides:       nagios-plugins-load = %{version}
Obsoletes:      nagios-plugins-load <= 1.5

%description load
This plugin tests the current system load average.

%package log
Summary:        Log file pattern detector
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Provides:       nagios-plugins-log = %{version}
Obsoletes:      nagios-plugins-log <= 1.5

%description log
This plugin provides a log file pattern detector - excluding old
logfile entries and searching for the given query.

%package mailq
Summary:        Check mail queues
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       perl
Provides:       nagios-plugins-mailq = %{version}
Obsoletes:      nagios-plugins-mailq <= 1.5
%if 0%{?suse_version}
Requires:       smtp_daemon
%endif

%description mailq
This plugin checks the number of messages in the mail queue (supports multiple
sendmail queues, qmail).

%package mrtg
Summary:        Check average or maximum value in an MRTG logfile
Group:          System/Monitoring
%if 0%{?suse_version}
Recommends:     mrtg
%endif
Provides:       nagios-plugins-mrtg = %{version}
Obsoletes:      nagios-plugins-mrtg <= 1.5

%description mrtg
This plugin will check either the average or maximum value of one of the
two variables recorded in an MRTG log file.

%package mrtgtraf
Summary:        Check incoming/outgoing transfer rates of a router
Group:          System/Monitoring
%if 0%{?suse_version}
Recommends:     mrtg
%endif
Provides:       nagios-plugins-mrtgtraf = %{version}
Obsoletes:      nagios-plugins-mrtgtraf <= 1.5

%description mrtgtraf
This plugin will check the incoming/outgoing transfer rates of a router,
switch, etc recorded in an MRTG log.  If the newest log entry is older
than <expire_minutes>, a WARNING status is returned. If either the
incoming or outgoing rates exceed the <icl> or <ocl> thresholds (in
Bytes/sec), a CRITICAL status results.  If either of the rates exceed
the <iwl> or <owl> thresholds (in Bytes/sec), a WARNING status results.

%package mysql
Summary:        Test a MySQL DBMS
Group:          System/Monitoring
Provides:       nagios-plugins-mysql = %{version}
Obsoletes:      nagios-plugins-mysql <= 1.5
Provides:       monitoring-plugins-mysql_query = %{version}-%{release}

%description mysql
This plugin tests a MySQL DBMS to determine whether it is active and
accepting queries. It provides the two checks: 'check_mysql' and
'check_mysql_query'.

%package nagios
Summary:        Check nagios server
Group:          System/Monitoring
Requires:       monitoring_daemon
Provides:       nagios-plugins-nagios = %{version}
Obsoletes:      nagios-plugins-nagios <= 1.5

%description nagios
This plugin checks the status of the Nagios process on the local machine. The
plugin will check to make sure the Nagios status log is no older than the
number of minutes specified by the expires option.

It also checks the process table for a process matching the command argument.

%package nt
Summary:        Collect data from NSClient service
Group:          System/Monitoring
Provides:       nagios-plugins-nt = %{version}
Obsoletes:      nagios-plugins-nt <= 1.5

%description nt
This plugin collects data from the NSClient service running on a
Windows NT/2000/XP/2003 server.

%package ntp_peer
Summary:        Check health of an NTP server
Group:          System/Monitoring
Provides:       nagios-plugins-ntp_peer = %{version}
Obsoletes:      nagios-plugins-ntp_peer <= 1.5

%description ntp_peer
Use this plugin to check the health of an NTP server. It supports
checking the offset with the sync peer, the jitter and stratum.

This plugin will not check the clock offset between the local host and NTP
server; please use check_ntp_time for that purpose.

%package ntp_time
Summary:        Check clock offset with the ntp server
Group:          System/Monitoring
Provides:       nagios-plugins-ntp_time = %{version}
Obsoletes:      nagios-plugins-ntp_time <= 1.5
Provides:       %{name}-ntp = %{version}
%if 0%{?suse_version}
Recommends:     apparmor-parser
Recommends:     apparmor-profiles
%else
#Requires:       apparmor-parser
#Requires:       apparmor-profiles
%endif

%description ntp_time
This plugin checks the clock offset between the local host and a remote NTP
server. It is independent of any commandline programs or external libraries.

%package nwstat
Summary:        Check MRTGEXT NLM running
Group:          System/Monitoring
Provides:       nagios-plugins-nwstat = %{version}
Obsoletes:      nagios-plugins-nwstat <= 1.5

%description nwstat
This plugin attempts to contact the MRTGEXT NLM running on a Novell server to
gather the requested system information.

%package oracle
Summary:        Check Oracle status
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Provides:       nagios-plugins-oracle = %{version}
Obsoletes:      nagios-plugins-oracle <= 1.5

%description oracle
Check Oracle database health status.

%package overcr
Summary:        Check Over-CR collector daemon
Group:          System/Monitoring
Provides:       nagios-plugins-overcr = %{version}
Obsoletes:      nagios-plugins-overcr <= 1.5

%description overcr
This plugin attempts to contact the Over-CR collector daemon running on the
remote UNIX server in order to gather the requested system information.

%package pgsql
Summary:        Test a PostgreSQL DBMS
Group:          System/Monitoring
Provides:       nagios-plugins-pgsql = %{version}
Obsoletes:      nagios-plugins-pgsql <= 1.5

%description pgsql
This plugin tests a PostgreSQL DBMS to determine whether it is active and
accepting queries. It provides the check 'check_pgsql'.

%package ping
Summary:        Check connection statistics
Group:          System/Monitoring
Requires:       iputils
Provides:       nagios-plugins-ping = %{version}
Obsoletes:      nagios-plugins-ping <= 1.5

%description ping
Use ping to check connection statistics for a remote host.

This plugin uses the ping command to probe the specified host for packet loss
(percentage) and round trip average (milliseconds).

%package procs
Summary:        Check processes
Group:          System/Monitoring
Provides:       nagios-plugins-procs = %{version}
Obsoletes:      nagios-plugins-procs <= 1.5
Provides:       monitoring-plugins-procs_perf = %{version}
Obsoletes:      monitoring-plugins-procs_perf < %{version}

%description procs
This plugin checks the number of currently running processes and generates
WARNING or CRITICAL states if the process count is outside the specified
threshold ranges.

The process count can be filtered by process owner, parent process PID, current
state (e.g., 'Z'), or may be the total number of running processes.

%if 0%{?suse_version}
%package radius
Summary:        Test RADIUS server
Group:          System/Monitoring
Provides:       nagios-plugins-radius = %{version}
Obsoletes:      nagios-plugins-radius <= 1.5

%description radius
This plugin tests a RADIUS server to see if it is accepting connections.  The
server to test must be specified in the invocation, as well as a user name and
password. A configuration file may also be present. The format of the
configuration file is described in the radiusclient library sources.  The
password option presents a substantial security issue because the password can
possibly be determined by careful watching of the command line in a process
listing. This risk is exacerbated because nagios will run the plugin at regular
predictable intervals. Please be sure that the password used does not allow
access to sensitive system resources.
%endif

%package real
Summary:        Test REAL service
Group:          System/Monitoring
Provides:       nagios-plugins-real = %{version}
Obsoletes:      nagios-plugins-real <= 1.5

%description real
This plugin will attempt to open an RTSP connection with the host.  Successul
connects return STATE_OK, refusals and timeouts return STATE_CRITICAL, other
errors return STATE_UNKNOWN.  Successful connects, but incorrect reponse
messages from the host result in STATE_WARNING return values.

%package rpc
Summary:        Check RPC service
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       perl
Requires:       rpcbind
Provides:       nagios-plugins-rpc = %{version}
Obsoletes:      nagios-plugins-rpc <= 1.5

%description rpc
Check if a rpc service is registered and running using rpcinfo.

%ifnarch ppc ppc64 sparc sparc64 s390 s390x
%package sensors
Summary:        Check hardware status using lm_sensors
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       grep
Requires:       sensors
Provides:       nagios-plugins-sensors = %{version}
Obsoletes:      nagios-plugins-sensors <= 1.5

%description sensors
This plugin checks hardware status using the lm_sensors package.
%endif

%package smtp
Summary:        Check SMTP connections
Group:          System/Monitoring
Provides:       nagios-plugins-smtp = %{version}
Obsoletes:      nagios-plugins-smtp <= 1.5

%description smtp
This plugin will attempt to open an SMTP connection with the given host.

%package snmp
Summary:        SNMP monitoring
Group:          System/Monitoring
Requires:       net-snmp
Provides:       nagios-plugins-snmp = %{version}
Obsoletes:      nagios-plugins-snmp <= 1.5

%description snmp
The Simple Network Management Protocol (SNMP) can be used to monitor
network-attached devices for conditions that warrant administrative attention.

This package includes the 'check_snmp' plugin for Nagios or Icinga.

%package ssh
Summary:        Check SSH service
Group:          System/Monitoring
Provides:       nagios-plugins-ssh = %{version}
Obsoletes:      nagios-plugins-ssh <= 1.5

%description ssh
Try to connect to an SSH server at specified server and port.

%package swap
Summary:        Check swap space
Group:          System/Monitoring
Provides:       nagios-plugins-swap = %{version}
Obsoletes:      nagios-plugins-swap <= 1.5

%description swap
Check swap space on local machine.

%package tcp
Summary:        Tests TCP and UDP connections
Group:          System/Monitoring
Provides:       nagios-plugins-tcp = %{version}
Obsoletes:      nagios-plugins-tcp <= 1.5
Provides:       %{name}-clamd = %{version}
Provides:       nagios-plugins-clamd = %{version}
Obsoletes:      nagios-plugins-clamd <= 1.5
Provides:       %{name}-ftp = %{version}
Provides:       nagios-plugins-ftp = %{version}
Obsoletes:      nagios-plugins-ftp <= 1.5
Provides:       %{name}-imap = %{version}
Provides:       nagios-plugins-imap = %{version}
Obsoletes:      nagios-plugins-imap <= 1.5
Provides:       %{name}-jabber = %{version}
Provides:       nagios-plugins-jabber = %{version}
Obsoletes:      nagios-plugins-jabber <= 1.5
Provides:       %{name}-nntp = %{version}
Provides:       nagios-plugins-nntp = %{version}
Obsoletes:      nagios-plugins-nntp <= 1.5
Provides:       %{name}-nntps = %{version}
Provides:       nagios-plugins-nntps = %{version}
Obsoletes:      nagios-plugins-nntps <= 1.5
Provides:       %{name}-pop = %{version}
Provides:       nagios-plugins-pop = %{version}
Obsoletes:      nagios-plugins-pop <= 1.5
Provides:       %{name}-simap = %{version}
Provides:       nagios-plugins-simap = %{version}
Obsoletes:      nagios-plugins-simap <= 1.5
Provides:       %{name}-spop = %{version}
Provides:       nagios-plugins-spop = %{version}
Obsoletes:      nagios-plugins-spop <= 1.5
Provides:       %{name}-ssmtp = %{version}
Provides:       nagios-plugins-ssmtp = %{version}
Obsoletes:      nagios-plugins-ssmtp <= 1.5
Provides:       %{name}-udp = %{version}
Provides:       nagios-plugins-udp = %{version}
Obsoletes:      nagios-plugins-udp <= 1.5

%description tcp
This plugin tests TCP connections with the specified host (or unix socket).

This package contains the following checks:
* check_clamd
* check_ftp
* check_imap
* check_jabber
* check_nntp
* check_nntps
* check_pop
* check_simap
* check_spop
* check_ssmtp
* check_tcp
* check_udp

%package time
Summary:        Check the time on the specified host
Group:          System/Monitoring
Provides:       nagios-plugins-time = %{version}
Obsoletes:      nagios-plugins-time <= 1.5

%description time
This plugin will check the time on the specified host.

%package ups
Summary:        Test UPS service on the specified host
Group:          System/Monitoring
Provides:       nagios-plugins-ups = %{version}
Obsoletes:      nagios-plugins-ups <= 1.5

%description ups
This plugin tests the UPS service on the specified host.

Network UPS Tools from www.networkupstools.org must be running for this plugin
to work.

%package uptime
Summary:        Test the uptime of the system
Group:          System/Monitoring
Provides:       nagios-plugins-ups = %{version}
Obsoletes:      nagios-plugins-ups <= 1.5

%description uptime
This plugin tests the uptime on the system using /proc/uptime

%package users
Summary:        Check number of users currently logged in
Group:          System/Monitoring
Provides:       nagios-plugins-users = %{version}
Obsoletes:      nagios-plugins-users <= 1.5

%description users
This plugin checks the number of users currently logged in on the local system
and generates an error if the number exceeds the thresholds specified.

%package wave
Summary:        Check wave signal strength
Group:          System/Monitoring
Requires:       %{name}-common = %{version}
Requires:       net-snmp
Requires:       perl
Provides:       nagios-plugins-wave = %{version}
Obsoletes:      nagios-plugins-wave <= 1.5

%description wave
Check the wave signal strength via SNMP.

%package cups
Summary:        Check cups service
Group:          System/Monitoring
Requires:       cups-client
Provides:       nagios-plugins-cups = %{version}
Obsoletes:      nagios-plugins-cups <= 1.5

%description cups
Check the status of a remote CUPS server, all printers there
or one selected. It can also check queue there:
it will provide the size of the queue of age of queue.

%prep
%setup -q
%if 0%{?suse_version}
mkdir -p example/permissions.d
cp %{S:11} example/permissions.d/%{name}
%endif
cp %{S:12} ./README.SUSE
cp %{S:13} ./README.SUSE-check_dhcp
cp %{S:14} ./README.SUSE-check_icmp
cp %{S:15} ./README.SUSE-check_ide_smart
cp %{S:20} ./README.SUSE-check_cups
rm plugins-scripts/check_ircd.pl
install -m0644 %{S:26} plugins-scripts/check_ircd.pl
cp %{S:28} ./README.SUSE-check_ping
cp %{S:29} ./README.SUSE-check_ntp_time

for extension in mysql pgsql sqlite3 ; do
cat >> README.SUSE-dbi-$extension << EOF
This program connects to an (SQL) database using DBI and checks the
specified metric against threshold levels. The default metric is
the result of the specified query.

This virtual package requires the needed libraries for check_dbi to work
with the libdbi driver for $extension.
EOF
done

%patch1 -p1
%patch6 -p1
%patch11 -p1
%patch15 -p1
# Debian patches
%patch118 -p1
%patch119 -p1
%patch121 -p1
find -type f -exec chmod 644 {} +

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -DLDAP_DEPRECATED"
gettextize -f
autoreconf -fi
chmod a+x NP-VERSION-GEN
chmod +x configure # needed as configure script is not executable in 1.5..
%configure \
	--enable-static=no \
	--enable-extra-opts \
	--libexecdir=%{nagios_plugindir} \
	--sysconfdir=%{nagios_sysconfdir} \
	--with-apt-get-command=%{apt_get_command} \
	--with-cgiurl=/nagios/cgi-bin \
	--with-fping-command=%{_sbindir}/fping \
    --with-fping6-command=%{_sbindir}/fping6 \
	--with-ipv6 \
	--with-ntpq-command=%{_sbindir}/ntpq \
	--with-ntpdc-command=%{_sbindir}/ntpdc \
	--with-ntpdate-command=%{_sbindir}/ntpdate \
	--with-openssl=%{_prefix} \
	--with-perl=%{_bindir}/perl \
	--with-pgsql=%{_prefix} \
	--with-ping6-command='/bin/ping6 -n -U -w %d -c %d %s' \
	--with-proc-loadavg=/proc/loadavg \
	--with-ps-command="/bin/ps axwo 'stat uid pid ppid vsz rss pcpu etime comm args'" \
	--with-ps-format='%s %d %d %d %d %d %f %s %s %n' \
	--with-ps-cols=10 \
	--with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos' \
%if 0%{?suse_version} > 1300
	--with-rpcinfo-command=/sbin/rpcinfo \
%else
	--with-rpcinfo-command=%{_sbindir}/rpcinfo \
%endif
	--with-qstat-command=%{qstat_command} \
	--with-mysql=%{_prefix} \
	--disable-rpath
make all %{?_smp_mflags}

%install
sed -i 's,^MKINSTALLDIRS.*,MKINSTALLDIRS = ../mkinstalldirs,' po/Makefile
%make_install install-root
install -m 0755 %{S:18} %{buildroot}%{nagios_plugindir}/check_cups
# provide check_host and check_rta_multi as on Debian
if [ -x %{buildroot}%{nagios_plugindir}/check_icmp ] ; then
	test -f %{buildroot}%{nagios_plugindir}/check_host && rm -f %{buildroot}%{nagios_plugindir}/check_host
	test -f %{buildroot}%{nagios_plugindir}/check_rta_multi && rm -f %{buildroot}%{nagios_plugindir}/check_rta_multi
	ln -s %{nagios_plugindir}/check_icmp %{buildroot}%{nagios_plugindir}/check_host ;
	ln -s %{nagios_plugindir}/check_icmp %{buildroot}%{nagios_plugindir}/check_rta_multi ;
fi
# Factory maintainers do not want packages requiring software not in Factory: remove the checks
%if 0%{?suse_version} >= 01310
rm %{buildroot}%{nagios_plugindir}/check_apt
rm %{buildroot}%{nagios_plugindir}/check_game
%endif

# fix "use lib" on installed perl checks
pushd %{buildroot}%{nagios_plugindir}
for file in $(find -maxdepth 1 -type f); do
    sed -i 's|use lib "nagios/plugins".*;|use lib "%{nagios_plugindir}";|g;
            s|use lib "/usr/local/nagios/libexec".*;|use lib "%{nagios_plugindir}";|g' $file
done
popd
# check_sensors makes no sense on some archs
%ifarch ppc ppc64 sparc sparc64 s390 s390x
rm -f %{buildroot}/%{nagios_plugindir}/check_sensors
%endif
# provie procs_perf symlink for compatibility
ln -s %{nagios_plugindir}/check_procs %{buildroot}%{nagios_plugindir}/check_procs_perf
# install Apparmor profiles
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE16} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE17} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE19} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE22} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE23} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE24} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE25} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE30} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE31} %{buildroot}%{_sysconfdir}/apparmor.d/
%if 0%{?suse_version} >= 1500
install -m 644 %{SOURCE35} %{buildroot}%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_procs
%else
install -m 644 %{SOURCE32} %{buildroot}%{_sysconfdir}/apparmor.d/
%endif
install -m 644 %{SOURCE33} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 644 %{SOURCE34} %{buildroot}%{_sysconfdir}/apparmor.d/

# install nrpe snipplets
mkdir -p %{buildroot}%{nrpe_sysconfdir}
install -m 644 %{SOURCE50} %{buildroot}%{nrpe_sysconfdir}/check_mailq.cfg
install -m 644 %{SOURCE51} %{buildroot}%{nrpe_sysconfdir}/check_load.cfg
install -m 644 %{SOURCE52} %{buildroot}%{nrpe_sysconfdir}/check_ntp_time.cfg
install -m 644 %{SOURCE53} %{buildroot}%{nrpe_sysconfdir}/check_swap.cfg
install -m 644 %{SOURCE54} %{buildroot}%{nrpe_sysconfdir}/check_partition_root.cfg
install -m 644 %{SOURCE55} %{buildroot}%{nrpe_sysconfdir}/check_proc_cron.cfg
install -m 644 %{SOURCE56} %{buildroot}%{nrpe_sysconfdir}/check_total_procs.cfg
install -m 644 %{SOURCE57} %{buildroot}%{nrpe_sysconfdir}/check_users.cfg
install -m 644 %{SOURCE58} %{buildroot}%{nrpe_sysconfdir}/check_zombie_procs.cfg
install -m 644 %{SOURCE59} %{buildroot}%{nrpe_sysconfdir}/check_mysql.cfg
install -m 644 %{SOURCE60} %{buildroot}%{nrpe_sysconfdir}/check_ups.cfg

# inform the users about the deprecated monitoring-plugins-extras package
cat >> README.SUSE-deprecated << EOF
The monitoring-plugins-extras package is deprecated.

The checks formerly packaged here are now packaged separately.

For example, to install check_fping just install monitoring-plugins-fping.
EOF
cat >> README.SUSE-all << EOF
This virtual package recommends all currently available, official
Nagios plugins.

It does not require the subpackages as you might not have all needed
dependend packages available.
EOF
# install ghost file for extra-opts
install -Dm 644  %{SOURCE27} %{buildroot}%{_sysconfdir}/%{name}/README
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.ini

# find locale files
%find_lang %{name}

%if 0%{?suse_version}
%post dhcp
# in case somebody uses the permissions file we provide
# in docdir, run permission here
if [ -f %{_sysconfdir}/permissions.d/monitoring-plugins ]; then
%if 0%{?suse_version} < 1210
%run_permissions
%else
	%set_permissions monitoring-plugins
%endif
fi

%post icmp
if [ -f %{_sysconfdir}/permissions.d/monitoring-plugins ]; then
# in case somebody uses the permissions file we provide
# in docdir, run permission here
%if 0%{?suse_version} < 1210
%run_permissions
%else
%set_permissions monitoring-plugins
%endif
fi

%post ide_smart
if [ -f %{_sysconfdir}/permissions.d/monitoring-plugins ]; then
# in case somebody uses the permissions file we provide
# in docdir, run permission here
%if 0%{?suse_version} < 1210
%run_permissions
%else
%set_permissions monitoring-plugins
%endif
fi
%endif

%files
%defattr(-,root,root)
%doc ABOUT-NLS ACKNOWLEDGEMENTS AUTHORS ChangeLog CODING FAQ 
%doc NEWS README REQUIREMENTS SUPPORT README.SUSE
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%if 0%{?suse_version}
%doc example
%endif

%files all
%defattr(-,root,root)
%doc README.SUSE-all

%if 0%{?suse_version} < 01310
%files apt
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_apt
%endif

%files breeze
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_breeze

%files by_ssh
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_by_ssh

%files cluster
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_cluster

%files common -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS ACKNOWLEDGEMENTS AUTHORS ChangeLog CODING FAQ 
%doc NEWS README REQUIREMENTS SUPPORT README.SUSE
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%if 0%{?suse_version}
%doc example
%endif
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/README
%ghost %config(noreplace) %{_sysconfdir}/%{name}/%{name}.ini
%defattr(0755,root,root)
%{nagios_plugindir}/negate
%{nagios_plugindir}/urlize
%{nagios_plugindir}/utils.sh
%attr(0644,root,root) %{nagios_plugindir}/utils.pm

%files dbi
%defattr(-,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_dbi

%files dbi-mysql
%defattr(-,root,root)
%doc README.SUSE-dbi-mysql

%files dbi-pgsql
%defattr(-,root,root)
%doc README.SUSE-dbi-pgsql

%files dbi-sqlite3
%defattr(-,root,root)
%doc README.SUSE-dbi-sqlite3

%files dhcp
%defattr(-,root,root)
%doc README.SUSE-check_dhcp
%dir %{nagios_plugindir}
%dir %{_sysconfdir}/apparmor.d
%attr(0755,root,root) %{nagios_plugindir}/check_dhcp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_dhcp

%files dig
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_dig

%files disk
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_disk
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_disk
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_partition_root.cfg

%files disk_smb
%defattr(0755,root,root)
%{nagios_plugindir}/check_disk_smb

%files dns
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_dns

%files dummy
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_dummy

%files extras
%defattr(0644,root,root,0755)
%doc README.SUSE-deprecated

%files file_age
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_file_age

%files flexlm
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_flexlm

%files fping
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_fping

%if 0%{?suse_version} < 01310
%files game
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_game
%endif

%files hpjd
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_hpjd

%files http
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_http

%files icmp
%defattr(-,root,root)
%doc README.SUSE-check_icmp
%dir %{nagios_plugindir}
%attr(0755,root,root) %{nagios_plugindir}/check_icmp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_icmp
%{nagios_plugindir}/check_host
%{nagios_plugindir}/check_rta_multi

%files ifoperstatus
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ifoperstatus

%files ifstatus
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ifstatus

%files ide_smart
%defattr(-,root,root)
%doc README.SUSE-check_ide_smart
%dir %{nagios_plugindir}
%attr(0755,root,root) %{nagios_plugindir}/check_ide_smart
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_ide_smart

%files ircd
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ircd

%files ldap
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ldap
%{nagios_plugindir}/check_ldaps

%files load
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_load
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_load.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_load

%files log
%defattr(0755,root,root)
%{nagios_plugindir}/check_log

%files mailq
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_mailq
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_mailq.cfg

%files mrtg
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_mrtg

%files mrtgtraf
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_mrtgtraf

%files mysql
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_mysql
%{nagios_plugindir}/check_mysql_query
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_mysql.cfg

%files nagios
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_nagios

%files nt
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_nt

%files ntp_peer
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ntp_peer

%files ntp_time
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_ntp
%{nagios_plugindir}/check_ntp_time
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_ntp_time
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_ntp_time.cfg

%files nwstat
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_nwstat

%files oracle
%defattr(0755,root,root)
%{nagios_plugindir}/check_oracle

%files overcr
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_overcr

%files pgsql
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_pgsql

%files ping
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ping
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_ping

%files procs
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_procs
%{nagios_plugindir}/check_procs_perf
%defattr(0644,root,root)
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_procs
%config(noreplace) %{nrpe_sysconfdir}/check_proc_cron.cfg
%config(noreplace) %{nrpe_sysconfdir}/check_total_procs.cfg
%config(noreplace) %{nrpe_sysconfdir}/check_zombie_procs.cfg

%if 0%{?suse_version}
%files radius
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_radius
%endif

%files real
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_real

%files rpc
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_rpc

%ifnarch ppc ppc64 sparc sparc64 s390 s390x
%files sensors
%defattr(0755,root,root)
%{nagios_plugindir}/check_sensors
%endif

%files smtp
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_smtp

%files snmp
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_snmp

%files ssh
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_ssh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_ssh

%files swap
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_swap
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_swap
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_swap.cfg

%files tcp
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_clamd
%{nagios_plugindir}/check_ftp
%{nagios_plugindir}/check_imap
%{nagios_plugindir}/check_jabber
%{nagios_plugindir}/check_nntp
%{nagios_plugindir}/check_nntps
%{nagios_plugindir}/check_pop
%{nagios_plugindir}/check_simap
%{nagios_plugindir}/check_spop
%{nagios_plugindir}/check_ssmtp
%{nagios_plugindir}/check_tcp
%{nagios_plugindir}/check_udp

%files time
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_time

%files ups
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_ups
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_ups.cfg

%files uptime
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_uptime

%files users
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%dir %{nrpe_sysconfdir}
%{nagios_plugindir}/check_users
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_users
%attr(0644,root,root) %config(noreplace) %{nrpe_sysconfdir}/check_users.cfg

%files wave
%defattr(0755,root,root)
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_wave

%files cups
%defattr(-,root,root)
%doc README.SUSE-check_cups
%dir %{nagios_plugindir}
%dir %{_sysconfdir}/apparmor.d
%attr(0755,root,root)%{nagios_plugindir}/check_cups
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_cups

%changelog
