#
# spec file for package protobuf21
#
# Copyright (c) 2024 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define sover 3_21_12
%define tarname protobuf
%define extra_java_flags -source 7 -target 7
# requires gmock, which is not yet in the distribution
%bcond_with    check
%bcond_with    java
%bcond_with    python3
%if 0%{?gcc_version} < 11
%define with_gcc 11
%endif
Name:           protobuf21
Version:        21.12
Release:        0
Summary:        Protocol Buffers - Google's data interchange format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/protocolbuffers/protobuf
Source0:        https://github.com/protocolbuffers/protobuf/archive/v%{version}.tar.gz#/%{tarname}-%{version}.tar.gz
Source1:        manifest.txt.in
Source2:        baselibs.conf
Source1000:     %{name}-rpmlintrc
Patch0:         gcc12-disable-__constinit-with-c++-11.patch
# https://github.com/protocolbuffers/protobuf/pull/10355
Patch1:         10355.patch
Provides:       protobuf = %{version}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(zlib)
%if %{with check}
BuildRequires:  libgmock-devel >= 1.7.0
%endif
%if %{with java}
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
%endif

%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
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
Requires:       gcc-c++
Requires:       libprotobuf%{sover} = %{version}
Requires:       libprotobuf-lite%{sover}
Requires:       pkgconfig(zlib)
Conflicts:      protobuf2-devel
Provides:       libprotobuf-devel = %{version}
Provides:       protobuf-devel = %{version}
Obsoletes:      protobuf-devel <= 21.12

%description devel
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n %{name}-java
Summary:        Java Bindings for Google Protocol Buffers
Group:          Development/Libraries/Java
Requires:       java >= 1.6.0

%description -n %{name}-java
This package contains the Java bindings for Google Protocol Buffers.

%if 0%{?python_subpackage_only}
%package -n python-%{name}
Summary:        Python Bindings for Google Protocol Buffers
Group:          Development/Libraries/Python
Requires:       python-six >= 1.9

%description -n python-%{name}
This package contains the Python bindings for Google Protocol Buffers.

%else

%package -n python3-%{name}
Summary:        Python3 Bindings for Google Protocol Buffers
Group:          Development/Libraries/Python
Requires:       python3-six >= 1.9

%description -n python3-%{name}
This package contains the Python bindings for Google Protocol Buffers.
%endif

%prep
%autosetup -p1 -n %{tarname}-%{version}

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

%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%cmake \
  -Dprotobuf_BUILD_TESTS=OFF \
  %{nil}
%cmake_build

%if %{with java}
pushd java
../src/protoc --java_out=core/src/main/java -I../src ../src/google/protobuf/descriptor.proto
mkdir classes
javac %{extra_java_flags} -d classes core/src/main/java/com/google/protobuf/*.java
sed -e 's/@VERSION@/%{version}/' < %{SOURCE1} > manifest.txt
jar cfm %{name}-java-%{version}.jar manifest.txt -C classes com
popd
%endif

%if %{with python3}
pushd python
%python_build
popd
%endif

%if %{with check}
%check
%make_build check
%endif

%install
%cmake_install
install -Dm 0644 editors/proto.vim %{buildroot}%{_datadir}/vim/site/syntax/proto.vim
# no need for that
find %{buildroot} -type f -name "*.la" -delete -print

%if %{with java}
pushd java
install -D -m 0644 %{name}-java-%{version}.jar %{buildroot}%{_javadir}/%{name}-java.jar
ln -s %{name}-java.jar %{buildroot}%{_javadir}/%{name}.jar
install -D -m 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}-parent.pom
%add_maven_depmap %{name}-parent.pom
install -D -m 0644 bom/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-bom.pom
%add_maven_depmap %{name}-bom.pom
install -D -m 0644 core/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-java.pom
%add_maven_depmap %{name}-java.pom %{name}-java.jar
popd
%endif

%if %{with python3}
pushd python
%python_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%fdupes %{buildroot}%{_prefix}

%post -n libprotobuf%{sover} -p /sbin/ldconfig
%postun -n libprotobuf%{sover} -p /sbin/ldconfig
%post -n libprotoc%{sover} -p /sbin/ldconfig
%postun -n libprotoc%{sover} -p /sbin/ldconfig
%post -n libprotobuf-lite%{sover} -p /sbin/ldconfig
%postun -n libprotobuf-lite%{sover} -p /sbin/ldconfig

%files -n libprotobuf%{sover}
%license LICENSE
%{_libdir}/libprotobuf.so.3.%{version}*

%files -n libprotoc%{sover}
%{_libdir}/libprotoc.so.3.%{version}*

%files -n libprotobuf-lite%{sover}
%{_libdir}/libprotobuf-lite.so.3.%{version}*

%files devel
%doc CHANGES.txt CONTRIBUTORS.txt README.md
%{_bindir}/protoc
%{_bindir}/protoc-3.%{version}*
%{_includedir}/google
%{_libdir}/pkgconfig/*
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so
%{_libdir}/cmake/protobuf
%{_datadir}/vim

%if %{with java}
%files -n %{name}-java -f java/.mfiles
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
