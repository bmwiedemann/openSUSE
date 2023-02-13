#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test-py38"
%define psuffix -test-py38
%define skip_python39 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python38 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python38 1
%define skip_python39 1
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_with extratest
# enable pytest color output for local debugging: osc --with pytestcolor
%bcond_with pytestcolor
Name:           python-scikit-learn%{psuffix}
Version:        1.2.1
Release:        0
Summary:        Python modules for machine learning and data mining
License:        BSD-3-Clause
URL:            https://scikit-learn.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit-learn-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29.24}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module joblib >= 1.1.1}
BuildRequires:  %{python_module numpy-devel >= 1.17.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 1.3.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module threadpoolctl >= 2.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  openblas-devel
BuildRequires:  python-rpm-macros
# Check sklearn/_min_dependencies.py for dependencies
Requires:       python-joblib >= 1.0.0
Requires:       python-numpy >= 1.17.3
Requires:       python-scipy >= 1.3.2
Requires:       python-threadpoolctl >= 2.0.0
Requires:       python-xml
Suggests:       python-matplotlib >= 3.1.3
Suggests:       python-pandas
Suggests:       python-seaborn
Provides:       python-sklearn = %{version}-%{release}
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       sklearn = %{version}-%{release}
%endif
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pytest >= 5.3.1}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module scikit-learn = %{version}}
%if %{with extratest}
BuildRequires:  %{python_module matplotlib >= 3.1.3}
BuildRequires:  %{python_module pandas >= 1.0.5}
BuildRequires:  %{python_module scikit-image >= 0.16.2}
%endif
%endif
# /SECTION
%python_subpackages

%description
Scikit-learn is a python module for machine learning built on top of
scipy.

%prep
%autosetup -p1 -n scikit-learn-%{version}
rm -rf sklearn/.pytest_cache
%if !%{with pytestcolor}
sed -i '/--color=yes/d' setup.cfg
%endif

%build
%if !%{with test}
export CFLAGS="%{optflags}"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
mkdir test_dir
pushd test_dir
export SKLEARN_SKIP_NETWORK_TESTS=1
# fails with scipy 1.10 gh#scikit-learn/scikit-learn#25403
NO_TESTS="test_spectral_embedding_two_components"
%ifarch %{ix86} %{arm}
# Precision-related errors on 32 bit
# https://github.com/scikit-learn/scikit-learn/issues/19230
NO_TESTS+=" or test_convergence_dtype_consistency"
NO_TESTS+=" or test_imputation_missing_value_in_test_array"
%endif
%pytest_arch -v --pyargs sklearn -n auto -k "not ($NO_TESTS)"
popd
%endif

%if !%{with test}
%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitearch}/sklearn/
%{python_sitearch}/scikit_learn-%{version}.dist-info
%endif

%changelog
