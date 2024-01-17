#
# spec file for package python-lineup-widget
#
# Copyright (c) 2023 SUSE LLC
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


%define shortversion 4
Name:           python-lineup-widget
Version:        4.0.0
Release:        0
License:        MIT
Summary:        Wrapper around the LineUpjs library for multi attribute rankings
URL:            https://github.com/lineupjs/lineup_widget
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/l/lineup-widget/lineup_widget-%{version}.tar.gz
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module nbclassic}
BuildRequires:  %{python_module pandas >= 0.18.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-pandas >= 0.18.0
Requires:       (python-notebook < 7 or python-nbclassic)
Provides:       python-lineup_widget = %{version}-%{release}
BuildArch:      noarch

%python_subpackages

%description
LineUp is an interactive technique designed to create, visualize and explore
rankings of items based on a set of heterogeneous attributes.

This package provides the python interface.

%package     -n jupyter-lineup-widget
Summary:        Python package to export interactive HTML pages from Jupyter Notebooks
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       (jupyter-notebook < 7 or jupyter-nbclassic)
Requires:       python3dist(lineup-widget) = %{shortversion}
Suggests:       python3-lineup-widget

%description -n jupyter-lineup-widget
NBinteract is a Python package that creates interactive webpages from Jupyter
notebooks. NBinteract also has built-in support for interactive plotting.
These interactions are driven by data, not callbacks, allowing authors to focus
on the logic of their programs.

This package provides the jupyter notebook extensions.

%prep
%setup -q -n lineup_widget-%{version}

%build
%pyproject_wheel
sed -i 's/\r$//' README.md lineup_widget/__init__.py lineup_widget/static/*.svg
find . -type f -exec chmod a-x '{}' ';'

%install
%pyproject_install
%jupyter_move_config

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
export JUPYTER_CONFIG_DIR=%{buildroot}%{_jupyter_confdir}
%{python_expand # no python tests available
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import lineup_widget'
jupyter-%{$python_bin_suffix} nbclassic-extension list 2>&1 | grep 'lineup.*enabled'
}
rm -f %{buildroot}%{_jupyter_confdir}migrated

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/lineup_widget-%{version}.dist-info
%{python_sitelib}/lineup_widget/

%files -n jupyter-lineup-widget
%license LICENSE.txt
%doc README.md
%_jupyter_config %{_jupyter_nb_notebook_confdir}/lineup_widget.json
%{_jupyter_nbextension_dir}/lineup_widget/

%changelog
