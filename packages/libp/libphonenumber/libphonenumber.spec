#
# spec file for package libphonenumber
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lib_ver 9
%define lib_ver2 9.0
Name:           libphonenumber
Version:        9.0.14
Release:        0
Summary:        Library for parsing, formatting, and validating international phone numbers
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/libphonenumber
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM (hopefully, https://github.com/google/libphonenumber/pull/3903)
Patch1:         0001-Fix-build-with-Boost-1.89.0.patch
# PATCH-FIX-DOWNSTREAM (see https://github.com/google/libphonenumber/pull/2874)
Patch2:         0001-Revert-Fix-typo-in-arguments-to-add_metadata_gen_tar.patch
Patch3:         0001-Add-support-to-protobuf-3.25.1.patch
Patch4:         0002-Avoid-intermediate-proto-object-library.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_date_time-devel >= 1.40.0
BuildRequires:  libboost_headers-devel >= 1.40.0
BuildRequires:  libboost_thread-devel >= 1.40.0
BuildRequires:  pkgconfig
# Actual version requirement unknown
BuildRequires:  cmake(absl)
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
Requires:       libboost_date_time-devel >= 1.40.0
Requires:       libboost_thread-devel >= 1.40.0
Requires:       cmake(absl)
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
# (https://github.com/google/libphonenumber/pull/2556)
%cmake \
	-DBUILD_STATIC_LIB=OFF \
	-DBUILD_TESTING=ON \
	-DBUILD_GEOCODER=OFF \
	-DREGENERATE_METADATA=OFF \
	%{nil}
%cmake_build

%install
cd cpp
%cmake_install

%check
cd cpp/build
%make_build tests

%ldconfig_scriptlets -n %{name}%{lib_ver}

%files -n %{name}%{lib_ver}
%license LICENSE*
%{_libdir}/libphonenumber.so.%{lib_ver}
%{_libdir}/libphonenumber.so.%{lib_ver2}

%files devel
%license LICENSE*
%{_libdir}/libphonenumber.so
%{_includedir}/phonenumbers/
%dir %{_libdir}/cmake/
%{_libdir}/cmake/libphonenumber/

%changelog
