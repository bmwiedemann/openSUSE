#
# spec file for package googletest
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _name   googlemock
Name:           googletest
Version:        1.8.1
Release:        0
Summary:        Google C++ Testing Framework
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/googletest
Source0:        https://github.com/google/googletest/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
Source1:        googletest-rpmlintrc
BuildRequires:  cmake >= 2.6.4
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(pthread-stubs)

%description
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian).
Based on the xUnit architecture. Supports automatic test discovery,
a rich set of assertions, user-defined assertions, death tests,
fatal and non-fatal failures, value- and type-parameterized tests,
various options for running the tests, and XML test report generation.

%package -n     gtest
Summary:        Development files for the Google C++ Testing Framework
Group:          Development/Libraries/C and C++
Recommends:     %{_name} = %{version}
Obsoletes:      %{name}-devel < %{version}
Obsoletes:      lib%{name}0 < %{version}
Provides:       %{name}-devel = %{version}

%description -n gtest
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian).
Based on the xUnit architecture. Supports automatic test discovery,
a rich set of assertions, user-defined assertions, death tests,
fatal and non-fatal failures, value- and type-parameterized tests,
various options for running the tests, and XML test report generation.

This package provides shared libraries and header files for development
with googletest.

%package -n     gmock
Summary:        Development files for the Google C++ Mocking Framework
Group:          Development/Libraries/C and C++
Recommends:     %{name} = %{version}
Provides:       %{_name}-devel

%description -n gmock
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s specifics in
mind, Google C++ Mocking Framework (or Google Mock for short) is a library for
writing and using C++ mock classes.

This package provides shared libraries and header files for development
with googlemock.

%prep
%setup -q -n %{name}-release-%{version}

%build
%cmake
%make_jobs

%install
%cmake_install
# Install the source code needed by some applications
mkdir -p %{buildroot}%{_includedir}/gmock/src && install -m 0644 googlemock/src/* %{buildroot}%{_includedir}/gmock/src
mkdir -p %{buildroot}%{_includedir}/gtest/src && install -m 0644 googletest/src/* %{buildroot}%{_includedir}/gtest/src

%files -n gtest
%license %{name}/LICENSE
%doc %{name}/CHANGES %{name}/CONTRIBUTORS %{name}/README.md
%{_libdir}/libgtest.so
%{_libdir}/libgtest_main.so
%{_includedir}/gtest
%{_libdir}/pkgconfig/gtest*.pc

%files -n gmock
%license %{_name}/LICENSE
%doc %{_name}/CHANGES %{_name}/CONTRIBUTORS %{_name}/README.md
%{_libdir}/libgmock.so
%{_libdir}/libgmock_main.so
%{_includedir}/gmock
%{_libdir}/cmake/GTest
%{_libdir}/pkgconfig/gmock*.pc

%changelog
