#
# spec file for package flint
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


%define version_unconverted 2.6.3

Name:           flint
%define lname	libflint14
Version:        2.6.3
Release:        0
Summary:        C library for doing number theory
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            http://flintlib.org/

#Git-Clone:     https://github.com/wbhart/flint2
Source:         %name-%version.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 5
BuildRequires:  libtool
BuildRequires:  mpfr-devel >= 3
BuildRequires:  ntl-devel
BuildRequires:  xz

%description
FLINT (Fast Library for Number Theory) is a C library in support of
computations in number theory. It is also a research project into
algorithms in number theory. At this stage, FLINT consists mainly of
fast integer and polynomial arithmetic and linear algebra.

%package -n %lname
Summary:        C library for doing number theory
Group:          System/Libraries

%description -n %lname
FLINT (Fast Library for Number Theory) is a C library in support of
computations in number theory. It is also a research project into
algorithms in number theory. At this stage, FLINT consists mainly of
fast integer and polynomial arithmetic and linear algebra.

%package devel
Summary:        Development files for flint
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
FLINT (Fast Library for Number Theory) is a C library in support of
computations in number theory. It is also a research project into
algorithms in number theory. At this stage, FLINT consists mainly of
fast integer and polynomial arithmetic and linear algebra.

This subpackage contains the include files and library links for
developing against the FLINT library.

%prep
%autosetup -p1

%build
./configure --prefix="%_prefix" --disable-static --reentrant --with-ntl \
	CFLAGS="%optflags" CXXFLAGS="%optflags"
make %{?_smp_mflags} VERBOSE=1

%install
%make_install LIBDIR="%_lib"
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libflint.so.14*
%license LICENSE

%files devel
%_includedir/flint/
%_libdir/libflint.so
%doc NEWS

%changelog
