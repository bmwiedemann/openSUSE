#
# spec file for package cddlib
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


Name:           cddlib
%define lname   libcdd0
Version:        0.94m
Release:        0
Summary:        Library for finding vertices of convex polytopes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.inf.ethz.ch/personal/fukudak/cdd_home/

Source:         https://github.com/cddlib/cddlib/releases/download/%version/%name-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gmp-devel >= 3

%description
cddlib is a C implementation of the Double Description Method of
Motzkin et al. for generating all vertices (i.e. extreme points) and
extreme rays of a general convex polyhedron in R^d given by a system
of linear inequalities.

%package -n %lname
Summary:        Library for finding vertices of convex polytopes
Group:          System/Libraries

%description -n %lname
cddlib is a C implementation of the Double Description Method of
Motzkin et al. for generating all vertices (i.e. extreme points) and
extreme rays of a general convex polyhedron in R^d given by a system
of linear inequalities.

%package devel
Summary:        Header files for cddlib
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       gmp-devel

%description devel
cddlib is a C implementation of the Double Description Method of
Motzkin et al. for generating all vertices (i.e. extreme points) and
extreme rays of a general convex polyhedron in R^d given by a system
of linear inequalities.

This package contains the headers for the C library.

%package doc
Summary:        Documentation for the cddlib API
Group:          Documentation/Other
BuildArch:      noarch

%description doc
cddlib is an implementation of the Double Description Method of
Motzkin et al.

This package contains the documentation to cddlib.

%package tools
Summary:        Programs for vertex generation using Double Description Method
Group:          Productivity/Scientific/Math
Provides:       cddlib-devel:/usr/bin/scdd
Conflicts:      cddlib-devel < 0.94l

%description tools
cddlib is a C implementation of the Double Description Method of
Motzkin et al. for generating all vertices (i.e. extreme points) and
extreme rays of a general convex polyhedron in R^d given by a system
of linear inequalities.

This package contains the command-line utilities of cddlib.

%prep
%autosetup -p1

%build
%configure --enable-shared --disable-static --docdir="%_docdir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libcdd*.so.*

%files devel
%_libdir/libcdd*.so
%_includedir/*
%_libdir/pkgconfig/*.pc

%files doc
%_docdir/%name/

%files tools
%_bindir/*
%license COPYING

%changelog
