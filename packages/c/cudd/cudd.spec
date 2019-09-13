#
# spec file for package cudd
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


Name:           cudd
%define lname	libcudd-3_0_0-0
Version:        3.0.0
Release:        0
Summary:        Binary Decision Diagram manipulation library
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            http://vlsi.colorado.edu/~fabio/

#Source:         ftp://vlsi.colorado.edu/pub/%name-%version.tar.gz (website shutdown)
Source:         %name-%version.tar.gz
BuildRequires:  gcc-c++

%description
CUDD (Colorado University Decision Diagram) is a package for the
manipulation of Binary Decision Diagrams (BDDs), Algebraic Decision
Diagrams (ADDs) and Zero-suppressed Binary Decision Diagrams (ZDDs).

%package -n %lname
Summary:        Binary Decision Diagram manipulation library
Group:          System/Libraries

%description -n %lname
CUDD is a package for the manipulation of Binary Decision Diagrams
(BDDs), Algebraic Decision Diagrams (ADDs) and Zero-suppressed Binary
Decision Diagrams (ZDDs).

%package devel
Summary:        Development files for CUDD, a package for Binary Decision Diagram manipulation
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
CUDD is a package for the manipulation of Binary Decision Diagrams
(BDDs), Algebraic Decision Diagrams (ADDs) and Zero-suppressed Binary
Decision Diagrams (ZDDs).

This subpackage contains the include files and library links for
developing against cudd's libraries.

%prep
%autosetup -p1

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE
%_libdir/libcudd*.so.0*

%files devel
%_includedir/cudd*
%_libdir/libcudd*.so

%changelog
