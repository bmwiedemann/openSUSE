#
# spec file for package primecount
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           primecount
Version:        7.13
Release:        0
Summary:        Count the number of primes
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/kimwalisch/primecount
Source0:        https://github.com/kimwalisch/primecount/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.7
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  asciidoc
BuildRequires:  libprimesieve-devel

%description
primecount is a command-line program that counts the primes below an
integer x ≤ 10^31 using highly optimized implementations of the
combinatorial prime counting algorithms.

%package -n libprimecount7
Summary:        C/C++ library for counting prime numbers

%description -n libprimecount7
This package contains the shared runtime library for primecount.

%package -n libprimecount-devel
Summary:        Development files for the primecount library
Requires:       libprimecount7 = %{version}

%description -n libprimecount-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primecount library.

%prep
%setup -q

%build
%cmake -DBUILD_LIBPRIMESIEVE=OFF \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_STATIC_LIBS=OFF \
       -DBUILD_MANPAGE=ON \
       -DBUILD_TESTS=ON \
       -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%post -n libprimecount7 -p /sbin/ldconfig
%postun -n libprimecount7 -p /sbin/ldconfig

%check
%ctest

%files
%doc README.md ChangeLog
%{_bindir}/primecount
%{_mandir}/man1/primecount.1%{?ext_man}

%files -n libprimecount7
%license COPYING
%{_libdir}/libprimecount.so.*

%files -n libprimecount-devel
%doc doc/libprimecount.md
%{_libdir}/libprimecount.so
%{_includedir}/primecount.h
%{_includedir}/primecount.hpp
%{_libdir}/pkgconfig/primecount.pc

%changelog
