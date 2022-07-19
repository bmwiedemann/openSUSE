#
# spec file for package librsb
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


Name:           librsb
%define lname	librsb0
Version:        1.3.0.1
Release:        0
Summary:        Shared memory parallel sparse matrix and sparse BLAS library
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://librsb.sf.net/

Source:         http://downloads.sf.net/%name/%name-%version.tar.gz
Source2:        http://downloads.sf.net/%name/%name-%version.tar.gz.asc
Source9:        %name.keyring
Patch1:         pun.diff
Patch2:         reproducible.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gsl-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel

%description
librsb is a library for sparse matrix computations featuring the
Recursive Sparse Blocks (RSB) matrix format. This format allows cache
efficient and multi-threaded (that is, shared memory parallel)
operations on large sparse matrices.

%package -n %lname
Summary:        Shared memory parallel sparse matrix and sparse BLAS library
Group:          System/Libraries

%description -n %lname
librsb is a library for sparse matrix computations featuring the
Recursive Sparse Blocks (RSB) matrix format. This format allows cache
efficient and multi-threaded (that is, shared memory parallel)
operations on large sparse matrices.

librsb implements the Sparse BLAS standard, as specified in the BLAS
Forum documents.

%package devel
Summary:        Development files for librsb, a Recursive Sparse Blocks matrix format lirary
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
librsb is a library for sparse matrix computations featuring the
Recursive Sparse Blocks (RSB) matrix format. This format allows cache
efficient and multi-threaded (that is, shared memory parallel)
operations on large sparse matrices.

This subpackage contains libraries and header files for developing
applications that want to make use of librsb.

%prep
%autosetup -p1

%build
autoreconf -fi
# meminfo chosen for smaller machines too
%configure --docdir="%_docdir/%name" --disable-static CFLAGS="%optflags -Wno-unused" \
    --with-memhinfo=L3:16/64/8192K,L2:16/64/2048K,L1:8/64/16K
%make_build -j1

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/librsb.so.0*

%files devel
%_includedir/*
%_bindir/rsbench
%_bindir/librsb-config
%_libdir/librsb.so
%_docdir/%name/
%license COPYING

%changelog
