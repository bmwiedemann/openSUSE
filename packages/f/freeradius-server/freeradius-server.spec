#
# spec file for package freeradius-server
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


%define unitname radiusd
Name:           freeradius-server
Version:        3.0.25
Release:        0

# Disable FreeTDS on SLE12. We never shipped it enabled with FreeTDS.
%if 0%{?suse_version} > 1330 || 0%{?is_opensuse}
%bcond_without freetds
%bcond_without memcached
%else
%bcond_with    freetds
%bcond_with    memcached
%endif

Summary:        RADIUS Server
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Productivity/Networking/Radius/Servers
URL:            http://www.freeradius.org/
Source:         ftp://ftp.freeradius.org/pub/freeradius/%{name}-%{version}.tar.bz2
Source99:       ftp://ftp.freeradius.org/pub/freeradius/%{name}-%{version}.tar.bz2.sig
# keyring downloaded via link @ ftp://ftp.freeradius.org/pub/freeradius/README
Source100:      freeradius.keyring
Source1:        radiusd.service
Source2:        freeradius-tmpfiles.conf
Patch0:         freeradius-server-fix-perl-shbang.patch
Patch1:         freeradius-server-tmpfiles.patch
Patch3:         freeradius-server-rcradiusd.patch
Patch5:         freeradius-server-rlm_sql_unixodbc-configure.patch
Patch6:         freeradius-server-radclient-init-error-buffer.patch
Patch7:         freeradius-server-opensslversion.patch
Patch8:         freeradius-server-enable-python3.patch
BuildRequires:  apache2-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
%if %{with freetds}
BuildRequires:  freetds-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  krb5-devel
BuildRequires:  libcom_err-devel
BuildRequires:  libcurl-devel
BuildRequires:  libidn-devel
BuildRequires:  libjson-devel
%if %{with memcached}
BuildRequires:  libmemcached-devel
%endif
BuildRequires:  libmysqlclient-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel > 1.0
BuildRequires:  pam-devel
BuildRequires:  perl
BuildRequires:  postgresql-devel
BuildRequires:  python3-devel
BuildRequires:  sqlite3-devel
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(apr-1)
Requires:       %{name}-libs = %{version}
Requires:       coreutils
Requires:       pwdutils
Requires(pre):  openssl
Requires(pre):  perl
Recommends:     logrotate
Provides:       freeradius = %{version}
Provides:       radiusd
Obsoletes:      freeradius < %{version}
%{?libperl_requires}
Conflicts:      icradius
Conflicts:      radiusd-cistron
Conflicts:      radiusd-livingston
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

#bsc#1055679 - freeradius-server does not provide winbind/AD auth
BuildRequires:  pkgconfig(wbclient)

%description
Remote Authentication Dial-In User Service (RADIUS) is a networking
protocol that provides centralized Authentication, Authorization, and
Accounting (AAA or Triple A) management for users who connect and
use a network service.

FreeRADIUS is a modular RADIUS implementation.

%package libs
Summary:        FreeRADIUS shared library
Group:          System/Libraries

%description libs
The FreeRADIUS shared libraries.

%package utils
Summary:        FreeRADIUS Clients
Group:          Productivity/Networking/Radius/Clients
Requires:       %{name}-libs = %{version}

%description utils
Collection of FreeRADIUS utilities.

%package devel
Summary:        FreeRADIUS Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs = %{version}

%description devel
FreeRADIUS header files for development.

%package doc
Summary:        FreeRADIUS Documentation
Group:          Documentation/HTML

%description doc
FreeRADIUS documentation.

%package ldap
Summary:        LDAP support for freeradius
Group:          System/Daemons
BuildRequires:  openldap2-devel
Requires:       %{name} = %{version}

%description ldap
FreeRADIUS plugin providing LDAP support.

%package ldap-schemas
Summary:        FreeRADIUS support for OpenLDAP
Group:          System/Daemons
Requires:       openldap2

%description ldap-schemas
FreeRADIUS schemas for OpenLDAP.

%package krb5
Summary:        Kerberos 5 support for freeradius
Group:          System/Daemons
BuildRequires:  krb5-devel
Requires:       %{name} = %{version}

%description krb5
FreeRADIUS plugin providing Kerberos 5 authentication support.

%package perl
Summary:        Perl support for freeradius
Group:          System/Daemons
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::Embed)
Requires:       %{name} = %{version}
Requires:       perl

%description perl
FreeRADIUS plugin providing Perl support.

%package python3
Summary:        Python3 support for freeradius
Group:          System/Daemons
Requires:       %{name} = %{version}

%description python3
FreeRADIUS plugin providing Python3 support.

%package mysql
Summary:        MySQL support for freeradius
Group:          System/Daemons
BuildRequires:  mysql-devel
Requires:       %{name} = %{version}

%description mysql
FreeRADIUS plugin providing MySQL support.

%package postgresql
Summary:        Postgresql support for freeradius
Group:          System/Daemons
BuildRequires:  postgresql-devel
Requires:       %{name} = %{version}

%description postgresql
FreeRADIUS plugin providing PostgreSQL support.

%package sqlite
Summary:        SQLite support for freeradius
Group:          System/Daemons
BuildRequires:  sqlite3-devel
Requires:       %{name} = %{version}

%description sqlite
FreeRADIUS plugin providing SQLite support.

%prep
%autosetup -p1

%build
autoreconf -fi
export CFLAGS="%{optflags} -DLDAP_DEPRECATED -fstack-protector -fPIC -DPIC"
%if 0%{?suse_version} > 1550
export LDFLAGS="-pie $(python3-config --embed --libs)"
%else
export LDFLAGS="-pie"
%endif

%configure \
  --disable-static \
  --libdir=%{_libdir}/freeradius \
  --with-unixodbc-dir=%{_prefix} \
  --disable-ltdl-install \
  --enable-strict-dependencies \
  --with-edir \
  --with-gnu-ld \
  --with-system-libtool \
  --with-system-libltdl \
  --with-udpfromto \
  --without-rlm_eap_ikev2 \
  --without-rlm_eap_tnc \
  --with-rlm-krb5-lib-dir=%{_libdir} \
  --without-rlm_opendirectory \
  --without-rlm_sql_db2 \
  --without-rlm_sql_firebird \
  --without-rlm_sql_iodbc \
  --without-rlm_redis \
  --without-rlm_rediswho \
  --without-rlm_sql_oracle \
  --without-rlm_securid \
  --without-rlm_python \
  --with-rlm-python3-include-dir=%{_includedir}/python%{python3_version}%{py3_abiflags} \
%if ! %{with memcached}
  --without-rlm_cache_memcached \
%endif
%if ! %{with freetds}
  --without-rlm_sql_freetds \
%endif
  --disable-silent-rules \
  --disable-openssl-version-check
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_localstatedir}/lib/radiusd
make install R=%{buildroot} INSTALLSTRIP=
# Install ldap schema
install -d         %{buildroot}%{_sysconfdir}/openldap/schema
install -m 0644 -t %{buildroot}%{_sysconfdir}/openldap/schema doc/schemas/ldap/openldap/*.{ldif,schema}
# modify default configuration
RADDB=%{buildroot}%{_sysconfdir}/raddb
perl -i -pe 's/^#user =.*$/user = radiusd/'   $RADDB/radiusd.conf
perl -i -pe 's/^#group =.*$/group = radiusd/' $RADDB/radiusd.conf
/sbin/ldconfig -n %{buildroot}%{_libdir}/freeradius
# logs
touch %{buildroot}%{_localstatedir}/log/radius/radutmp
touch %{buildroot}%{_localstatedir}/log/radius/radius.log
# SUSE
%if 0%{?suse_version} > 1500
install -d     %{buildroot}%{_pam_vendordir}
install -m 644 suse/radiusd-pam %{buildroot}%{_pam_vendordir}/radiusd
%else
install -d     %{buildroot}%{_sysconfdir}/pam.d
install -m 644 suse/radiusd-pam %{buildroot}%{_sysconfdir}/pam.d/radiusd
%endif
install -d     %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 suse/radiusd-logrotate %{buildroot}%{_sysconfdir}/logrotate.d/radiusd
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{unitname}.conf
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{unitname}.service
# name the rc script according to the systemd unit
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcradiusd
cp -al %{buildroot}%{_sbindir}/radiusd %{buildroot}%{_sbindir}/radrelay
install -D -d -m 0710 %{buildroot}%{_rundir}/radiusd
mv -v doc/README doc/README.doc
# remove unneeded stuff
rm %{buildroot}%{_sysconfdir}/raddb/certs/*.crl
rm %{buildroot}%{_sysconfdir}/raddb/certs/*.crt
rm %{buildroot}%{_sysconfdir}/raddb/certs/*.csr
rm %{buildroot}%{_sysconfdir}/raddb/certs/*.der
rm %{buildroot}%{_sysconfdir}/raddb/certs/*.key
rm %{buildroot}%{_sysconfdir}/raddb/certs/*.pem
rm %{buildroot}%{_sysconfdir}/raddb/certs/*.p12
rm %{buildroot}%{_sysconfdir}/raddb/certs/index.*
rm %{buildroot}%{_sysconfdir}/raddb/certs/serial*
rm %{buildroot}%{_sysconfdir}/raddb/certs/dh
rm doc/source/.gitignore
rm %{buildroot}%{_sbindir}/rc.radiusd
rm -r %{buildroot}%{_datadir}/doc/freeradius*
rm -r %{buildroot}%{_libdir}/freeradius/*.*a
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/dhcp/mssql
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/main/mssql
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/ippool/mssql
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/mssql
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/dhcp/oracle
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/main/oracle
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/ippool/oracle
rm -r %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/oracle
rm %{buildroot}%{_sysconfdir}/raddb/mods-available/python
rm %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/ippool/mongo/queries.conf
rm %{buildroot}%{_sysconfdir}/raddb/mods-config/sql/main/mongo/queries.conf
rm %{buildroot}%{_sysconfdir}/raddb/sites-available/coa-relay

%pre
getent group radiusd >/dev/null || %{_sbindir}/groupadd -r radiusd
getent passwd radiusd >/dev/null || %{_sbindir}/useradd -r -g radiusd \
	-s /bin/false -c "Radius daemon" -d %{_localstatedir}/lib/radiusd \
	radiusd

# boo#912714: add radiusd to winbind group for ntlm_auth
# add winbind group and fail silently if it already exists
%{_bindir}/getent group winbind >/dev/null \
  || %{_sbindir}/groupadd -r winbind
# add radiusd to winbind group
%{_bindir}/gpasswd -a radiusd winbind

%service_add_pre %{unitname}.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/radiusd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%post
%service_add_post %{unitname}.service
systemd-tmpfiles --create %{_tmpfilesdir}/%{unitname}.conf

%preun
%service_del_preun %{unitname}.service

%postun
%service_del_postun %{unitname}.service

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/radiusd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files doc
%defattr(-,root,root)
%doc doc/*
%license LICENSE COPYRIGHT

%files
%defattr(-,root,root)
# doc
%doc CREDITS doc/ChangeLog
%license LICENSE COPYRIGHT
# SUSE
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/radiusd
%else
%config %{_sysconfdir}/pam.d/radiusd
%endif
%config %{_sysconfdir}/logrotate.d/radiusd
%{_sbindir}/rcradiusd
%dir %attr(755,radiusd,radiusd) %{_localstatedir}/lib/radiusd
# configs
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/trigger.conf
%defattr(-,root,radiusd)
%{_sysconfdir}/raddb/README.rst
%config(noreplace) %{_sysconfdir}/raddb/dictionary
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/clients.conf
%config(noreplace) %{_sysconfdir}/raddb/hints
%config(noreplace) %{_sysconfdir}/raddb/huntgroups
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/proxy.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/radiusd.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/experimental.conf
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/certs
%{_sysconfdir}/raddb/certs/Makefile
%{_sysconfdir}/raddb/certs/passwords.mk
%{_sysconfdir}/raddb/certs/README.md
%{_sysconfdir}/raddb/certs/xpextensions
%{_sysconfdir}/raddb/panic.gdb
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/certs/*.cnf
%attr(750,root,radiusd) %{_sysconfdir}/raddb/certs/bootstrap
%{_tmpfilesdir}/%{unitname}.conf
%{_unitdir}/%{unitname}.service

# mods-config
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config
%{_sysconfdir}/raddb/mods-config/README.rst
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/attr_filter
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/attr_filter/*
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/files
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/files/*
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/preprocess
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/moonshot-targeted-ids/*
%dir %attr(750,root,radiusd) /etc/raddb/mods-config/sql/moonshot-targeted-ids
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/preprocess/*
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/mysql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/mysql/schema.sql
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool/postgresql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/postgresql/procedure.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/counter
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/cui
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/dhcp
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main
#%%attr(640,root,radiusd) %%{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/oracle/queries.conf
#%%attr(640,root,radiusd) %%{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/oracle/schema.sql
%attr(640,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/sqlite/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/unbound
%attr(640,root,radiusd) %{_sysconfdir}/raddb/mods-config/unbound/default.conf

# sites-available
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/sites-available
%{_sysconfdir}/raddb/sites-available/README
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/control-socket
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/decoupled-accounting
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/robust-proxy-accounting
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/soh
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/coa
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/example
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/inner-tunnel
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/dhcp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/check-eap-tls
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/status
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/dhcp.relay
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/virtual.example.com
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/originate-coa
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/vmps
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/default
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/proxy-inner-tunnel
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/dynamic-clients
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/copy-acct-to-home-server
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/buffered-sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/tls
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/abfab-tls
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/abfab-tr-idp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/channel_bindings
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/challenge
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/resource-check
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/sites-available/totp

# sites-enabled
# symlink: %%{_sysconfdir}/raddb/sites-enabled/xxx -> ../sites-available/xxx
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/sites-enabled
%config(missingok) %{_sysconfdir}/raddb/sites-enabled/inner-tunnel
%config(missingok) %{_sysconfdir}/raddb/sites-enabled/default

# mods-available
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-available
%{_sysconfdir}/raddb/mods-available/README.rst
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/always
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/attr_filter
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/cache
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/cache_eap
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/chap
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/counter
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/cui
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/date
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/detail
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/detail.example.com
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/detail.log
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/dhcp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/dhcp_files
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/dhcp_passwd
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/dhcp_sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/dhcp_sqlippool
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/digest
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/dynamic_clients
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/eap
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/echo
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available%{_sysconfdir}_group
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/exec
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/expiration
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/expr
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/files
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/idn
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/inner-eap
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/ippool
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/linelog
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/logintime
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/mac2ip
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/mac2vlan
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/moonshot-targeted-ids
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/mschap
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/ntlm_auth
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/opendirectory
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/otp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/pam
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/pap
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/passwd
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/preprocess
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/python3
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/radutmp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/realm
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/redis
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/rediswho
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/replicate
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/rest
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/smbpasswd
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/smsotp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/soh
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/sometimes
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/sql_map
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/sqlcounter
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/sqlippool
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/sradutmp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/totp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/unix
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/utf8
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/wimax
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/yubikey
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/unbound
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/unpack
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/abfab_psk_sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/couchbase

# mods-enabled
# symlink: %%{_sysconfdir}/raddb/mods-enabled/xxx -> ../mods-available/xxx
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-enabled
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/always
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/attr_filter
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/cache_eap
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/chap
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/date
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/detail
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/detail.log
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/digest
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/dynamic_clients
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/eap
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/echo
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/exec
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/expiration
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/expr
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/files
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/linelog
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/logintime
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/mschap
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/ntlm_auth
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/pap
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/passwd
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/preprocess
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/radutmp
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/realm
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/replicate
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/soh
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/sradutmp
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/totp
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/unix
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/utf8
%config(missingok) %{_sysconfdir}/raddb/mods-enabled/unpack

# policy
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/policy.d
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/accounting
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/canonicalization
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/control
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/cui
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/dhcp
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/eap
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/filter
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/moonshot-targeted-ids
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/operator-name
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/abfab-tr
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/debug
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/policy.d/rfc7542

%config(noreplace) %{_sysconfdir}/raddb/users
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/templates.conf
%attr(710,radiusd,radiusd) %dir %ghost %{_rundir}/radiusd
# binaries
%defattr(-,root,root)
%{_sbindir}/checkrad
%{_sbindir}/radiusd
%{_sbindir}/radmin
%{_sbindir}/radrelay
%{_sbindir}/raddebug
# man-pages
%{_mandir}/man5/*
%{_mandir}/man8/*
# dictionaries
%attr(755,root,root) %dir %{_datadir}/freeradius
%{_datadir}/freeradius/*
# logs
%attr(700,radiusd,radiusd) %dir %{_localstatedir}/log/radius/
%attr(700,radiusd,radiusd) %dir %{_localstatedir}/log/radius/radacct/
%attr(644,radiusd,radiusd) %{_localstatedir}/log/radius/radutmp
%config(noreplace) %attr(600,radiusd,radiusd) %{_localstatedir}/log/radius/radius.log

# loadable modules
%dir %attr(755,root,root) %{_libdir}/freeradius
%{_libdir}/freeradius/proto_dhcp.so
%{_libdir}/freeradius/proto_vmps.so
%{_libdir}/freeradius/rlm_always.so
%{_libdir}/freeradius/rlm_attr_filter.so
%{_libdir}/freeradius/rlm_cache.so
%{_libdir}/freeradius/rlm_chap.so
%{_libdir}/freeradius/rlm_counter.so
%{_libdir}/freeradius/rlm_cram.so
%{_libdir}/freeradius/rlm_date.so
%{_libdir}/freeradius/rlm_detail.so
%{_libdir}/freeradius/rlm_dhcp.so
%{_libdir}/freeradius/rlm_digest.so
%{_libdir}/freeradius/rlm_dynamic_clients.so
%{_libdir}/freeradius/rlm_eap.so
%{_libdir}/freeradius/rlm_eap_fast.so
%{_libdir}/freeradius/rlm_eap_gtc.so
%{_libdir}/freeradius/rlm_eap_md5.so
%{_libdir}/freeradius/rlm_eap_mschapv2.so
%{_libdir}/freeradius/rlm_eap_peap.so
%{_libdir}/freeradius/rlm_eap_pwd.so
%{_libdir}/freeradius/rlm_eap_sim.so
%{_libdir}/freeradius/rlm_eap_tls.so
%{_libdir}/freeradius/rlm_eap_ttls.so
%{_libdir}/freeradius/rlm_exec.so
%{_libdir}/freeradius/rlm_expiration.so
%{_libdir}/freeradius/rlm_expr.so
%{_libdir}/freeradius/rlm_files.so
%{_libdir}/freeradius/rlm_ippool.so
%{_libdir}/freeradius/rlm_linelog.so
%{_libdir}/freeradius/rlm_logintime.so
%{_libdir}/freeradius/rlm_mschap.so
%{_libdir}/freeradius/rlm_otp.so
%{_libdir}/freeradius/rlm_pam.so
%{_libdir}/freeradius/rlm_pap.so
%{_libdir}/freeradius/rlm_passwd.so
%{_libdir}/freeradius/rlm_preprocess.so
%{_libdir}/freeradius/rlm_radutmp.so
%{_libdir}/freeradius/rlm_realm.so
%{_libdir}/freeradius/rlm_replicate.so
%{_libdir}/freeradius/rlm_rest.so
%{_libdir}/freeradius/rlm_soh.so
%{_libdir}/freeradius/rlm_sometimes.so
%{_libdir}/freeradius/rlm_sql.so
%{_libdir}/freeradius/rlm_sql_map.so
%{_libdir}/freeradius/rlm_sqlcounter.so
%{_libdir}/freeradius/rlm_sqlippool.so
%if %{with freetds}
%{_libdir}/freeradius/rlm_sql_freetds.so
%endif
%{_libdir}/freeradius/rlm_sql_null.so
%{_libdir}/freeradius/rlm_test.so
%{_libdir}/freeradius/rlm_totp.so
%{_libdir}/freeradius/rlm_unix.so
%{_libdir}/freeradius/rlm_utf8.so
%{_libdir}/freeradius/rlm_wimax.so
%{_libdir}/freeradius/rlm_yubikey.so
%{_libdir}/freeradius/rlm_sql_unixodbc.so
%{_libdir}/freeradius/rlm_unpack.so
%if %{with memcached}
%{_libdir}/freeradius/rlm_cache_memcached.so
%endif
%{_libdir}/freeradius/rlm_cache_rbtree.so

%files utils
%defattr(-,root,root)
%{_mandir}/man1/*
%{_bindir}/*

%files libs
%defattr(-,root,root)
%license LICENSE COPYRIGHT
# RADIUS shared libs
%attr(755,root,root) %dir %{_libdir}/freeradius
%attr(755,root,root) %{_libdir}/freeradius/lib*.so*

%files devel
%defattr(-,root,root)
%dir %attr(755,root,root) %{_includedir}/freeradius
%attr(644,root,root) %{_includedir}/freeradius/*.h

%files krb5
%defattr(-,root,root)
%{_libdir}/freeradius/rlm_krb5.so
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/krb5

%files perl
%defattr(-,root,root)
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/perl

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/perl
%{_sysconfdir}/raddb/mods-config/perl/example.pl

%{_libdir}/freeradius/rlm_perl.so

%files python3
%defattr(-,root,root)
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/python3
%attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/python3/example.py
%attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/python3/radiusd.py
%{_libdir}/freeradius/rlm_python3.so

%files mysql
%defattr(-,root,root)
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/counter/mysql
%attr(640,root,radiusd) %config(noreplace)%{_sysconfdir}/raddb/mods-config/sql/counter/mysql/dailycounter.conf
%attr(640,root,radiusd) %config(noreplace)%{_sysconfdir}/raddb/mods-config/sql/counter/mysql/weeklycounter.conf
%attr(640,root,radiusd) %config(noreplace)%{_sysconfdir}/raddb/mods-config/sql/counter/mysql/expire_on_login.conf
%attr(640,root,radiusd) %config(noreplace)%{_sysconfdir}/raddb/mods-config/sql/counter/mysql/monthlycounter.conf
%attr(640,root,radiusd) %config(noreplace)%{_sysconfdir}/raddb/mods-config/sql/counter/mysql/noresetcounter.conf

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/cui/mysql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/cui/mysql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/cui/mysql/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/dhcp/mysql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/mysql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/mysql/schema.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/mysql/setup.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool/mysql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/mysql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/mysql/schema.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/mysql/procedure.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/mysql/procedure-no-skip-locked.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/mysql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/mysql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/mysql/procedure.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/mysql/procedure-no-skip-locked.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main/mysql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/process-radacct.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/setup.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/extras
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/extras/wimax
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/extras/wimax/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/mysql/extras/wimax/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main/ndb
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/ndb/setup.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/ndb/schema.sql
%{_sysconfdir}/raddb/mods-config/sql/main/ndb/README

%{_libdir}/freeradius/rlm_sql_mysql.so

%files postgresql
%defattr(-,root,root)
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/counter/postgresql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/postgresql/dailycounter.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/postgresql/weeklycounter.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/postgresql/expire_on_login.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/postgresql/monthlycounter.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/postgresql/noresetcounter.conf

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/cui/postgresql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/cui/postgresql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/cui/postgresql/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/dhcp/postgresql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/postgresql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/postgresql/schema.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/postgresql/setup.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool/postgresql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/postgresql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/postgresql/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/postgresql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/postgresql/procedure.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/postgresql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/postgresql/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql/process-radacct.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql/setup.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql/extras
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql/extras/voip-postpaid.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/postgresql/extras/cisco_h323_db_schema.sql

%{_libdir}/freeradius/rlm_sql_postgresql.so

%files sqlite
%defattr(-,root,root)
%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/cui/sqlite
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/cui/sqlite/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/cui/sqlite/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/counter/sqlite
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/sqlite/dailycounter.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/sqlite/weeklycounter.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/sqlite/expire_on_login.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/sqlite/monthlycounter.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/counter/sqlite/noresetcounter.conf

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/dhcp/sqlite
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/sqlite/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/dhcp/sqlite/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool/sqlite
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/sqlite/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool/sqlite/schema.sql

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/sqlite
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/ippool-dhcp/sqlite/queries.conf

%dir %attr(750,root,radiusd) %{_sysconfdir}/raddb/mods-config/sql/main/sqlite
%attr(750,root,radiusd) %config %{_sysconfdir}/raddb/mods-config/sql/main/sqlite/process-radacct-refresh.sh
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/sqlite/process-radacct-schema.sql
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/sqlite/queries.conf
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-config/sql/main/sqlite/schema.sql

%{_libdir}/freeradius/rlm_sql_sqlite.so

%files ldap
%defattr(-,root,root)
%{_libdir}/freeradius/rlm_ldap.so
%attr(640,root,radiusd) %config(noreplace) %{_sysconfdir}/raddb/mods-available/ldap

%files ldap-schemas
%defattr(-,root,root)
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%config %{_sysconfdir}/openldap/schema/freeradius*.schema
%config %{_sysconfdir}/openldap/schema/freeradius*.ldif

%changelog
