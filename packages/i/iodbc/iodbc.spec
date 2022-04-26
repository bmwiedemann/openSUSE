#
# spec file for package iodbc
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


Name:           iodbc
Version:        3.52.14
Release:        0
Summary:        ODBC compliant driver manager
License:        BSD-3-Clause OR LGPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://www.iodbc.org/
Source:         https://download.sourceforge.net/iodbc/libiodbc-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-nonvoid-return.diff -- https://github.com/openlink/iODBC/issues/58
Patch0:         fix-nonvoid-return.diff
BuildRequires:  pkgconfig(gtk+-2.0)

%description
The iODBC Driver Manager is an implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

%package -n libiodbc-devel
Summary:        Headers for iODBC
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libdrvproxy2 = %{version}
Requires:       libiodbc2 = %{version}
Requires:       libiodbcadm2 = %{version}
Requires:       pkgconfig(gtk+-2.0)

%description -n libiodbc-devel
This package contains headers for the iODBC Driver Manager.

%package -n libiodbc2
Summary:        Libraries needed to run iODBC
Group:          System/Libraries
Conflicts:      libiodbc3 <= 3.52.14

%description -n libiodbc2
The iODBC Driver Manager is an implementation of the SAG CLI andx
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package provides the shared libraries needed by iODBC.

%package -n libdrvproxy2
Summary:        Administration library for iODBC
Group:          System/Libraries

%description -n libdrvproxy2
This package provides libdrvproxy for administering iODBC

%package -n libiodbcadm2
Summary:        Administration library for iODBC
Group:          System/Libraries

%description -n libiodbcadm2
This package provides libiodbcadm for administering iODBC

%package admin
Summary:        Administration tools for iODBC
Group:          Development/Libraries/C and C++

%description admin
The iODBC Driver Manager is an implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package provides tools for configuring and administering iODBC.

%prep
%autosetup -n libiodbc-%{version} -p1

%build
%configure \
    --disable-static \
    --disable-libodbc \
    --disable-dependency-tracking

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libiodbc2 -p /sbin/ldconfig
%postun -n libiodbc2 -p /sbin/ldconfig
%post   -n libiodbcadm2 -p /sbin/ldconfig
%postun -n libiodbcadm2 -p /sbin/ldconfig
%post   -n libdrvproxy2 -p /sbin/ldconfig
%postun -n libdrvproxy2 -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/iodbctest
%{_bindir}/iodbctestw
%{_mandir}/man1/iodbctest.1*
%{_mandir}/man1/iodbctestw.1*

%files admin
%license LICENSE
%{_bindir}/iodbcadm-gtk
%{_mandir}/man1/iodbcadm-gtk.1*

%files -n libiodbc-devel
%license LICENSE LICENSE.LGPL LICENSE.BSD
%doc AUTHORS ChangeLog NEWS README
%doc etc/odbc.ini.sample
%doc etc/odbcinst.ini.sample
%{_bindir}/iodbc-config
%{_datadir}/libiodbc
%{_includedir}/iodbcext.h
%{_includedir}/iodbcinst.h
%{_includedir}/iodbcunix.h
%{_includedir}/isql.h
%{_includedir}/isqlext.h
%{_includedir}/isqltypes.h
%{_includedir}/odbcinst.h
%{_includedir}/sql.h
%{_includedir}/sqlext.h
%{_includedir}/sqltypes.h
%{_includedir}/sqlucode.h
%{_libdir}/libdrvproxy.so
%{_libdir}/libiodbc.so
%{_libdir}/libiodbcadm.so
%{_libdir}/libiodbcinst.so
%{_libdir}/pkgconfig/libiodbc.pc
%{_mandir}/man1/iodbc-config.1*

%files -n libiodbc2
%license LICENSE
%{_libdir}/libiodbc.so.*
%{_libdir}/libiodbcinst.so.*

%files -n libdrvproxy2
%license LICENSE
%{_libdir}/libdrvproxy.so.*

%files -n libiodbcadm2
%license LICENSE
%{_libdir}/libiodbcadm.so.*

%changelog
