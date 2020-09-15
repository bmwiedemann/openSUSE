#
# spec file for package 4ti2
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


Name:           4ti2
Version:        1.6.9
Release:        0
Summary:        Package for algebraic, geometric and combinatorial problems on linear spaces
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://4ti2.github.io/

Source:         https://github.com/4ti2/4ti2/releases/download/Release_1_6_9/4ti2-1.6.9.tar.gz
Patch1:         4ti2-docdir.diff
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  gcc-c++ >= 4.3
BuildRequires:  glpk-devel >= 4.52
BuildRequires:  gmp-devel >= 4.1.4
BuildRequires:  libtool

%description
4ti2 is a collection of programs that compute and solve algebraic,
geometric and combinational problems on linear spaces.

%package -n lib4ti2-0
Summary:        Library for computation of Gröbner bases with 4ti2
Group:          System/Libraries

%description -n lib4ti2-0
This package contains the 4ti2 program library, which comes in three
flavors:
- 32-bit precision integers
- 64-bit precision integers
- arbitrary precision integer support through use of GNU MP

%package -n libzsolve0
Summary:        Library for solving linear systems over integers for 4ti2
Group:          System/Libraries

%description -n libzsolve0
This package contains the 4ti2 library for solving systems linear systems over
integers (\mathbb{Z}).

%package devel
Summary:        Development files for 4ti2
Group:          Development/Libraries/C and C++
Requires:       lib4ti2-0 = %version
Requires:       libzsolve0 = %version

%description devel
This subpackage contains the include files and library links for
developing against 4ti2's libraries.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --enable-shared --disable-static \
	--includedir="%_includedir/%name" --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
%make_install
b="%buildroot"
rm -f "$b/%_libdir"/*.la
mkdir -p "$b/%_bindir" "$b/%_libexecdir/%name"
mv "$b/%_bindir"/* "$b/%_libexecdir/%name/"
pushd "$b/%_libexecdir/%name"
for i in *; do
	ln -s "%_libexecdir/%name/$i" "$b/%_bindir/4ti2_$i"
done

%post   -n lib4ti2-0 -p /sbin/ldconfig
%postun -n lib4ti2-0 -p /sbin/ldconfig
%post   -n libzsolve0 -p /sbin/ldconfig
%postun -n libzsolve0 -p /sbin/ldconfig

%files
%license COPYING
%doc doc/[34a-z]*
%_bindir/4ti2*
%_libexecdir/%name/

%files -n lib4ti2-0
%_libdir/lib4ti2gmp.so.0*
%_libdir/lib4ti2int32.so.0*
%_libdir/lib4ti2int64.so.0*
%_libdir/lib4ti2common.so.0*
%_libdir/lib4ti2util.so.0*

%files -n libzsolve0
%_libdir/libzsolve.so.0*

%files devel
%_includedir/%name/
%_libdir/lib*.so

%changelog
