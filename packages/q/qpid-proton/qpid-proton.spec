#
# spec file for package qpid-proton
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# SONAME majors live in c/versions.cmake + cpp/versions.cmake and move independently
%global         qpid_proton_soversion 11
%global         qpid_proton_core_soversion 10
%global         qpid_proton_cpp_soversion 12
%global         qpid_proton_proactor_soversion 1
%global         qpid_proton_tls_soversion 0
%define         python_subpackage_only 1
Name:           qpid-proton
Version:        0.40.0
Release:        0
Summary:        A messaging library
License:        Apache-2.0
URL:            https://qpid.apache.org/proton/
# archive.apache.org keeps old releases; downloads.apache.org drops them on the next
Source0:        https://archive.apache.org/dist/qpid/proton/%{version}/%{name}-%{version}.tar.gz
Source1:        https://archive.apache.org/dist/qpid/proton/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
# -test ships CTest helpers + catch.hpp deliberately; rpmlint calls them devel files
Source99:       qpid-proton-rpmlintrc
BuildRequires:  %{python_module base >= 3.9}
# pyproject build-system requirement
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# readelf and nm, used by the %%check linkage guard
BuildRequires:  binutils
BuildRequires:  cmake >= 3.16
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# for regenerating the expired test certificates in %%check
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
%python_subpackages

%description
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton%{qpid_proton_soversion}
Summary:        C library for Qpid Proton
# <= 0.34.0 shipped .so.11 from the mis-named libqpid-proton10, still in SLE-15 backports
Conflicts:      libqpid-proton10 <= 0.34.0

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
# sources and AMQP fixtures only
BuildArch:      noarch

%description -n qpid-proton-test
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton-cpp%{qpid_proton_cpp_soversion}
Summary:        C++ library for Qpid Proton

%description -n libqpid-proton-cpp%{qpid_proton_cpp_soversion}
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton-proactor%{qpid_proton_proactor_soversion}
Summary:        Proactor library for Qpid Proton

%description -n libqpid-proton-proactor%{qpid_proton_proactor_soversion}
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package -n libqpid-proton-tls%{qpid_proton_tls_soversion}
Summary:        Raw connection TLS library for Qpid Proton

%description -n libqpid-proton-tls%{qpid_proton_tls_soversion}
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

This subpackage contains the TLS engine for raw connections, which is
usable independently of the AMQP transport.

%package devel
Summary:        Development libraries for writing messaging apps with Qpid Proton
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
Requires:       libqpid-proton-core%{qpid_proton_core_soversion} = %{version}-%{release}
Requires:       libqpid-proton-cpp%{qpid_proton_cpp_soversion} = %{version}-%{release}
Requires:       libqpid-proton-proactor%{qpid_proton_proactor_soversion} = %{version}-%{release}
Requires:       libqpid-proton-tls%{qpid_proton_tls_soversion} = %{version}-%{release}

%description devel
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%package devel-doc
Summary:        Documentation for the C development libraries for Qpid Proton
BuildArch:      noarch

%description devel-doc
Proton is a messaging library.

This subpackage contains the documentation.

# NOTE: the name on pypi for the package is python-qpid-proton so the name
# for the RPM package should be <flavor>-python-qpid-proton (python-$pypi_name)

%package -n python-python-qpid-proton
Summary:        Python language bindings for the Qpid Proton messaging framework
# cffi module links the core library instead of bundling proton-c
Requires:       libqpid-proton-core%{qpid_proton_core_soversion} = %{version}-%{release}
Requires:       python-cffi >= 1.0.0
# These will automatically be rewritten for the python flavors
# including additional python- for python2 and python3- for the primary provider
# flavor
Provides:       python-qpid-proton = %{version}
Obsoletes:      python-qpid-proton < %{version}

%description -n python-python-qpid-proton
Proton is a messaging library. It can be used in brokers, client
libraries, routers, bridges and proxies. Proton is based on the AMQP
1.0 messaging standard.

%prep
%autosetup -p1

%build
# Options pinned rather than autodetected, so a package appearing in the build
# root cannot change what we ship:
# SASL_IMPL=none       Cyrus becomes the ONLY impl once linked, and libsasl2 pulls
#                      in no mechanism plugins -> every handshake fails. Enabling
#                      it needs Requires on the plugin packages.
# ENABLE_JSONCPP=OFF   enables connect.json loading from the CWD
# RUNTIME_CHECK=OFF    wraps every test in valgrind if valgrind is installed
# WARNING_ERROR=OFF    upstream -Werror (PROTON-2473): any new warning = FTBFS
# PYTHON_ISOLATED=NO   otherwise the test wiring pip-installs cffi from the network
# BUILD_TLS=ON         libqpid-proton-tls, off upstream. SONAME still 0, so the
#                      subpackage name must follow once upstream settles the ABI.
# Python_EXECUTABLE    else CMake picks the NEWEST interpreter and %%check cannot
#                      import the module it built
%cmake \
    -DBUILD_BINDINGS="cpp;python" \
    -DPython_EXECUTABLE=%{_bindir}/python3 \
    -DBUILD_PYTHON_UNBUNDLED_PKG=ON \
    -DBUILD_TESTING=ON \
    -DBUILD_TLS=ON \
    -DENABLE_BENCHMARKS=NO \
    -DENABLE_FUZZ_TESTING=NO \
    -DENABLE_PEP8_TEST=NO \
    -DENABLE_PYTHON_ISOLATED=NO \
    -DENABLE_TOX_TEST=NO \
    -DENABLE_JSONCPP=OFF \
    -DENABLE_WARNING_ERROR=OFF \
    -DRUNTIME_CHECK=OFF \
    -DSASL_IMPL=none

%cmake_build all docs

# $QPID_PYTHON_UNBUNDLING drives python/setup.py: unset bundles a static proton-c
# into cproton_ffi*.so, "unbundled" pkg-configs libqpid-proton-core instead.
# CMake's own .pc resolves prefix from ${pcfiledir}/../.., only valid once
# installed -- hence the build-tree stub. cffi forwards just -I/-L/-l and never an
# rpath, so the module ends up with a plain DT_NEEDED.
protonbuild=$PWD
mkdir -p "$protonbuild/pkgconfig"
# printf, not a here document: format_spec_file rewrites leading pkg-config
# keywords as if they were RPM tags
printf 'Name: Proton Core\nDescription: Qpid Proton C core library, uninstalled build tree\nVersion: %{version}\nCflags: -I%s/c/include\nLibs: -L%s/c -lqpid-proton-core\n' \
    "$protonbuild" "$protonbuild" > "$protonbuild/pkgconfig/libqpid-proton-core.pc"

# Build the wheel from a COPY: with BUILD_TESTING on, CMake drops an rpath-linked
# devtree cproton_ffi*.so into build/python. %%check still needs it; the package
# must not get it.
cp -a "$protonbuild/python" "$protonbuild/python-wheel"
pushd "$protonbuild/python-wheel"
rm -rf build dist cproton_ffi.c cproton_ffi*.so
export PKG_CONFIG_PATH="$protonbuild/pkgconfig${PKG_CONFIG_PATH:+:$PKG_CONFIG_PATH}"
export QPID_PYTHON_UNBUNDLING=unbundled
%pyproject_wheel
popd

%install
%cmake_install

pushd %{__builddir}/python-wheel
%pyproject_install
popd
# pip installs the extension 0644; it is a shared object
find %{buildroot} -name 'cproton_ffi*.so' -exec chmod 0755 {} +

# caught by upstream's include/proton/*.[hi] glob; nothing uses SWIG any more
rm %{buildroot}%{_includedir}/proton/cproton.i

# duplicate of the %%license copy
rm %{buildroot}%{_datadir}/proton/LICENSE.txt

mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/proton/docs/* %{buildroot}%{_docdir}/%{name}/
rmdir %{buildroot}%{_datadir}/proton/docs

# Fix the env shebangs but keep everything 0644: these are example/test *sources*,
# and making them executable would give -doc an interpreter dependency. Matched by
# name so doxygen output, .p12 keystores and .amqp fixtures keep their timestamps.
find %{buildroot}%{_datadir}/proton -type f \( -name '*.py' -o -name '*.sh' \) \
    -exec sed -i -e '1s|^#!/usr/bin/env python3$|#!%{_bindir}/python3|' \
                 -e '1s|^#!/usr/bin/env bash$|#!/bin/bash|' {} +
find %{buildroot}%{_datadir}/proton -type f -exec chmod 0644 {} +

# Per subpackage, never buildroot-wide: rpm does not preserve hardlinks across
# packages, so one flavour's site-packages must not point into another's.
%fdupes %{buildroot}%{_datadir}/proton/examples
%fdupes %{buildroot}%{_datadir}/proton/tests
%fdupes %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_libdir}/cmake
# Not %%python_expand: it renames ./build away, which here is the CMake build dir
for sitedir in %{buildroot}%{_libdir}/python3.*/site-packages; do
%fdupes "$sitedir"
done

%check
set -o pipefail
srcdir=$PWD

# The shipped test certs expired 2025-11-24 (PROTON-2908, fixed after 0.40.0), so
# every TLS test fails. Recipe from their own ssl-certs/README.txt. Deliberately
# here and not %%prep: after %%install the buildroot copies stay pristine, so only
# the tree the tests read is touched and the package stays reproducible.
for certdir in $(find . -type d -name ssl-certs); do
    pushd "$certdir"
    for cert in tserver:test_server tclient:test_client; do
        name=${cert%%:*}
        openssl req -x509 -newkey rsa:2048 -days 3650 \
            -subj "/CN=${cert#*:}/OU=proton_test" \
            -passout "pass:${name}pw" \
            -keyout "$name-private-key.pem" -out "$name-certificate.pem"
    done
    popd
done

pushd %{__builddir}
# python-integration-test: leak harness asserting absolute gc.get_objects() deltas
# python-test: run by hand below instead, see there
# --no-tests=error: registration is conditional, so a silent zero-test %%check
# would otherwise stay green. Not parallel: several tests assert ms budgets.
ctest --output-on-failure --force-new-ctest-process --no-tests=error \
    -E '^(python-integration-test|python-test)$'
popd

# By hand against the INSTALLED binding of EVERY flavour: ctest would run this once
# with whichever interpreter CMake picked, leaving the other flavour's extension
# untested. test_schedule_cancel_many is skipped -- 12345 cancellations in 10 s
# measures the build worker. timeout: out of ctest we lose its own cap.
mkdir -p %{__builddir}/pyverify
pushd %{__builddir}/pyverify
%{python_expand # every flavour, against what the package actually ships
PATH="$srcdir/%{__builddir}/c/tools:$PATH" \
PYTHONPATH=%{buildroot}%{$python_sitearch} \
LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
timeout 1800 $python "$srcdir/python/tests/proton-test" \
    -i proton_tests.reactor.ExceptionTest.test_schedule_cancel_many

# Guard: the binding is selected by an env var in %%build, so a change there could
# silently re-bundle proton-c. Assert both DT_NEEDED and the absence of local pn_*.
so=$(ls %{buildroot}%{$python_sitearch}/cproton_ffi*.so)
test -f "$so"
readelf -d "$so" | grep -q 'NEEDED.*libqpid-proton-core\.so\.%{qpid_proton_core_soversion}'
if nm -D --defined-only "$so" | grep -q ' T pn_message_free'; then
    echo "cproton_ffi defines proton's own symbols: the binding was bundled" >&2
    exit 1
fi
PYTHONPATH=%{buildroot}%{$python_sitearch} LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
    $python -c 'from proton import Message, VERSION; from proton.reactor import Container; print(VERSION)'
}
popd

%ldconfig_scriptlets -n libqpid-proton%{qpid_proton_soversion}
%ldconfig_scriptlets -n libqpid-proton-core%{qpid_proton_core_soversion}
%ldconfig_scriptlets -n libqpid-proton-cpp%{qpid_proton_cpp_soversion}
%ldconfig_scriptlets -n libqpid-proton-proactor%{qpid_proton_proactor_soversion}
%ldconfig_scriptlets -n libqpid-proton-tls%{qpid_proton_tls_soversion}

%files -n libqpid-proton%{qpid_proton_soversion}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libqpid-proton.so.*

%files -n libqpid-proton-core%{qpid_proton_core_soversion}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libqpid-proton-core.so.*

%files -n libqpid-proton-cpp%{qpid_proton_cpp_soversion}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libqpid-proton-cpp.so.*

%files -n libqpid-proton-proactor%{qpid_proton_proactor_soversion}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libqpid-proton-proactor.so.*

%files -n libqpid-proton-tls%{qpid_proton_tls_soversion}
%license LICENSE.txt NOTICE.txt
%{_libdir}/libqpid-proton-tls.so.*

%files test
%license LICENSE.txt NOTICE.txt
%dir %{_datadir}/proton
%{_datadir}/proton/tests

%files devel
%license LICENSE.txt NOTICE.txt
%{_includedir}/proton
%{_libdir}/libqpid-proton.so
%{_libdir}/libqpid-proton-core.so
%{_libdir}/libqpid-proton-cpp.so
%{_libdir}/libqpid-proton-proactor.so
%{_libdir}/libqpid-proton-tls.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{_libdir}/pkgconfig/libqpid-proton-core.pc
%{_libdir}/pkgconfig/libqpid-proton-cpp.pc
%{_libdir}/pkgconfig/libqpid-proton-proactor.pc
%{_libdir}/pkgconfig/libqpid-proton-tls.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Proton
%dir %{_libdir}/cmake/ProtonCpp
%{_libdir}/cmake/Proton/*.cmake
%{_libdir}/cmake/ProtonCpp/*.cmake

%files devel-doc
%license LICENSE.txt NOTICE.txt
%dir %{_datadir}/proton
%{_datadir}/proton/CMakeLists.txt
%doc %{_datadir}/proton/README.md
%{_datadir}/proton/examples
%{_docdir}/%{name}

%files %{python_files python-qpid-proton}
%license LICENSE.txt NOTICE.txt
%{python_sitearch}/cproton_ffi*.so
%{python_sitearch}/cproton.py
%pycache_only %{python_sitearch}/__pycache__/cproton*
%{python_sitearch}/proton
%{python_sitearch}/python_qpid_proton-%{version}*-info

%changelog
