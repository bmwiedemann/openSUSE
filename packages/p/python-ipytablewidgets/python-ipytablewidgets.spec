#
# spec file for package python-ipytablewidgets
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


Name:           python-ipytablewidgets
Version:        0.3.2
Release:        0
Summary:        Widgets to help facilitate reuse of large tables across widgets
License:        BSD-3-Clause
URL:            https://github.com/progressivis/ipytablewidgets
Source:         https://files.pythonhosted.org/packages/source/i/ipytablewidgets/ipytablewidgets-%{version}.tar.gz
BuildRequires:  %{python_module ipywidgets >= 7.5.0}
BuildRequires:  %{python_module jupyter_packaging}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module numpy >= 1.10.4}
BuildRequires:  %{python_module pandas >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traitlets >= 4.3.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-ipywidgets >= 7.5.0
Requires:       python-lz4
Requires:       python-numpy >= 1.10.4
Requires:       python-pandas >= 1.0.0
Requires:       python-traitlets >= 4.3.0
Recommends:     jupyter-ipytablewidgets
Recommends:     jupyter-ipytablewidgets-jupyterlab
BuildArch:      noarch
%python_subpackages

%description
Traitlets and widgets to efficiently data tables (e.g. Pandas DataFrame) using the jupyter notebook

ipytablewidgets is a set of widgets and traitlets to reuse of large tables such as Pandas DataFrames
across different widgets, and different packages.

The major parts of ipytablewidgets are:

- Traits/Widgets definitions
- Adapters to convert tables to those traits
- Serializers/deserializers to send the data across the network
- Apropriate javascript handling and representation of the data

%package -n jupyter-ipytablewidgets
Summary:        Jupyter Notebook extension for python-ipytablewidgets
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipytablewidgets) = %{version}
Suggests:       python3-ipytablewidgets

%description -n jupyter-ipytablewidgets
Traitlets and widgets to efficiently data tables (e.g. Pandas DataFrame) using the jupyter notebook

This package provides the jupyter notebook extension

%package -n jupyter-ipytablewidgets-jupyterlab
Summary:        Jupyterlab extension for python-ipytablewidgets
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipytablewidgets) = %{version}
Suggests:       python3-ipytablewidgets

%description -n jupyter-ipytablewidgets-jupyterlab
Traitlets and widgets to efficiently data tables (e.g. Pandas DataFrame) using the jupyter notebook

This package provides the jupyterlab extension

%prep
%setup -q -n ipytablewidgets-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# all tests are npm/js tests requiring network (Galata)

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ipytablewidgets
%{python_sitelib}/ipytablewidgets-%{version}.dist-info

%files -n jupyter-ipytablewidgets
%license LICENSE
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/jupyter-tablewidgets.json
%{_jupyter_nbextension_dir}/jupyter-tablewidgets

%files -n jupyter-ipytablewidgets-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir3}/jupyter-tablewidgets

%changelog
