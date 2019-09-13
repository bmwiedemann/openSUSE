#
# spec file for package dd-opentracing-cpp
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


%define soversion 0
%define libname libdd_opentracing%{soversion}

Name:           dd-opentracing-cpp
Version:        1.0.1
Release:        0
Summary:        Datadog Opentracing C++ client
License:        Apache-2.0
Group:          Development/Languages/C and C++
Url:            https://github.com/DataDog/dd-opentracing-cpp
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  msgpack-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  opentracing-cpp-devel
BuildRequires:  zlib-devel

%description
C++ client for Datalog Opentracing.

%package -n %{libname}
Summary:        Shared library for Datalog Opentracing C++ client
Group:          System/Libraries

%description -n %{libname}
Shared library for dd-opentracing-cpp - C++ client for Datalog Opentracing.

%package devel
Summary:        Development files for Datalog Opentracing C++ client
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for dd-opentracing-cpp - C++ client for Datalog Opentracing.

%prep
%setup -q
# Use version packaged in distribution
rm -r 3rd_party/include/nlohmann

%build
%cmake
%make_jobs

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libdd_opentracing.so.0

%files devel
%{_includedir}/datadog
%{_includedir}/datadog/opentracing.h
%{_libdir}/libdd_opentracing.so

%changelog
