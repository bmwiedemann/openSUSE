#
# spec file for package hhdate
#
# Copyright (c) 2023 SUSE LLC
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


%global somajor 3
%global libname libdate-tz%{somajor}
Name:           hhdate
Version:        3.0.1
Release:        0
Summary:        Date and time library based on the C++11/14/17 chrono header
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/HowardHinnant/date
Source:         hhdate-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A date and time library based on the C++11/14/17 chrono header.

%package  -n    %{libname}
Summary:        Development files for the hhdate library
Group:          Development/Libraries/C and C++

%description    -n %{libname}
A date and time library based on the C++11/14/17 chrono header.

%package        devel
Summary:        Development files for the hhdate library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Conflicts:      %{name} <= %{version}

%description    devel
A date and time library based on the C++11/14/17 chrono header.

%prep
%setup -q

%build
%cmake -DBUILD_TZ_LIB=ON -DUSE_SYSTEM_TZ_DB=ON
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libdate-tz.so.%{somajor}*
%license LICENSE.txt

%files devel
%license LICENSE.txt
%{_includedir}/date/
%{_libdir}/cmake/date/
%{_libdir}/libdate-tz.so

%changelog
