#
# spec file for package mpfi
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


Name:           mpfi
%define lname	libmpfi0
Version:        1.5.4
Release:        0
Summary:        Multi-precision floating-point interval arithmetic computation library
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            http://mpfi.gforge.inria.fr/

#SVN-Clone:	svn://scm.gforge.inria.fr/svnroot/mpfi/trunk
# Download depends on the file ID, not the filename!
Source:         https://gforge.inria.fr/frs/download.php/file/38111/mpfi-1.5.4.tgz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gmp-devel >= 4.1.0
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  mpfr-devel >= 3
BuildRequires:  pkgconfig
Requires(post): %install_info_prereq
Requires(postun): %install_info_prereq

%description
MPFI is a C library for arbitrary precision interval arithmetic with
intervals represented using MPFR reliable floating-point numbers.

The purpose of an arbitrary precision interval arithmetic is on the
one hand to get "guaranteed" results, thanks to interval computation,
and on the other hand to obtain accurate results, thanks to multiple
precision arithmetic.

%package -n %lname
Summary:        Multi-precision floating-point interval arithmetic computation library
Group:          System/Libraries

%description -n %lname
MPFI is a C library for arbitrary precision interval arithmetic with
intervals represented using MPFR reliable floating-point numbers.

The purpose of an arbitrary precision interval arithmetic is on the
one hand to get "guaranteed" results, thanks to interval computation,
and on the other hand to obtain accurate results, thanks to multiple
precision arithmetic.

%package devel
Summary:        Development files for the MPFI interval arithmetic computation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
MPFI is a C library for arbitrary precision interval arithmetic with
intervals represented using MPFR reliable floating-point numbers.

This subpackage provides the development headers and libraries for it.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
#make check #upstream broke it in 1.5.4

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%post devel
%install_info --info-dir="%_infodir" "%_infodir/mpfi.info.gz"

%postun devel
%install_info_delete --info-dir="%_infodir" "%_infodir/mpfi.info.gz"

%files -n %lname
%_libdir/libmpfi.so.0*

%files devel
%_includedir/mpfi*.h
%_libdir/libmpfi.so
%_infodir/mpfi.info*

%changelog
