#
# spec file for package python-ipysheet
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


%define         skip_python2 1
Name:           python-ipysheet
Version:        0.7.0
Release:        0
Summary:        Spreadsheet widget for the Jupyter notebook
License:        MIT
URL:            https://github.com/QuantStack/ipysheet
Source:         https://files.pythonhosted.org/packages/source/i/ipysheet/ipysheet-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module jupyter_packaging >= 0.7.9 with %python-jupyter_packaging < 1}
BuildRequires:  %{python_module jupyterlab >= 3.0.0 with %python-jupyterlab < 4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipysheet = %{version}
Requires:       (python-ipywidgets >= 7.5.0 with python-ipywidgets < 9)
Recommends:     python-pscript
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.5.0 with %python-ipywidgets < 9}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pscript}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Jupyter widget providing spreadsheets for the Jupyter notebook.

WARNING
Due to Handsontable licensing changes ipysheet is stuck witch the
outdated Handsontable version 6.2.2 (open-source). We recommend
not using ipysheet anymore. We suggest an alternative like
ipydatagrid.

This package provides the python interface.

%package -n jupyter-ipysheet
Summary:        Spreadsheet widget for the Jupyter notebook - Jupyterfiles
Requires:       python3-ipysheet = %{version}
Requires:       (jupyter-ipywidgets >= 7.5.0 with jupyter-ipywidgets < 9)
Requires:       (jupyter-jupyterlab or jupyter-notebook)
Provides:       jupyter-ipysheet = %{version}-%{release}

%description -n jupyter-ipysheet
A Jupyter widget providing spreadsheets for the Jupyter notebook.

This package provides the extensions for jupyter notebook and jupyterlab.

%prep
%autosetup -p1 -n ipysheet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipysheet/
%{python_sitelib}/ipysheet-%{version}.dist-info

%files -n jupyter-ipysheet
%license LICENSE
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/ipysheet.json
%{_jupyter_nbextension_dir}/ipysheet
%{_jupyter_labextensions_dir3}/ipysheet

%changelog
