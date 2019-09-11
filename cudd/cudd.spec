#
# spec file for package cudd
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


Name:           cudd
%define lname	libcudd-3_0_0-0
Version:        3.0.0
Release:        0
Summary:        Manipulation of Binary Decision Diagrams
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
Url:            http://vlsi.colorado.edu/~fabio/

Source:         ftp://vlsi.colorado.edu/pub/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++

%description
CUDD is a package for the manipulation of Binary Decision Diagrams
(BDDs), Algebraic Decision Diagrams (ADDs) and Zero-suppressed Binary
Decision Diagrams (ZDDs).

%package -n %lname
Summary:        CUDD libraries
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
%setup -q

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
b="%buildroot"
make %{?_smp_mflags} install DESTDIR="$b"
rm -f "$b/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc LICENSE
%_libdir/libcudd*.so.0*

%files devel
%defattr(-,root,root)
%_includedir/cudd*
%_libdir/libcudd*.so

%changelog
