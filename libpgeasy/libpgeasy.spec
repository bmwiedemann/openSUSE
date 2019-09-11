#
# spec file for package libpgeasy
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define 				lname %{name}3
Name:           libpgeasy
Version:        3.0.4
Release:        0
Summary:        Simplified C Client Interface for PostgreSQL
License:        BSD-3-Clause
Group:          Productivity/Databases/Clients
Url:            http://gborg.postgresql.org/project/pgeasy
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  krb5-devel
BuildRequires:  postgresql-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LIBPGEASY is a simplified C interface that hides some of the complexity
of LIBPQ.

%package -n %{lname}
Summary:        Simplified C Client Interface for PostgreSQL
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} = %{version}

%description -n %{lname}
LIBPGEASY is a simplified C interface that hides some of the complexity
of LIBPQ.

%package devel
Summary:        Development files for Simplified C Client Interface for PostgreSQL
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
LIBPGEASY is a simplified C interface that hides some of the complexity
of LIBPQ.

This subpackage contains the headers for libcec.

%prep
%setup -q

%build
%configure \
	--with-pqinclude=%{_includedir}/pgsql \
	--with-pqlib=%{_libdir} \
	--disable-static \
	--with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root,-)
%doc CHANGES README
%{_libdir}/libpgeasy.so.3*

%files devel
%defattr(-,root,root,-)
%doc CHANGES README docs/*.html examples
%{_libdir}/libpgeasy.so
%{_includedir}/libpgeasy.h

%changelog
