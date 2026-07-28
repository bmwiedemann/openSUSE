#
# spec file for package python-dask-ml
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-dask-ml
Version:        2025.1.0
Release:        0
Summary:        A library for distributed and parallel machine learning
License:        BSD-3-Clause
URL:            https://github.com/dask/dask-ml
Source:         https://files.pythonhosted.org/packages/source/d/dask-ml/dask_ml-%{version}.tar.gz
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask-glm}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module distributed}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module multipledispatch}
BuildRequires:  %{python_module numba}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  fdupes
# scipy/numba dlopen libopenblas.so.0 when the package is imported
BuildRequires:  libopenblas_pthreads0
BuildRequires:  python-rpm-macros
Requires:       python-dask
Requires:       python-dask-array
Requires:       python-dask-dataframe
Requires:       python-dask-glm
Requires:       python-distributed
Requires:       python-multipledispatch
Requires:       python-numba
Requires:       python-numpy
Requires:       python-packaging
Requires:       python-pandas
Requires:       python-scikit-learn
Requires:       python-scipy
BuildArch:      noarch
%python_subpackages

%description
Dask-ML provides scalable machine learning in Python using Dask alongside
popular machine learning libraries like Scikit-Learn and XGBoost.

%prep
%autosetup -p1 -n dask_ml-%{version}

%build
# hatch-vcs (setuptools_scm) can't derive the version from the sdist (no .git);
# use the package-specific PRETEND var
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_DASK_ML=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# %%pyproject_check_import is a Fedora macro; smoke-test the import directly
export LD_LIBRARY_PATH=%{_libdir}/openblas-pthreads${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import dask_ml"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/dask_ml
%{python_sitelib}/dask_ml-%{version}.dist-info

%changelog
