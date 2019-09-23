#
# spec file for package librsb
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           librsb
%define lname	librsb0
%define rversion	1.2.0-rc7
Version:        1.2.0~rc7
Release:        0
Summary:        Shared memory parallel sparse matrix and sparse BLAS library
License:        LGPL-3.0+
Group:          Productivity/Scientific/Math
Url:            http://librsb.sf.net/

Source:         http://downloads.sf.net/%name/%name-%rversion.tar.gz
Patch1:         pun.diff
Patch2:         reproducible.patch
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  gsl-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -qn librsb-%rversion
%patch -P 1 -p1
%patch2 -p1

%build
%configure --docdir="%_docdir/%name" --disable-static CFLAGS="%optflags -Wno-unused" \
    --with-memhinfo=L3:16/64/8192K,L2:16/64/2048K,L1:8/64/16K
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/librsb.so.0*

%files devel
%defattr(-,root,root)
%_includedir/*
%_bindir/rsbench
%_bindir/librsb-config
%_libdir/librsb.so
%_docdir/%name/
%doc COPYING

%changelog
