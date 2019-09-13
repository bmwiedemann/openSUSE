#
# spec file for package opentracing-cpp
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


%define sover 1
%define src_install_dir /usr/src/%{name}

Name:           opentracing-cpp
Version:        1.5.0
Release:        0
Summary:        OpenTracing C++ API
License:        MIT
Group:          Development/Languages/C and C++
Url:            http://opentracing.io/
Source0:        https://github.com/opentracing/opentracing-cpp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++

%description
C++ implementation of the OpenTracing API.

%package -n libopentracing-cpp1
Summary:        OpenTracing C++ API
Group:          System/Libraries

%description -n libopentracing-cpp1
C++ implementation of the OpenTracing API.

%package devel
Summary:        Development files for the OpenTracing C++ API
Group:          Development/Languages/C and C++
Requires:       libopentracing-cpp1 = %{version}

%description devel
Development files for opentracing-cpp - the C++ implementation of the
OpenTracing API.

%package source
Summary:        Source code of the OpenTracing C++ API
Group:          Development/Sources
BuildArch:      noarch

%description source
Source code of opentracing-cpp - the C++ implementation of the OpenTracing API.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS=-fPIC -DBUILD_DYNAMIC_LIBS=ON -DBUILD_TESTING=OFF -DLIB_INSTALL_DIR=%{_libdir}
%make_jobs

%install
%cmake_install
# Install sources
mkdir -p %{buildroot}%{src_install_dir}
tar -xzf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
%fdupes %{src_install_dir}

%post -n libopentracing-cpp1 -p /sbin/ldconfig

%postun -n libopentracing-cpp1 -p /sbin/ldconfig

%files -n libopentracing-cpp1
%license LICENSE
%doc ChangeLog README.md
%dir %{_libdir}/cmake/OpenTracing
%{_libdir}/cmake/OpenTracing/OpenTracingConfig.cmake
%{_libdir}/cmake/OpenTracing/OpenTracingConfigVersion.cmake
%{_libdir}/cmake/OpenTracing/OpenTracingTargets-release.cmake
%{_libdir}/cmake/OpenTracing/OpenTracingTargets.cmake
%{_libdir}/libopentracing.so.%{sover}
%{_libdir}/libopentracing.so.%{version}
%{_libdir}/libopentracing_mocktracer.so.%{sover}
%{_libdir}/libopentracing_mocktracer.so.%{version}

%files devel
%dir %{_includedir}/opentracing
%{_includedir}/opentracing/config.h
%{_includedir}/opentracing/dynamic_load.h
%{_includedir}/opentracing/noop.h
%{_includedir}/opentracing/propagation.h
%{_includedir}/opentracing/span.h
%{_includedir}/opentracing/string_view.h
%{_includedir}/opentracing/symbols.h
%{_includedir}/opentracing/tracer.h
%{_includedir}/opentracing/tracer_factory.h
%{_includedir}/opentracing/util.h
%{_includedir}/opentracing/value.h
%{_includedir}/opentracing/version.h

%dir %{_includedir}/opentracing/expected
%{_includedir}/opentracing/expected/expected.hpp

%dir %{_includedir}/opentracing/ext
%{_includedir}/opentracing/ext/tags.h

%dir %{_includedir}/opentracing/mocktracer
%{_includedir}/opentracing/mocktracer/in_memory_recorder.h
%{_includedir}/opentracing/mocktracer/json.h
%{_includedir}/opentracing/mocktracer/json_recorder.h
%{_includedir}/opentracing/mocktracer/recorder.h
%{_includedir}/opentracing/mocktracer/symbols.h
%{_includedir}/opentracing/mocktracer/tracer.h
%{_includedir}/opentracing/mocktracer/tracer_factory.h

%dir %{_includedir}/opentracing/variant
%{_includedir}/opentracing/variant/recursive_wrapper.hpp
%{_includedir}/opentracing/variant/variant.hpp

%{_libdir}/libopentracing.so
%{_libdir}/libopentracing_mocktracer.so

%files source
%{src_install_dir}

%changelog
