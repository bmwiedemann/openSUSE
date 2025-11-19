#
# spec file for package protobuf
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


%define tarname protobuf
# see cmake/abseil-cpp.cmake and src/google/protobuf/port_def.inc
%define abseil_min_version 20250512.1
%global         sover 33_1_0
%if 0%{?gcc_version} < 11
%define with_gcc 11
%endif
# requires gmock, which is not yet in the distribution
%bcond_with    check
%global protoc_arch %{_arch}
%ifarch x86_64 %{?x86_64}
%global protoc_arch x86_64
%endif
%ifarch ppc
%global protoc_arch ppc_32
%endif
%ifarch ppc64
%global protoc_arch ppc_64
%endif
%ifarch ppc64le
%global protoc_arch ppcle_64
%endif
%ifarch %{ix86}
%global protoc_arch x86_32
%endif
%ifarch ia64
%global protoc_arch itanium_64
%endif
%ifarch s390
%global protoc_arch s390_32
%endif
%ifarch s390x
%global protoc_arch s390_64
%endif
%ifarch %{arm}
%global protoc_arch arm_32
%endif
%ifarch aarch64 %{arm64}
%global protoc_arch aarch_64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global protoc_arch sparc_32
%endif
# 64 bit sparc
%ifarch sparc64
%global protoc_arch sparc_64
%endif
Name:           protobuf
Version:        33.1
Release:        0
Summary:        Protocol Buffers - Google's data interchange format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/protocolbuffers/protobuf
Source0:        https://github.com/protocolbuffers/protobuf/releases/download/v%{version}/%{tarname}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
# see cmake/abseil-cpp.cmake
BuildRequires:  pkgconfig(absl_absl_check) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_absl_log) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_algorithm) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_base) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_bind_front) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_bits) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_btree) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_cleanup) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_cord) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_core_headers) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_debugging) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_die_if_null) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_dynamic_annotations) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_flags) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_flat_hash_map) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_flat_hash_set) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_function_ref) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_hash) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_layout) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_log_globals) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_log_initialize) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_log_severity) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_memory) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_node_hash_map) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_node_hash_set) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_random_distributions) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_random_random) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_span) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_status) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_statusor) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_strings) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_synchronization) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_time) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_type_traits) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_utility) >= %{abseil_min_version}
BuildRequires:  pkgconfig(zlib)
%if %{with check}
BuildRequires:  libgmock-devel >= 1.7.0
%endif

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n libprotobuf%{sover}
Summary:        Protocol Buffers - Google's data interchange format
Group:          System/Libraries

%description -n libprotobuf%{sover}
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n libprotoc%{sover}
Summary:        Protocol Buffers - Google's data interchange format
Group:          System/Libraries

%description -n libprotoc%{sover}
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n libprotobuf-lite%{sover}
Summary:        Protocol Buffers - Google's data interchange format
Group:          System/Libraries

%description -n libprotobuf-lite%{sover}
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n libutf8_range-%{sover}
Summary:        UTF-8 validation libraries from Protobuf
Group:          System/Libraries

%description -n libutf8_range-%{sover}
UTF-8 string validation library with optional SIMD acceleration (armv8a NEON,
SSE4 and AVX2).

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       libprotobuf%{sover} = %{version}
Requires:       libprotobuf-lite%{sover} = %{version}
Requires:       libutf8_range-%{sover} = %{version}
Conflicts:      protobuf2-devel
Conflicts:      protobuf21-devel
Provides:       libprotobuf-devel = %{version}
# Not generated automatically without javapackages-local as dependency
Provides:       mvn(com.google.protobuf:protoc:exe:linux-%{protoc_arch}:)

%description devel
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%prep
%autosetup -p1 -n %{tarname}-%{version}

mkdir gmock

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# tests are not part of offical tar ball
%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%cmake \
  -Dprotobuf_BUILD_TESTS=OFF \
  %{nil}
%cmake_build

%if %{with check}
%check
%make_build check
%endif

%install
%cmake_install
install -Dm 0644 editors/proto.vim %{buildroot}%{_datadir}/vim/site/syntax/proto.vim
install -D java/core/src/main/resources/google/protobuf/java_features.proto %{buildroot}%{_includedir}/java/core/src/main/resources/google/protobuf/java_features.proto

# create maven metadata for the protoc executable
install -dm 0755 %{buildroot}%{_datadir}/maven-metadata
cat <<__PROTOBUF__ >>%{buildroot}%{_datadir}/maven-metadata/%{name}-protoc.xml
<metadata xmlns="http://fedorahosted.org/xmvn/METADATA/2.3.0">
  <artifacts>
    <artifact>
      <groupId>com.google.protobuf</groupId>
      <artifactId>protoc</artifactId>
      <extension>exe</extension>
      <classifier>linux-%{protoc_arch}</classifier>
      <version>4.%{version}</version>
      <path>%{_bindir}/protoc</path>
    </artifact>
  </artifacts>
</metadata>
__PROTOBUF__

%fdupes %{buildroot}%{_prefix}

# SLE12 does not define this macro
%if %{undefined ldconfig_scriptlets}
%post -n libprotobuf%{sover} -p /sbin/ldconfig
%postun -n libprotobuf%{sover} -p /sbin/ldconfig
%post -n libprotoc%{sover} -p /sbin/ldconfig
%postun -n libprotoc%{sover} -p /sbin/ldconfig
%post -n libprotobuf-lite%{sover} -p /sbin/ldconfig
%postun -n libprotobuf-lite%{sover} -p /sbin/ldconfig
%post -n libutf8_range-%{sover} -p /sbin/ldconfig
%postun -n libutf8_range-%{sover} -p /sbin/ldconfig
%else
%ldconfig_scriptlets -n libprotobuf%{sover}
%ldconfig_scriptlets -n libprotoc%{sover}
%ldconfig_scriptlets -n libprotobuf-lite%{sover}
%ldconfig_scriptlets -n libutf8_range-%{sover}
%endif

%files -n libprotobuf%{sover}
%license LICENSE
%{_libdir}/libprotobuf.so.%{version}.0

%files -n libprotoc%{sover}
%license LICENSE
%{_libdir}/libprotoc.so.%{version}.0

%files -n libprotobuf-lite%{sover}
%license LICENSE
%{_libdir}/libprotobuf-lite.so.%{version}.0

%files -n libutf8_range-%{sover}
%license LICENSE
%{_libdir}/libutf8_range.so.%{version}.0
%{_libdir}/libutf8_validity.so.%{version}.0

%files devel
%license LICENSE
%doc CONTRIBUTORS.txt README.md
%{_bindir}/protoc*
%{_includedir}/google
%dir %{_includedir}/java
%dir %{_includedir}/java/core
%dir %{_includedir}/java/core/src
%dir %{_includedir}/java/core/src/main
%dir %{_includedir}/java/core/src/main/resources
%dir %{_includedir}/java/core/src/main/resources/
%dir %{_includedir}/java/core/src/main/resources/google
%dir %{_includedir}/java/core/src/main/resources/google/protobuf
%{_includedir}/java/core/src/main/resources/google/protobuf/java_features.proto
%{_includedir}/upb
%{_includedir}/*.h
%{_libdir}/cmake/protobuf
%{_libdir}/cmake/utf8_range
%{_libdir}/pkgconfig/*
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so
%{_libdir}/libupb.a
%{_libdir}/libutf8_range.so
%{_libdir}/libutf8_validity.so
%{_datadir}/vim
%{_datadir}/maven-metadata

%changelog
