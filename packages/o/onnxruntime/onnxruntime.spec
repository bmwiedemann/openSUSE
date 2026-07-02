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
# eigen 3.4-branch snapshot ORT pins in cmake/deps.txt; bundled only on
# Leap/SLE (suse_version < 1699), whose system eigen is the older 3.4.0 release.
# (3.4.90 = the post-3.4.0 development version this snapshot reports.)
%define eigen_commit    1d8b82b0740839c0de7f1242a3585e3390ff5f33
%define eigen_ver       3.4.90

Name:           onnxruntime
Version:        1.27.0
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
# eigen (MPL-2.0) -- used only on Leap/SLE 16.x, whose system eigen is the 3.4.0
# release; that predates the ArrayBase min/max<NaNPropagation> overloads ORT's
# element_wise_ops.cc needs (added on eigen's 3.4 branch after the 3.4.0 tag).
# Factory ships eigen 5.0 and keeps using the system package (see %%prep / %%build).
Source25:       https://github.com/eigen-mirror/eigen/archive/%{eigen_commit}/eigen-%{eigen_commit}.zip

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
# System eigen3: Factory ships 5.0, which has the min/max<NaNPropagation>
# ArrayBase overloads ORT needs. Leap/SLE 16.x ship only the eigen 3.4.0
# release, which predates them, so there we bundle ORT's 3.4-branch snapshot
# instead (see Source25, %%prep and %%build) and do not require the system one.
%if 0%{?suse_version} >= 1699
BuildRequires:  eigen3-devel
%endif
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

# date/onnx/SafeInt are statically linked into the built libraries (the shared
# lib and the python extension); eigen too on Leap/SLE. Declared once here for
# bundled-library tracking.
Provides:       bundled(date) = %{date_ver}
Provides:       bundled(onnx) = %{onnx_ver}
Provides:       bundled(SafeInt) = %{safeint_ver}
%if 0%{?suse_version} < 1699
Provides:       bundled(eigen3) = %{eigen_ver}
%endif

%description
ONNX Runtime is a cross-platform inference and training machine-learning
accelerator. It is compatible with many popular ML/DNN frameworks,
including PyTorch, TensorFlow/Keras, scikit-learn, and more.

%if %{without python}
%package -n libonnxruntime%{sover}
Summary:        ONNX Runtime shared library
# date/onnx/SafeInt are statically linked into this library (see deps note above);
# eigen too on Leap/SLE.

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
# date/onnx/SafeInt are statically linked into the pybind extension (eigen too on
# Leap/SLE).
Requires:       python%{pysuff}-numpy
Requires:       python%{pysuff}-protobuf
Requires:       python%{pysuff}-flatbuffers
Requires:       python%{pysuff}-packaging
Requires:       python%{pysuff}-sympy

%description -n python%{pysuff}-onnxruntime
Python %{pyver} bindings for ONNX Runtime. Provides the 'onnxruntime'
Python package for running ONNX models with high performance.
%endif

%prep
%autosetup -p1

# Leap/SLE (suse_version < 1699) carry older system libraries than Factory; two
# ONNX Runtime assumptions break there. Both branches are skipped on Factory/
# Tumbleweed, which keep the upstream behaviour unchanged.
%if 0%{?suse_version} < 1699
# (1) Protobuf: the SLFO protobuf21 packages ship no CMake config, unlike Factory's
# protobuf21-devel which provides cmake(protobuf). ONNX Runtime declares Protobuf
# with "FIND_PACKAGE_ARGS NAMES Protobuf protobuf", and the NAMES keyword forces
# find_package into config-only mode -- so on Leap detection fails and the
# (disconnected) FetchContent fallback aborts configure. Switch that one declare to
# CMake's module-mode FindProtobuf, which locates the standard-path protobuf Leap
# does ship (/usr/include/google/protobuf, %{_libdir}/libprotobuf.so, /usr/bin/protoc)
# and creates the expected protobuf::* targets.
sed -i 's|FIND_PACKAGE_ARGS NAMES Protobuf protobuf|FIND_PACKAGE_ARGS MODULE|' \
    cmake/external/onnxruntime_external_deps.cmake
# (2) Abseil: the hardcoded ABSEIL_LIBS list is generated for abseil 20250814 and
# names targets (e.g. absl::tracing_internal) that the older system abseil on Leap
# (20240722) does not provide, which fails the link/generate step. Prune any list
# entry whose target does not exist; the symbols those targets would carry are not
# referenced by the targets the older abseil does provide.
cat >> cmake/external/abseil-cpp.cmake <<'EOF'

# openSUSE (injected by the spec): drop ABSEIL_LIBS entries absent from the system abseil.
foreach(_absl_lib IN LISTS ABSEIL_LIBS)
  if(NOT TARGET ${_absl_lib})
    list(REMOVE_ITEM ABSEIL_LIBS ${_absl_lib})
  endif()
endforeach()
EOF
# (3) Eigen: Leap/SLE ship the eigen 3.4.0 release, which predates the ArrayBase
# min/max<NaNPropagation> overloads ORT's element_wise_ops.cc uses (added on
# eigen's 3.4 maintenance branch after the 3.4.0 tag, and present in the post-3.4
# snapshot ORT pins in cmake/deps.txt). Drop system-eigen3.patch's find so
# FetchContent builds the bundled 3.4-branch snapshot instead (see %%build).
sed -i '/FIND_PACKAGE_ARGS NAMES Eigen3/d' cmake/external/eigen.cmake
%endif

mkdir _deps
# bundled deps openSUSE does not package: date, onnx, SafeInt
unzip -qo %{SOURCE11} -d _deps
unzip -qo %{SOURCE17} -d _deps
unzip -qo %{SOURCE21} -d _deps
%if 0%{?suse_version} < 1699
# eigen, bundled on Leap/SLE only (see the %%prep workaround block above)
unzip -qo %{SOURCE25} -d _deps
%endif

%build
# System libraries are selected by ONNX Runtime's own
# FETCHCONTENT_TRY_FIND_PACKAGE_MODE=OPT_IN: every dependency that declares
# FIND_PACKAGE_ARGS upstream (protobuf, abseil, re2, eigen3, flatbuffers,
# cpuinfo, boost/mp11, nlohmann_json, ms-gsl) is taken from the system, helped by
# the system-*.patch files.  Only date, onnx and SafeInt are not packaged by
# openSUSE; those fall back to the bundled source in FETCHCONTENT_SOURCE_DIR_<n>.
# (On Leap/SLE 16.x, eigen joins that bundled set -- its system 3.4.0 is too old;
# see Source25 and the %%prep eigen note.)
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
%if 0%{?suse_version} < 1699
    -DFETCHCONTENT_SOURCE_DIR_EIGEN3=%{_builddir}/%{name}-%{version}/_deps/eigen-%{eigen_commit} \
%endif
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
