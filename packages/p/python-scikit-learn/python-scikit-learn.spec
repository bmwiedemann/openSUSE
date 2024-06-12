#
# spec file for package python-scikit-learn
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


%{?sle15_python_module_pythons}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%else
%define psuffix -%{flavor}
%bcond_without test
%if "%{flavor}" != "test-py310"
%define skip_python310 1
%endif
%if "%{flavor}" != "test-py311"
%define skip_python311 1
%endif
%if "%{flavor}" != "test-py312"
%define skip_python312 1
%endif
# Skip empty buildsets, last one is for sle15_python_module_pythons
%if "%{shrink:%{pythons}}" == "" || ("%pythons" == "python311" && 0%{?skip_python311})
ExclusiveArch:  donotbuild
%define python_module() %flavor-not-enabled-in-buildset-for-suse-%{?suse_version}
%endif
%endif
# optionally test with extra packages
%bcond_with extratest
# enable pytest color output for local debugging: osc --with pytestcolor
%bcond_with pytestcolor

Name:           python-scikit-learn%{psuffix}
Version:        1.5.0
Release:        0
Summary:        Python modules for machine learning and data mining
License:        BSD-3-Clause
URL:            https://scikit-learn.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit_learn-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.0.10}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module joblib >= 1.2.0}
BuildRequires:  %{python_module meson-python}
BuildRequires:  %{python_module numpy-devel >= 1.19.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 1.6.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module threadpoolctl >= 2.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
# Default gcc in leap is gcc 7
%if 0%{?suse_version} == 1500 && 0%{?sle_version} <= 150600
BuildRequires:  gcc8-c++
BuildRequires:  gcc8-fortran
%else
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
%endif
BuildRequires:  openblas-devel
BuildRequires:  python-rpm-macros
# Check sklearn/_min_dependencies.py for dependencies
Requires:       python-joblib >= 1.2.0
Requires:       python-numpy >= 1.19.5
Requires:       python-scipy >= 1.6.0
Requires:       python-threadpoolctl >= 2.0.0
Suggests:       python-matplotlib >= 3.3.4
Suggests:       python-pandas
Suggests:       python-seaborn
Provides:       python-sklearn = %{version}-%{release}
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       sklearn = %{version}-%{release}
%endif
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pytest >= 7.1.2}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module scikit-learn = %{version}}
%if %{with extratest}
BuildRequires:  %{python_module matplotlib >= 3.3.4}
BuildRequires:  %{python_module pandas >= 1.1.5}
BuildRequires:  %{python_module scikit-image >= 0.17.2}
%endif
%endif
# /SECTION
%python_subpackages

%description
Scikit-learn is a python module for machine learning built on top of
scipy.

%prep
%autosetup -p1 -n scikit_learn-%{version}
rm -rf sklearn/.pytest_cache
%if !%{with pytestcolor}
sed -i '/--color=yes/d' setup.cfg
%endif

# Fix shebang for version, this is used during pyproject_wheel
sed -i 's|python|python3|' sklearn/_build_utils/version.py

%build
%if !%{with test}
%if 0%{?suse_version} == 1500 && 0%{?sle_version} <= 150600
export CC=gcc-8 CXX=g++-8
%endif
export CFLAGS="%{optflags}"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install

%{python_expand #
# Remove shebang from non executable
sed -i '/#!.*env python/d' %{buildroot}%{$python_sitearch}/sklearn/_build_utils/version.py
# Remove empty file
rm %{buildroot}%{$python_sitearch}/sklearn/_built_with_meson.py
# Fix file permissions
chmod 0644 %{buildroot}%{$python_sitearch}/sklearn/cluster/_optics.py
chmod 0644 %{buildroot}%{$python_sitearch}/sklearn/ensemble/tests/test_weight_boosting.py
}
%python_compileall

%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

# Remove devel files
%{python_expand #
rm -rf %{buildroot}%{$python_sitearch}/sklearn/svm/src
rm -rf %{buildroot}%{$python_sitearch}/sklearn/utils/src
}

%if %{with test}
%check
mkdir test_dir
pushd test_dir
export SKLEARN_SKIP_NETWORK_TESTS=1
NO_TESTS="testeverythingifnotmatch"
%ifarch %{ix86} %{arm}
# Precision-related errors on 32 bit
# https://github.com/scikit-learn/scikit-learn/issues/19230
NO_TESTS+=" or test_convergence_dtype_consistency"
NO_TESTS+=" or test_imputation_missing_value_in_test_array"
NO_TESTS+=" or test_graphviz_toy"
NO_TESTS+=" or test_forest_classifier_oob"
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
