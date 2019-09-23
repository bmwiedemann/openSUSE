#
# spec file for package zipkin-cpp-opentracing
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


Name:           zipkin-cpp-opentracing
Version:        0.3.1
Release:        0
Summary:        OpenTracing Tracer implementation for Zipkin in C++
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/rnburn/%{name}
Source:         https://github.com/rnburn/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cmake-lib-install-dir.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  opentracing-cpp-devel
BuildRequires:  pkgconfig(libcurl)

%description
OpenTracing Tracet implementation for Zipkin in a form of library in C++

%package -n libzipkin-cpp-opentracing0
Summary:        OpenTracing Tracer implementation for Zipkin in C++
Group:          System/Libraries

%description -n libzipkin-cpp-opentracing0
OpenTracing Tracer implementation for Zipkin in a form of library in C++

%package devel
Summary:        Development files for OpenTracing implementation for Zipkin
Group:          Development/Libraries/C and C++
Requires:       libzipkin-cpp-opentracing0 = %{version}

%description devel
Development files for OpenTracing implementation for Zipkin (C++ library)

%package devel-static
Summary:        Static libraries for OpenTracing implementation for Zipkin
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
Static libraries for OpenTracing implementation for Zipkin (in C++)

%prep
%setup -q
%patch0 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_STATIC_LIBS=ON -DBUILD_TESTING=OFF

%install
%cmake_install

%post -n libzipkin-cpp-opentracing0 -p /sbin/ldconfig

%postun -n libzipkin-cpp-opentracing0 -p /sbin/ldconfig

%files -n libzipkin-cpp-opentracing0
%license LICENSE
%{_libdir}/libzipkin.so.0
%{_libdir}/libzipkin.so.0.3.1
%{_libdir}/libzipkin_opentracing.so.0
%{_libdir}/libzipkin_opentracing.so.0.3.1

%files devel
%doc README.md

%dir %{_includedir}/zipkin
%{_includedir}/zipkin/flags.h
%{_includedir}/zipkin/hex.h
%{_includedir}/zipkin/ip_address.h
%{_includedir}/zipkin/opentracing.h
%{_includedir}/zipkin/optional.h
%{_includedir}/zipkin/span_context.h
%{_includedir}/zipkin/trace_id.h
%{_includedir}/zipkin/tracer.h
%{_includedir}/zipkin/tracer_interface.h
%{_includedir}/zipkin/utility.h
%{_includedir}/zipkin/zipkin_core_types.h

%{_libdir}/libzipkin.so
%{_libdir}/libzipkin_opentracing.so

%files devel-static
%{_libdir}/libzipkin.a
%{_libdir}/libzipkin_opentracing.a

%changelog
