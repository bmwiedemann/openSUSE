#
# spec file for package onnxruntime
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == ""
%bcond_with python
%else
%bcond_without python
%if "%{flavor}" == "python311"
%define pyver  3.11
%define pysuff 311
%elif "%{flavor}" == "python313"
%define pyver  3.13
%define pysuff 313
%elif "%{flavor}" == "python314"
%define pyver  3.14
%define pysuff 314
%else
%{error:Unknown flavor '%{flavor}'}
%endif
%define python python%{pyver}
# %%python_sitearch is hardcoded to the system-default python3, not the flavor
# being built, so override it with the flavor-specific platlib path. Otherwise
# the %%install cleanup and %%files reference the wrong site-packages directory
# for any flavor whose version differs from the default interpreter.
%define python_sitearch %{_libdir}/python%{pyver}/site-packages
%endif

%global sover   1

# ---------------------------------------------------------------------------
# Dependencies
# ---------------------------------------------------------------------------
# ONNX Runtime is validated against the dependency versions pinned in its
# cmake/deps.txt, but it supports consuming system libraries instead.  We take
# everything from system packages and bundle only the three dependencies
# openSUSE does not ship:
#
#   System:  protobuf21, abseil-cpp + re2, eigen3, flatbuffers, cpuinfo,
#            boost (mp11), nlohmann_json, ms-gsl, pybind11.
#   Bundled: date, onnx (C++), SafeInt.
#
# System libraries are selected with small system-*.patch files (see Patch*
# below) plus ONNX Runtime's FETCHCONTENT_TRY_FIND_PACKAGE_MODE=OPT_IN; the
# bundled three are pointed at by FETCHCONTENT_SOURCE_DIR_<name> in %%build, and
# FETCHCONTENT_FULLY_DISCONNECTED=ON makes any missing system dep fail the build
# instead of attempting a download.
# ---------------------------------------------------------------------------
%define date_ver        3.0.1
%define onnx_ver        1.21.0
%define safeint_ver     3.0.28

# Statically linked bundled libraries, declared on every binary package that
# ships them (the shared library and the python extension module).
%define bundled_provides() \
Provides:       bundled(date) = %{date_ver} \
Provides:       bundled(onnx) = %{onnx_ver} \
Provides:       bundled(SafeInt) = %{safeint_ver} \
%{nil}

Name:           onnxruntime
Version:        1.26.0
Release:        0
Summary:        Cross-platform machine-learning inference and training accelerator
Group:          Development/Libraries/Other
License:        MIT AND Apache-2.0 AND MPL-2.0 AND BSL-1.0 AND BSD-2-Clause
URL:            https://github.com/microsoft/onnxruntime
Source0:        %{name}-%{version}.tar.zst

# -----------------------------------------------------------------------
# Bundled FetchContent dependencies (no network access in OBS).
# Only the deps openSUSE does not package are bundled; everything else comes
# from system libraries (see BuildRequires / %%build).
#
#   deps.txt name    →  FetchContent name  →  cmake variable
#   date             →  date               →  FETCHCONTENT_SOURCE_DIR_DATE
#   onnx             →  onnx               →  FETCHCONTENT_SOURCE_DIR_ONNX
#   safeint          →  safeint            →  FETCHCONTENT_SOURCE_DIR_SAFEINT
# -----------------------------------------------------------------------
# date (MIT)
Source11:       https://github.com/HowardHinnant/date/archive/refs/tags/v%{date_ver}.zip#/date-%{date_ver}.zip
# ONNX (Apache-2.0)
Source17:       https://github.com/onnx/onnx/archive/refs/tags/v%{onnx_ver}.zip#/onnx-%{onnx_ver}.zip
# SafeInt (MIT)
Source21:       https://github.com/dcleblanc/SafeInt/archive/refs/tags/%{safeint_ver}.zip#/SafeInt-%{safeint_ver}.zip

Patch0:         gcc-false-positives.patch
Patch1:         system-pybind11.patch
# Drop ORT's exact-version gate on abseil so the system abseil-cpp can be used
Patch2:         abseil-system-version.patch
# Let ORT find the system eigen3 via find_package
Patch3:         system-eigen3.patch
# Take Boost/mp11 from the system instead of the bundled mp11 snapshot
Patch4:         system-mp11.patch
# Take flatbuffers from the system (alias shared target; schemas regenerated in %%build)
Patch5:         system-flatbuffers.patch

# MLAS only supports these architectures
ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake >= 3.28
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 11
BuildRequires:  ninja
BuildRequires:  python3 >= 3.11
# python3-base guarantees the /usr/bin/python3 interpreter in the buildroot
# (the bare python3 meta does not ship it); used for the flatbuffers schema
# regeneration in %%build.
BuildRequires:  python3-base
BuildRequires:  unzip
BuildRequires:  zstd
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  execstack
# Dependencies taken from system libraries instead of bundling (see deps
# comment above). protobuf21 pins the exact 21.12 the runtime needs and
# provides protoc; do NOT pull the default protobuf-devel (34.x).
BuildRequires:  protobuf21-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  ms-gsl-devel
# abseil + re2 must be a matched pair (re2 is built against this abseil)
BuildRequires:  abseil-cpp-devel
BuildRequires:  re2-devel
# System eigen3 (openSUSE ships 5.0; ONNX Runtime 1.26 builds against it)
BuildRequires:  eigen3-devel
# flatbuffers-devel provides the headers, CMake config and /usr/bin/flatc
BuildRequires:  flatbuffers-devel
BuildRequires:  cpuinfo-devel
# Boost.Mp11 (header-only) + BoostConfig.cmake for find_package(Boost)
BuildRequires:  libboost_headers-devel

%if %{with python}
BuildRequires:  python%{pysuff}-devel
BuildRequires:  python%{pysuff}-pybind11-devel
BuildRequires:  python%{pysuff}-numpy-devel
BuildRequires:  python%{pysuff}-packaging
BuildRequires:  python%{pysuff}-pip
BuildRequires:  python%{pysuff}-setuptools
BuildRequires:  python%{pysuff}-wheel
%endif

%description
ONNX Runtime is a cross-platform inference and training machine-learning
accelerator. It is compatible with many popular ML/DNN frameworks,
including PyTorch, TensorFlow/Keras, scikit-learn, and more.

%if %{without python}
%package -n libonnxruntime%{sover}
Summary:        ONNX Runtime shared library
%{bundled_provides}

%description -n libonnxruntime%{sover}
This package contains the ONNX Runtime shared library needed at runtime
by applications and language bindings.

%package devel
Summary:        Development files for ONNX Runtime
Requires:       libonnxruntime%{sover} = %{version}

%description devel
Header files, CMake config, and the unversioned shared library symlink
for developing applications against ONNX Runtime.
%endif

%if %{with python}
%package -n python%{pysuff}-onnxruntime
Summary:        Python %{pyver} bindings for ONNX Runtime
Requires:       python%{pysuff}-numpy
Requires:       python%{pysuff}-protobuf
Requires:       python%{pysuff}-flatbuffers
Requires:       python%{pysuff}-packaging
Requires:       python%{pysuff}-sympy
%{bundled_provides}

%description -n python%{pysuff}-onnxruntime
Python %{pyver} bindings for ONNX Runtime. Provides the 'onnxruntime'
Python package for running ONNX models with high performance.
%endif

%prep
%autosetup -p1

mkdir _deps
# bundled deps openSUSE does not package: date, onnx, SafeInt
unzip -qo %{SOURCE11} -d _deps
unzip -qo %{SOURCE17} -d _deps
unzip -qo %{SOURCE21} -d _deps

%build
# System libraries are selected by ONNX Runtime's own
# FETCHCONTENT_TRY_FIND_PACKAGE_MODE=OPT_IN: every dependency that declares
# FIND_PACKAGE_ARGS upstream (protobuf, abseil, re2, eigen3, flatbuffers,
# cpuinfo, boost/mp11, nlohmann_json, ms-gsl) is taken from the system, helped by
# the system-*.patch files.  Only date, onnx and SafeInt are not packaged by
# openSUSE; those fall back to the bundled source in FETCHCONTENT_SOURCE_DIR_<n>.
# FETCHCONTENT_FULLY_DISCONNECTED=ON blocks network access, so a missing system
# dependency fails the build instead of being downloaded.

# Regenerate the flatbuffers schemas with the system flatc so the generated
# headers match the system flatbuffers runtime.
python3 onnxruntime/core/flatbuffers/schema/compile_schema.py --flatc %{_bindir}/flatc
python3 onnxruntime/lora/adapter_format/compile_schema.py --flatc %{_bindir}/flatc

%if %{with python}
export CXXFLAGS="${CXXFLAGS} -Wno-error=uninitialized"
%endif

pushd cmake
# Needed for static->shared linking with LTO
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# ONNX Runtime sets COMPILE_WARNING_AS_ERROR per target; newer GCC (15 on
# Tumbleweed) emits false positives (e.g. -Wfree-nonheap-object) that would
# abort the build, so disable warnings-as-errors for packaging (as NixOS does).
%cmake \
    --compile-no-warning-as-error \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DFETCHCONTENT_TRY_FIND_PACKAGE_MODE=OPT_IN \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
    -DONNX_CUSTOM_PROTOC_EXECUTABLE=%{_bindir}/protoc \
    -DFETCHCONTENT_SOURCE_DIR_DATE=%{_builddir}/%{name}-%{version}/_deps/date-%{date_ver} \
    -DFETCHCONTENT_SOURCE_DIR_ONNX=%{_builddir}/%{name}-%{version}/_deps/onnx-%{onnx_ver} \
    -DFETCHCONTENT_SOURCE_DIR_SAFEINT=%{_builddir}/%{name}-%{version}/_deps/SafeInt-%{safeint_ver} \
%if %{with python}
    -Donnxruntime_ENABLE_DLPACK=OFF \
    -Donnxruntime_ENABLE_PYTHON=ON \
    -DPython_EXECUTABLE=/usr/bin/python%{pyver} \
%else
    -Donnxruntime_ENABLE_PYTHON=OFF \
%endif
    -Donnxruntime_BUILD_SHARED_LIB=ON \
    -Donnxruntime_BUILD_UNIT_TESTS=OFF \
    -Donnxruntime_BUILD_BENCHMARKS=OFF \
    -Donnxruntime_ENABLE_TRAINING=OFF \
    -Donnxruntime_USE_FULL_PROTOBUF=ON

%cmake_build
popd

%install
%if %{with python}
cp -a cmake/build/onnxruntime/* onnxruntime/
python%{pyver} -m pip install \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    --no-deps \
    --no-build-isolation \
    .

rm -rf %{buildroot}%{_prefix}/bin
rm -f %{buildroot}%{python_sitearch}/onnxruntime/capi/libonnxruntime.so*
execstack -c %{buildroot}%{python_sitearch}/onnxruntime/capi/onnxruntime_pybind11_state.so
find %{buildroot}%{python_sitearch}/onnxruntime -name '*.so' -exec strip --strip-unneeded {} +
find %{buildroot}%{python_sitearch}/onnxruntime -name '*.py' -not -executable -exec sed -i '1{\@^#!/@d}' {} +
%fdupes %{buildroot}%{python_sitearch}
%else
pushd cmake
%cmake_install
popd
%ldconfig_scriptlets -n libonnxruntime%{sover}
%endif

%if %{without python}
%files -n libonnxruntime%{sover}
%license LICENSE
%doc ThirdPartyNotices.txt
%{_libdir}/libonnxruntime.so.%{sover}*

%files devel
%{_includedir}/onnxruntime/
%{_libdir}/libonnxruntime.so
%{_libdir}/libonnxruntime_providers_shared.so
%{_libdir}/cmake/onnxruntime/
%{_libdir}/pkgconfig/libonnxruntime.pc
%endif

%if %{with python}
%files -n python%{pysuff}-onnxruntime
%license LICENSE
%{python_sitearch}/onnxruntime/
%{python_sitearch}/onnxruntime-*.dist-info/
%endif

%changelog
