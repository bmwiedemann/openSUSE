#
# spec file for package cJSON
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%global sover   1
%global libname libcjson%{sover}
Name:           cJSON
Version:        1.7.14
Release:        0
Summary:        JSON parser library written in ANSI C
License:        MIT
Group:          System/Libraries
URL:            https://github.com/DaveGamble/cJSON
Source:         https://github.com/DaveGamble/cJSON/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cJSON-fix-cmake-include-path.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig

%description
A simple JSON parser library written in ANSI C.

%package -n %{libname}
Summary:        JSON parser library written in ANSI C
Group:          System/Libraries

%description -n %{libname}
A simple JSON parser library written in ANSI C.

%package devel
Summary:        Development files for the cJSON library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
A simple JSON parser library written in ANSI C.

This subpackage contains libraries and header files for developing
applications that want to make use of libcjson.

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%files -n %{libname}
%license LICENSE
%doc CHANGELOG.md CONTRIBUTORS.md README.md
%{_libdir}/libcjson.so.%{sover}*

%files devel
%dir %{_includedir}/cjson
%{_includedir}/cjson/cJSON.h
%dir %{_libdir}/cmake/cJSON
%{_libdir}/cmake/cJSON/*.cmake
%{_libdir}/libcjson.so
%{_libdir}/pkgconfig/libcjson.pc

%changelog
