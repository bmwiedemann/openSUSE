#
# spec file for package python-scikit-learn
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-scikit-learn
Version:        0.23.2
Release:        0
Summary:        Python modules for machine learning and data mining
License:        BSD-3-Clause
URL:            https://scikit-learn.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit-learn-%{version}.tar.gz
# PATCH-FIX-UPSTREAM assert_allclose-for-FP-comparison.patch gh#scikit-learn/scikit-learn#18031 mcepl@suse.com
# Use assert_allclose instead of equality in FP comparison
Patch0:         assert_allclose-for-FP-comparison.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.13.3}
BuildRequires:  %{python_module scipy >= 0.19.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module threadpoolctl >= 2.0.0}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  openblas-devel
BuildRequires:  python-rpm-macros
Requires:       python-joblib >= 0.11
Requires:       python-matplotlib
Requires:       python-numpy >= 1.13.3
Requires:       python-scipy >= 0.19.1
Requires:       python-threadpoolctl >= 2.0.0
Requires:       python-xml
Provides:       python-sklearn
Provides:       sklearn
# SECTION test requirements
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module xml}
# /SECTION
%python_subpackages

%description
Scikit-learn is a python module for machine learning built on top of
scipy.

%prep
%autosetup -p1 -n scikit-learn-%{version}

rm -rf sklearn/.pytest_cache

%build
%python_build
%{python_expand for d in %{buildroot}%{$python_sitelib} %{buildroot}%{$python_sitearch}; do \
if [ -d $d ]; then
  # find $d -name \*.pyc -delete
  $python -m compileall $d
  $python -O -m compileall $d
fi
done }

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Precision-related errors on non-x86 platforms
%ifarch %{ix86} x86_64
%check
export SKLEARN_SKIP_NETWORK_TESTS=1
# export PYTHONDONTWRITEBYTECODE=1
NO_TESTS="test_feature_importance_regression or test_minibatch_with_many_reassignments"
NO_TESTS="$NO_TESTS or test_sparse_coder_parallel_mmap or test_explained_variances"
# test_negative_sample_weights_mask_all_samples[weights-are-zero-NuSVC] Fatal Python error: Aborted
NO_TESTS="$NO_TESTS or test_negative_sample_weights_mask_all_samples"
export NO_TESTS
mv sklearn sklearn_temp
rm -rf build _build.*
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
rm -rf build _build.*
py.test-%{$python_bin_suffix} -p no:cacheprovider -v -k "not ($NO_TESTS)" %{buildroot}%{$python_sitearch}/sklearn
}
mv sklearn_temp sklearn
%endif

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitearch}/sklearn/
%{python_sitearch}/scikit_learn-%{version}-py*.egg-info

%changelog
