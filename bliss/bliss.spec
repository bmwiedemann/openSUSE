#
# spec file for package bliss
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


Name:           bliss
%define lname   libbliss-0_73
Version:        0.73
Release:        0
Summary:        A Tool for Computing Automorphism Groups and Canonical Labelings of Graphs
License:        LGPL-3.0
Group:          Productivity/Scientific/Math
Url:            http://www.tcs.hut.fi/Software/bliss/

Source:         http://www.tcs.hut.fi/Software/bliss/%name-%version.zip
Patch1:         bliss-am.diff
Patch2:         bliss-nodate.diff
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bliss is a tool for computing automorphism groups and canonical forms
of graphs. It has both a command line user interface as well as C++
and C programming language APIs.

%package -n %lname
Summary:        Library for computing automorphism groups and canonical forms of graphs
Group:          System/Libraries

%description -n %lname
bliss is a tool for computing automorphism groups and canonical forms
of graphs.

%package devel
Summary:        Development files for bliss, a math library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
bliss is a tool for computing automorphism groups and canonical forms
of graphs.

This subpackage contains libraries and header files for developing
applications that want to make use of the Bliss library.

%prep
%setup -q
%patch -P 1 -P 2 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING*
%_bindir/bliss*

%files -n %lname
%defattr(-,root,root)
%_libdir/libbliss-0.73.so
%_libdir/libbliss_gmp-0.73.so

%files devel
%defattr(-,root,root)
%_libdir/libbliss.so
%_libdir/libbliss_gmp.so
%_includedir/bliss/

%changelog
