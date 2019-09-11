#
# spec file for package mpfi
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mpfi
%define lname	libmpfi0
Version:        1.5.3
Release:        0
Summary:        Multi-precision floating-point interval arithmetic computation library
License:        LGPL-2.1+
Group:          Productivity/Scientific/Math
Url:            http://mpfi.gforge.inria.fr/

#SVN-Clone:	svn://scm.gforge.inria.fr/svnroot/mpfi/trunk
# Download depends on the file ID, not the filename!
Source:         https://gforge.inria.fr/frs/download.php/file/37331/mpfi-1.5.3.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gmp-devel >= 4.1.0
BuildRequires:  mpfr-devel >= 2.4.2
BuildRequires:  pkgconfig
PreReq:         %install_info_prereq

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
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags};

%check
make %{?_smp_mflags} check;

%install
b="%buildroot";
make install DESTDIR="$b";
rm -f "$b/%_libdir"/*.la;

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%post devel
%install_info --info-dir="%_infodir" "%_infodir/mpfi.info.gz"

%postun devel
%install_info_delete --info-dir="%_infodir" "%_infodir/mpfi.info.gz"

%files -n %lname
%defattr(-,root,root)
%_libdir/libmpfi.so.0*

%files devel
%defattr(-,root,root)
%_includedir/mpfi*.h
%_libdir/libmpfi.so
%_infodir/mpfi.info*

%changelog
