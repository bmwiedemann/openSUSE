#
# spec file for package python-pyarrow
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
%bcond_with xsimd
%define plainpython python
# See git submodule /testing pointing to the correct revision
%define arrow_testing_commit d2a13712303498963395318a4eb42872e66aead7
# See git submodule /cpp/submodules/parquet-testing pointing to the correct revision
%define parquet_testing_commit c7cf1374cf284c0c73024cd1437becea75558bf8
%if %{suse_version} <= 1500
# requires __has_builtin with keywords
%define gccver 13
%endif
Name:           python-pyarrow
Version:        19.0.1
Release:        0
Summary:        Python library for Apache Arrow
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://arrow.apache.org/
# SourceRepository: https://github.com/apache/arrow
Source0:        apache-arrow-%{version}.tar.gz
Source1:        arrow-testing-%{version}.tar.gz
Source2:        parquet-testing-%{version}.tar.gz
Source99:       python-pyarrow.rpmlintrc
BuildRequires:  %{python_module Cython >= 0.29.31}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.25}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?gccver}-c++
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  cmake(re2)
BuildRequires:  pkgconfig(arrow) = %{version}
BuildRequires:  pkgconfig(arrow-acero) = %{version}
BuildRequires:  pkgconfig(arrow-dataset) = %{version}
BuildRequires:  pkgconfig(bzip2) >= 1.0.8
BuildRequires:  pkgconfig(gmock) >= 1.10
BuildRequires:  pkgconfig(gtest) >= 1.10
BuildRequires:  pkgconfig(parquet) = %{version}
Requires:       python-numpy >= 1.25
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python library for Apache Arrow.

Apache Arrow defines a language-independent columnar
memory format for flat and hierarchical data, organized
for efficient analytic operations on modern hardware like
CPUs and GPUs. The Arrow memory format also supports
zero-copy reads for lightning-fast data access without
serialization overhead.

Arrow's libraries implement the format and provide building
blocks for a range of use cases, including high performance
analytics. Many popular projects use Arrow to ship columnar
data efficiently or as the basis for analytic engines.

%package devel
Summary:        Python library for Apache Arrow - header files
Requires:       python-Cython
Requires:       python-pyarrow = %{version}
Requires:       %plainpython(abi) = %python_version
Supplements:    (python-devel and python-pyarrow)

%description devel
Python library for Apache Arrow.

This package provides the header files within the python
platlib for consuming modules using cythonization.

%prep
%setup -n arrow-apache-arrow-%{version} -a1 -a2
%autopatch -p1

%build
pushd python
%{?gccver:export CXX=g++-%{gccver}}
%{?gccver:export CC=gcc-%{gccver}}
export CFLAGS="%{optflags}"
export PYARROW_BUILD_TYPE=relwithdebinfo
export PYARROW_BUILD_VERBOSE=1
%{?_smp_build_ncpus:export PYARROW_PARALLEL=%{_smp_build_ncpus}}
export PYARROW_WITH_HDFS=1
export PYARROW_WITH_DATASET=1
export PYARROW_WITH_PARQUET=1
export PYARROW_WITH_PARQUET_ENCRYPTION=0
export PYARROW_PARQUET_USE_SHARED=1
# x86_64-v1 does not have the advanced SIMD instructions. TW is stuck on it, we can't have -v3 through hwcaps as non-lib.
export PYARROW_CMAKE_OPTIONS=" \
%ifarch aarch64
   -DARROW_SIMD_LEVEL:STRING=%{?with_xsimd:NEON}%{!?with_xsimd:NONE} \
%else
   -DARROW_SIMD_LEVEL:STRING="NONE" \
%endif
   -DARROW_RUNTIME_SIMD_LEVEL:STRING=%{?with_xsimd:MAX}%{!?with_xsimd:NONE} \
"
%pyproject_wheel
popd

%install
pushd python
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
popd

%check
%{?gccver:export CXX=g++-%{gccver}}
%{?gccver:export CC=gcc-%{gccver}}
export ARROW_TEST_DATA="${PWD}/arrow-testing-%{arrow_testing_commit}/data"
export PARQUET_TEST_DATA="${PWD}/parquet-testing-%{parquet_testing_commit}/data"
# flaky tests
donttest="test_total_bytes_allocated"
donttest="$donttest or test_batch_lifetime"
# worker crashes, we don't have an s3 setup in obs anyway
donttest="$donttest or test_s3fs_limited_permissions_create_bucket"
%ifarch %{ix86} %{arm32}
# tests conversion to 64bit datatypes
donttest="$donttest or test_conversion"
donttest="$donttest or test_dictionary_to_numpy"
donttest="$donttest or test_foreign_buffer"
donttest="$donttest or test_from_numpy_nested"
donttest="$donttest or test_integer_limits"
donttest="$donttest or test_memory_map_large_seeks"
donttest="$donttest or test_primitive_serialization"
donttest="$donttest or test_python_file_large_seeks"
donttest="$donttest or test_schema_sizeof"
%endif
%pytest_arch --pyargs pyarrow -n auto -k "not ($donttest)"
%pytest_arch --pyargs pyarrow -n auto -k "$donttest" || :

%files %{python_files}
%doc README.md
%license LICENSE.txt NOTICE.txt
%{python_sitearch}/pyarrow
%exclude %{python_sitearch}/pyarrow/include
%exclude %{python_sitearch}/pyarrow/src
%exclude %{python_sitearch}/pyarrow/lib.h
%exclude %{python_sitearch}/pyarrow/lib_api.h
%{python_sitearch}/pyarrow-%{version}.dist-info

%files %{python_files devel}
%doc README.md
%license LICENSE.txt NOTICE.txt
%{python_sitearch}/pyarrow/include
%{python_sitearch}/pyarrow/src
%{python_sitearch}/pyarrow/lib.h
%{python_sitearch}/pyarrow/lib_api.h

%changelog
