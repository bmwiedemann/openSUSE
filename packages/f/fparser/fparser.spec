#
# spec file for package fparser
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fparser
%define lname	libfparser-4_5_2
Summary:        Library to evaluate strings as mathematical functions
License:        LGPL-3.0
Group:          Development/Libraries/C and C++
Version:        4.5.2
Release:        0
Url:            http://warp.povusers.org/FunctionParser/

Source:         http://warp.povusers.org/FunctionParser/%name%version.zip
Patch1:         fparser-build-system.diff
Patch2:         fparser-gmp-mpfr.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel >= 2.4
BuildRequires:  pkgconfig
BuildRequires:  unzip

%description
This C++ library offers a class which can be used to parse and
evaluate a mathematical function from a string (which might be e.g.
requested from the user). The syntax of the function string is
similar to mathematical expressions written in C/C++ (the exact
syntax is specified later in this document). The function can then be
evaluated with different values of variables.

%package -n %lname
Summary:        Library to evaluate strings as mathematical functions
Group:          System/Libraries

%description -n %lname
This C++ library offers a class which can be used to parse and
evaluate a mathematical function from a string (which might be e.g.
requested from the user). The syntax of the function string is
similar to mathematical expressions written in C/C++ (the exact
syntax is specified later in this document). The function can then be
evaluated with different values of variables.

%package devel
Summary:        Development files for libfparser
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This C++ library offers a class which can be used to parse and
evaluate a mathematical function from a string (which might be e.g.
requested from the user). The syntax of the function string is
similar to mathematical expressions written in C/C++ (the exact
syntax is specified later in this document). The function can then be
evaluated with different values of variables.

For example, a function like "sin(sqrt(x*x+y*y))" can be parsed from
a string (either std::string or a C-style string) and then evaluated
with different values of x and y. This library can be useful for
evaluating user-inputted functions, or in some cases interpreting
mathematical expressions in a scripting language.

%prep
%setup -q -c -n %name%version
ln -s mpfr fparser;
%patch -P 1 -P 2 -p1

%build
export CFLAGS="%optflags -DFP_SUPPORT_COMPLEX_NUMBERS"
export CXXFLAGS="$CFLAGS"
autoreconf -fi;
%configure --disable-static
make %{?_smp_mflags};

%install
make install DESTDIR="%buildroot";
rm -f "%buildroot/%_libdir"/*.la;

%files -n %lname
%defattr(-,root,root)
%_libdir/libfparser-*.so

%files devel
%defattr(-,root,root)
%_includedir/fparser*
%_libdir/libfparser.so
%_libdir/pkgconfig/*.pc

%changelog
