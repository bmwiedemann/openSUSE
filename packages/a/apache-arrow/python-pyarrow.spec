#
# spec file for package python-pyarrow
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


%bcond_with xsimd
%define plainpython python
Name:           python-pyarrow
Version:        15.0.1
Release:        0
Summary:        Python library for Apache Arrow
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://arrow.apache.org/
# SourceRepository: https://github.com/apache/arrow
Source0:        apache-arrow-%{version}.tar.gz
Source99:       python-pyarrow.rpmlintrc
# PATCH-FIX-UPSTREAM apache-arrow-pr40230-glog-0.7.patch gh#apache/arrow#40230
Patch0:         apache-arrow-pr40230-glog-0.7.patch
# PATCH-FIX-UPSTREAM apache-arrow-pr40275-glog-0.7-2.patch gh#apache/arrow#40275
Patch1:         apache-arrow-pr40275-glog-0.7-2.patch
BuildRequires:  %{python_module Cython >= 0.29.31}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.16.6 with %python-numpy-devel < 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  apache-arrow-acero-devel-static = %{version}
BuildRequires:  apache-arrow-dataset-devel-static = %{version}
BuildRequires:  apache-arrow-devel = %{version}
BuildRequires:  apache-arrow-devel-static = %{version}
BuildRequires:  apache-parquet-devel = %{version}
BuildRequires:  apache-parquet-devel-static = %{version}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libzstd-devel-static
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  cmake(re2)
BuildRequires:  pkgconfig(bzip2) >= 1.0.8
BuildRequires:  pkgconfig(gmock) >= 1.10
BuildRequires:  pkgconfig(gtest) >= 1.10
Requires:       (python-numpy >= 1.16.6 with python-numpy < 2)
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest-lazy-fixture}
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
%autosetup -p1 -n arrow-apache-arrow-%{version}
# we disabled the jemalloc backend in apache-arrow
sed -i 's/should_have_jemalloc = sys.platform == "linux"/should_have_jemalloc = False/' python/pyarrow/tests/test_memory.py

%build
pushd python
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
# flaky
donttest="test_total_bytes_allocated"
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
