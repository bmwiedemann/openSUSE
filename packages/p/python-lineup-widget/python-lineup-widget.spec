#
# spec file for package python-lineup-widget
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
Name:           python-lineup-widget
Version:        4.0.0
Release:        0
License:        MIT
Summary:        Wrapper around the LineUpjs library for multi attribute rankings
URL:            https://github.com/lineupjs/lineup_widget
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/l/lineup-widget/lineup_widget-%{version}.tar.gz
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

%build
%python_build
sed -i 's/\r$//' README.md lineup_widget/__init__.py lineup_widget/static/*.svg
find . -type f -exec chmod a-x '{}' ';'

%install
%python_install
%jupyter_move_config

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

#%%check
# no python unit tests

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
