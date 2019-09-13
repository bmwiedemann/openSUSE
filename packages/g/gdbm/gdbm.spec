#
# spec file for package gdbm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname	libgdbm6
%define lcompat libgdbm_compat4
Name:           gdbm
Version:        1.18.1
Release:        0
Summary:        GNU dbm key/data database
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/gdbm/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        baselibs.conf
Source4:        %{name}.keyring
# PATCH-FIX-SUSE: remove the build date from src/version.c
Patch4:         gdbm-no-build-date.patch
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  readline-devel
%lang_package

%description
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

The basic use of GDBM is to store key/data pairs in a data file. Each
key must be unique and each key is paired with only one data item.

The library provides primitives for storing key/data pairs, searching
and retrieving the data by its key and deleting a key along with its
data. It also supports sequential iteration over all key/data pairs in
a database.

%package -n %{lname}
Summary:        GNU dbm key/data database
License:        GPL-3.0-or-later
Group:          System/Libraries
Recommends:     %{name}-lang = %{version}
# O/P added in 12.2
Obsoletes:      gdbm < %{version}-%{release}
Provides:       gdbm = %{version}-%{release}

%description -n %{lname}
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

The basic use of GDBM is to store key/data pairs in a data file. Each
key must be unique and each key is paired with only one data item.

The library provides primitives for storing key/data pairs, searching
and retrieving the data by its key and deleting a key along with its
data. It also supports sequential iteration over all key/data pairs in
a database.

%package -n %{lcompat}
Summary:        GNU dbm key/data database compat wrapper
License:        GPL-3.0-or-later
Group:          System/Libraries
Recommends:     %{name}-lang = %{version}
# Was provided in older sonames
Conflicts:      libgdbm3

%description -n %{lcompat}
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

This library is providing compatibility wrappers.

%package devel
Summary:        Development files for the dbm key/data database library
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lcompat} = %{version}
Requires:       %{lname} = %{version}
Requires(pre):  %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q
%patch4 -p1

%build

%configure \
  --disable-static \
  --disable-silent-rules \
  --enable-libgdbm-compat \
  --enable-nls \
  --with-readline
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
echo "/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
GROUP ( %{_libdir}/libgdbm.so %{_libdir}/libgdbm_compat.so )" > %{buildroot}/%{_libdir}/libndbm.so

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n %{lcompat} -p /sbin/ldconfig
%postun -n %{lcompat} -p /sbin/ldconfig

%files lang -f %{name}.lang

%files -n %{lname}
%license COPYING
%{_libdir}/libgdbm.so.*

%files -n %{lcompat}
%license COPYING
%{_libdir}/libgdbm_compat.so.*

%files devel
%doc README NEWS
%{_bindir}/*
%{_includedir}/dbm.h
%{_includedir}/gdbm.h
%{_includedir}/ndbm.h
%{_infodir}/gdbm.info%{?ext_info}
%{_libdir}/libgdbm.so
%{_libdir}/libgdbm_compat.so
%{_libdir}/libndbm.so
%{_mandir}/man1/*%{ext_man}
%{_mandir}/man3/gdbm.3%{?ext_man}

%changelog
