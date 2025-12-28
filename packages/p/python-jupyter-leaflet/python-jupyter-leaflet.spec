#
# spec file for package python-jupyter-leaflet
#
# Copyright (c) 2025 SUSE LLC
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


%define distversion 0.20
Name:           python-jupyter-leaflet
Version:        0.20.0
Release:        0
Summary:        Leaflet extensions for JupyterLab and Jupyter Notebook
License:        MIT
URL:            https://github.com/jupyter-widgets/ipyleaflet
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_leaflet/jupyter_leaflet-%{version}.tar.gz
BuildRequires:  %{python_module hatch-jupyter-builder >= 0.8.1}
BuildRequires:  %{python_module hatch-nodejs-version >= 0.3.2}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Provides:       python-jupyter_leaflet = %{version}-%{release}
Requires:       jupyter-leaflet = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nbclassic}
# /SECTION
%python_subpackages

%description
Interactive leaflet widget for the Jupyter notebook

The reference Python backend is ipyleaflet

%package     -n jupyter-leaflet
Summary:        Interactive leaflet widget for the Jupyter notebook - Jupyter files
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(jupyter-leaflet) = %{distversion}
Suggests:       python3-jupyter-leaflet

%description -n jupyter-leaflet
Interactive leaflet widget for the Jupyter notebook

This package provides the extensions for jupyter notebook and jupyterlab.

%prep
%autosetup -p1 -n jupyter_leaflet-%{version}
sed -i '/\[tool.hatch.build.hooks.jupyter-builder\]/ a \   skip-if-exists = ["labextension/static"]' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
export JUPYTER_CONFIG_PATH=%{buildroot}%{_jupyter_confdir}
%{python_expand # no python tests available
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import jupyter_leaflet'
jupyter-%{$python_bin_suffix} nbclassic-extension list 2>&1 | grep 'jupyter-leaflet.*enabled'
jupyter-%{$python_bin_suffix} labextension list 2>&1 | grep 'jupyter-leaflet.*enabled'
}

%files %{python_files}
%{python_sitelib}/jupyter_leaflet
%{python_sitelib}/jupyter_leaflet-%{version}.dist-info

%files -n jupyter-leaflet
%license LICENSE
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/jupyter-leaflet.json
%{_jupyter_nbextension_dir}/jupyter-leaflet
%{_jupyter_labextensions_dir3}/jupyter-leaflet

%changelog
