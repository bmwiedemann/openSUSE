#
# spec file for package python-ipysheet
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python36 1
Name:           python-ipysheet
Version:        0.5.0
Release:        0
Summary:        Spreadsheet widget for the Jupyter notebook
License:        MIT
URL:            https://github.com/QuantStack/ipysheet
Source:         https://files.pythonhosted.org/packages/source/i/ipysheet/ipysheet-%{version}.tar.gz
BuildRequires:  %{python_module jupyter_packaging >= 0.7.9}
BuildRequires:  %{python_module jupyterlab >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ipywidgets >= 7.5.0
Requires:       python-jupyter-server >= 1.6
Recommends:     python-pscript
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.5.0}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter-server >= 1.6}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pscript}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Jupyter widget providing spreadsheets for the Jupyter notebook.

This package provides the python interface.

%prep
%setup -q -n ipysheet-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipysheet/
%{python_sitelib}/ipysheet-%{version}-py*.egg-info
%license LICENSE

%changelog
