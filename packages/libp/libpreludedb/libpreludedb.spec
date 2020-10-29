#
# spec file for package libpreludedb
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


%{!?python_sitearch3: %global python_sitearch3 %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define sover 7
%define sover_cpp 2
Name:           libpreludedb
Version:        5.2.0
Release:        0
Summary:        Framework to easy access to the Prelude database
# Prelude is GPL-2.0+
# libmissing is LGPL-2.1+
# libmissing/test is GPL-3.0+
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://www.prelude-siem.org/attachments/download/233/RPM-GPG-KEY-Prelude-IDS#/%{name}.keyring
# Fix undefined non weak symbol
Patch0:         libpreludedb-undefined_non_weak_symbol.patch
Patch1:         libpreludedb-fix_gtkdoc_1.32.patch
Patch3:         libpreludedb-force_preludedb_admin_with_py3.patch
Patch4:         libpreludedb-update_m4_postgresql.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  libprelude-devel >= 5.2.0
BuildRequires:  mysql-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel >= 3.0.0
Requires:       libprelude-tools >= 5.2.0
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  postgresql-server-devel
%endif

%description
The PreludeDB Library provides an abstraction layer upon the type and the
format of the database used to store IDMEF alerts. It allows developers
to use the Prelude IDMEF database easily and efficiently without
worrying about SQL, and to access the database independently of the
type/format of the database.

%package -n %{name}%{sover}
Summary:        Prelude Libraries
Group:          System/Libraries

%description -n %{name}%{sover}
The PreludeDB Library provides an abstraction layer upon the type and the
format of the database used to store IDMEF alerts. It allows developers
to use the Prelude IDMEF database easily and efficiently without
worrying about SQL, and to access the database independently of the
type/format of the database.

%package -n %{name}cpp%{sover_cpp}
Summary:        Prelude Libraries
Group:          System/Libraries

%description -n %{name}cpp%{sover_cpp}
The PreludeDB Library provides an abstraction layer upon the type and the
format of the database used to store IDMEF alerts. It allows developers
to use the Prelude IDMEF database easily and efficiently without
worrying about SQL, and to access the database independently of the
type/format of the database.

%package devel
Summary:        Development files for libpreludedb
Group:          Development/Libraries/C and C++
Requires:       automake
Requires:       libprelude-devel >= 5.2.0
Requires:       libpreludedb%{sover} = %{version}
Requires:       libpreludedbcpp%{sover_cpp} = %{version}
Requires:       mysql-devel
Requires:       postgresql-devel
Requires:       sqlite-devel

%description devel
The PreludeDB Library provides an abstraction layer upon the type
and the format of the database used to store IDMEF alerts. It
allows developers to use the Prelude IDMEF database easily and
efficiently without worrying about SQL, and to access the
database independently of the type/format of the database.

%package devel-bindings
Summary:        Development files for libpreludedb
Group:          Development/Libraries/C and C++
Requires:       libpreludedb-devel = %{version}
Requires:       python-devel
Requires:       python3-devel
Requires:       swig

%description devel-bindings
The PreludeDB Library provides an abstraction layer upon the type
and the format of the database used to store IDMEF alerts. It
allows developers to use the Prelude IDMEF database easily and
efficiently without worrying about SQL, and to access the
database independently of the type/format of the database.

%package -n preludedb-tools
Summary:        Tools of libpreludedb
Group:          Productivity/Networking/Security

%description -n preludedb-tools
The PreludeDB Library provides an abstraction layer upon the type
and the format of the database used to store IDMEF alerts. It
allows developers to use the Prelude IDMEF database easily and
efficiently without worrying about SQL, and to access the
database independently of the type/format of the database.

%package plugins
Summary:        Plugin to use prelude with a classic schema
Group:          Productivity/Networking/Security

%description plugins
This plugin allows prelude to store alerts into a classic
schema in database.

%package mysql
Summary:        Plugin to use prelude with a mysql database
Group:          Productivity/Networking/Security
Requires:       libpreludedb-plugins = %{version}
Requires:       mysql
Requires:       mysql-server

%description mysql
This plugin allows prelude to store alerts into a mysql database.

%package pgsql
Summary:        Plugin to use prelude with a pgsql database
Group:          Productivity/Networking/Security
Requires:       libpreludedb-plugins = %{version}
Requires:       postgresql-server

%description pgsql
This plugin allows prelude to store alerts into a pgsql database.

%package sqlite
Summary:        Plugin to use prelude with a sqlite database
Group:          Productivity/Networking/Security
Requires:       libpreludedb-plugins = %{version}
Requires:       sqlite

%description sqlite
This plugin allows prelude to store alerts into a sqlite database.

%package -n python3-%{name}
Summary:        Python 3 bindings for libpreludedb
Group:          Development/Languages/Python

%description -n python3-%{name}
Python 3 bindings for libpreludedb generated by SWIG.

%package doc
Summary:        Libprelude documentation
Group:          Documentation/HTML

%description doc
Libprelude documentation files.

%prep
%setup -q
%patch0
%patch1
%patch3
%patch4

%build
%configure --with-html-dir=%{_defaultdocdir}/%{name}-%{version}/html \
           --without-python2 \
           --disable-static \
           --enable-gtk-doc

sed -i.rpath -e 's|LD_RUN_PATH=""||' bindings/Makefile
sed -i.rpath -e 's|^sys_lib_dlsearch_path_spec="/lib %{_prefix}/lib|sys_lib_dlsearch_path_spec="/%{_lib} %{_libdir}|' libtool

%make_build

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/libpreludedb%{sover}/swig/python
cp bindings/libpreludedbcpp.i %{buildroot}%{_datadir}/libpreludedb%{sover}/swig/
cp bindings/python/libpreludedbcpp-python.i %{buildroot}%{_datadir}/libpreludedb%{sover}/swig/python
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'

%post -n libpreludedb%{sover} -p /sbin/ldconfig
%post -n libpreludedbcpp%{sover_cpp} -p /sbin/ldconfig
%postun -n libpreludedb%{sover} -p /sbin/ldconfig
%postun -n libpreludedbcpp%{sover_cpp} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%{_libdir}/libpreludedb.so.%{sover}*

%files -n %{name}cpp%{sover_cpp}
%license COPYING
%{_libdir}/libpreludedbcpp.so.%{sover_cpp}*

%files -n preludedb-tools
%license COPYING
%{_mandir}/man1/preludedb-admin.1%{?ext_man}
%{_bindir}/preludedb-admin

%files plugins
%license COPYING
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/formats/

%files devel
%license COPYING
%{_bindir}/libpreludedb-config
%{_includedir}/libpreludedb
%{_libdir}/libpreludedb.so
%{_libdir}/libpreludedbcpp.so
%{_datadir}/aclocal/libpreludedb.m4
%{_mandir}/man1/libpreludedb-config.1%{?ext_man}

%files devel-bindings
%license COPYING
%dir %{_datadir}/libpreludedb%{sover}/
%dir %{_datadir}/libpreludedb%{sover}/swig/
%{_datadir}/libpreludedb%{sover}/swig/libpreludedbcpp.i
%dir %{_datadir}/libpreludedb%{sover}/swig/python/
%{_datadir}/libpreludedb%{sover}/swig/python/libpreludedbcpp-python.i

%files -n python3-%{name}
%license COPYING
%{python_sitearch3}/*

%files mysql
%license COPYING
%defattr(0755,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/sql
%{_libdir}/%{name}/plugins/sql/mysql.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/classic
%attr(0644,root,root) %{_datadir}/%{name}/classic/mysql*.sql
%attr(0755,root,root) %{_datadir}/%{name}/classic/*.sh

%files sqlite
%license COPYING
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/sql
%{_libdir}/%{name}/plugins/sql/sqlite3.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/classic
%{_datadir}/%{name}/classic/sqlite*

%files pgsql
%license COPYING
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/sql
%{_libdir}/%{name}/plugins/sql/pgsql.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/classic
%{_datadir}/%{name}/classic/pgsql*

%files doc
%license COPYING LICENSE.README
%doc %{_docdir}/%{name}-%{version}
%doc ChangeLog README NEWS HACKING.README

%changelog
