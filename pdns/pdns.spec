#
# spec file for package pdns
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


%bcond_without systemd
%if 0%{?fedora_version} >= 24 || 0%{?fc24}%{?fc25}
%bcond_with    systemd_separetedlibs
%else
%bcond_without systemd_separetedlibs
%endif
#
%bcond_without pdns_lua
%bcond_without pdns_mydns
%bcond_with    pdns_experimental_gss_tsig
%bcond_without pdns_odbc
%bcond_without pdns_sqlite3
%bcond_with    pdns_tinydns
%if 0%{?is_opensuse}
%bcond_without pdns_geoip
%else
%bcond_with    pdns_geoip
%endif
%if 0%{?suse_version} > 1315 || 0%{?is_opensuse}
%bcond_without pdns_protobuf
%else
%bcond_with    pdns_protobuf
%endif
%bcond_without pdns_tools
%bcond_without pdns_pkcs11
%bcond_without pdns_zeromq
Name:           pdns
Version:        4.1.13
Release:        0
Summary:        Authoritative-only nameserver
License:        GPL-2.0-only
Group:          Productivity/Networking/DNS/Servers
URL:            https://www.powerdns.com/
Source:         https://downloads.powerdns.com/releases/pdns-%{version}.tar.bz2
Source2:        README.opendbx
Source3:        https://downloads.powerdns.com/releases/pdns-%{version}.tar.bz2.sig
Source4:        https://powerdns.com/powerdns-keyblock.asc#/pdns.keyring
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
%{?systemd_requires}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_program_options-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with pdns_geoip}
BuildRequires:  GeoIP-devel
BuildRequires:  yaml-cpp-devel
%endif
%if %{with pdns_experimental_gss_tsig}
BuildRequires:  pkgconfig(gss)
BuildRequires:  pkgconfig(krb5-gssapi)
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
%if %{with pdns_protobuf}
BuildRequires:  protobuf-devel
%endif
%if %{with pdns_sqlite3}
BuildRequires:  sqlite-devel >= 3
%endif
%if %{with pdns_odbc}
BuildRequires:  unixODBC-devel
%endif
#
%if %{with pdns_opendbx}
BuildRequires:  opendbx-backend-pgsql
BuildRequires:  opendbx-devel
%endif
%if %{with pdns_pkcs11}
BuildRequires:  pkgconfig(p11-kit-1)
%endif
%if %{with pdns_zeromq}
BuildRequires:  zeromq-devel
%endif
%if %{with systemd_separetedlibs}
BuildRequires:  pkgconfig(libsystemd)
%endif

# FIXME: use proper Requires(pre/post/preun/...)
#PreReq:         pdns-common
#Requires(post): pdns-common
Requires(pre):  pdns-common
Requires:       pdns-common

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

%if %{with pdns_mydns}
%package backend-mydns
#
Summary:        MyDNS backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-mydns
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the MyDNS backend for pdns.

%endif

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

%package backend-opendbx
#
Summary:        OpenDBX backend for pdns
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}

%description backend-opendbx
The PowerDNS Nameserver is a authoritative-only nameserver.
It conforms to contemporary DNS standards documents.

This package holds the OpenDBX backend for pdns.

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

%prep
%setup -q
%patch0 -p1
%if %{with pdns_opendbx}
cp %{SOURCE2} README.opendbx
%endif

%build
%configure \
  --docdir=%{_docdir}/%{name}/ \
  --disable-silent-rules \
  --with-socketdir=%{_localstatedir} \
  --localstatedir=%{_localstatedir} \
  --enable-libsodium \
  --enable-reproducible \
%if %{with pdns_protobuf}
  --with-protobuf \
%endif
%if %{with pdns_experimental_gss_tsig}
  --enable-experimental-gss-tsig \
%endif
  --sysconfdir=%{_sysconfdir}/%{name} \
  --libdir=%{_libdir} \
  --with-pgsql-lib=%{_libdir} \
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
%if %{with pdns_oracle}
  goracle  \
%endif
  gpgsql   \
%if %{with pdns_sqlite3}
  gsqlite3 \
%endif
  ldap     \
%if %{with pdns_lua}
  lua      \
%endif
%if %{with pdns_mydns}
  mydns    \
%endif
%if %{with pdns_opendbx}
  opendbx  \
%endif
%if %{with pdns_oracle}
  oracle   \
%endif
  pipe     \
  random   \
  remote   \
%if %{with pdns_tinydns}
  tinydns  \
%endif
  "\
%if %{with pdns_tools}
  --enable-tools \
%endif
  --disable-static
make %{?_smp_mflags}

%install
%make_install

sed -i "s:# setgid=:setgid=pdns:g
s:# setuid=:setuid=pdns:g" \
  %{buildroot}%{_sysconfdir}/%{name}/pdns.conf-dist
mv %{buildroot}%{_sysconfdir}/%{name}/pdns.conf-dist %{buildroot}%{_sysconfdir}/%{name}/pdns.conf

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

find %{buildroot} -type f -name "*.la" -delete -print

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc AUTHORS NEWS NOTICE README*
%license COPYING
%exclude %{_docdir}/%{name}/*.sql
%exclude %{_docdir}/%{name}/*.schema
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%config(noreplace) %attr(640,root,pdns) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/dnsbulktest
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
%if %{with pdns_protobuf}
%{_bindir}/dnspcap2protobuf
%{_mandir}/man1/dnspcap2protobuf.1%{?ext_man}
%endif
%{_mandir}/man1/dnsbulktest.1%{?ext_man}
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
%{_libdir}/%{name}/librandombackend.so*

%files backend-mysql
%{_libdir}/%{name}/libgmysqlbackend.so*
%doc %{_docdir}/%{name}/*.mysql.sql

%if %{with pdns_mydns}
%files backend-mydns
%{_libdir}/%{name}/libmydnsbackend.so*
%endif

%if %{with pdns_lua}
%files backend-lua
%{_libdir}/%{name}/libluabackend.so*
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

%if %{with pdns_opendbx}
%files backend-opendbx
%{_libdir}/%{name}/libopendbxbackend.so*
%endif

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

%changelog
