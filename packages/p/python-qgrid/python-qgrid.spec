#
# spec file for package python-qgrid
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_with     test
Name:           python-qgrid
Version:        1.1.1
Release:        0
Summary:        Grid for sorting and filtering DataFrames in Jupyter notebooks
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/quantopian/qgrid
Source:         https://files.pythonhosted.org/packages/source/q/qgrid/qgrid-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-ipywidgets >= 7.0.0
BuildRequires:  python-pandas >= 0.18.0
BuildRequires:  python-rpm-macros
Requires:       jupyter-qgrid = %{version}
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-pandas >= 0.18.0
Provides:       python-jupyter_qgrid = %{version}
Obsoletes:      python-jupyter_qgrid <= %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module pandas >= 0.18.0}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
An Interactive Grid for Sorting and Filtering DataFrames in Jupyter Notebook.

This package provides the python interface.

%package     -n jupyter-qgrid
Summary:        Grid for sorting and filtering DataFrames in Jupyter notebooks
Requires:       python-notebook >= 4.0.0
Requires:       python3-qgrid = %{version}
Requires(post): jupyter-notebook >= 4.0.0
Requires(post): jupyter-ipywidgets >= 7.0.0
Requires(post): python3-pandas >= 0.18.0
Requires(preun): jupyter-notebook >= 4.0.0
Requires(preun): jupyter-ipywidgets >= 7.0.0
Requires(preun): python3-pandas >= 0.18.0

%description -n jupyter-qgrid
An Interactive Grid for Sorting and Filtering DataFrames in Jupyter Notebook.

This package provides the jupyter notebook extension.

%prep
%setup -q -n qgrid-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_nbextension_dir}
%{python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/qgrid/tests/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/qgrid/tests/
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}/qgrid/tests/

%post -n jupyter-qgrid
%{jupyter_nbextension_enable qgrid}

%preun -n jupyter-qgrid
%{jupyter_nbextension_disable qgrid}

%if %{with test}
%check
export PYTHONDONTWRITEBYTECODE=1
%pytest qgrid
%endif

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/qgrid/
%{python_sitelib}/qgrid-%{version}-py*.egg-info

%files -n jupyter-qgrid
%license LICENSE
%{_jupyter_nbextension_dir}/qgrid/

%changelog
