#
# spec file for package muparser
#
# Copyright (c) 2022 SUSE LLC
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


Name:           muparser
%define lname	libmuparser2_3_4
Version:        2.3.4
Release:        0
Summary:        A math parser library
License:        MIT
Group:          Productivity/Scientific/Math
URL:            http://muparser.beltoforion.de/
Source:         https://github.com/beltoforion/muparser/archive/v%version.tar.gz
Patch0:         muparser-abiversion.diff
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
muParser is an extensible math parser library written in C++. It
works by transforming a mathematical expression into bytecode and
precalculating constant parts of the expression.

%package -n %lname
Summary:        Library to evaluate strings as mathematical functions
Group:          System/Libraries

%description -n %lname
muParser is an extensible math parser library written in C++. It
works by transforming a mathematical expression into bytecode and
precalculating constant parts of the expression.

%package devel
Summary:        Development files for muparser
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
muParser is an extensible math parser library written in C++. It
works by transforming a mathematical expression into bytecode and
precalculating constant parts of the expression.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX="%_prefix"
%cmake_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libmuparser.so.2*
%license LICENSE

%files devel
%_includedir/muParser*.h
%_libdir/libmuparser.so
%_libdir/cmake/
%_libdir/pkgconfig/muparser.pc
%doc CHANGELOG

%changelog
