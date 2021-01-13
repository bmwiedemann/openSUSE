#
# spec file for package primesieve
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


Name:           primesieve
Version:        7.6
Release:        0
Summary:        A prime number generator
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/kimwalisch/primesieve
Source0:        https://github.com/kimwalisch/primesieve/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.7
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  asciidoc
BuildRequires:  pkgconfig

%description
primesieve is a command-line program that generates primes using the
sieve of Eratosthenes algorithm. It can generate primes and prime
k-tuplets (twin primes, prime triplets, ...) up to 2^64 and find the
nth prime.

%package -n libprimesieve9
Summary:        C/C++ library for generating prime numbers

%description -n libprimesieve9
This package contains the shared runtime library for primesieve.

%package -n libprimesieve-devel
Summary:        Development files for the primesieve library
Requires:       libprimesieve9 = %{version}

%description -n libprimesieve-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primesieve library.
It also contains the API documentation of the library.

%prep
%setup -q

%build
%cmake -DBUILD_DOC=ON \
       -DBUILD_MANPAGE=ON \
       -DBUILD_TESTS=ON \
       -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build
%cmake_build doc

find doc/html -name '*.md5' -delete
cp -rf doc/html ..

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%post -n libprimesieve9 -p /sbin/ldconfig
%postun -n libprimesieve9 -p /sbin/ldconfig

%check
%ctest

%files -n primesieve
%doc README.md ChangeLog
%{_bindir}/primesieve
%{_mandir}/man1/primesieve.1%{?ext_man}

%files -n libprimesieve9
%license COPYING
%{_libdir}/libprimesieve.so.*

%files -n libprimesieve-devel
%doc html examples
%{_libdir}/libprimesieve.so
%{_includedir}/primesieve.h
%{_includedir}/primesieve.hpp
%dir %{_includedir}/primesieve
%{_includedir}/primesieve/StorePrimes.hpp
%{_includedir}/primesieve/iterator.h
%{_includedir}/primesieve/iterator.hpp
%{_includedir}/primesieve/primesieve_error.hpp
%dir %{_libdir}/cmake/primesieve
%{_libdir}/cmake/primesieve/*.cmake
%{_libdir}/pkgconfig/primesieve.pc

%changelog
