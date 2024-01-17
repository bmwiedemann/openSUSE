#
# spec file for package courier-authlib
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


Name:           courier-authlib
Version:        0.72.0
Release:        0
Summary:        Courier authentication library
License:        SUSE-GPL-3.0-with-openssl-exception
Group:          Productivity/Networking/Email/Servers
URL:            https://www.courier-mta.org/imap/
Source0:        https://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2.sig
# Keyring downloaded from https://www.courier-mta.org/KEYS.bin#/%%{name}.keyring
Source2:        %{name}.keyring
Source3:        courier-authdaemon-rpmlintrc
Source12:       courier-authdaemon.service
Source13:       courier-authlib.tmpfile
Patch0:         %{name}-authdaemonrc.patch
BuildRequires:  courier-unicode-devel >= 2.1
BuildRequires:  expect
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel >= 9.1
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(systemd)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  postgresql-server-devel
%endif
BuildRequires:  procps
BuildRequires:  sqlite3-devel
Requires(pre):  group(mail)
%{?systemd_requires}

%description
The Courier authentication library provides authentication services for
other Courier applications.

%package devel
Summary:        Development libraries for the Courier authentication library
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       %{name}-ldap = %{version}
Requires:       %{name}-mysql = %{version}
Requires:       %{name}-pgsql = %{version}
Requires:       %{name}-pipe = %{version}
Requires:       %{name}-sqlite = %{version}
Requires:       %{name}-userdb = %{version}

%description devel
This package contains the development libraries and files needed to
compile Courier packages that use this authentication library.	Install
this package in order to build the rest of the Courier packages.  After
they are built and installed this package can be removed.  Files in
this package are not needed at runtime.

%package userdb
Summary:        Userdb support for the Courier authentication library
Group:          Productivity/Networking/Email/Servers

%description userdb
This package installs the userdb support for the Courier authentication
library.  Userdb is a simple way to manage virtual mail accounts using
a GDBM-based database file.

%package ldap
Summary:        LDAP support for the Courier authentication library
Group:          Productivity/Networking/Email/Servers

%description ldap
This package installs LDAP support for the Courier authentication
library. Install this package in order to be able to authenticate using
LDAP.

%package mysql
Summary:        MySQL support for the Courier authentication library
Group:          Productivity/Networking/Email/Servers

%description mysql
This package installs MySQL support for the Courier authentication
library. Install this package in order to be able to authenticate using
MySQL.

%package pgsql
Summary:        PostgreSQL support for the Courier authentication library
Group:          Productivity/Networking/Email/Servers

%description pgsql
This package installs PostgreSQL support for the Courier authentication
library. Install this package in order to be able to authenticate using
PostgreSQL.

%package pipe
Summary:        Pipe support for the Courier authentication library
Group:          Productivity/Networking/Email/Servers

%description pipe
This package installs Pipe support for the Courier authentication
library. Install this package in order to be able to authenticate using
Pipe.

%package sqlite
Summary:        SQLite support for the Courier authentication library
Group:          Productivity/Networking/Email/Servers

%description sqlite
This package installs SQLite support for the Courier authentication
library. Install this package in order to be able to authenticate using
SQLite.

%prep
%setup -q
%patch0

%build
export CFLAGS="%{optflags} -DLDAP_DEPRECATED=1"
%configure \
	--libexecdir=%{_prefix}/lib \
	--datadir=%{_datadir}/courier-imap \
	--sharedstatedir=%{_sharedstatedir}/%{name} \
	--with-piddir=%{_rundir} \
	--disable-root-check \
	--enable-unicode \
	--with-authdaemonvar=%{_rundir}/%{name} \
	--host=%{_host} --build=%{_build} --target=%{_target_platform}
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}%{_libdir}/%{name}/lib*.so* %{buildroot}%{_libdir}
rm -f %{buildroot}/%{_libdir}/%{name}/*.{a,la}
install -m 755 sysconftool %{buildroot}/%{_prefix}/lib/%{name}
install -D -m 0644 %{SOURCE12} %{buildroot}/%{_unitdir}/courier-authdaemon.service
# systemd need to create a tmp dir: /run/courier-authlib
install -d -m755 %{buildroot}%{_tmpfilesdir}
install -D -m 0644 %{SOURCE13} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -fs service %{buildroot}/%{_sbindir}/rccourier-authdaemon

%pre
%service_add_pre courier-authdaemon.service

%preun
%if 0%{?suse_version}
%stop_on_removal courier-authdaemon
%endif
%service_del_preun courier-authdaemon.service
if [ "$1" = "0" ]; then
	for i in socket pid pid.lock; do
		rm -f %{_rundir}/%{name}/$i
	done
fi

%post
/sbin/ldconfig
%{_prefix}/lib/%{name}/sysconftool %{_sysconfdir}/authlib/*.dist >/dev/null
%service_add_post courier-authdaemon.service
%tmpfiles_create %{_prefix}/lib/tmpfiles.d/%{name}.conf

%postun
/sbin/ldconfig
%service_del_postun courier-authdaemon.service

%post userdb -p /sbin/ldconfig
%postun userdb -p /sbin/ldconfig
%post ldap -p /sbin/ldconfig
%postun ldap -p /sbin/ldconfig
%post mysql -p /sbin/ldconfig
%postun mysql -p /sbin/ldconfig
%post pgsql -p /sbin/ldconfig
%postun pgsql -p /sbin/ldconfig
%post pipe -p /sbin/ldconfig
%postun pipe -p /sbin/ldconfig
%post sqlite -p /sbin/ldconfig
%postun sqlite -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README README*html
%license COPYING*
%doc NEWS AUTHORS ChangeLog authldap.schema
%dir %{_sysconfdir}/authlib
%config %{_sysconfdir}/authlib/*
%{_sbindir}/authdaemond
%{_sbindir}/authenumerate
%{_sbindir}/authpasswd
%{_sbindir}/authtest
%{_sbindir}/courierlogger
%{_sbindir}/rccourier-authdaemon
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/sysconftool
%{_prefix}/lib/%{name}/authdaemond
%{_prefix}/lib/%{name}/authsystem.passwd
%{_prefix}/lib/%{name}/makedatprog
%{_libdir}/libauthcustom.so.*
%{_libdir}/libauthpam.so.*
%{_libdir}/libcourierauth.so.*
%{_libdir}/libcourierauthcommon.so.*
%{_libdir}/libcourierauthsasl.so.*
%{_libdir}/libcourierauthsaslclient.so.*
%{_mandir}/man1/*
%{_unitdir}/courier-authdaemon.service
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%ghost %dir %{_rundir}/%{name}

%files devel
%defattr(-,root,root,-)
%doc authlib.html auth_*.html
%{_bindir}/courierauthconfig
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%files userdb
%defattr(-,root,root,-)
%{_sbindir}/makeuserdb
%{_sbindir}/pw2userdb
%{_sbindir}/userdb
%{_sbindir}/userdbpw
%{_libdir}/libauthuserdb.so.*
%{_mandir}/man8/*userdb*

%files ldap
%defattr(-,root,root,-)
%doc README.ldap authldap.schema
%{_libdir}/libauthldap.so.*

%files mysql
%defattr(-,root,root,-)
%{_libdir}/libauthmysql.so.*

%files pgsql
%defattr(-,root,root,-)
%{_libdir}/libauthpgsql.so.*

%files pipe
%defattr(-,root,root,-)
%{_libdir}/libauthpipe.so.*

%files sqlite
%defattr(-,root,root,-)
%{_libdir}/libauthsqlite.so.*

%changelog
