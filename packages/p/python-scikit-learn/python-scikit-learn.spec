#
# spec file for package python-scikit-learn
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


%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
%bcond_with extratest
Name:           python-scikit-learn
Version:        1.0.2
Release:        0
Summary:        Python modules for machine learning and data mining
License:        BSD-3-Clause
URL:            https://scikit-learn.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit-learn-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.28.5}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module joblib >= 0.11}
BuildRequires:  %{python_module numpy-devel >= 1.14.6}
BuildRequires:  %{python_module scipy >= 1.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module threadpoolctl >= 2.0.0}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  openblas-devel
BuildRequires:  python-rpm-macros
Requires:       python-joblib >= 0.11
Requires:       python-numpy >= 1.14.6
Requires:       python-scipy >= 1.0.0
Requires:       python-threadpoolctl >= 2.0.0
Requires:       python-xml
Provides:       python-sklearn
Suggests:       python-matplotlib
Suggests:       python-pandas
Suggests:       python-seaborn
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       sklearn
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 4.0}
%if %{with extratest}
BuildRequires:  %{python_module matplotlib >= 2.1.1}
BuildRequires:  %{python_module pandas >= 0.25.0}
BuildRequires:  %{python_module scikit-image >= 0.13}
%endif
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

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Precision-related errors on non-x86 platforms
%ifarch %{ix86} x86_64
%check
export SKLEARN_SKIP_NETWORK_TESTS=1
NO_TESTS="test_feature_importance_regression or test_minibatch_with_many_reassignments"
NO_TESTS+=" or test_sparse_coder_parallel_mmap or test_explained_variances"
# test_negative_sample_weights_mask_all_samples[weights-are-zero-NuSVC] Fatal Python error: Aborted
NO_TESTS+=" or test_negative_sample_weights_mask_all_samples"
# Disable test_fetch_openml_verify_checksum for now, no clue why it fail.
NO_TESTS+=" or test_fetch_openml_verify_checksum[True]"
NO_TESTS+=" or test_fetch_openml_verify_checksum[False]"

# Precision-related errors on 32 bit arch
# https://github.com/scikit-learn/scikit-learn/issues/19230
%ifarch i586 %{arm}
NO_TESTS+=" or test_convergence_dtype_consistency"
%endif

mkdir test_dir
pushd test_dir
%pytest_arch -p no:cacheprovider -v -k "not ($NO_TESTS)" %{buildroot}%{$python_sitearch}/sklearn
popd
%endif

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitearch}/sklearn/
%{python_sitearch}/scikit_learn-%{version}*-info

%changelog
