#
# spec file for package kea
#
# Copyright (c) 2025 SUSE LLC
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


%define asiodns_sover 62
%define asiolink_sover 88
%define cc_sover 82
%define cfgrpt_sover 3
%define config_sover 83
%define cryptolink_sover 64
%define d2srv_sover 63
%define database_sover 76
%define dhcp_sover 109
%define dhcp_ddns_sover 68
%define dhcpsrv_sover 131
%define dns_sover 71
%define eval_sover 84
%define exceptions_sover 45
%define hooks_sover 120
%define http_sover 87
%define log_interprocess_sover 3
%define log_sover 75
%define mysql_sover 88
%define pgsql_sover 88
%define process_sover 90
%define stats_sover 53
%define tcp_sover 33
%define util_io_sover 12
%define util_sover 101
Name:           kea
Version:        3.0.2
Release:        0
Summary:        Dynamic Host Configuration Protocol daemon
License:        MPL-2.0
Group:          Productivity/Networking/Boot/Servers
URL:            https://kea.isc.org/
#Git-Clone:     https://gitlab.isc.org/isc-projects/kea
#Github is out of date / abandoned(?)
Source:         https://ftp.isc.org/isc/kea/%version/kea-%version.tar.xz
Source2:        https://ftp.isc.org/isc/kea/%version/kea-%version.tar.xz.asc
# https://www.isc.org/pgpkey/
Source3:        kea.keyring
Source4:        kea-dhcp4.service
Source5:        kea-dhcp6.service
Source6:        kea-dhcp-ddns.service
Source7:        kea-ctrl-agent.service
Patch1:         kea-boost1_89.patch
BuildRequires:  meson
BuildRequires:  freeradius-server-devel
BuildRequires:  gcc-c++
BuildRequires:  libmysqlclient-devel
BuildRequires:  libtool >= 2
BuildRequires:  log4cplus-devel
BuildRequires:  pkg-config >= 0.23
BuildRequires:  postgresql-server-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sysuser-tools
BuildRequires:  xz
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  fdupes
%sysusers_requires
Suggests:       %name-hooks = %version
%if 0%{?suse_version} >= 1500
BuildRequires:  (libboost_system-devel if boost-devel < 1.89)
%endif
BuildRequires:  boost-devel
BuildRequires:  systemd-rpm-macros

%description
Kea is a new DHCPv4/DHCPv6 server being developed by ISC in C++, a
continuation of the DHCP server in the (ended) BIND10 project. The
objective of this project is to provide a very high-performance,
extensible DHCP server engine for use by enterprises and service
providers, either as-is or with extensions and modifications.

%package        doc
Summary:        Documentation for Kea
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
This package contains the documentation for Kea.

%package hooks
Summary:        Standard Kea DHCP hooks/plugins
Group:          System/Libraries

%description hooks
A standard set of external libraries used to provide additional
functionality for Kea DHCP server

%package -n libkea-asiodns%asiodns_sover
Summary:        Kea DHCP server asiolink abstraction layer library
Group:          System/Libraries

%description -n libkea-asiodns%asiodns_sover
The asiodns library provides an abstraction layer between BIND10/Kea
modules and the asiolink library.

%package -n libkea-asiolink%asiolink_sover
Summary:        Kea DHCP server socket I/O abstraction layer library
Group:          System/Libraries

%description -n libkea-asiolink%asiolink_sover
The asiolink library provides an abstraction layer between BIND10/Kea
modules and the socket I/O subsystem Kea is using (currently,
boost::asio).

%package -n libkea-cc%cc_sover
Summary:        Kea DHCP server command channel library
Group:          System/Libraries

%description -n libkea-cc%cc_sover
libkea-cc is used for the control channel protocol between keactrl
and the server.

%package -n libkea-cfgrpt%cfgrpt_sover
Summary:        Kea DHCP server config report library
Group:          System/Libraries

%description -n libkea-cfgrpt%cfgrpt_sover
The cfgrpt library is used for generating configuration reports for Kea,
providing detailed JSON-formatted summaries of the server's current
configuration.

%package -n libkea-config%config_sover
Summary:        Kea DHCP server configuration client library
Group:          System/Libraries

%description -n libkea-config%config_sover
The Kea DHCP server can be managed at runtime via the Control
Channel. The CC allows an external entity (e.g. a tool run by a
sysadmin or a script) to issue commands to the server which can
influence its behavior or retreive information from it. Examples
envisioned are: reconfiguration, statistics retrieval and
manipulation, and shutdown.

Communication over the Control Channel is conducted using JSON
structures.

%package -n libkea-cryptolink%cryptolink_sover
Summary:        Kea DHCP server crypto abstraction layer library
Group:          System/Libraries

%description -n libkea-cryptolink%cryptolink_sover
The Kea cryptolink library is an abstraction layer for crypto
library backends (such as Botan, OpenSSL).

%package -n libkea-d2srv%d2srv_sover
Summary:        Kea DHCP-DDNS service library
Group:          System/Libraries

%description -n libkea-d2srv%d2srv_sover
This library provides DHCP-DDNS specific event loop and business logic.

%package -n libkea-database%database_sover
Summary:        Kea database abstraction library
Group:          System/Libraries

%description -n libkea-database%database_sover
Kea's database abstraction library.

%package -n libkea-dhcp%dhcp_sover
Summary:        Kea DHCP library
Group:          System/Libraries

%description -n libkea-dhcp%dhcp_sover
libdhcp is an all-purpose DHCP-manipulation library, written in
C++. It offers packet parsing and assembly, DHCPv4 and DHCPv6 options
parsing and assembly, interface detection, and socket operations It
can be used by server, client, relay, performance tools and other
DHCP-related tools. For a server-specific library, see
libkea-dhcpsrv.

%package -n libkea-dhcp_ddns%dhcp_ddns_sover
Summary:        Kea DHCP Dynamic DNS library
Group:          System/Libraries

%description -n libkea-dhcp_ddns%dhcp_ddns_sover
This is a library of classes for sending and receiving requests used
by ISC's DHCP-DDNS (aka D2) service to carry out DHCP-driven DNS
updates.

%package -n libkea-dhcpsrv%dhcpsrv_sover
Summary:        Kea DHCP server component library
Group:          System/Libraries

%description -n libkea-dhcpsrv%dhcpsrv_sover
This library contains code used for the DHCPv4 and DHCPv6 servers'
operations, including the "Lease Manager" that manages information
about leases and the "Configuration Manager" that stores the servers'
configuration etc.

%package -n libkea-dns%dns_sover
Summary:        Kea DHCP server component library
Group:          System/Libraries

%description -n libkea-dns%dns_sover
One of the many libraries the Kea DHCP server is composed of.

%package -n libkea-eval%eval_sover
Summary:        Kea DHCP expression evaluation library
Group:          System/Libraries

%description -n libkea-eval%eval_sover
The core of the libeval library is a parser that is able to parse an
expression (e.g. option[123].text == 'APC'). This is currently used
for client classification.

%package -n libkea-exceptions%exceptions_sover
Summary:        Kea DHCP server component library
Group:          System/Libraries

%description -n libkea-exceptions%exceptions_sover
One of the many libraries the Kea DHCP server is composed of.

%package -n libkea-hooks%hooks_sover
Summary:        Kea DHCP server hook library
Group:          System/Libraries

%description -n libkea-hooks%hooks_sover
The hooks framework is a Kea system that simplifies the way that
users can write code to modify the behavior of Kea. Instead of
altering the Kea source code, they write functions that are compiled
and linked into one or more dynamic shared objects. The library is
specified in the Kea configuration and, at runtime, Kea dynamically
loads the library into its address space. At various points in the
processing, the component "calls out" to functions in the library,
passing to them the data is it currently working on. They can examine
and modify the data as required.

%package -n libkea-http%http_sover
Summary:        Kea DHCP http communication library
Group:          System/Libraries

%description -n libkea-http%http_sover
This library is used by Control Agent to establish HTTP connections,
receive messages and send responses over HTTP. This library uses
boost ASIO for creating TCP connections and asynchronously receive
and send the data over the sockets.

%package -n libkea-log-interprocess%log_interprocess_sover
Summary:        Kea DHCP log interprocess library
Group:          System/Libraries

%description -n libkea-log-interprocess%log_interprocess_sover
The log-interprocess library facilitates the transfer of logging messages
between the different Kea processes.

%package -n libkea-log%log_sover
Summary:        Kea DHCP logging system library
Group:          System/Libraries

%description -n libkea-log%log_sover
This library contains the Kea logging system, which is based on the
log4J logging system common in Java development, and includes the
following ideas: a set of severity levels; a hierarchy of logging
sources; separation of message use from message text.

%package -n libkea-mysql%mysql_sover
Summary:        Kea MySQL database library
Group:          System/Libraries

%description -n libkea-mysql%mysql_sover
Kea's database library for MySQL.

%package -n libkea-pgsql%pgsql_sover
Summary:        Kea PostgreSQL database library
Group:          System/Libraries

%description -n libkea-pgsql%pgsql_sover
Kea's database library for PostgreSQL.

%package -n libkea-process%process_sover
Summary:        Kea DHCP process abstraction library
Group:          System/Libraries

%description -n libkea-process%process_sover
One of the many libraries the Kea DHCP server is composed of.

%package -n libkea-stats%stats_sover
Summary:        Kea DHCP Statistics Manager library
Group:          System/Libraries

%description -n libkea-stats%stats_sover
One of the many libraries the Kea DHCP server is composed of.

%package -n libkea-tcp%tcp_sover
Summary:        Kea TCP library
Group:          System/Libraries

%description -n libkea-tcp%tcp_sover
One of the many libraries the Kea DHCP server is composed of.

%package -n libkea-util-io%util_io_sover
Summary:        Kea I/O utility function library
Group:          System/Libraries

%description -n libkea-util-io%util_io_sover
One of the many libraries the Kea DHCP server is composed of.

%package -n libkea-util%util_sover
Summary:        Kea utility function library
Group:          System/Libraries

%description -n libkea-util%util_sover
One of the many libraries the Kea DHCP server is composed of.

%package -n python3-kea
Summary:        Python interface to Kea DHCP server
Group:          Development/Libraries/Python

%description -n python3-kea
Python3 interface to ISC Kea DHCP server.

%package devel
Summary:        Development files for the Kea DHCP server
Group:          Development/Libraries/C and C++
Requires:       libkea-asiodns%asiodns_sover = %version
Requires:       libkea-asiolink%asiolink_sover = %version
Requires:       libkea-cc%cc_sover = %version
Requires:       libkea-cfgrpt%cfgrpt_sover = %version
Requires:       libkea-config%config_sover = %version
Requires:       libkea-cryptolink%cryptolink_sover = %version
Requires:       libkea-d2srv%d2srv_sover = %version
Requires:       libkea-database%database_sover = %version
Requires:       libkea-dhcp%dhcp_sover = %version
Requires:       libkea-dhcp_ddns%dhcp_ddns_sover = %version
Requires:       libkea-dhcpsrv%dhcpsrv_sover = %version
Requires:       libkea-dns%dns_sover = %version
Requires:       libkea-eval%eval_sover = %version
Requires:       libkea-exceptions%exceptions_sover = %version
Requires:       libkea-hooks%hooks_sover = %version
Requires:       libkea-http%http_sover = %version
Requires:       libkea-log-interprocess%log_interprocess_sover = %version
Requires:       libkea-log%log_sover = %version
Requires:       libkea-mysql%mysql_sover = %version
Requires:       libkea-pgsql%pgsql_sover = %version
Requires:       libkea-process%process_sover = %version
Requires:       libkea-stats%stats_sover = %version
Requires:       libkea-tcp%tcp_sover = %version
Requires:       libkea-util%util_sover = %version
Requires:       libkea-util-io%util_io_sover = %version
# Bundy DHCP and Kea share the same origin, so conflict
Conflicts:      otheproviders(pkgconfig(dns++))

%description devel
Development files for the Kea DHCP server

%prep
%autosetup -p1 -n kea-%version
%if 0%{?suse_version} < 1600
%patch -R -P 1 -p1
%endif

%build
export FREERADIUS_INCLUDE="%_includedir/freeradius"
export FREERADIUS_LIB=""
export FREERADIUS_DICTIONARY=""
%meson --install-umask 022 -D netconf=disabled
%meson_build
%meson_build doc

%install
b=%buildroot
%meson_install
find %buildroot -type f -name "*.la" -delete -print
mkdir -p "$b/%_unitdir" "$b/%_sysusersdir"
cp %_sourcedir/*.service "$b/%_unitdir/"
echo 'u keadhcp - "Kea DHCP server" /var/lib/kea' >system-user-keadhcp.conf
cp -a system-user-keadhcp.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-keadhcp.conf random system-user-keadhcp.conf

perl -i -pe 's{%_localstatedir/log/kea-}{%_localstatedir/log/kea/}' \
	"$b/%_sysconfdir/kea"/*.conf

mkdir -p "$b%_localstatedir/log/kea"

# Remove unnecessary files
rm -Rf "%buildroot/%python3_sitelib/kea/__pycache__"
# Remove meson-info directory as it contains non reproducable files
rm -Rf "%{buildroot}/%{_datadir}/kea/meson-info"
%fdupes %{buildroot}/%{_datadir}/doc/kea

%pre -f random.pre
%service_add_pre kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%post
%service_add_post kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service
if [ "$1" -gt 1 ]; then
	chown -R keadhcp:keadhcp "%_localstatedir/lib/kea"
	chown -R keadhcp:keadhcp "%_localstatedir/log/kea"
	find %_sysconfdir/kea/ -type f -name '*.conf' -exec chown root:keadhcp {} +
	find %_sysconfdir/kea/ -type f -name '*.conf' -exec chmod 640 {} +
fi
bigkea_enabled=$(/usr/bin/systemctl is-enabled kea.service 2>/dev/null || :)
bigkea_active=$(/usr/bin/systemctl is-active kea.service 2>/dev/null || :)
use_dhcp4=$(grep -ie ^dhcp4=yes /etc/kea/keactrl.conf 2>/dev/null || :)
use_dhcp6=$(grep -ie ^dhcp6=yes /etc/kea/keactrl.conf 2>/dev/null || :)
use_ddns=$(grep -ie ^dhcp_ddns=yes /etc/kea/keactrl.conf 2>/dev/null || :)
use_agent=$(grep -ie ^ctrl_agent=yes /etc/kea/keactrl.conf 2>/dev/null || :)
if [ "$bigkea_enabled" = "enabled" ]; then
	echo "Transferring enablement of kea.service to new split units..."
	/usr/bin/systemctl disable kea.service || :
	if [ -n "$use_dhcp4" ]; then
		/usr/bin/systemctl enable kea-dhcp4.service || :
	fi
	if [ -n "$use_dhcp6" ]; then
		/usr/bin/systemctl enable kea-dhcp6.service || :
	fi
	if [ -n "$use_ddns" ]; then
		/usr/bin/systemctl enable kea-dhcp-ddns.service || :
	fi
	if [ -n "$use_agent" ]; then
		/usr/bin/systemctl enable kea-ctrl-agent.service || :
	fi
fi
if [ "$bigkea_active" = "active" ]; then
	echo "Transferring active state of kea.service to new split units..."
	/usr/bin/systemctl disable --now kea.service || :
	if [ -n "$use_dhcp4" ]; then
		/usr/bin/systemctl start kea-dhcp4.service || :
	fi
	if [ -n "$use_dhcp6" ]; then
		/usr/bin/systemctl start kea-dhcp6.service || :
	fi
	if [ -n "$use_ddns" ]; then
		/usr/bin/systemctl start kea-dhcp-ddns.service || :
	fi
	if [ -n "$use_agent" ]; then
		/usr/bin/systemctl start kea-ctrl-agent.service || :
	fi
fi

%preun
%service_del_preun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%postun
%service_del_postun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%ldconfig_scriptlets -n libkea-asiodns%asiodns_sover
%ldconfig_scriptlets -n libkea-asiolink%asiolink_sover
%ldconfig_scriptlets -n libkea-cc%cc_sover
%ldconfig_scriptlets -n libkea-cfgrpt%cfgrpt_sover
%ldconfig_scriptlets -n libkea-config%config_sover
%ldconfig_scriptlets -n libkea-cryptolink%cryptolink_sover
%ldconfig_scriptlets -n libkea-d2srv%d2srv_sover
%ldconfig_scriptlets -n libkea-database%database_sover
%ldconfig_scriptlets -n libkea-dhcp%dhcp_sover
%ldconfig_scriptlets -n libkea-dhcp_ddns%dhcp_ddns_sover
%ldconfig_scriptlets -n libkea-dhcpsrv%dhcpsrv_sover
%ldconfig_scriptlets -n libkea-dns%dns_sover
%ldconfig_scriptlets -n libkea-eval%eval_sover
%ldconfig_scriptlets -n libkea-exceptions%exceptions_sover
%ldconfig_scriptlets -n libkea-hooks%hooks_sover
%ldconfig_scriptlets -n libkea-http%http_sover
%ldconfig_scriptlets -n libkea-log-interprocess%log_interprocess_sover
%ldconfig_scriptlets -n libkea-log%log_sover
%ldconfig_scriptlets -n libkea-mysql%mysql_sover
%ldconfig_scriptlets -n libkea-pgsql%pgsql_sover
%ldconfig_scriptlets -n libkea-process%process_sover
%ldconfig_scriptlets -n libkea-stats%stats_sover
%ldconfig_scriptlets -n libkea-tcp%tcp_sover
%ldconfig_scriptlets -n libkea-util-io%util_io_sover
%ldconfig_scriptlets -n libkea-util%util_sover

%files
%dir %attr(0755,root,root) %_sysconfdir/kea
%config(noreplace) %attr(0640,root,keadhcp) %_sysconfdir/kea/*.conf
%_mandir/man8/*.8%{?ext_man}
%_sbindir/kea*
%_sbindir/perfdhcp
%_datadir/kea/
%_unitdir/*.service
%dir %attr(0750,keadhcp,keadhcp) %_localstatedir/lib/kea
%_sysusersdir/*
%attr(0750,keadhcp,keadhcp) %_localstatedir/log/kea/

%files doc
%doc %_datadir/doc/kea/
%exclude %_datadir/doc/kea/html/.buildinfo

%files hooks
%dir %_libdir/kea
%_libdir/kea/hooks/
%dir %{_sysconfdir}/kea/radius
%{_sysconfdir}/kea/radius/dictionary

%files -n libkea-asiodns%asiodns_sover
%_libdir/libkea-asiodns.so.%asiodns_sover
%_libdir/libkea-asiodns.so.%asiodns_sover.*

%files -n libkea-asiolink%asiolink_sover
%_libdir/libkea-asiolink.so.%asiolink_sover
%_libdir/libkea-asiolink.so.%asiolink_sover.*

%files -n libkea-cc%cc_sover
%_libdir/libkea-cc.so.%cc_sover
%_libdir/libkea-cc.so.%cc_sover.*

%files -n libkea-cfgrpt%cfgrpt_sover
%_libdir/libkea-cfgrpt.so.%cfgrpt_sover
%_libdir/libkea-cfgrpt.so.%cfgrpt_sover.*

%files -n libkea-config%config_sover
%_libdir/libkea-config.so.%config_sover
%_libdir/libkea-config.so.%config_sover.*

%files -n libkea-cryptolink%cryptolink_sover
%_libdir/libkea-cryptolink.so.%cryptolink_sover
%_libdir/libkea-cryptolink.so.%cryptolink_sover.*

%files -n libkea-d2srv%d2srv_sover
%_libdir/libkea-d2srv.so.%d2srv_sover
%_libdir/libkea-d2srv.so.%d2srv_sover.*

%files -n libkea-database%database_sover
%_libdir/libkea-database.so.%database_sover
%_libdir/libkea-database.so.%database_sover.*

%files -n libkea-dhcp%dhcp_sover
%_libdir/libkea-dhcp.so.%dhcp_sover
%_libdir/libkea-dhcp.so.%dhcp_sover.*

%files -n libkea-dhcp_ddns%dhcp_ddns_sover
%_libdir/libkea-dhcp_ddns.so.%dhcp_ddns_sover
%_libdir/libkea-dhcp_ddns.so.%dhcp_ddns_sover.*

%files -n libkea-dhcpsrv%dhcpsrv_sover
%_libdir/libkea-dhcpsrv.so.%dhcpsrv_sover
%_libdir/libkea-dhcpsrv.so.%dhcpsrv_sover.*

%files -n libkea-dns%dns_sover
%_libdir/libkea-dns.so.%dns_sover
%_libdir/libkea-dns.so.%dns_sover.*

%files -n libkea-eval%eval_sover
%_libdir/libkea-eval.so.%eval_sover
%_libdir/libkea-eval.so.%eval_sover.*

%files -n libkea-exceptions%exceptions_sover
%_libdir/libkea-exceptions.so.%exceptions_sover
%_libdir/libkea-exceptions.so.%exceptions_sover.*

%files -n libkea-hooks%hooks_sover
%_libdir/libkea-hooks.so.%hooks_sover
%_libdir/libkea-hooks.so.%hooks_sover.*

%files -n libkea-http%http_sover
%_libdir/libkea-http.so.%http_sover
%_libdir/libkea-http.so.%http_sover.*

%files -n libkea-log-interprocess%log_interprocess_sover
%_libdir/libkea-log-interprocess.so.%log_interprocess_sover
%_libdir/libkea-log-interprocess.so.%log_interprocess_sover.*

%files -n libkea-log%log_sover
%_libdir/libkea-log.so.%log_sover
%_libdir/libkea-log.so.%log_sover.*

%files -n libkea-mysql%mysql_sover
%_libdir/libkea-mysql.so.%mysql_sover
%_libdir/libkea-mysql.so.%mysql_sover.*

%files -n libkea-pgsql%pgsql_sover
%_libdir/libkea-pgsql.so.%pgsql_sover
%_libdir/libkea-pgsql.so.%pgsql_sover.*

%files -n libkea-process%process_sover
%_libdir/libkea-process.so.%process_sover
%_libdir/libkea-process.so.%process_sover.*

%files -n libkea-stats%stats_sover
%_libdir/libkea-stats.so.%stats_sover
%_libdir/libkea-stats.so.%stats_sover.*

%files -n libkea-tcp%tcp_sover
%_libdir/libkea-tcp.so.%tcp_sover
%_libdir/libkea-tcp.so.%tcp_sover.*

%files -n libkea-util-io%util_io_sover
%_libdir/libkea-util-io.so.%util_io_sover
%_libdir/libkea-util-io.so.%util_io_sover.*

%files -n libkea-util%util_sover
%_libdir/libkea-util.so.%util_sover
%_libdir/libkea-util.so.%util_sover.*

%files -n python3-kea
%python3_sitelib/kea/

%files devel
%_includedir/kea/
%_libdir/libkea*.so
%{_libdir}/pkgconfig/*.pc
%{_bindir}/kea-msg-compiler

%changelog
