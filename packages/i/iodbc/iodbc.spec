#
# spec file for package iodbc
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           iodbc
Version:        3.52.14
Release:        0
Summary:        ODBC compliant driver manager
License:        LGPL-2.0 or BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.iodbc.org/
Source:         https://download.sourceforge.net/iodbc/libiodbc-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-nonvoid-return.diff -- https://github.com/openlink/iODBC/issues/58
Patch0:         fix-nonvoid-return.diff
BuildRequires:  pkgconfig(gtk+-2.0)

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

%package -n libiodbc-devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libiodbc3 = %{version}
Requires:       libdrvproxy2 = %{version}
Requires:       libiodbcadm2 = %{version}
Requires:       pkgconfig(gtk+-2.0)

%description -n libiodbc-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libiodbc3
Summary:        Libraries needed to run iODBC
Group:          Development/Libraries/C and C++

%description -n libiodbc3
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package provides the shared libraries needed by iODBC

%package -n libdrvproxy2
Summary:        Administration library for iODBC
Group:          Development/Libraries/C and C++

%description -n libdrvproxy2
This package provides libdrvproxy for administering iODBC

%package -n libiodbcadm2
Summary:        Administration library for iODBC
Group:          Development/Libraries/C and C++

%description -n libiodbcadm2
This package provides libiodbcadm for administering iODBC

%package admin
Summary:        Administration tools for iODBC
Group:          Development/Libraries/C and C++

%description admin
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package provides tools for configuring and administering iODBC

%prep
%setup -q -n libiodbc-%{version}
%patch0 -p1

%build
%configure \
    --disable-static \
    --disable-libodbc \
    --disable-dependency-tracking

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libiodbc3 -p /sbin/ldconfig
%postun -n libiodbc3 -p /sbin/ldconfig
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

%files -n libiodbc3
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
