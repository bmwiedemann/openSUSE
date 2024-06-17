#
# spec file for package freetds
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


Name:           freetds
Version:        1.4.17
Release:        0
Summary:        A free re-implementation of the TDS (Tabular Data Stream) protocol
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.freetds.org/
Source:         https://www.freetds.org/files/stable/freetds-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         configure-return-void-fix.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(nettle)
Requires:       glibc-locale

%description
FreeTDS is a project to document and implement the TDS (Tabular Data Stream)
protocol. TDS is used by Sybase and Microsoft for client to database server
communications. FreeTDS includes call level interfaces for DB-Lib, CT-Lib,
and ODBC.

%package config
Summary:        A free re-implementation of the TDS (Tabular Data Stream) protocol
License:        LGPL-2.1-or-later
Obsoletes:      libfreetds < %{version}
Provides:       %{name} = %{version}
Provides:       libfreetds = %{version}
Obsoletes:      %{name} < %{version}

%description config
FreeTDS is a project to document and implement the TDS (Tabular Data Stream)
protocol. TDS is used by Sybase and Microsoft for client to database server
communications.

This subpackage contains default configuration files and documentation for
them.

%package    tools
Summary:        Applications for working with the TDS (Tabular Data Stream) protocol
License:        GPL-2.0-or-later AND LGPL-2.1-or-later

%description tools
FreeTDS is a project to document and implement the TDS (Tabular Data Stream)
protocol. TDS is used by Sybase and Microsoft for client to database server
communications. FreeTDS includes call level interfaces for DB-Lib, CT-Lib,
and ODBC.

This package provides application to allow users to make use of the protocol.

%package    devel
Summary:        Include files needed for development with FreeTDS
License:        LGPL-2.1-or-later
Requires:       libct4 = %{version}
Requires:       libsybdb5 = %{version}
Requires:       libtdsodbc0 = %{version}

%description devel
The freetds-devel package contains the files necessary for development with
the FreeTDS libraries.

%package -n libct4
Summary:        FreeTDS standalone driver with modern API
License:        LGPL-2.1-or-later

%description -n libct4
ct-lib refers to Sybase's second-generation API, which fixes a number
of implementation and conceptual gaps in db-lib (libsybdb). libct is
not the most complete implementation yet.

%package -n libsybdb5
Summary:        FreeTDS standalone driver with classic API
License:        LGPL-2.1-or-later

%description -n libsybdb5
db-lib is the oldest and simplest API, and the only API supported by
both vendors, which has some relevance when porting applications that
use the vendors' libraries. db-lib was the first API implemented by
FreeTDS, and is still the best one supported. Anything that can be
done in FreeTDS can be done through db-lib.

%package    -n libtdsodbc0
Summary:        FreeTDS ODBC Driver for unixODBC
License:        LGPL-2.1-or-later
Requires:       unixODBC >= 2.0.0

%description -n libtdsodbc0
The ODBC drivers is the FreeTDS's project most recent addition. Its
chief advantage is that it makes FreeTDS servers look like other ODBC
servers, a big help to people who know ODBC and/or write applications
for several kinds of servers.

%package    doc
Summary:        User documentation for FreeTDS
License:        GPL-2.0-or-later AND LGPL-2.1-or-later

%description doc
The freetds-doc package contains the useguide and reference of FreeTDS
and can be installed even if FreeTDS main package is not installed

%prep
%autosetup -p1

%build
%configure \
  --with-unixodbc=%{_prefix} \
  --enable-threadsafe \
  --enable-krb5 \
  --sysconfdir=%{_sysconfdir} \
  --with-tdsver=auto \
  --disable-static \
%if 0%{?suse_version} >= 1310
  --with-gnutls \
%endif
  --with-pic
%make_build RPM_OPT_FLAGS="%{optflags}"

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# Fix docu location
install -d %{buildroot}%{_docdir}/freetds
mv %{buildroot}%{_datadir}/doc/freetds/* %{buildroot}%{_docdir}/freetds/
rm -rf %{buildroot}%{_docdir}/freetds* %{buildroot}%{_datadir}/doc/freetds-*
# Fix permissions
find %{buildroot}%{_datadir}     -type f -print0 | xargs -0 chmod -x
find %{buildroot}%{_sysconfdir}  -type f -print0 | xargs -0 chmod -x

%fdupes %{buildroot}/%{_prefix}

%post   -n libct4 -p /sbin/ldconfig
%postun -n libct4 -p /sbin/ldconfig
%post   -n libsybdb5 -p /sbin/ldconfig
%postun -n libsybdb5 -p /sbin/ldconfig

%post -n libtdsodbc0
echo "[FreeTDS]
Description = FreeTDS unixODBC Driver
Driver = %{_libdir}/libtdsodbc.so.0
Setup = %{_libdir}/libtdsodbc.so.0" | odbcinst -i -d -r || true
echo "[SQL Server]
Description = FreeTDS unixODBC Driver
Driver = %{_libdir}/libtdsodbc.so.0
Setup = %{_libdir}/libtdsodbc.so.0" | odbcinst -i -d -r || true
/sbin/ldconfig

%postun -n libtdsodbc0 -p /sbin/ldconfig

%preun -n libtdsodbc0
odbcinst -u -d -n 'FreeTDS'
odbcinst -u -d -n 'SQL Server'

%files config
%config %{_sysconfdir}/*
%{_mandir}/man5/*.5%{?ext_man}

%files tools
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files devel
%{_libdir}/*.so
%{_includedir}/*

%files -n libct4
%license COPYING*
%{_libdir}/libct.so.4*

%files -n libsybdb5
%license COPYING*
%{_libdir}/libsybdb.so.5*

%files -n libtdsodbc0
%license COPYING*
%{_libdir}/libtdsodbc.so.*

%files doc
%doc AUTHORS.md NEWS.md README.md TODO.md

%changelog
