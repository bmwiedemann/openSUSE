#
# spec file for package python-joblib
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


%{?sle15_python_module_pythons}
Name:           python-joblib
Version:        1.5.3
Release:        0
Summary:        Module for using Python functions as pipeline jobs
License:        BSD-3-Clause
URL:            https://github.com/joblib/joblib
Source:         https://files.pythonhosted.org/packages/source/j/joblib/joblib-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Also avoid a DeprecationWarning when using fork() under
# multiprocessing
Patch1:         also-filter-new-fork-warning.patch
# PATCH-FIX-UPSTREAM fix-tests-numpy-2.4.patch gh#joblib/joblib#1770
Patch2:         fix-tests-numpy-2.4.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module threadpoolctl}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-lz4
Recommends:     python-numpy
Recommends:     python-psutil
Suggests:       python-dask-distributed
BuildArch:      noarch
%python_subpackages

%description
Joblib is a set of tools to provide lightweight pipelining in
Python. In particular, joblib offers:

  1. transparent disk-caching of the output values and lazy re-evaluation
     (memoize pattern)

  2. parallel computing

  3. logging and tracing of the execution

Joblib can handle large data and has specific optimizations for `numpy` arrays.

%prep
%autosetup -p1 -n joblib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# turn off unreliable tests across architectures
# https://bugzilla.suse.com/show_bug.cgi?id=1177209
# they have been seen failing for the first time on following
# architectures:
#  s390x:
#  test_hash_numpy_noncontiguous
#  test_hashes_are_different_between_c_and_fortran_contiguous_arrays
#  test_hashes_stay_the_same_with_numpy_objects
#  test_non_contiguous_array_pickling
#  x86_64:
#  test_multithreaded_parallel_termination_resource_tracker_silent
#  aarch64:
#  test_resource_tracker_silent_when_reference_cycles
#  test_child_raises_parent_exits_cleanly
#  i586:
#  test_nested_loop_error_in_grandchild_resource_tracker_silent
#
# always fails:
# test_parallel_call_cached_function_defined_in_jupyter
DISABLED_TESTS="test_multithreaded_parallel_termination_resource_tracker_silent or \
                test_resource_tracker_silent_when_reference_cycles or \
                test_child_raises_parent_exits_cleanly or \
                test_nested_loop_error_in_grandchild_resource_tracker_silent or \
                test_parallel_call_cached_function_defined_in_jupyter"
if [ $(python3 -c 'import sys; print(sys.byteorder)') != "little" ]; then
  DISABLED_TESTS+=" or test_joblib_pickle_across_python_versions or \
		test_hash_numpy_noncontiguous or \
                test_hashes_are_different_between_c_and_fortran_contiguous_arrays or \
                test_hashes_stay_the_same_with_numpy_objects or \
                test_non_contiguous_array_pickling"
fi
%pytest -k "not ($DISABLED_TESTS)"

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/joblib-%{version}.dist-info
%{python_sitelib}/joblib/

%changelog
