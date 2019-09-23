#
# spec file for package python-lineup-widget
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lineup-widget
Version:        1.0.7
Release:        0
License:        MIT
Summary:        Wrapper around the LineUpjs library for multi attribute rankings
Url:            https://github.com/datavisyn/lineup_widget
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/l/lineup-widget/lineup_widget-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/lineupjs/lineup_widget/v%{version}/LICENSE.txt
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pandas >= 0.18.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-notebook
Requires:       python-pandas >= 0.18.0
BuildArch:      noarch

%python_subpackages

%description
LineUp is an interactive technique designed to create, visualize and explore
rankings of items based on a set of heterogeneous attributes. 

This package provides the python interface.

%package     -n jupyter-lineup-widget
Summary:        Python package to export interactive HTML pages from Jupyter Notebooks
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-notebook
Requires:       python3-lineup-widget = %{version}

%description -n jupyter-lineup-widget
NBinteract is a Python package that creates interactive webpages from Jupyter
notebooks. NBinteract also has built-in support for interactive plotting.
These interactions are driven by data, not callbacks, allowing authors to focus
on the logic of their programs.

This package provides the jupyter notebook extensions.

%prep
%setup -q -n lineup_widget-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%jupyter_move_config

chmod a-x %{buildroot}%{_jupyter_nb_notebook_confdir}/lineup_widget.json
chmod a-x %{buildroot}%{_jupyter_nbextension_dir}/lineup_widget/*
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/lineup_widget-%{version}-py*.egg-info/*
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/lineup_widget/*.py
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/lineup_widget/static/*

%python_expand sed -i 's/\r$//' %{buildroot}%{$python_sitelib}/lineup_widget/__init__.py
%python_expand sed -i 's/\r$//' %{buildroot}%{$python_sitelib}/lineup_widget/static/*.svg
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/lineup_widget-%{version}-py*.egg-info
%{python_sitelib}/lineup_widget/

%files -n jupyter-lineup-widget
%license LICENSE.txt
%doc README.md
%config %{_jupyter_nb_notebook_confdir}/lineup_widget.json
%{_jupyter_nbextension_dir}/lineup_widget/

%changelog
