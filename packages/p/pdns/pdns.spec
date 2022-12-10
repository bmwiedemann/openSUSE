#
# spec file for package pdns
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


%if 0%{?fedora_version} >= 24 || 0%{?fc24}%{?fc25}
%bcond_with    systemd_separetedlibs
%else
%bcond_without systemd_separetedlibs
%endif
#
%bcond_without pdns_lua
%bcond_without pdns_odbc
%bcond_without pdns_sqlite3
%bcond_with    pdns_tinydns
%if 0%{?is_opensuse}
%bcond_without pdns_geoip
%bcond_without pdns_ixfrdist
%define ixfrdist_services ixfrdist.service ixfrdist@.service
%else
%bcond_with    pdns_geoip
%bcond_with    pdns_ixfrdist
%endif
%bcond_without pdns_tools
%bcond_without pdns_pkcs11
%bcond_without pdns_zeromq
%if 0%{?suse_version} >= 1550
%bcond_without pdns_lmdb
%else
%bcond_with    pdns_lmdb
%endif

%if 0%{?suse_version} < 1500
BuildRequires:  gcc9-c++
%define compiler_ver -9
%else
BuildRequires:  gcc-c++
%endif

%define services %{name}.service %{name}@.service %{?ixfrdist_services}

%ifarch %ix86 %arm
ExclusiveArch:  no-32bit-build
%endif

Name:           pdns
Version:        4.7.3
Release:        0
Summary:        Authoritative-only nameserver
License:        GPL-2.0-only
Group:          Productivity/Networking/DNS/Servers
URL:            https://www.powerdns.com/
Source:         https://downloads.powerdns.com/releases/pdns-%{version}.tar.bz2
Source1:        https://downloads.powerdns.com/releases/pdns-%{version}.tar.bz2.sig
Source2:        https://powerdns.com/powerdns-keyblock.asc#/pdns.keyring
Patch0:         pdns-4.0.3_allow_dacoverride_in_capset.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  sqlite-devel >= 3
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_serialization-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with pdns_geoip} || %{with pdns_ixfrdist}
BuildRequires:  yaml-cpp-devel >= 0.5
%endif
%if %{with pdns_geoip}
BuildRequires:  pkgconfig(libmaxminddb)
%endif
%if %{with pdns_lua}
BuildRequires:  lua-devel
%endif
%if %{with pdns_tinydns}
# FIXME: Could not find libcdb/tinycdb
%endif
%if 0%{?suse_version}
BuildRequires:  openldap2-devel
%else
BuildRequires:  openldap-devel
%endif
#BuildRequires:  ragel
%if %{with pdns_sqlite3}
BuildRequires:  sqlite-devel >= 3
%endif
%if %{with pdns_odbc}
BuildRequires:  unixODBC-devel
%endif
#
%if %{with pdns_pkcs11}
BuildRequires:  pkgconfig(p11-kit-1)
%endif
%if %{with pdns_zeromq}
BuildRequires:  zeromq-devel
%endif
%if %{with systemd_separetedlibs}
BuildRequires:  pkgconfig(libsystemd)
%endif
%if %{with pdns_lmdb}
BuildRequires:  lmdb-devel
%endif

# FIXME: use proper Requires(pre/post/preun/...)
#PreReq:         pdns-common
#Requires(post): pdns-common
Requires(pre):  pdns-common
Requires:       pdns-common
# dropped with version 4.3.0
Obsoletes:      pdns-backend-mydns < %{version}

Provides:       bundled(ipcrypt)
Provides:       bundled(json11)
Provides:       bundled(lmdb-safe)
Provides:       bundled(luawrapper)
Provides:       bundled(protozero) = 1.70
Provides:       bundled(yahttp)

%description
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents. Furthermore, PowerDNS
interfaces with almost any database.

%package backend-mysql
#
Summary:        MySQL backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-mysql
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the MySQL backend for pdns.

%package backend-postgresql
#
Summary:        PostgreSQL backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-postgresql
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the PostgreSQL backend for pdns.

%if %{with pdns_odbc}
%package backend-godbc
#
Summary:        ODBC backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-godbc
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the ODBC backend for pdns.
%endif

%package backend-sqlite3
#
Summary:        SQLite 3 backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-sqlite3
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the SQLite 3 backend for pdns.

%package backend-ldap
#
Summary:        LDAP backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-ldap
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the LDAP backend for pdns.

%package backend-lua
#
Summary:        Lua backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-lua
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the Lua backend for pdns.

%package backend-remote
#
Summary:        Remote backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-remote
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the remote backend for pdns.

%package backend-geoip
#
Summary:        GeoIP backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-geoip
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the GeoIP backend for pdns.

%if %{with pdns_lmdb}
%package backend-lmdb
#
Summary:        LMDB backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-lmdb
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the LMDB backend for pdns.
%endif

%prep
%autosetup -n %{name}-%{version} -p1

%build
export CXX=g++%{?compiler_ver}
%configure \
  --docdir=%{_docdir}/%{name}/ \
  --disable-silent-rules \
  --with-socketdir=%{_localstatedir} \
  --localstatedir=%{_localstatedir} \
  --enable-reproducible \
  --with-libsodium \
  --with-service-user=pdns \
  --with-service-group=pdns \
  --with-socketdir=/run/ \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --libdir=%{_libdir} \
  --with-mysql-lib=%{_libdir} \
%if %{with pdns_pkcs11}
  --enable-experimental-pkcs11 \
%endif
%if %{with sanitizer}
  --enable-asan         \
  --enable-msan         \
  --enable-tsan         \
  --enable-lsan         \
  --enable-ubsan        \
%endif
  --enable-malloc-trace \
%if %{with pdns_zeromq}
  --enable-remotebackend-zeromq \
%endif
  --with-modules="" \
%if %{with pdns_lua}
  --with-lua \
%endif
  --with-dynmodules="\
  bind     \
%if %{with pdns_geoip}
  geoip    \
%endif
  gmysql   \
%if %{with pdns_odbc}
  godbc    \
%endif
  gpgsql   \
%if %{with pdns_sqlite3}
  gsqlite3 \
%endif
  ldap     \
%if %{with pdns_lmdb}
  lmdb     \
%endif
%if %{with pdns_lua}
  lua2     \
%endif
  pipe     \
  remote   \
%if %{with pdns_tinydns}
  tinydns  \
%endif
  "\
%if %{with pdns_tools}
  --enable-tools \
%if %{with pdns_ixfrdist}
  --enable-ixfrdist \
%endif
%endif
  --disable-static
make %{?_smp_mflags} all

%install
%make_install

sed -i "s:# setgid=:setgid=pdns:g
s:# setuid=:setuid=pdns:g" \
  %{buildroot}%{_sysconfdir}/%{name}/pdns.conf-dist
mv %{buildroot}%{_sysconfdir}/%{name}/pdns.conf-dist %{buildroot}%{_sysconfdir}/%{name}/pdns.conf

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%if %{with pdns_ixfrdist}
mv %{buildroot}%{_sysconfdir}/%{name}/ixfrdist.{example.yml,yml}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcixfrdist
%endif

find %{buildroot} -type f -name "*.la" -delete -print

%pre
%service_add_pre %{services}

%post
%service_add_post %{services}

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%files
%doc NOTICE README*
%license COPYING
%exclude %{_docdir}/%{name}/*.sql
%exclude %{_docdir}/%{name}/*.schema
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%config(noreplace) %attr(640,root,pdns) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/dnsbulktest
%{_bindir}/dnspcap2calidns
%{_bindir}/dnsreplay
%{_bindir}/dnsscan
%{_bindir}/dnsscope
%{_bindir}/dnstcpbench
%{_bindir}/dnswasher
%{_bindir}/nproxy
%{_bindir}/nsec3dig
%{_bindir}/saxfr
%{_bindir}/calidns
%{_bindir}/dnsgram
%{_bindir}/dumresp
%{_bindir}/ixplore
%{_bindir}/sdig
%{_bindir}/pdns_control
%{_bindir}/pdns_notify
%{_bindir}/pdnsutil
%{_bindir}/stubquery
%{_bindir}/zone2sql
%{_bindir}/zone2json
%{_sbindir}/rcpdns
%{_sbindir}/pdns_server
%{_bindir}/dnspcap2protobuf
%{_mandir}/man1/dnspcap2protobuf.1%{?ext_man}
%{_mandir}/man1/dnsbulktest.1%{?ext_man}
%{_mandir}/man1/dnspcap2calidns.1%{?ext_man}
%{_mandir}/man1/dnsgram.1%{?ext_man}
%{_mandir}/man1/dnsscan.1%{?ext_man}
%{_mandir}/man1/ixplore.1%{?ext_man}
%{_mandir}/man1/nsec3dig.1%{?ext_man}
%{_mandir}/man1/saxfr.1%{?ext_man}
%{_mandir}/man1/sdig.1%{?ext_man}
%{_mandir}/man1/dnstcpbench.1%{?ext_man}
%{_mandir}/man1/dnsreplay.1%{?ext_man}
%{_mandir}/man1/dnsscope.1%{?ext_man}
%{_mandir}/man1/dnswasher.1%{?ext_man}
%{_mandir}/man1/pdns_control.1%{?ext_man}
%{_mandir}/man1/pdns_notify.1%{?ext_man}
%{_mandir}/man1/pdns_server.1%{?ext_man}
%{_mandir}/man1/pdnsutil.1%{?ext_man}
%{_mandir}/man1/zone2json.1%{?ext_man}
%{_mandir}/man1/zone2sql.1%{?ext_man}
%{_mandir}/man1/calidns.1%{?ext_man}
%{_mandir}/man1/dumresp.1%{?ext_man}
%{_mandir}/man1/nproxy.1%{?ext_man}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libpipebackend.so*
%{_libdir}/%{name}/libbindbackend.so*
%if %{with pdns_ixfrdist}
%config(noreplace) %attr(640,root,pdns) %{_sysconfdir}/%{name}/ixfrdist.yml
%{_unitdir}/ixfrdist.service
%{_unitdir}/ixfrdist@.service
%{_bindir}/ixfrdist
%{_sbindir}/rcixfrdist
%{_mandir}/man5/ixfrdist.yml.5%{?ext_man}
%{_mandir}/man1/ixfrdist.1%{?ext_man}
%endif

%files backend-mysql
%{_libdir}/%{name}/libgmysqlbackend.so*
%doc %{_docdir}/%{name}/*.mysql.sql

%if %{with pdns_lua}
%files backend-lua
%{_libdir}/%{name}/liblua2backend.so*
%endif

%files backend-postgresql
%{_libdir}/%{name}/libgpgsqlbackend.so*
%doc %{_docdir}/%{name}/*.pgsql.sql

%if %{with pdns_sqlite3}
%files backend-sqlite3
%{_libdir}/%{name}/libgsqlite3backend.so*
%doc %{_docdir}/%{name}/*.sqlite3.sql
%endif

%files backend-ldap
%{_bindir}/zone2ldap
%{_libdir}/%{name}/libldapbackend.so*
%{_mandir}/man1/zone2ldap.1%{?ext_man}
%doc %{_docdir}/%{name}/*.schema

%if %{with pdns_odbc}
%files backend-godbc
%{_libdir}/%{name}/libgodbcbackend.so*
%endif

%if %{with pdns_geoip}
%files backend-geoip
%{_libdir}/%{name}/libgeoipbackend.so*
%endif

%files backend-remote
%{_libdir}/%{name}/libremotebackend.so

%if %{with pdns_lmdb}
%files backend-lmdb
%{_libdir}/%{name}/liblmdbbackend.so
%endif

%changelog
