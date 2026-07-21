#
# spec file for package python-dask-glm
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


Name:           python-dask-glm
Version:        0.4.0
Release:        0
Summary:        Generalized Linear Models with Dask
License:        BSD-3-Clause
URL:            https://github.com/dask/dask-glm
Source:         https://files.pythonhosted.org/packages/source/d/dask-glm/dask_glm-%{version}.tar.gz
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module distributed}
BuildRequires:  %{python_module multipledispatch}
BuildRequires:  %{python_module numba}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sparse}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
# scipy/numba dlopen libopenblas.so.0 when the package is imported
BuildRequires:  libopenblas_pthreads0
BuildRequires:  python-rpm-macros
Requires:       python-cloudpickle
Requires:       python-dask
Requires:       python-distributed
Requires:       python-multipledispatch
Requires:       python-numba
Requires:       python-numpy
Requires:       python-scikit-learn
Requires:       python-scipy
Requires:       python-sparse
BuildArch:      noarch
%python_subpackages

%description
Generalized Linear Models with Dask.

%prep
%autosetup -p1 -n dask_glm-%{version}
# setuptools_scm yields 0.0.0 from the sdist even with PRETEND_VERSION set;
# pin the version statically instead
sed -i -e 's/^dynamic = \["version"\]/version = "%{version}"/' \
       -e '/^\[tool\.setuptools_scm\]/,/^local_scheme/d' pyproject.toml

%build
# setuptools_scm (v8) can't derive the version from the sdist (no .git); the
# generic PRETEND var is ignored, so use the package-specific one
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_DASK_GLM=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# %%pyproject_check_import is a Fedora macro; smoke-test the import directly
export LD_LIBRARY_PATH=%{_libdir}/openblas-pthreads${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import dask_glm"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/dask_glm
%{python_sitelib}/dask_glm-%{version}.dist-info

%changelog
