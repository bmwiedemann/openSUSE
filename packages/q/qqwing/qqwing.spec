#
# spec file for package qqwing
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           qqwing
Version:        1.3.4
Release:        0
Summary:        Sudoku solver and generator
License:        GPL-2.0-or-later
Group:          Amusements/Games/Logic
Url:            http://ostermiller.org/qqwing/
Source:         http://ostermiller.org/qqwing/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE qqwing-help-compiler.patch dimstar@opensuse.org -- Help gcc to realize that this is all options for the switch statement
Patch0:         qqwing-help-compiler.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
QQwing is a Sudoku puzzle generator and solver. It offers the following features.

 * Fast. It can solve 1000 puzzles in 1 second and generate 1000 puzzles in 25 seconds.
 * Uses logic. Uses as many solve techniques as possible when solving puzzles rather than guessing.
 * Rates puzzles. Most generators don't give an indication of the difficulty of a Sudoku puzzle. QQwing does.
 * Can print solve instructions. Tells steps that need to be taken to solve any puzzle.
 * Customizable output style. Including a CSV style that is easy to import into a database.

%package -n libqqwing2
Summary:        Sudoku solver and generator
Group:          System/Libraries

%description -n libqqwing2
QQwing is a Sudoku puzzle generator and solver. It offers the following features.

 * Fast. It can solve 1000 puzzles in 1 second and generate 1000 puzzles in 25 seconds.
 * Uses logic. Uses as many solve techniques as possible when solving puzzles rather than guessing.
 * Rates puzzles. Most generators don't give an indication of the difficulty of a Sudoku puzzle. QQwing does.
 * Can print solve instructions. Tells steps that need to be taken to solve any puzzle.
 * Customizable output style. Including a CSV style that is easy to import into a database.

%package devel
Summary:        Sudoku solver and generator
Group:          Development/Languages/C and C++
Requires:       libqqwing2 = %{version}

%description devel
QQwing is a Sudoku puzzle generator and solver. It offers the following features.

 * Fast. It can solve 1000 puzzles in 1 second and generate 1000 puzzles in 25 seconds.
 * Uses logic. Uses as many solve techniques as possible when solving puzzles rather than guessing.
 * Rates puzzles. Most generators don't give an indication of the difficulty of a Sudoku puzzle. QQwing does.
 * Can print solve instructions. Tells steps that need to be taken to solve any puzzle.
 * Customizable output style. Including a CSV style that is easy to import into a database.

%prep
%setup -q
# Disable, needs rebase
#patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libqqwing2 -p /sbin/ldconfig
%postun -n libqqwing2 -p /sbin/ldconfig

%files
%{_bindir}/qqwing
%{_mandir}/man1/qqwing.1%{?ext_man}

%files -n libqqwing2
%license COPYING
%doc README
%{_libdir}/libqqwing.so.*

%files devel
%{_includedir}/qqwing.hpp
%{_libdir}/libqqwing.so
%{_libdir}/pkgconfig/qqwing.pc

%changelog
