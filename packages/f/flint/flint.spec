#
# spec file for package flint
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define version_unconverted 3.0~5831

Name:           flint
%define lname	libflint0
Version:        3.0~5831
Release:        0
Summary:        C library for doing number theory
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Url:            http://flintlib.org/

Source:         %name-%version.tar.xz
Patch1:         0001-build-provide-autotools-files.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q
%patch -P 1 -p1

%build
chmod a+x *.sh
./autogen.sh
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%ifarch x86_64 %ix86
export CFLAGS="$CFLAGS -mno-popcnt"
export CXXFLAGS="$CXXFLAGS -mno-popcnt"
%endif
%configure --disable-static --with-ntl --enable-reentrant
make %{?_smp_mflags} V=0

%install
b="%buildroot";
%make_install DESTDIR="$b"
rm -f "$b/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libflint.so.0*
%doc gpl-2.0.txt

%files devel
%defattr(-,root,root)
%_includedir/flint/
%_libdir/libflint.so

%changelog
