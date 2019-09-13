#
# spec file for package courier-authlib
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


Name:           courier-authlib
Summary:        Courier authentication library
License:        SUSE-GPL-3.0-with-openssl-exception
Group:          Productivity/Networking/Email/Servers
Version:        0.68.0
Release:        0
Url:            http://www.courier-mta.org/imap/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-%{version}.tar.bz2.sig
Source2:        courier-authdaemon-rpmlintrc
Source11:       courier-authdaemon.init
Source12:       courier-authdaemon.service
Source13:       courier-authlib.tmpfile
Patch0:         %{name}-authdaemonrc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         coreutils
BuildRequires:  courier-unicode-devel >= 2.0
BuildRequires:  expect
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  postgresql-devel >= 9.1
%if 0%{?suse_version} > 1500
BuildRequires:  postgresql-server-devel
%endif
BuildRequires:  procps
BuildRequires:  sqlite3-devel
Requires:       expect

%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define has_systemd 1
%endif

%description
The Courier authentication library provides authentication services for
other Courier applications.

%package devel
Summary:        Development libraries for the Courier authentication library
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

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
export CFLAGS="$RPM_OPT_FLAGS -DLDAP_DEPRECATED=1"
%configure \
	--libexecdir=%{_prefix}/lib \
	--datadir=%{_datadir}/courier-imap \
	--sharedstatedir=%{_sharedstatedir}/%{name} \
%if 0%{?has_systemd}
	--with-piddir=/run \
%else
	--with-piddir=/var/run \
%endif
	--disable-root-check \
	--enable-unicode \
%if 0%{?has_systemd}
	--with-authdaemonvar=/run/%{name} \
%else
	--with-authdaemonvar=%{_localstatedir}/run/%{name} \
%endif
	--host=%{_host} --build=%{_build} --target=%{_target_platform}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_libdir}/%{name}/lib*.so* %{buildroot}%{_libdir}
rm -f %{buildroot}/%{_libdir}/%{name}/*.{a,la}
install -m 755 sysconftool %{buildroot}/%{_prefix}/lib/%{name}
install -m 755 authmigrate %{buildroot}/%{_prefix}/lib/%{name}
%if 0%{?has_systemd}
install -D -m 0644 %{S:12} %{buildroot}/%{_unitdir}/courier-authdaemon.service
# systemd need to create a tmp dir: /run/courier-authlib
install -D -m 0644 %{S:13} %{buildroot}/%{_prefix}/lib/tmpfiles.d/%{name}.conf
ln -fs service %{buildroot}/%{_sbindir}/rccourier-authdaemon
%else
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
install -m 755 %{S:11} %{buildroot}/%{_sysconfdir}/init.d/courier-authdaemon
ln -fs ../../%{_sysconfdir}/init.d/courier-authdaemon \
  %{buildroot}%{_sbindir}/rccourier-authdaemon
%endif

%pre
%if 0%{?has_systemd}
%service_add_pre courier-authdaemon.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal courier-authdaemon
%endif
%if 0%{?has_systemd}
%service_del_preun courier-authdaemon.service
%endif
if [ "$1" = "0" ]; then
	for i in socket pid pid.lock; do
%if 0%{?has_systemd}
		rm -f /run/%{name}/$i
%else
		rm -f %{_localstatedir}/run/%{name}/$i
%endif
	done
fi

%post
/sbin/ldconfig
%{_prefix}/lib/%{name}/authmigrate >/dev/null
%{_prefix}/lib/%{name}/sysconftool %{_sysconfdir}/authlib/*.dist >/dev/null

%if 0%{?has_systemd}
%service_add_post courier-authdaemon.service
# Create our dirs immediatly, after a manual package install.
# After a reboot systemd/aaa_base will take care.
install -d /run/%{name}
%else
%if 0%{?suse_version}
%{fillup_and_insserv -f courier-authdaemon}
%endif
install -d %{_localstatedir}/run/%{name}
%endif

%postun
/sbin/ldconfig
%if 0%{?has_systemd}
%service_del_postun courier-authdaemon.service
%else
%if 0%{?suse_version}
%restart_on_update courier-authdaemon
%insserv_cleanup
%endif
%endif

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
%doc NEWS COPYING* AUTHORS ChangeLog authldap.schema
%dir %{_sysconfdir}/authlib
%config %{_sysconfdir}/authlib/*
%{_sbindir}/authdaemond
%{_sbindir}/authenumerate
%{_sbindir}/authpasswd
%{_sbindir}/authtest
%{_sbindir}/courierlogger
%{_sbindir}/rccourier-authdaemon
%dir /usr/lib/%{name}
/usr/lib/%{name}/authmigrate
/usr/lib/%{name}/sysconftool
/usr/lib/%{name}/authdaemond
/usr/lib/%{name}/authsystem.passwd
/usr/lib/%{name}/makedatprog
%{_libdir}/libauthcustom.so
%{_libdir}/libauthpam.so
%{_libdir}/libcourierauth.so
%{_libdir}/libcourierauthcommon.so
%{_libdir}/libcourierauthsasl.so
%{_libdir}/libcourierauthsaslclient.so
%{_mandir}/man1/*
%if 0%{?has_systemd}
%{_unitdir}/courier-authdaemon.service
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%ghost %dir /run/%{name}
%else
%{_sysconfdir}/init.d/courier-authdaemon
%ghost %dir %{_localstatedir}/run/%{name}
%endif

%files devel
%defattr(-,root,root,-)
%doc authlib.html auth_*.html
%{_bindir}/courierauthconfig
%{_includedir}/*
%{_mandir}/man3/*

%files userdb
%defattr(-,root,root,-)
%{_sbindir}/makeuserdb
%{_sbindir}/pw2userdb
%{_sbindir}/userdb
%{_sbindir}/userdb-test-cram-md5
%{_sbindir}/userdbpw
%{_libdir}/libauthuserdb.so
%{_mandir}/man8/*userdb*

%files ldap
%defattr(-,root,root,-)
%doc README.ldap authldap.schema
%{_libdir}/libauthldap.so

%files mysql
%defattr(-,root,root,-)
%{_libdir}/libauthmysql.so

%files pgsql
%defattr(-,root,root,-)
%{_libdir}/libauthpgsql.so

%files pipe
%defattr(-,root,root,-)
%{_libdir}/libauthpipe.so

%files sqlite
%defattr(-,root,root,-)
%{_libdir}/libauthsqlite.so

%changelog
