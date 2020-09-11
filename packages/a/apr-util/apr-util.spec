#
# spec file for package apr-util
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


%define         apuver 1
%define         libname lib%{name}%{apuver}
%define         dso_libdir %{_libdir}/apr-util-%{apuver}
%define         includedir %{_includedir}/apr-%{apuver}
Name:           apr-util
Version:        1.6.1
Release:        0
Summary:        Apache Portable Runtime (APR) Utility Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            http://apr.apache.org/
Source:         http://www.apache.org/dist/apr/apr-util-%{version}.tar.bz2
Patch1:         apr-util-1.4.1-testmemcache-initialize-values-array.patch
Patch2:         apr-util-visibility.patch
# PATCH-FIX-OPENSUSE apr-util-mariadb-10.2.patch dimstar@opensuse.org -- Fix build with mariadb 10.2
Patch3:         apr-util-mariadb-10.2.patch
# PATCH-FIX-OPENSUSE apr-util-postgresql.patch max@suse.com -- Fix build with PostgreSQL 11
Patch4:         apr-util-postgresql.patch
# https://svn.apache.org/viewvc?view=revision&revision=1825312
Patch5:         apr-util-apr_dbm_gdbm-fix-handling-of-error-codes.patch
BuildRequires:  apr-devel
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  gdbm-devel
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel >= 9.1.0
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
%requires_ge    libapr1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A companion library to APR, the Apache Portable Runtime.

%package -n %{libname}
Summary:        Apache Portable Runtime (APR) Utility Library
License:        Apache-2.0
Group:          System/Libraries
%requires_ge    libapr1

%description -n %{libname}
A companion library to APR, the Apache Portable Runtime.

%package devel
Summary:        Development files for the Apache Portable Runtime (APR) Utility Library
# apu-config returns -lldap -lber -ldb-<dbversion> -lexpat
# until this is fixed the devel package should require those
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Provides:       %{libname}-devel = %{version}
Obsoletes:      %{libname}-devel < %{version}-%{release}
Requires:       %{libname} = %{version}
Requires:       apr-devel
Requires:       gdbm-devel
Requires:       libexpat-devel
Requires:       openldap2-devel

%description devel
This subpackage contains header files for developing applications
that want to make use of the APR Utility library.

%package -n %{libname}-dbd-mysql
Summary:        DBD driver for MySQL
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{libname} = %{version}

%description -n %{libname}-dbd-mysql
DBD driver for MySQL database.

%package -n %{libname}-dbd-pgsql
Summary:        DBD driver for PostgreSQL
License:        Apache-2.0
Group:          System/Libraries
Requires:       %{libname} = %{version}

%description -n %{libname}-dbd-pgsql
DBD driver for PostgreSQL database.

%package -n %{libname}-dbd-sqlite3
Summary:        DBD driver for SQLite 3
License:        Apache-2.0
Group:          System/Libraries
Requires:       %{libname} = %{version}

%description -n %{libname}-dbd-sqlite3
DBD driver for SQLite 3 database.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
echo 'HTML_TIMESTAMP=NO' >> docs/doxygen.conf
export ac_cv_ldap_set_rebind_proc_style=three
rm -rf aclocal.m4 autom4te*.cache
autoreconf -fiv
sed -i -e '/OBJECTS_all/s, dbd/apr_dbd_[^ ]*\.lo,,g' build-outputs.mk
# all DBD driveres are built by default, nowadays -- except mysql
%configure \
    --includedir=%{includedir} \
    --with-crypto \
    --with-openssl=%{_prefix} \
    --with-apr=%{_bindir}/apr-1-config \
    --with-expat=%{_prefix} \
    --with-ldap \
    --with-mysql \
    --with-pgsql \
    --with-gdbm
make %{?_smp_mflags} CFLAGS="%{optflags} -DOPENSSL_LOAD_CONF -fvisibility=hidden"
make %{?_smp_mflags} dox

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mv docs/dox/html html
# multiacrh anti-borker
perl -pi -e "s|^LDFLAGS=.*|LDFLAGS=\"\"|g" %{buildroot}%{_bindir}/apu-%{apuver}-config
# includes anti-borker
perl -pi -e "s|-I%{_includedir}/mysql||g" %{buildroot}%{_bindir}/apu-%{apuver}-config
# unpackaged files
rm -f %{buildroot}/%{_libdir}/aprutil.exp

find %{buildroot} -type f -name "*.la" -print -delete

%check
# fails on qemu, works on real hardware
%if !0%{?qemu_user_space_build:1}
# We are not thread safe in tests
make -j1 check
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc CHANGES
%doc LICENSE
%doc NOTICE
%{_libdir}/libaprutil-%{apuver}.so.*
%dir %{dso_libdir}
%{dso_libdir}/apr_ldap*
%{dso_libdir}/apr_dbm_gdbm*
%{dso_libdir}/apr_crypto_openssl*

%files -n %{libname}-dbd-mysql
%defattr(-,root,root,-)
%{dso_libdir}/apr_dbd_mysql*

%files -n %{libname}-dbd-pgsql
%defattr(-,root,root,-)
%{dso_libdir}/apr_dbd_pgsql*

%files -n %{libname}-dbd-sqlite3
%defattr(-,root,root,-)
%{dso_libdir}/apr_dbd_sqlite3*

%files devel
%defattr(-,root,root)
%doc html
%dir %{includedir}
%{includedir}/*.h
%{_libdir}/libaprutil-%{apuver}.so
%{_bindir}/apu-%{apuver}-config
%{_libdir}/pkgconfig/apr-util-%{apuver}.pc

%changelog
