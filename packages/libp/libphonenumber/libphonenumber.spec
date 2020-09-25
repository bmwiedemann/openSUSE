#
# spec file for package libphonenumber
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libphonenumber
Version:        8.12.10
Release:        0
%define lib_ver 8
%define lib_ver2 8.12
Summary:        Library for parsing, formatting, and validating international phone numbers
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/libphonenumber
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  java
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(icu-i18n) >= 4.4
BuildRequires:  pkgconfig(icu-uc) >= 4.4
BuildRequires:  pkgconfig(protobuf) >= 2.4

%description
Google's common Java, C++ and JavaScript library for parsing, formatting,
and validating international phone numbers.

%package     -n %{name}%{lib_ver}
Summary:        Library for parsing, formatting, and validating international phone numbers
Group:          System/Libraries

%description -n %{name}%{lib_ver}
Google's common Java, C++ and JavaScript library for parsing, formatting,
and validating international phone numbers. The Java version is optimized
for running on smartphones, and is used by the Android framework since 4.0
(Ice Cream Sandwich).

%package        devel
Summary:        Library for parsing, formatting, and validating international phone numbers
Group:          Development/Libraries/C and C++
Requires:       %{name}%{lib_ver} = %{version}
Requires:       pkgconfig(protobuf) >= 2.4

%description    devel
Google's common Java, C++ and JavaScript library for parsing, formatting,
and validating international phone numbers. The Java version is optimized
for running on smartphones, and is used by the Android framework since 4.0
(Ice Cream Sandwich).


This package provides libraries and header files for developing applications
that use libphonenumber.

%prep
%autosetup -p1

%build
cd cpp
# Enabling the geocoder breaks quite a lot due to broken cmakelists
%cmake -DBUILD_STATIC_LIB=OFF -DBUILD_SHARED_LIB=ON -DBUILD_TESTING=ON -DBUILD_GEOCODER=OFF
%make_jobs

%install
cd cpp
%cmake_install

%check
cd cpp/build
%make_jobs tests

%post -n %{name}%{lib_ver} -p /sbin/ldconfig
%postun -n %{name}%{lib_ver} -p /sbin/ldconfig

%files -n %{name}%{lib_ver}
%license LICENSE*
%{_libdir}/libphonenumber.so.%{lib_ver}
%{_libdir}/libphonenumber.so.%{lib_ver2}

%files devel
%{_libdir}/libphonenumber.so
%{_includedir}/phonenumbers/

%changelog
