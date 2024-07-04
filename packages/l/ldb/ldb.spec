#
# spec file for package ldb
#
# Copyright (c) 2024 SUSE LLC
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


%{!?py3_soflags:  %global py3_soflags cpython-%{python3_version_nodots}m}
%{!?py3_soflags_dash:   %global py3_soflags_dash %(echo %{py3_soflags} | sed "s/_/-/g")}

%global with_lmdb 0
%if 0%{?suse_version} > 1320
%ifarch x86_64
%global with_lmdb 1
%endif
%endif

%define lmdb_version 0.9.16
%define talloc_version 2.4.2
%define tdb_version 1.4.10
%define tevent_version 0.16.1

Name:           ldb
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
%if 0%{?suse_version} > 1500
%ifnarch ppc
BuildRequires:  libcmocka-devel >= 1.1.3
%endif
%endif
BuildRequires:  libtalloc-devel >= %{talloc_version}
BuildRequires:  libtdb-devel >= %{tdb_version}
BuildRequires:  libtevent-devel >= %{tevent_version}
BuildRequires:  libxslt
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  python3-talloc >= %{talloc_version}
BuildRequires:  python3-talloc-devel >= %{talloc_version}
BuildRequires:  python3-tdb >= %{tdb_version}
BuildRequires:  python3-tevent >= %{tevent_version}
%if 0%{?suse_version} >= 1330
BuildRequires:  libtirpc-devel
%endif
%if %{with_lmdb}
BuildRequires:  lmdb-devel >= %{lmdb_version}
%endif

URL:            https://ldb.samba.org/
Version:        2.9.1
Release:        0
Summary:        An LDAP-like embedded database
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Source:         https://download.samba.org/pub/ldb/ldb-%{version}.tar.gz
Source1:        https://download.samba.org/pub/ldb/ldb-%{version}.tar.asc
Source2:        ldb.keyring
Source4:        baselibs.conf
Patch0:         ldb-python3.5-fix-soabi_name.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LDB is an LDAP-like embedded database.

%package -n libldb2
Summary:        An LDAP-like embedded database
Group:          System/Libraries
Obsoletes:      libldb1 < %{version}

%description -n libldb2
LDB is an LDAP-like embedded database.

This package includes the ldb2 library.

%package -n libldb-devel
Summary:        Libraries and Header Files to Develop Programs with ldb2 Support
Group:          Development/Libraries/C and C++
Requires:       libldb2 = %{version}
Requires:       pkg-config

%description -n libldb-devel
LDB is an LDAP-like embedded database.

Libraries and Header Files to Develop Programs with ldb2 Support.

%package -n ldb-tools
Summary:        Tools to manipulate LDB files
Group:          Development/Libraries/C and C++

%description -n ldb-tools
Tools to manipulate LDB files.

%package -n python3-ldb
Summary:        Python3 bindings for the LDB library
Group:          Development/Libraries/Python
Requires:       libldb2 = %{version}
Obsoletes:      python-ldb

%description -n python3-ldb
This package contains the python3 bindings for the LDB library.

%package -n python3-ldb-devel
Summary:        Development files for the Python3 bindings for the LDB library
Group:          Development/Libraries/Python
Requires:       pkg-config
Requires:       python3-ldb = %{version}
Obsoletes:      python-ldb-devel

%description -n python3-ldb-devel
This package contains the development files for the Python bindings for the
LDB library.

%prep
%setup -n ldb-%{version} -q
%autopatch -p1

%build
%if 0%{?suse_version} > 1110
	export SUSE_ASNEEDED=0
%endif
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -DIDMAP_RID_SUPPORT_TRUSTED_DOMAINS"
%define bundled_libs cmocka
%if 0%{?suse_version} > 1500
%ifnarch ppc
	%define bundled_libs NONE
%endif
%endif

export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -DIDMAP_RID_SUPPORT_TRUSTED_DOMAINS"
CONFIGURE_OPTIONS="\
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath \
	--disable-rpath-install \
	--disable-silent-rules \
	--with-modulesdir=%{_libdir}/ldb2/modules \
	--with-privatelibdir=%{_libdir}/ldb2 \
	--bundled-libraries=%{bundled_libs} \
	--builtin-libraries=replace \
%if !%{with_lmdb}
	--without-ldb-lmdb \
%endif
"
./configure ${CONFIGURE_OPTIONS}
make %{?_smp_mflags} \
	all
doxygen Doxyfile
# remove man page with bogus full build dir in path
rm -f apidocs/man/man3/_*_ldb-%{version}_include_.3

%check
%if %{with_lmdb}
LD_LIBRARY_PATH="bin/shared:bin/shared/private" \
LDB_MODULES_PATH="bin/modules" \
make test
%endif

%install
%make_install

# Install API documentation
cp -a apidocs/man/* %{buildroot}/%{_mandir}

sed -i 's;-lpyldb-util.%{py3_soflags_dash};-lpyldb-util.%{py3_soflags};g' %{buildroot}/%{_libdir}/pkgconfig/pyldb-util.%{py3_soflags}.pc

%post -n libldb2 -p /sbin/ldconfig

%postun -n libldb2 -p /sbin/ldconfig

%post -n python3-ldb -p /sbin/ldconfig

%postun -n python3-ldb -p /sbin/ldconfig

%files -n libldb2
%defattr(-,root,root)
%{_libdir}/libldb.so.2*
%dir %{_libdir}/ldb2
%{_libdir}/ldb2/libldb-key-value.so
%{_libdir}/ldb2/libldb-tdb-err-map.so
%{_libdir}/ldb2/libldb-tdb-int.so
%dir %{_libdir}/ldb2/modules
%dir %{_libdir}/ldb2/modules/ldb
%{_libdir}/ldb2/modules/ldb/asq.so
%{_libdir}/ldb2/modules/ldb/paged_searches.so
%{_libdir}/ldb2/modules/ldb/rdn_name.so
%{_libdir}/ldb2/modules/ldb/sample.so
%{_libdir}/ldb2/modules/ldb/server_sort.so
%{_libdir}/ldb2/modules/ldb/skel.so
%{_libdir}/ldb2/modules/ldb/tdb.so
%{_libdir}/ldb2/modules/ldb/ldb.so
%if 0%{?suse_version} <= 1500
%{_libdir}/ldb2/libcmocka-ldb.so
%endif
%ifarch ppc
%{_libdir}/ldb2/libcmocka-ldb.so
%endif
%if %{with_lmdb}
%{_libdir}/ldb2/libldb-mdb-int.so
%{_libdir}/ldb2/modules/ldb/mdb.so
%endif

%files -n libldb-devel
%defattr(-,root,root)
%{_includedir}/ldb.h
%{_includedir}/ldb_errors.h
%{_includedir}/ldb_handlers.h
%{_includedir}/ldb_module.h
%{_includedir}/ldb_version.h
%{_libdir}/libldb.so
%{_libdir}/pkgconfig/ldb.pc
%{_mandir}/man3/ldb*.3.*
%{_mandir}/man3/ldif*.3.*

%files -n ldb-tools
%defattr(-,root,root)
%{_bindir}/ldbadd
%{_bindir}/ldbdel
%{_bindir}/ldbedit
%{_bindir}/ldbmodify
%{_bindir}/ldbrename
%{_bindir}/ldbsearch
%{_libdir}/ldb2/libldb-cmdline.so
%{_mandir}/man1/ldbadd.1.*
%{_mandir}/man1/ldbdel.1.*
%{_mandir}/man1/ldbedit.1.*
%{_mandir}/man1/ldbmodify.1.*
%{_mandir}/man1/ldbrename.1.*
%{_mandir}/man1/ldbsearch.1.*

%files -n python3-ldb
%defattr(-,root,root)
%{_libdir}/libpyldb-util.%{py3_soflags}.so.*
%{python3_sitearch}/_ldb_text.py
%if 0%{?centos_version} > 599 || 0%{?fedora_version} > 11 || 0%{?rhel_version} > 599
%{python3_sitearch}/__pycache__/_ldb_text.cpython-*.py[co]
%endif
%{python3_sitearch}/ldb.%{py3_soflags}.so

%files -n python3-ldb-devel
%defattr(-,root,root)
%{_includedir}/pyldb.h
%{_libdir}/libpyldb-util.%{py3_soflags}.so
%{_libdir}/pkgconfig/pyldb-util.%{py3_soflags}.pc
%{_mandir}/man3/PyLdb*.3.*

%changelog
