#
# spec file for package protobuf
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
%define extra_java_flags -source 8 -target 8
# see cmake/abseil-cpp.cmake and src/google/protobuf/port_def.inc
%define abseil_min_version 20230125.3
# requires gmock, which is not yet in the distribution
%bcond_with    check
%bcond_without java
%bcond_without python3
%{?sle15_python_module_pythons}
Name:           protobuf
Version:        25.4
%global         sover 25_4_0
Release:        0
Summary:        Protocol Buffers - Google's data interchange format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/protocolbuffers/protobuf
Source0:        https://github.com/protocolbuffers/protobuf/releases/download/v%{version}/%{tarname}-%{version}.tar.gz
Source1:        manifest.txt.in
Source2:        baselibs.conf
BuildRequires:  %{python_module abseil}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
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
BuildRequires:  pkgconfig(absl_log_initialize) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_log_severity) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_memory) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_node_hash_map) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_node_hash_set) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_optional) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_span) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_status) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_statusor) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_strings) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_synchronization) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_time) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_type_traits) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_utility) >= %{abseil_min_version}
BuildRequires:  pkgconfig(absl_variant) >= %{abseil_min_version}
BuildRequires:  pkgconfig(zlib)
%if %{with check}
BuildRequires:  libgmock-devel >= 1.7.0
%endif
%if %{with java}
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
%endif

%if 0%{?suse_version} >= 1500
# generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
# same "defaults" for all distributions, used in files section
%define python_files() -n python3-%{**}
%define python_sitelib %{python3_sitelib}
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

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       libprotobuf%{sover} = %{VERSION}
Requires:       libprotobuf-lite%{sover}
Conflicts:      protobuf2-devel
Conflicts:      protobuf21-devel
Provides:       libprotobuf-devel = %{VERSION}

%description devel
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%if 0%{?python_subpackage_only}
%package -n python-%{name}
Version:        4.%{VERSION}
Summary:        Python Bindings for Google Protocol Buffers
Group:          Development/Libraries/Python
BuildArch:      noarch

%description -n python-%{name}
This package contains the Python bindings for Google Protocol Buffers.

%else

%package -n python3-%{name}
Version:        4.%{VERSION}
Summary:        Python3 Bindings for Google Protocol Buffers
Group:          Development/Libraries/Python
BuildArch:      noarch

%description -n python3-%{name}
This package contains the Python bindings for Google Protocol Buffers.
%endif

%package -n %{name}-java
Summary:        Java Bindings for Google Protocol Buffers
Group:          Development/Libraries/Java
Requires:       java >= 1.6.0
BuildArch:      noarch

%description -n %{name}-java
This package contains the Java bindings for Google Protocol Buffers.

%prep
%autosetup -p1 -n %{tarname}-%{VERSION}

# python module have their own version specified in python/google/protobuf/__init__.py
grep -qF "'4.%{VERSION}'" python/google/protobuf/__init__.py

# The previous blank line is crucial for older system being able
# to use the autosetup macro
mkdir gmock

%if %{with python3}
# only needed for test suite which we don't call anyways.
# googleapis is broken on sle12
sed -i '/apputils/d' python/setup.py
sed -i '/google_test_dir/d' python/setup.py
%endif
# kill shebang that we do not really want
sed -i -e '/env python/d' python/google/protobuf/internal/*.py

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# tests are not part of offical tar ball
%cmake \
  -Dprotobuf_BUILD_TESTS=OFF \
  -Dprotobuf_ABSL_PROVIDER=package
%cmake_build

%if %{with java}
pushd ../java
../build/protoc --java_out=core/src/main/java -I../src ../src/google/protobuf/descriptor.proto
mkdir classes
javac %{extra_java_flags} -d classes core/src/main/java/com/google/protobuf/*.java
sed -e 's/@VERSION@/%{version}/' < %{SOURCE1} > manifest.txt
jar cfm %{name}-java-%{version}.jar manifest.txt -C classes com
popd
%endif

pushd ../python
export PROTOC=../build/protoc
%python_build
popd

%if %{with check}
%check
%make_build check
%endif

%install
%cmake_install
install -Dm 0644 editors/proto.vim %{buildroot}%{_datadir}/vim/site/syntax/proto.vim

%if %{with java}
pushd java
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 %{name}-java-%{version}.jar %{buildroot}%{_javadir}/%{name}-java.jar
ln -s %{name}-java.jar %{buildroot}%{_javadir}/%{name}.jar
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} core/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-java.pom
%add_maven_depmap %{name}-java.pom %{name}-java.jar
popd
%endif

pushd python
export PROTOC=../build/protoc
%python_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets -n libprotobuf%{sover}
%ldconfig_scriptlets -n libprotoc%{sover}
%ldconfig_scriptlets -n libprotobuf-lite%{sover}

%files -n libprotobuf%{sover}
%license LICENSE
%{_libdir}/libprotobuf.so.%{VERSION}.0

%files -n libprotoc%{sover}
%license LICENSE
%{_libdir}/libprotoc.so.%{VERSION}.0

%files -n libprotobuf-lite%{sover}
%license LICENSE
%{_libdir}/libprotobuf-lite.so.%{VERSION}.0

%files devel
%license LICENSE
%doc CONTRIBUTORS.txt README.md
%{_bindir}/protoc*
%{_includedir}/google
%dir %{_includedir}/java
%dir %{_includedir}/java/core
%dir %{_includedir}/java/core/src
%dir %{_includedir}/java/core/src/main
%dir %{_includedir}/java/core/src/main/java
%dir %{_includedir}/java/core/src/main/java/com
%dir %{_includedir}/java/core/src/main/java/com/google
%dir %{_includedir}/java/core/src/main/java/com/google/protobuf
%{_includedir}/java/core/src/main/java/com/google/protobuf/java_features.proto
%{_includedir}/*.h
%{_libdir}/cmake/protobuf
%{_libdir}/cmake/utf8_range
%{_libdir}/pkgconfig/*
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so
%{_libdir}/libutf8_range.a
%{_libdir}/libutf8_validity.a
%{_datadir}/vim

%if %{with java}
%files -n %{name}-java -f java/.mfiles
%license LICENSE
%{_javadir}/%{name}.jar
%endif

%if %{with python3}
%files %{python_files %{name}}
%license LICENSE
%dir %{python_sitelib}/google
%{python_sitelib}/google/protobuf
%{python_sitelib}/protobuf*nspkg.pth
%{python_sitelib}/protobuf*info
%endif

%changelog
