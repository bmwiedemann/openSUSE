#
# spec file for package qpid-proton
#
# Copyright (c) 2023 SUSE LLC
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
%define oldpython python
%global         qpid_proton_soversion 11
%global         qpid_proton_core_soversion 10
%global         qpid_proton_cpp_soversion 12
%global         qpid_proton_proactor_soversion 1
# libqpid-proton dependency leaves detritus in __pycache__ on Red Hat which should be excluded from RPM
%if 0%{?fedora} || 0%{?rhel}
%define _unpackaged_files_terminate_build 0
%endif
Name:           qpid-proton
Version:        0.38.0
Release:        0
Summary:        A messaging library
License:        Apache-2.0
Group:          Productivity/Networking/Other
URL:            https://qpid.apache.org/proton/
Source0:        https://www.apache.org/dist/qpid/proton/%{version}/%{name}-%{version}.tar.gz
# devel files in test package
Source99:       qpid-proton-rpmlintrc
Patch0:         qpid-proton-openssl-3.0.0.patch
# PATCH-FIX-OPENSUSE qpid-oythonbuild.patch -- disable compiling with wrong interpreter
Patch1:         qpid-pythonbuild.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig >= 2.0.9
%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
%define python_files() -n python3-%{**}
%define python_sitearch %python3_sitearch
%endif

%description
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton%{qpid_proton_soversion}
Summary:        C library for Qpid Proton
Group:          System/Libraries

%description -n libqpid-proton%{qpid_proton_soversion}
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton-core%{qpid_proton_core_soversion}
Summary:        Core library for Qpid Proton
# Moved to its own package due to different so version
Conflicts:      libqpid-proton10 <= 0.34.0

%description -n libqpid-proton-core%{qpid_proton_core_soversion}
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n qpid-proton-test
Summary:        Test files for Qpid Proton
Group:          Development/Libraries/C and C++

%description -n qpid-proton-test
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton-cpp%{qpid_proton_cpp_soversion}
Summary:        C++ library for Qpid Proton
Group:          System/Libraries

%description -n libqpid-proton-cpp%{qpid_proton_cpp_soversion}
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton-proactor%{qpid_proton_proactor_soversion}
Summary:        Proactor library for Qpid Proton
Group:          System/Libraries

%description -n libqpid-proton-proactor%{qpid_proton_proactor_soversion}
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package devel
Summary:        Development libraries for writing messaging apps with Qpid Proton
Group:          Development/Libraries/C and C++
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
Requires:       libqpid-proton-core%{qpid_proton_core_soversion} = %{version}-%{release}
Requires:       libqpid-proton-cpp%{qpid_proton_cpp_soversion} = %{version}-%{release}

%description devel
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package devel-doc
Summary:        Documentation for the C development libraries for Qpid Proton
Group:          Documentation/Other
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
BuildArch:      noarch

%description devel-doc
Proton is a messaging library.

This subpackage contains the documentation.

%if 0%{?python_subpackage_only}
# NOTE: the name on pypi for the package is python-qpid-proton so the name
# for the RPM package should be <flavor>-python-qpid-proton (python-$pypi_name)
%package -n python-python-qpid-proton
Summary:        Python language bindings for the Qpid Proton messaging framework
Group:          Development/Libraries/Python
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
# These will automatically be rewritten for the python flavors
# including additional python- for python2 and python3- for the primary provider
# flavor
Provides:       python-qpid-proton = %{version}
Obsoletes:      python-qpid-proton < %{version}

%description -n python-python-qpid-proton
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%else
# for distributions with no support for python_subpackage_only

%package -n python3-python-qpid-proton
Summary:        Python language bindings for the Qpid Proton messaging framework
Group:          Development/Libraries/Python
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
Provides:       python3-qpid-proton = %{version}
Obsoletes:      python3-qpid-proton < %{version}

%description -n python3-python-qpid-proton
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.
%endif

%prep
%autosetup -p1

%build
%cmake \
    -DPROTON_DISABLE_RPATH=true \
    -DNOBUILD_RUBY=1 \
    -DNOBUILD_PHP=1 \
    -DSYSINSTALL_PERL=1 \
    -DSYSINSTALL_PYTHON=1 \
    -DCHECK_SYSINSTALL_PYTHON=0 \
    "-DCMAKE_C_FLAGS=$CFLAGS -Wno-deprecated-declarations"

make %{?_smp_mflags} all docs
# build from the created sdist for all enabled python flavors
pushd python/dist
# Note: never python_expand in the root source tree. It removes the build/ directory
%python_build
popd

%install
%cmake_install

pushd build/python/dist
%python_install
%python_expand chmod +x %{buildroot}%{$python_sitearch}/*_cproton*.so
popd

find %{buildroot}%{_datadir}/proton/examples/ -type f | xargs chmod -x

mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/proton/docs/* %{buildroot}%{_docdir}/%{name}/

%fdupes %{buildroot}

%post -n libqpid-proton%{qpid_proton_soversion} -p /sbin/ldconfig
%postun -n libqpid-proton%{qpid_proton_soversion} -p /sbin/ldconfig
%post -n libqpid-proton-core%{qpid_proton_core_soversion} -p /sbin/ldconfig
%postun -n libqpid-proton-core%{qpid_proton_core_soversion} -p /sbin/ldconfig
%post -n libqpid-proton-cpp%{qpid_proton_cpp_soversion} -p /sbin/ldconfig
%postun -n libqpid-proton-cpp%{qpid_proton_cpp_soversion} -p /sbin/ldconfig
%post -n libqpid-proton-proactor%{qpid_proton_proactor_soversion} -p /sbin/ldconfig
%postun -n libqpid-proton-proactor%{qpid_proton_proactor_soversion} -p /sbin/ldconfig

%files -n libqpid-proton%{qpid_proton_soversion}
%{_libdir}/libqpid-proton.so.*

%files -n libqpid-proton-core%{qpid_proton_core_soversion}
%{_libdir}/libqpid-proton-core.so.*

%files -n libqpid-proton-cpp%{qpid_proton_cpp_soversion}
%{_libdir}/libqpid-proton-cpp.so.*

%files -n libqpid-proton-proactor%{qpid_proton_proactor_soversion}
%{_libdir}/libqpid-proton-proactor.so.*

%files test
%dir %{_datadir}/proton/tests
%{_datadir}/proton/tests/*

%files devel
%{_includedir}/proton
%{_libdir}/libqpid-proton.so
%{_libdir}/libqpid-proton-core.so
%{_libdir}/libqpid-proton-cpp.so
%{_libdir}/libqpid-proton-proactor.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{_libdir}/pkgconfig/libqpid-proton-core.pc
%{_libdir}/pkgconfig/libqpid-proton-cpp.pc
%{_libdir}/pkgconfig/libqpid-proton-proactor.pc
%dir %{_libdir}/cmake/Proton
%dir %{_libdir}/cmake/ProtonCpp
%{_libdir}/cmake/Proton/*.cmake
%{_libdir}/cmake/ProtonCpp/*.cmake

%files devel-doc
%{_datadir}/proton/CMakeLists.txt
%{_datadir}/proton/LICENSE.txt
%dir %{_datadir}/proton
%doc %{_datadir}/proton/README.md
%{_datadir}/proton/examples
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/api-c
%{_docdir}/%{name}/api-cpp

%files %{python_files python-qpid-proton}
%{python_sitearch}/*_cproton*.so
%{python_sitearch}/cproton.py*
%pycache_only %{python_sitearch}/__pycache__/cproton*
%{python_sitearch}/proton
%{python_sitearch}/python_qpid_proton-%{version}*-info

%changelog
