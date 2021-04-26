#
# spec file for package python-ipyleaflet
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
Name:           python-ipyleaflet
Version:        0.13.6
Release:        0
Summary:        A Jupyter widget for dynamic Leaflet maps
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipyleaflet
Source:         https://files.pythonhosted.org/packages/py2.py3/i/ipyleaflet/ipyleaflet-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyleaflet = %{version}
Requires:       python-Shapely
Requires:       python-branca >= 0.3.1
Requires:       python-ipywidgets >= 7.6.0
Recommends:     python-geopandas
Recommends:     python-netCDF4
Recommends:     python-scipy
Recommends:     python-xarray
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module branca >= 0.3.1}
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module ipywidgets >= 7.6.0}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module notebook}
# /SECTION
%python_subpackages

%description
A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

This package provides the python interface.

%package     -n jupyter-ipyleaflet
Summary:        A Jupyter widget for dynamic Leaflet maps - Jupyter files
Requires:       jupyter-ipywidgets >= 7.0.0
Requires:       jupyter-jupyterlab
Requires:       jupyter-notebook
Requires:       python3-ipyleaflet = %{version}
Provides:       jupyter-leaflet = %{version}-%{release}

%description -n jupyter-ipyleaflet
A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

This package provides the extensions for jupyter notebook and jupyterlab.

%prep
%setup -q -c -T

%build
# Not Needed

%install
%pyproject_install %{SOURCE0}

%{jupyter_move_config}
%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

cp %{buildroot}%{python3_sitelib}/ipyleaflet-%{version}.dist-info/LICENSE .

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
export JUPYTER_CONFIG_DIR=%{buildroot}%{_jupyter_confdir}
%{python_expand # no python tests available
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import ipyleaflet'
jupyter-%{$python_bin_suffix} nbextension list 2>&1 | grep 'jupyter-leaflet.*enabled'
jupyter-%{$python_bin_suffix} labextension list 2>&1 | grep 'jupyter-leaflet.*enabled'
}

%files %{python_files}
%license LICENSE
%{python_sitelib}/ipyleaflet/
%{python_sitelib}/ipyleaflet-%{version}.dist-info/

%files -n jupyter-ipyleaflet
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/jupyter-leaflet.json
%{_jupyter_nbextension_dir}/jupyter-leaflet/
%dir %{_jupyter_prefix}/labextensions
%{_jupyter_prefix}/labextensions/jupyter-leaflet

%changelog
