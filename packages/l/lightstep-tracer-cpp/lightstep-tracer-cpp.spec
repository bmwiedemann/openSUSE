#
# spec file for package lightstep-tracer-cpp
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


%define sover 0
%define libname liblightstep_tracer%{sover}
%define src_install_dir /usr/src/%{name}

Name:           lightstep-tracer-cpp
Version:        0.8.1
Release:        0
Summary:        C++ library for LightStep distributed tracing
License:        MIT
Group:          Development/Languages/C and C++
Url:            http://lightstep.com/
Source0:        %{name}-%{version}.tar.xz
Source100:      %{name}-rpmlintrc
Patch0:         lightstep-tracer-cpp-cmake-add-soversion.patch
Patch1:         lightstep-tracer-cpp-cmake-use-gnuinstalldirs.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  grpc-devel
BuildRequires:  opentracing-cpp-devel
BuildRequires:  protobuf-devel

%description
C++ library for the LightStep distributed tracing.

%package -n %{libname}
Summary:        C++ library for LightStep distributed tracing
Group:          System/Libraries

%description -n %{libname}
Shared library for lightstep-tracer-cpp - C++ library for LightStep
distributed tracing.

%package devel
Summary:        Development files for the LightStep C++ library
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for lightstep-tracer-cpp - C++ library for LightStep
distributed tracing.

%package source
Summary:        Source code of the LightStep C++ library
Group:          Development/Sources
BuildArch:      noarch

%description source
Development files for lightstep-tracer-cpp - C++ library for LightStep
distributed tracing.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake
%make_jobs

%install
%cmake_install
# Install sources
mkdir -p %{buildroot}%{src_install_dir}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
%fdupes %{src_install_dir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/liblightstep_tracer.so.0

%files devel
%{_includedir}/lightstep
%{_libdir}/liblightstep_tracer.so

%files source
%{src_install_dir}

%changelog
