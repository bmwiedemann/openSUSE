#
# spec file for package python-ipyleaflet
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


%define modname  ipyleaflet
%define         skip_python2 1
Name:           python-ipyleaflet
Version:        0.17.2
Release:        0
Summary:        A Jupyter widget for dynamic Leaflet maps
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/ipyleaflet
Source:         https://files.pythonhosted.org/packages/source/i/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module jupyter_packaging >= 0.12 with %python-jupyter_packaging < 1}
BuildRequires:  %{python_module jupyterlab >= 3 with %python-jupyterlab < 4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyleaflet = %{version}
Requires:       python-branca >= 0.5.0
Requires:       python-xyzservices >= 2021.8.1
Requires:       (python-ipywidgets >= 7.6.0 with python-ipywidgets < 9)
Requires:       (python-traittypes >= 0.2.1 with python-traittypes < 3)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.6.0 with %python-ipywidgets < 9}
BuildRequires:  %{python_module branca >= 0.5.0}
BuildRequires:  %{python_module traittypes >= 0.2.1 with %python-traittypes < 3}
BuildRequires:  %{python_module xyzservices >= 2021.8.1}
# /SECTION
%python_subpackages

%description
A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

This package provides the python interface.

%package     -n jupyter-ipyleaflet
Summary:        A Jupyter widget for dynamic Leaflet maps - Jupyter files
Requires:       python3-ipyleaflet = %{version}
Requires:       (jupyter-ipywidgets >= 7.6.0 with jupyter-ipywidgets < 9)
Requires:       (jupyter-jupyterlab or jupyter-notebook)
Provides:       jupyter-leaflet = %{version}-%{release}

%description -n jupyter-ipyleaflet
A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

This package provides the extensions for jupyter notebook and jupyterlab.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
export JUPYTER_CONFIG_DIR=%{buildroot}%{_jupyter_confdir}
%{python_expand # no python tests available
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import ipyleaflet'
jupyter-%{$python_bin_suffix} nbextension list 2>&1 | grep 'jupyter-leaflet.*enabled'
jupyter-%{$python_bin_suffix} labextension list 2>&1 | grep 'jupyter-leaflet.*enabled'
}
rm -f %{buildroot}%{_jupyter_confdir}migrated

%files %{python_files}
%license LICENSE
%{python_sitelib}/ipyleaflet/
%{python_sitelib}/ipyleaflet-%{version}.dist-info/

%files -n jupyter-ipyleaflet
%license LICENSE
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/jupyter-leaflet.json
%{_jupyter_nbextension_dir}/jupyter-leaflet/
%{_jupyter_labextensions_dir3}/jupyter-leaflet

%changelog
