#
# spec file for package cxsc
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


Name:           cxsc
%define lname   libcxsc2
Version:        2.5.4
Release:        0
Summary:        C++ library for Extended Scientific Computing (XSC)
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            http://www2.math.uni-wuppertal.de/wrswt/xsc/cxsc_new.html

Source:         http://www2.math.uni-wuppertal.de/wrswt/xsc/cxsc/cxsc-2-5-4.tar.gz
Patch1:         cxsc-libversion.diff
BuildRequires:  autoconf
BuildRequires:  automake >= 1.11
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
C-XSC is a libary for the development of numerical algorithms that
deliver highly accurate and automatically verified results. C-XSC can
do real, complex, interval, and complex interval arithmetic with
mathematically defined properties, dynamic vectors and matrices,
accurate dot products, predefined arithmetic operators with highest
accuracy, standard functions of high accuracy, dynamic
multiple-precision arithmetic and rounding control for the input and
output of data.

%package -n %lname
Summary:        C++ library for Extended Scientific Computing (XSC)
Group:          System/Libraries

%description -n %lname
C-XSC is a libary for the development of numerical algorithms that
deliver highly accurate and automatically verified results. C-XSC can
do real, complex, interval, and complex interval arithmetic with
mathematically defined properties, dynamic vectors and matrices,
accurate dot products, predefined arithmetic operators with highest
accuracy, standard functions of high accuracy, dynamic
multiple-precision arithmetic and rounding control for the input and
output of data.

%package devel
Summary:        Development files for Lattice Basis Reduction with cxsc
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
C-XSC is a libary for the development of numerical algorithms that
deliver highly accurate and automatically verified results.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%setup -qn %name-2-5-4
%patch -P 1 -p1
find . -name tmain -exec chmod a+x "{}" "+"

%build
mkdir -p m4
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_libexecdir/%name/
%doc docu/COPYING

%files -n %lname
%_libdir/libcxsc.so.2
%_libdir/libcxsc.so.%version

%files devel
%_includedir/%name/
%_libdir/libcxsc.so

%changelog
