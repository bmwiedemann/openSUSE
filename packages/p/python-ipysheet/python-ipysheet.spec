#
# spec file for package python-ipysheet
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
Name:           python-ipysheet
Version:        0.4.4
Release:        0
Summary:        Spreadsheet widget for the Jupyter notebook
License:        MIT
URL:            https://github.com/QuantStack/ipysheet
Source:         https://files.pythonhosted.org/packages/source/i/ipysheet/ipysheet-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipysheet = %{version}
Requires:       python-flexx
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-notebook
Requires:       python-numpy
Requires:       python-pandas
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flexx >= 0.3.1}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Jupyter widget providing spreadsheets for the Jupyter notebook.

This package provides the python interface.

%package     -n jupyter-ipysheet
Summary:        Spreadsheet widget for the Jupyter notebook
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-notebook
Requires:       python3-ipysheet = %{version}

%description -n jupyter-ipysheet
A Jupyter widget providing spreadsheets for the Jupyter notebook.

This package provides the jupyter notebook extension.

%prep
%setup -q -n ipysheet-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%jupyter_move_config
%fdupes %{buildroot}%{_jupyter_nb_notebook_confdir}
%fdupes %{buildroot}%{_jupyter_nbextension_dir}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipysheet/
%{python_sitelib}/ipysheet-%{version}-py*.egg-info
%license LICENSE

%files -n jupyter-ipysheet
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/ipysheet.json
%{_jupyter_nbextension_dir}/ipysheet/

%changelog
