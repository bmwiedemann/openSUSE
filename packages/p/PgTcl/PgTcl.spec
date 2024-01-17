#
# spec file for package PgTcl
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


Name:           PgTcl
BuildRequires:  postgresql-devel
BuildRequires:  tcl-devel
Summary:        Tcl Client Library for PostgreSQL
License:        MIT
Version:        1.7
Release:        0
Url:            http://pgfoundry.org/projects/pgtcl/
Source0:        libpgtcl-%version.tar.gz
Patch0:         pgtcl-stubs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the libpgtcl client library as a loadable Tcl
package. It is needed to access PostgreSQL databases from Tcl scripts.

%prep
%setup -q -n libpgtcl-%version
%patch0 -p 1

%build
CFLAGS=-DUSE_INTERP_ERRORLINE
%configure \
        --libdir=%tcl_archdir \
	--with-tcl=%_libdir \
	--with-postgres-include=%_includedir/pgsql \
	--with-postgres-lib=%_libdir
make %{?_smp_mflags}

%install
make install-binaries install-libraries PKG_HEADERS= DESTDIR=%buildroot

%files
%defattr(-,root,root,-)
%doc ChangeLog README README.async TODO
%doc doc/PGTCL-NOTES doc/libpgtcl.pdf doc/html
%tcl_archdir

%changelog
