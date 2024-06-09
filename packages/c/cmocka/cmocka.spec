#
# spec file for package cmocka
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 150000
%bcond_without docs
%else
# We need cmake >= 3.9 to build docs
%bcond_with docs
%endif

Name:           cmocka
Version:        1.1.7
Release:        0
Summary:        Lightweight library to simplify and generalize unit tests for C
License:        Apache-2.0
Group:          Productivity/Networking/Other
URL:            https://cmocka.org

Source0:        https://cmocka.org/files/1.1/%{name}-%{version}.tar.xz
Source1:        https://cmocka.org/files/1.1/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  glibc-devel
BuildRequires:  pkg-config

Obsoletes:      libcmocka-devel-static < %{version}

%description
cmocka is an elegant unit testing framework for C with support for mock
objects. It only requires the standard C library, works on a range of computing
platforms (including embedded) and with different compilers.

Features:
  * Support for mock objects
  * Only requires the C library
  * Several supported output formats (Subunit, TAP, jUnit XML)
  * Fully documented API
  * Test fixtures
  * Exception handling for signals (SIGSEGV, SIGILL, ...)
  * No fork() used
  * Very well tested
  * Testing of memory leaks, buffer overflows and underflows.

Also, CMocka tries to avoid the use of some of the newer features of C
compilers.

%package -n libcmocka0
Summary:        Lightweight library to simplify and generalize unit tests for C
Group:          System/Libraries

%description -n libcmocka0
cmocka is an elegant unit testing framework for C with support for mock
objects. It only requires the standard C library, works on a range of computing
platforms (including embedded) and with different compilers.

Features:
  * Support for mock objects
  * Only requires the C library
  * Several supported output formats (Subunit, TAP, jUnit XML)
  * Fully documented API
  * Test fixtures
  * Exception handling for signals (SIGSEGV, SIGILL, ...)
  * No fork() used
  * Very well tested
  * Testing of memory leaks, buffer overflows and underflows.

Also, CMocka tries to avoid the use of some of the newer features of C
compilers.

%package -n libcmocka-devel
Summary:        Development headers for the cmocka library
Group:          Development/Libraries/C and C++
Requires:       libcmocka0 = %{version}
Requires:       pkg-config
Requires:       (libcmocka-cmake if cmake)

%description -n libcmocka-devel
Development headers for the cmocka unit testing library.

%package -n libcmocka-doc
Summary:        Documentation for the cmocka library
Group:          Development/Libraries/C and C++
Enhances:       libcmocka-devel
Provides:       libcmocka-devel:%{_defaultdocdir}/libcmocka-devel

%description -n libcmocka-doc
Documentation for the cmocka unit testing library.

%package -n libcmocka-cmake
Summary:        cmake support for the cmocka library
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       libcmocka-devel = %{version}
Provides:       libcmocka-devel:%{_libdir}/cmake/cmocka

%description -n libcmocka-cmake
cmake support for developing with the cmocka unit testing library.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%cmake \
    -DCMAKE_SKIP_RPATH=OFF \
    -DWITH_STATIC_LIB=ON \
    -DWITH_CMOCKERY_SUPPORT=ON \
    -DUNIT_TESTING=ON

make %{?_smp_mflags}
%if %{with docs}
make docs
#endif  with docs
%endif

%install
%cmake_install

%check
pushd build
ctest --output-on-failure
popd

%post -n libcmocka0 -p /sbin/ldconfig

%postun -n libcmocka0 -p /sbin/ldconfig

%files -n libcmocka0
%doc AUTHORS README.md ChangeLog
%license COPYING
%{_libdir}/libcmocka.so.*

%files -n libcmocka-devel
%{_includedir}/cmocka.h
%{_includedir}/cmocka_pbc.h
%{_includedir}/cmockery
%{_libdir}/libcmocka.so
%{_libdir}/pkgconfig/cmocka.pc

%if %{with docs}
%files -n libcmocka-doc
%doc build/doc/html
%endif

%files -n libcmocka-cmake
%{_libdir}/cmake/cmocka

%changelog
