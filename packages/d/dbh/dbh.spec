#
# spec file for package dbh
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


Name:           dbh
%define lname	lib%{name}2
Summary:        Disk-Based Hash Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Version:        5.0.22
Release:        0
Url:            https://www.gnu.org/software/libdbh/

Source:         https://downloads.sf.net/dbh/%{lname}-%{version}.tar.gz
Patch0:         dbh-bigendian.patch
# PATCH-FIX-OPENSUSE -- bmwiedemann - make builds reproducible
Patch1:         reproducible.patch
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
Disk-based hashes is a method to create multidimensional binary trees
on disk. This library permits the extension of the database concept to
a plethora of electronic data, such as graphic information. With the
multidimensional binary tree, it is possible to mathematically prove
that access time to any particular record is minimized (using the
concept of critical points from calculus), which provides the means to
construct optimized databases for particular applications.

%package -n %lname
Summary:        Disk-Based Hash Library
Group:          System/Libraries
Obsoletes:      dbh < %version-%release
Provides:       dbh = %version-%release

%description -n %lname
Disk-based hashes is a method to create multidimensional binary trees
on disk. This library permits the extension of the database concept to
a plethora of electronic data, such as graphic information. With the
multidimensional binary tree, it is possible to mathematically prove
that access time to any particular record is minimized (using the
concept of critical points from calculus), which provides the means to
construct optimized databases for particular applications.

%package devel
Summary:        Development files for the Disk-Based Hash Library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Disk-based hashes is a method to create multidimensional binary trees
on disk. This library permits the extension of the database concept to
a plethora of electronic data, such as graphic information. With the
multidimensional binary tree, it is possible to mathematically prove
that access time to any particular record is minimized (using the
concept of critical points from calculus), which provides the means to
construct optimized databases for particular applications.

%prep
%setup -q -n %{lname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_datadir}/dbh
# create symlinks for man pages
%fdupes -s %buildroot/%_mandir
%fdupes -s examples

%check
make check

%files -n %lname
%_libdir/lib*.so.*

%files devel
%doc AUTHORS ChangeLog README examples/*.c examples/Makefile*
%license COPYING
%{_datadir}/gtk-doc
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.*

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%changelog
