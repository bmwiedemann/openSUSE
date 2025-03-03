#
# spec file for package collectd
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2005-2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define plugins apache apcups aggregation ascent battery bind  \\\
  capabilities ceph cgroups chrony curl curl_json curl_xml conntrack contextswitch cpu cpufreq cpusleep csv \\\
  df disk dns drbd \\\
  email entropy ethstat exec fhcount filecount fscache hddtemp hugepages \\\
  infiniband %{expand:%{rdt_plugin}} interface ipc iptables ipvs irq \\\
  load logfile log_logstash \\\
  madwifi match_empty_counter match_hashed match_regex match_timediff match_value \\\
  mdevents mbmon md memcached memory mmc multimeter \\\
  netlink network nfs nginx notify_nagios ntpd numa olsrd openvpn \\\
  perl ping protocols powerdns processes \\\
  rrdcached rrdtool %{expand:%{sensors_plugin}} serial statsd swap syslog \\\
  table tail tail_csv target_notification target_replace target_scale target_set target_v5upgrade \\\
  tcpconns teamspeak2 ted thermal threshold \\\
  unixsock uptime users uuid vmem vserver \\\
  wireless write_graphite write_http write_log write_sensu write_tsdb \\\
  write_prometheus zfs_arc zookeeper
%ifnarch s390 s390x
%bcond_without sensors
%define sensors_plugin sensors
%else
%bcond_with sensors
%define sensors_plugin %{nil}
%endif
# dpdk exclusive build arch requirements copied:
%ifarch aarch64 x86_64 ppc64le
%bcond_without dpdk
%else
%bcond_with dpdk
%endif
%ifarch x86_64 %{ix86}
%bcond_without intel_rdt
%define rdt_plugin intel_rdt
%else
%bcond_with intel_rdt
%define rdt_plugin %{nil}
%endif
%if 0%{?suse_version} >= 1330 && 0%{?suse_version} <= 1500
%bcond_without nut
%else
%bcond_with nut
%endif
%bcond_with epics
Name:           collectd
Version:        5.12.0.348.g93f9bdcb
Release:        0
Summary:        Statistics Collection Daemon for filling RRD Files
License:        GPL-2.0-only AND MIT
Group:          System/Monitoring
URL:            http://collectd.org/
# Source:         http://collectd.org/files/collectd-%%{version}.tar.bz2
Source:         collectd-%{version}.tar.bz2
Source1:        collectd.suse.init
Source2:        collectd.apache2.conf
Source3:        collectd-js.apache2.conf
Source99:       collectd-rpmlintrc
Patch1:         collectd-fix-config.patch
Patch2:         collectd-version.patch
Patch3:         collectd-perl-vendor.patch
# see http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=467072
Patch4:         collectd-fix_broken_perl-5.10.patch
Patch5:         collectd-fix_collection_cgi.patch
Patch6:         collectd-fix_spamassassin_doc.patch
Patch7:         collectd-fix_collectd_config_path_in_snmp_probe.patch
Patch8:         9e36cd85a2bb_sigrok_Update_to_support_libsigrok_0_4.patch
# PATCH-FIX-OPENSUSE avoid-pg-config.patch avoid pg_config if possible
Patch11:        avoid-pg-config.patch
Patch12:        harden_collectd.service.patch
# for /etc/apache2/... ownership (rpmlint):
BuildRequires:  apache2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  java-devel
BuildRequires:  libesmtp-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjansson-devel
BuildRequires:  libnetlink-devel
BuildRequires:  libpcap-devel
BuildRequires:  libpng-devel
BuildRequires:  libprotobuf-c-devel
BuildRequires:  libtool
BuildRequires:  libyajl-devel
BuildRequires:  linux-kernel-headers
BuildRequires:  make
BuildRequires:  mysql-devel >= 4.1.0
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  rrdtool
BuildRequires:  systemd-rpm-macros
BuildRequires:  xfsprogs-devel
BuildRequires:  pkgconfig(OpenIPMI)
BuildRequires:  pkgconfig(OpenIPMIpthread)
BuildRequires:  pkgconfig(dbi)
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libiptc)
BuildRequires:  pkgconfig(libmemcached)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(liboping)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(librrd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xtables)
BuildRequires:  pkgconfig(zlib)
Requires:       rrdtool
Requires(post): %fillup_prereq
# play nice with collectd-beta:
Obsoletes:      collectd-beta < %{version}
Provides:       collectd-beta = %{version}-%{release}
%{?systemd_requires}
%if %{with dpdk}
BuildRequires:  dpdk-devel >= 19.08
%endif
# intel_rdt -> pqos.h
# intel-cmt-cat exclusive build arch requirements copied:
%if %{with intel_rdt}
BuildRequires:  libpqos-devel
%endif
%if 0%{?sle_version} < 150000 || 0%{?is_opensuse}
BuildRequires:  pkgconfig(Qgpsmm)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(libsigrok)
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(libmodbus)
BuildRequires:  strip-nondeterminism
%endif
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libmosquitto)
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
BuildRequires:  pkgconfig(librabbitmq)
%endif
%if %{with nut}
BuildRequires:  pkgconfig(libnutclient)
%endif
%if %{with sensors}
BuildRequires:  sensors
Requires:       sensors
%endif
%if %{with epics}
BuildRequires:  epics-devel
%endif

%description
collectd is a daemon (written in C) that reads various system
statistics and updates RRD files. Statistics are very fine grained
with an update interval of 10 seconds.

%package web
Summary:        Web Frontend for watching the %{name} Statistics
Group:          System/Monitoring
Requires:       apache2
Requires:       perl
Requires:       rrdtool
Requires:       perl(CGI)
Requires:       perl(Data::Dumper)
Requires:       perl(HTML::Entities)
Requires:       perl(RRDs)
Requires:       perl(URI::Escape)
BuildArch:      noarch

%description web
Web frontend CGI for watching %{name} statistics from a browser.

Please look at %{_sysconfdir}/apache2/conf.d/%{name}.conf on how to enable.

%package web-js
Summary:        Web/JavaScript Frontend for watching %{name} Statistics
Group:          System/Monitoring
Requires:       apache2
Requires:       perl
Requires:       rrdtool
Requires:       perl(CGI)
Requires:       perl(Config::General)
Requires:       perl(Data::Dumper)
Requires:       perl(HTML::Entities)
Requires:       perl(JSON)
Requires:       perl(RRDs)
BuildArch:      noarch

%description web-js
Web/JavaScript frontend CGI for watching %{name} statistics from
a browser.

Please look at %{_sysconfdir}/apache2/conf.d/%{name}-js.conf on how to
enable.

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
%package plugin-amqp
Summary:        AMQP Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-amqp
The AMQP plugin transmits or receives values collected by collectd via the
Advanced Message Queuing Protocol (AMQP).
%endif

%if %{with epics}
%package plugin-epics
Summary:        EPICS CA Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Recommends:     epics-caRepeater

%description plugin-epics
EPICS CA for %{name} allow you to receive variables updates from the bus.
%endif

%package plugin-notify-desktop
Summary:        Desktop Notification Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-notify-desktop
Desktop Notification Support for %{name} allow you to receive
message delivery on your desktop.

%package plugin-ipmi
Summary:        OpenIPMI Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-ipmi
Optional %{name} plugin to monitor sensors using the OpenIPMI
library for IPMI enabled systems.

%package plugin-snmp
Summary:        SNMP Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Config::General)
Requires:       perl(SNMP)
Requires:       perl(Socket6)

%description plugin-snmp
Optional %{name} plugin to monitor devices using SNMP.

%package plugin-mysql
Summary:        MySQL Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-mysql
Optional %{name} plugin to monitor MySQL server instances.

%package plugin-openldap
Summary:        OpenLDAP plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-openldap
This plugin for collectd reads monitoring information
from OpenLDAP's cn=Monitor subtree.

%if %{with nut}
%package plugin-nut
Summary:        Network UPS Tools plugin for collectd
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-nut
This plugin for collectd provides Network UPS Tools support.
%endif

%package plugin-pcie
Summary:        PCIe Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-pcie
Optional %{name} plugin to monitor PCIe errors.

%package plugin-postgresql
Summary:        PostgreSQL Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-postgresql
Optional %{name} plugin to monitor PostgreSQL server instances.

%package plugin-python3
Summary:        Python3 API for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-python3
Optional %{name} Python3 API in order to write %{name} plugins in
Python3.

%package plugin-java
Summary:        Java API for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-java
Optional %{name} Java API in order to write %{name} plugins in
Java.

%package plugin-virt
Summary:        Virtual Machine Statistics Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-virt
Optional %{name} plugin to gather statistics from virtual
machines using libvirt.

%package plugin-dbi
Summary:        DBI Storage Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-dbi
Optional %{name} plugin to store sampling results into
various databases as supported by libdbi.

%package plugin-memcachec
Summary:        Memcache Daemon Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-memcachec
Optional %{name} plugin to sample memcached statistics.

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%package plugin-modbus
Summary:        TCP Modbus Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-modbus
Optional %{name} plugin to communicate with TCP Modbus devices.
%endif

%if 0%{?is_opensuse}
%package plugin-mqtt
Summary:        MQTT Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-mqtt
Optional %{name} plugin to send and receive MQTT messages.
%endif

%package plugin-pinba
Summary:        Pinba Collector Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-pinba
Optional %{name} plugin to receive and dispatch timing values from Pinba, a
profiling extension for PHP.

%if 0%{?sle_version} < 150000 || 0%{?is_opensuse}
%package plugin-sigrok
Summary:        Sigrok Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-sigrok
Optional %{name} plugin to collect measurements from
various devices supported by libsigrok.
%endif

%package plugin-smart
Summary:        SMART Monitoring Plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-smart
Optional %{name} plugin to monitor Self-Monitoring, Analysis and Reporting
Technology (SMART) information from disk drives.

%package plugin-lua
Summary:        Lua API for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Requires:       lua

%description plugin-lua
Optional %{name} Lua API in order to write %{name} plugins in Lua.

%if 0%{?sle_version} < 150000 || 0%{?is_opensuse}
%package plugin-gps
Summary:        GPSD monitoring plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-gps
Optional %{name} plugin to monitor gpsd.
%endif

%package plugin-mcelog
Summary:        Machine Check Exceptions plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-mcelog
Optional %{name} plugin to monitor machine check exceptions.

%package plugin-ovs
Summary:        Open vSwitch (OVS) plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-ovs
Optional %{name} plugin to monitor an OVS database.

%package plugin-synproxy
Summary:        Synproxy stats plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-synproxy
Optional %{name} plugin to monitor Synproxy stats.

%package plugin-write_stackdriver
Summary:        Write Stackdriver plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-write_stackdriver
Optional %{name} plugin to to write to Google Stackdriver.

%package plugin-write_syslog
Summary:        Write Syslog plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-write_syslog
Optional %{name} plugin to write values lists as syslog messages.

%package plugin-uptime
Summary:        Uptime plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-uptime
Optional %{name} plugin to collect system uptime statistics.

%package plugin-connectivity
Summary:        Connectivity plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-connectivity
Optional %{name} plugin to collect Event-based interface status.

%package plugin-procevent
Summary:        Procevent plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-procevent
Optional %{name} plugin to listen for process starts and exits via netlink.

%package plugin-sysevent
Summary:        Sysevent plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-sysevent
Optional %{name} plugin to listen to rsyslog events and submit matched values.
.

%package plugin-buddyinfo
Summary:        Buddyinfo plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-buddyinfo
Optional %{name} plugin for memory fragmentation.

%package plugin-logparser
Summary:        Logparser plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-logparser
Optional %{name} plugin for filtering and parsing logs.

%package plugin-ubi
Summary:        UBIFS plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-ubi
Optional %{name} plugin for reporting block state of flash memory devices with UBIFS filesystem.

%package plugin-write_influxdb_udp
Summary:        InfluxDB UDP protocol plugin for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-write_influxdb_udp
Optional %{name} plugin to send values to InfluxDB using line protocol via udp.
For HTTP line protocol use write_http plugin.

%package plugins-all
Summary:        All Monitoring Plugins for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-plugin-buddyinfo = %{version}-%{release}
Requires:       %{name}-plugin-connectivity = %{version}-%{release}
Requires:       %{name}-plugin-dbi = %{version}-%{release}
Requires:       %{name}-plugin-ipmi = %{version}-%{release}
Requires:       %{name}-plugin-java = %{version}-%{release}
Requires:       %{name}-plugin-logparser = %{version}-%{release}
Requires:       %{name}-plugin-lua = %{version}-%{release}
Requires:       %{name}-plugin-mcelog = %{version}-%{release}
Requires:       %{name}-plugin-memcachec = %{version}-%{release}
Requires:       %{name}-plugin-mysql = %{version}-%{release}
Requires:       %{name}-plugin-notify-desktop = %{version}-%{release}
Requires:       %{name}-plugin-openldap = %{version}-%{release}
Requires:       %{name}-plugin-ovs = %{version}-%{release}
Requires:       %{name}-plugin-pcie = %{version}-%{release}
Requires:       %{name}-plugin-pinba = %{version}-%{release}
Requires:       %{name}-plugin-postgresql = %{version}-%{release}
Requires:       %{name}-plugin-procevent = %{version}-%{release}
Requires:       %{name}-plugin-python3 = %{version}-%{release}
Requires:       %{name}-plugin-smart = %{version}-%{release}
Requires:       %{name}-plugin-snmp = %{version}-%{release}
Requires:       %{name}-plugin-synproxy = %{version}-%{release}
Requires:       %{name}-plugin-sysevent = %{version}-%{release}
Requires:       %{name}-plugin-ubi = %{version}-%{release}
Requires:       %{name}-plugin-uptime = %{version}-%{release}
Requires:       %{name}-plugin-virt = %{version}-%{release}
Requires:       %{name}-plugin-write_influxdb_udp = %{version}-%{release}
Requires:       %{name}-plugin-write_stackdriver = %{version}-%{release}
Requires:       %{name}-plugin-write_syslog = %{version}-%{release}
Requires:       %{name}-web = %{version}-%{release}
Requires:       %{name}-web-js = %{version}-%{release}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
Requires:       %{name}-plugin-amqp = %{version}-%{release}
%endif
%if 0%{?sle_version} < 150000  || 0%{?is_opensuse}
Requires:       %{name}-plugin-gps = %{version}-%{release}
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
Requires:       %{name}-plugin-modbus = %{version}-%{release}
%endif
%if 0%{?is_opensuse}
Requires:       %{name}-plugin-mqtt = %{version}-%{release}
%endif
%if 0%{?sle_version} < 150000 || 0%{?is_opensuse}
Requires:       %{name}-plugin-sigrok = %{version}-%{release}
%endif
%if %{with nut}
Requires:       %{name}-plugin-nut = %{version}-%{release}
%endif
BuildArch:      noarch

%description plugins-all
Metapackage that installs %{name} and all the available
monitoring plugin subpackages.

%package spamassassin
Summary:        Spamassassin Monitoring for %{name}
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Requires:       perl-spamassassin
BuildArch:      noarch

%description spamassassin
Plugin for filling %{name} with statistics from the
SpamAsssassin anti-spam engine.

%package plugin-dpdk
Summary:        Collect DPDK interface statistics
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}

%description plugin-dpdk
This plugin has a specific use case: monitoring DPDK applications
that don't expose stats in any other way than the DPDK xstats API.
For OVS or OVS-with-DPDK the Open vSwitch plugins (ovs) should be
used for collecting stats and events.

%package -n libcollectdclient1
Summary:        Library for %{name} clients
Group:          System/Monitoring
Provides:       libcollectdclient = %{version}-%{release}

%description -n libcollectdclient1
Library which abstracts communication with the %{name}
unixsock plugin for clients.

%package -n libcollectdclient-devel
Summary:        Development Environment for %{name} clients
Group:          Development/Libraries/C and C++
Requires:       libcollectdclient1 = %{version}-%{release}

%description -n libcollectdclient-devel
Library which abstracts communication with the %{name}
unixsock plugin for clients.
This package contains the required development environment
to write %{name} unixsock clients.

%prep
%autosetup -p1

sed -i 's|@@VERSION@@|%{version}|g' configure.ac

perl -p -i -e 's|(-L\$withval/lib)\b|${1}64|g' configure.ac configure

# unneeded files:
rm -fr \
     contrib/solaris-smf \
     contrib/redhat \
     contrib/sles*

%build
autoreconf -fiv

export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
export KERNEL_DIR=%{_prefix}/src/linux
%configure \
    --disable-werror \
    --disable-silent-rules \
    --disable-static \
    --with-java="$JAVA_HOME/" \
    --disable-turbostat

make %{?_smp_mflags}

%install
%make_install

# delete .la files
rm -f "%{buildroot}%{_libdir}"/*.{a,la}
rm -f "%{buildroot}%{_libdir}/collectd"/*.a

sed -i '/^dependency_libs=/ s|-L'"${RPM_BUILD_DIR}/%{name}-%{version}"'/src||g' "%{buildroot}%{_libdir}/collectd/python.la"

# delete if it exists (not packaged any more on openSUSE):
rm -rf "%{buildroot}%{_localstatedir}/adm/perl-modules/%{name}"

mkdir -p _rpmdoc_/java
mv contrib/GenericJMX.conf _rpmdoc_/java/

# fix permissions:
chmod 0755 "%{buildroot}%{_libdir}/collectd"/*.so
chmod 0644 "%{buildroot}%{_libdir}/collectd"/*.la

# create /var/lib/collectd to add it to the %files section:
install -d -m 0755 "%{buildroot}%{_localstatedir}/lib/collectd"

# Apache2 configuration for the CGI frontend:
install -D -m 0644 "%{SOURCE2}" "%{buildroot}%{_sysconfdir}/apache2/conf.d/%{name}.conf"
install -D -m 0755 contrib/collection.cgi "%{buildroot}/srv/www/collectd/collection.cgi"
install -D -m 0644 contrib/collection.conf "%{buildroot}%{_sysconfdir}/collectd/collection.conf"
sed -i 's|@@LIBDIR@@|%{_libdir}|g' "%{buildroot}%{_sysconfdir}/collectd/collection.conf"
# remove it from contrib, to avoid having it end up in the main package as well:
rm contrib/collection.cgi contrib/collection.conf

%perl_process_packlist
rm -rf "%{buildroot}%{_localstatedir}/adm/perl-modules"/*

# web-js CGI frontend (_must_ be installed _after_ perl_process_packlist)
install -d "%{buildroot}/srv/www/collectd-js"
mkdir -p _rpmdoc_/web-js
mv contrib/collection3/README _rpmdoc_/web-js/README
find contrib/collection3/ -name .htaccess -exec rm {} \;
cp -a \
     contrib/collection3/bin/* \
     contrib/collection3/share/* \
     "%{buildroot}/srv/www/collectd-js/"
mkdir -p "%{buildroot}%{_libexecdir}/collectd-js"
mv contrib/collection3/lib/* "%{buildroot}%{_libexecdir}/collectd-js/"

install -D -m 0644 contrib/collection3%{_sysconfdir}/collection.conf \
     "%{buildroot}%{_sysconfdir}/collectd/collection-js.conf"
rm -fr contrib/collection3%{_sysconfdir}
install -D -m 0644 "%{SOURCE3}" "%{buildroot}%{_sysconfdir}/apache2/conf.d/%{name}-js.conf"

# spamassassin (_must_ be installed _after_ perl_process_packlist)
install -D -m0644 contrib/SpamAssassin/example.cf \
     "%{buildroot}%{_datadir}/spamassassin/99_%{name}.cf"
install -D -m0644 contrib/SpamAssassin/Collectd.pm \
     "%{buildroot}%{perl_vendorlib}/Mail/SpamAssassin/Plugin/Collectd.pm"
pod2man \
     contrib/SpamAssassin/Collectd.pm \
     > "%{buildroot}%{perl_man3dir}/Mail::SpamAssassin::Plugin::Collectd.%{perl_man3ext}"
rm -rf contrib/SpamAssassin

# cussh script from contrib:
install -m0755 contrib/cussh.pl "%{buildroot}%{_bindir}/cussh"
install -d "%{buildroot}%{_mandir}/man1"
pod2man \
     -c "Collectd UNIX Socket Shell" \
     -n "CUSSH" \
     -s 1 \
     contrib/cussh.pl > "%{buildroot}%{_mandir}/man1/cussh.1"
rm contrib/cussh.pl

# snmp:
mkdir -p _rpmdoc_/snmp
sed -n '/^snmp-data\.conf/,$ p' contrib/README > _rpmdoc_/snmp/README
sed -i '/^snmp-data\.conf/,$ d' contrib/README
mv contrib/snmp-data.conf _rpmdoc_/snmp/
sed -i 's|\(\./\)snmp-probe-host\.px|collectd-snmp-probe-host|g' contrib/snmp-probe-host.px
pod2man \
     -c "Collectd SNMP Host Probe" \
     -n "COLLECTD-SNMP-PROBE-HOST" \
     -s 1 \
     contrib/snmp-probe-host.px \
     > "%{buildroot}%{_mandir}/man1/collectd-snmp-probe-host.1"
install -D -m0755 contrib/snmp-probe-host.px "%{buildroot}%{_bindir}/collectd-snmp-probe-host"
rm contrib/snmp-probe-host.px
install -d "%{buildroot}%{_mandir}/man1"

find contrib/ -name '*.orig' -delete
find contrib/ -name .gitignore -delete
sed -i 's/env //1' contrib/exec-borg

# plugin list:
echo -n > plugins.lst
for plugin in %{plugins}; do
     for ext in so la; do
     	 echo "%{_libdir}/collectd/${plugin}.${ext}" >> plugins.lst
     done
done

cat <<EOF >README.plugins-all
This package is empty but depends on all collectd plugin subpackages.
EOF

install -d -m 0755 "%{buildroot}%{_sbindir}"
install -D -m0644 contrib/systemd.collectd.service %{buildroot}%{_unitdir}/collectd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%if 0%?have_strip_nondeterminism > 0
    strip-all-nondeterminism %{buildroot}%{_datadir}/collectd/java/
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%pre
%service_add_pre %{name}.service

%post
%{fillup_only collectd}
%service_add_post %{name}.service

%post   -n libcollectdclient1 -p /sbin/ldconfig
%postun -n libcollectdclient1 -p /sbin/ldconfig

%files -f plugins.lst
%license COPYING
%doc AUTHORS ChangeLog README.md
%doc contrib
%config(noreplace) %{_sysconfdir}/collectd.conf
%dir %{_sysconfdir}/collectd
%{_bindir}/collectd-tg
%{_bindir}/collectd-nagios
%{_bindir}/collectdctl
%{_bindir}/cussh
%{_sbindir}/collectd
%{_sbindir}/collectdmon
%{_sbindir}/rccollectd
%dir %{_libdir}/collectd
%{_libdir}/collectd/notify_email.so
%{_libdir}/collectd/notify_email.la
%dir %{_datadir}/collectd
%{_datadir}/collectd/types.db
%{perl_vendorlib}/Collectd.pm
%dir %{perl_vendorlib}/Collectd
%{perl_vendorlib}/Collectd/*
%{perl_vendorarch}/auto/Collectd
%{_mandir}/man1/collectd.1%{?ext_man}
%{_mandir}/man1/collectdctl.1%{?ext_man}
%{_mandir}/man1/collectdmon.1%{?ext_man}
%{_mandir}/man1/collectd-tg.1%{?ext_man}
%{_mandir}/man1/collectd-nagios.1%{?ext_man}
%{_mandir}/man1/cussh.1%{?ext_man}
%{_mandir}/man5/collectd.conf.5%{?ext_man}
%{_mandir}/man5/collectd-email.5%{?ext_man}
%{_mandir}/man5/collectd-exec.5%{?ext_man}
%{_mandir}/man5/collectd-perl.5%{?ext_man}
%{_mandir}/man5/collectd-threshold.5%{?ext_man}
%{_mandir}/man5/collectd-unixsock.5%{?ext_man}
%{_mandir}/man5/types.db.5%{?ext_man}
%doc %{perl_man3dir}/Collectd::Unixsock.%{perl_man3ext}%{ext_man}
%dir %{_localstatedir}/lib/collectd
%{_unitdir}/collectd.service

%files web
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}.conf
%dir %{_sysconfdir}/collectd
%config(noreplace) %{_sysconfdir}/collectd/collection.conf
/srv/www/collectd

%files web-js
%doc _rpmdoc_/web-js/README
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}-js.conf
%dir %{_sysconfdir}/collectd
%config(noreplace) %{_sysconfdir}/collectd/collection-js.conf
/srv/www/collectd-js
%{_libexecdir}/collectd-js

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
%files plugin-amqp
%{_libdir}/collectd/amqp.so
%{_libdir}/collectd/amqp.la
%endif

%if %{with epics}
%files plugin-epics
%{_libdir}/collectd/epics.so
%{_libdir}/collectd/epics.la
%endif

%files plugin-notify-desktop
%{_libdir}/collectd/notify_desktop.so
%{_libdir}/collectd/notify_desktop.la

%files plugin-ipmi
%{_libdir}/collectd/ipmi.so
%{_libdir}/collectd/ipmi.la

%files plugin-snmp
%doc _rpmdoc_/snmp/*
%{_bindir}/collectd-snmp-probe-host
%{_mandir}/man1/collectd-snmp-probe-host.1%{?ext_man}
%{_libdir}/collectd/snmp*.so
%{_libdir}/collectd/snmp*.la
%{_mandir}/man5/collectd-snmp.5%{?ext_man}

%files plugin-pinba
%{_libdir}/collectd/pinba.so
%{_libdir}/collectd/pinba.la

%files plugin-mysql
%{_libdir}/collectd/mysql.so
%{_libdir}/collectd/mysql.la

%files plugin-pcie
%{_libdir}/collectd/pcie_errors.so
%{_libdir}/collectd/pcie_errors.la

%files plugin-postgresql
%{_libdir}/collectd/postgresql.so
%{_libdir}/collectd/postgresql.la
%config %{_datadir}/collectd/postgresql_default.conf

%files plugin-python3
%{_libdir}/collectd/python.so
%{_libdir}/collectd/python.la
%{_mandir}/man5/collectd-python.5%{?ext_man}

%files plugin-java
%doc _rpmdoc_/java/GenericJMX.conf
%{_libdir}/collectd/java.so
%{_libdir}/collectd/java.la
%{_datadir}/collectd/java
%{_mandir}/man5/collectd-java.5%{?ext_man}

%files plugin-virt
%{_libdir}/collectd/virt.so
%{_libdir}/collectd/virt.la

%files plugin-dbi
%{_libdir}/collectd/dbi.so
%{_libdir}/collectd/dbi.la

%files plugin-memcachec
%{_libdir}/collectd/memcachec.so
%{_libdir}/collectd/memcachec.la

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%files plugin-modbus
%{_libdir}/collectd/modbus.so
%{_libdir}/collectd/modbus.la
%endif

%if 0%{?is_opensuse}
%files plugin-mqtt
%{_libdir}/collectd/mqtt.so
%{_libdir}/collectd/mqtt.la
%endif

%if 0%{?sle_version} < 150000 || 0%{?is_opensuse}
%files plugin-sigrok
%{_libdir}/collectd/sigrok.so
%{_libdir}/collectd/sigrok.la

%files plugin-gps
%{_libdir}/collectd/gps.so
%{_libdir}/collectd/gps.la

%endif

%files plugin-smart
%{_libdir}/collectd/smart.so
%{_libdir}/collectd/smart.la

%files plugin-lua
%{_libdir}/collectd/lua.so
%{_libdir}/collectd/lua.la
%{_mandir}/man5/collectd-lua.5%{?ext_man}

%files plugin-openldap
%{_libdir}/collectd/openldap.so
%{_libdir}/collectd/openldap.la

%files plugin-mcelog
%{_libdir}/collectd/mcelog.so
%{_libdir}/collectd/mcelog.la

%files plugin-ovs
%{_libdir}/collectd/ovs_*.so
%{_libdir}/collectd/ovs_*.la

%files plugin-synproxy
%{_libdir}/collectd/synproxy.so
%{_libdir}/collectd/synproxy.la

%files plugin-write_stackdriver
%{_libdir}/collectd/write_stackdriver.so
%{_libdir}/collectd/write_stackdriver.la

%files plugin-write_syslog
%{_libdir}/collectd/write_syslog.so
%{_libdir}/collectd/write_syslog.la

%files plugin-uptime
%{_libdir}/collectd/check_uptime.la
%{_libdir}/collectd/check_uptime.so

%files plugin-connectivity
%{_libdir}/collectd/connectivity.la
%{_libdir}/collectd/connectivity.so

%files plugin-procevent
%{_libdir}/collectd/procevent.la
%{_libdir}/collectd/procevent.so

%files plugin-sysevent
%{_libdir}/collectd/sysevent.la
%{_libdir}/collectd/sysevent.so

%files plugin-buddyinfo
%{_libdir}/collectd/buddyinfo.la
%{_libdir}/collectd/buddyinfo.so

%files plugin-logparser
%{_libdir}/collectd/logparser.la
%{_libdir}/collectd/logparser.so

%files plugin-ubi
%{_libdir}/collectd/ubi.la
%{_libdir}/collectd/ubi.so

%files plugin-write_influxdb_udp
%{_libdir}/collectd/write_influxdb_udp.la
%{_libdir}/collectd/write_influxdb_udp.so

%if %{with nut}
%files plugin-nut
%{_libdir}/collectd/nut.so
%{_libdir}/collectd/nut.la
%endif

%files spamassassin
%dir %{_datadir}/spamassassin
%config(noreplace) %{_datadir}/spamassassin/99_%{name}.cf
%dir %{perl_vendorlib}/Mail
%dir %{perl_vendorlib}/Mail/SpamAssassin
%dir %{perl_vendorlib}/Mail/SpamAssassin/Plugin
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/Collectd.pm
%doc %{perl_man3dir}/Mail::SpamAssassin::Plugin::Collectd.%{perl_man3ext}%{ext_man}

%files plugin-dpdk
%if %{with dpdk}
%{_libdir}/collectd/dpdkevents.la
%{_libdir}/collectd/dpdkevents.so
%{_libdir}/collectd/dpdkstat.la
%{_libdir}/collectd/dpdkstat.so
%endif
%{_libdir}/collectd/dpdk_telemetry.la
%{_libdir}/collectd/dpdk_telemetry.so

%files plugins-all
%doc README.plugins-all

%files -n libcollectdclient1
%{_libdir}/libcollectdclient.so.1
%{_libdir}/libcollectdclient.so.1.*.*

%files -n libcollectdclient-devel
%{_includedir}/collectd
%{_libdir}/libcollectdclient.so
%{_libdir}/pkgconfig/libcollectdclient.pc

%changelog
