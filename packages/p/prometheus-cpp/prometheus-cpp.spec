#
# spec file for package prometheus-cpp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover_major 0
%define libname lib%{name}%{sover_major}

Name:           prometheus-cpp
Version:        0.8.0
Release:        0
Summary:        Prometheus client library for C++
License:        MIT
Url:            https://github.com/jupp0r/prometheus-cpp
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel

%description
Prometheus-cpp aims to enable Metrics-Driven Development for C++ services. It
implements the Prometheus Data Model, a powerful abstraction on which to collect
and expose metrics. It offers the possibility for metrics to be collected by
Prometheus, but other push/pull collections can be added as plugins.

%package -n %{libname}
Summary:        Shared libraries for prometheus-cpp

%description -n %{libname}
Prometheus-cpp aims to enable Metrics-Driven Development for C++ services. It
implements the Prometheus Data Model, a powerful abstraction on which to collect
and expose metrics. It offers the possibility for metrics to be collected by
Prometheus, but other push/pull collections can be added as plugins.

This package provides development files for prometheus-cpp.

%package devel
Summary:        Development files for prometheus-cpp
Requires:       %{libname} = %{version}

%description devel
Prometheus-cpp aims to enable Metrics-Driven Development for C++ services. It
implements the Prometheus Data Model, a powerful abstraction on which to collect
and expose metrics. It offers the possibility for metrics to be collected by
Prometheus, but other push/pull collections can be added as plugins.

This package provides development files for prometheus-cpp.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}*.so.%{sover_major}*

%files devel
%{_includedir}/prometheus
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}*.so

%changelog

