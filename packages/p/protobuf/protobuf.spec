#
# spec file for package protobuf
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define sover 3_21_12
%define tarname protobuf
%define src_install_dir %{_prefix}/src/%{name}
%define extra_java_flags -source 7 -target 7
# requires gmock, which is not yet in the distribution
%bcond_with    check
%bcond_without java
%bcond_without python2
%bcond_without python3
Name:           protobuf
Version:        21.12
Release:        0
Summary:        Protocol Buffers - Google's data interchange format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/protocolbuffers/protobuf
Source0:        https://github.com/protocolbuffers/protobuf/archive/v%{version}.tar.gz#/%{tarname}-%{version}.tar.gz
Source1:        manifest.txt.in
Source2:        baselibs.conf
Patch0:         gcc12-disable-__constinit-with-c++-11.patch
# https://github.com/protocolbuffers/protobuf/pull/10355
Patch1:         10355.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
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

%description devel
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package source
Summary:        Source code of protobuf
Group:          Development/Sources
BuildArch:      noarch

%description source
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

This package contains source code for Protocol Buffers.

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

%package -n python2-%{name}
Summary:        Python2 Bindings for Google Protocol Buffers
Group:          Development/Libraries/Python
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name} < %{version}
Requires:       python2-six >= 1.9

%description -n python2-%{name}
This package contains the Python bindings for Google Protocol Buffers.

%package -n python3-%{name}
Summary:        Python3 Bindings for Google Protocol Buffers
Group:          Development/Libraries/Python
Requires:       python3-six >= 1.9

%description -n python3-%{name}
This package contains the Python bindings for Google Protocol Buffers.
%endif

%prep
%autosetup -p1 -n %{tarname}-%{version}
mkdir gmock

%if %{with python2} || %{with python3}
# only needed for test suite which we don't call anyways.
# googleapis is broken on sle12
sed -i '/apputils/d' python/setup.py
sed -i '/google_test_dir/d' python/setup.py
%endif
# kill shebang that we do not really want
sed -i -e '/env python/d' python/google/protobuf/internal/*.py

%build
%define _lto_cflags %{nil}
autoreconf -fvi
%configure \
	--disable-static

make %{?_smp_mflags}

%if %{with java}
pushd java
../src/protoc --java_out=core/src/main/java -I../src ../src/google/protobuf/descriptor.proto
mkdir classes
javac %{extra_java_flags} -d classes core/src/main/java/com/google/protobuf/*.java
sed -e 's/@VERSION@/%{version}/' < %{SOURCE1} > manifest.txt
jar cfm %{name}-java-%{version}.jar manifest.txt -C classes com
popd
%endif

pushd python
%python_build
popd

%if %{with check}
%check
make %{?_smp_mflags} check
%endif

%install
%make_install
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

pushd python
%python_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{src_install_dir}
tar -xzf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}
# Fix env-script-interpreter rpmlint error
find %{buildroot}%{src_install_dir} -type f -name "*.js" -exec sed -i 's|#!.*%{_bindir}/env node|#!%{_bindir}/node|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!.*%{_bindir}/env python2.7|#!%{_bindir}/python2.7|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!.*%{_bindir}/env python|#!%{_bindir}/python|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.rb" -exec sed -i 's|#!.*%{_bindir}/env ruby|#!%{_bindir}/ruby|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!.*%{_bindir}/env bash|#!/bin/bash|' "{}" +
# And stop requiring ridiculously old Python version
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!%{_bindir}/python2.4|#!%{_bindir}/python2.7|' "{}" +
# Fix spurious-executable-perm rpmlint error
chmod -x %{buildroot}%{src_install_dir}/src/google/protobuf/arenastring.h
chmod -x %{buildroot}%{src_install_dir}/src/google/protobuf/reflection.h
# Fix version-control-internal-file rpmlint warning
find %{buildroot}%{src_install_dir} -type f -name ".gitignore" -exec rm -f "{}" +

%fdupes %{buildroot}%{_prefix}

%post -n libprotobuf%{sover} -p /sbin/ldconfig
%postun -n libprotobuf%{sover} -p /sbin/ldconfig
%post -n libprotoc%{sover} -p /sbin/ldconfig
%postun -n libprotoc%{sover} -p /sbin/ldconfig
%post -n libprotobuf-lite%{sover} -p /sbin/ldconfig
%postun -n libprotobuf-lite%{sover} -p /sbin/ldconfig

%files -n libprotobuf%{sover}
%license LICENSE
%{_libdir}/libprotobuf-3.%{version}.so

%files -n libprotoc%{sover}
%{_libdir}/libprotoc-3.%{version}.so

%files -n libprotobuf-lite%{sover}
%{_libdir}/libprotobuf-lite-3.%{version}.so

%files devel
%doc CHANGES.txt CONTRIBUTORS.txt README.md
%{_bindir}/protoc
%{_includedir}/google
%{_libdir}/pkgconfig/*
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so
%{_datadir}/vim

%files source
%{src_install_dir}

%if %{with java}
%files -n %{name}-java -f java/.mfiles
%{_javadir}/%{name}.jar
%endif

%if %{with python2} && ! 0%{?python_subpackage_only}
%files -n python2-%{name}
%license LICENSE
%{python2_sitelib}/*
%endif

%if %{with python3} || ( %{with python2} && 0%{?python_subpackage_only} )
%files %{python_files %{name}}
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
