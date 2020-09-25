#
# spec file for package antic
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


Name:           antic
%define lname	libantic0
Version:        0.2.2
Release:        0
Summary:        Algebraic Number Theory library in C
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/wbhart/antic/
Source:         https://github.com/wbhart/antic/archive/%version.tar.gz
BuildRequires:  flint-devel >= 2.6.3
BuildRequires:  flint-devel < 2.7
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel

%description
Antic is an algebraic number theory library.

%package -n %lname
Summary:        Algebraic Number Theory library in C
Group:          System/Libraries

%description -n %lname
Antic is an algebraic number theory library.

%package devel
Summary:        Development files for antic
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       flint-devel
Requires:       gmp-devel

%description devel
Antic is an algebraic number theory library.

This subpackage contains the include files and library links for
developing against the ANTIC library.

%prep
%autosetup -p1

%build
./configure --prefix="%_prefix" --disable-static \
	CFLAGS="%optflags"
%make_build QUIET_CC=""

%install
%make_install LIBDIR="%_lib"
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libantic.so.0*

%files devel
%_includedir/%name/
%_libdir/libantic.so
%license LICENSE

%changelog
