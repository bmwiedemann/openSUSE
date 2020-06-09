#
# spec file for package python-qgrid
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
Name:           python-qgrid
Version:        1.3.1
Release:        0
Summary:        Grid for sorting and filtering DataFrames in Jupyter notebooks
License:        Apache-2.0
URL:            https://github.com/quantopian/qgrid
Source:         https://files.pythonhosted.org/packages/source/q/qgrid/qgrid-%{version}.tar.gz
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module notebook >= 4.0.0}
BuildRequires:  %{python_module pandas >= 0.18.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-qgrid = %{version}
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-notebook >= 4.0.0
Requires:       python-pandas >= 0.18.0
BuildArch:      noarch
%python_subpackages

%description
An Interactive Grid for Sorting and Filtering DataFrames in Jupyter Notebook.

This package provides the python interface.

%package     -n jupyter-qgrid
Summary:        Grid for sorting and filtering DataFrames in Jupyter notebooks
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-notebook >= 4.0.0
Requires:       python3-qgrid = %{version}

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
%{python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/qgrid/tests/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/qgrid/tests/
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}/qgrid/tests/

PYTHONPATH=%{buildroot}%{python3_sitelib} jupyter nbextension install qgrid --user --py
PYTHONPATH=%{buildroot}%{python3_sitelib} jupyter nbextension enable qgrid --user --py

for f in ~/.jupyter/nbconfig/*.json ; do
    tdir=$( basename -s .json ${f} )
    install -Dm 644 ${f} %{buildroot}%{_jupyter_nb_confdir}/${tdir}.d/qgrid.json
done

%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{_jupyter_confdir}}

%check
# test_period_object_column - fails on serialization
%pytest -k 'not test_period_object_column'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/qgrid/
%{python_sitelib}/qgrid-%{version}-py*.egg-info

%files -n jupyter-qgrid
%license LICENSE
%{_jupyter_nbextension_dir}/qgrid/
%config %{_jupyter_nb_notebook_confdir}/qgrid.json

%changelog
