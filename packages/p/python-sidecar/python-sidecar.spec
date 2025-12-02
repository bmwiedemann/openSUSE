#
# spec file for package python-sidecar
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-sidecar
%define mainver 0.8.0
%define shortver 0.8
%define labver  0.8.0
Version:        %{mainver}
Release:        0
Summary:        A sidecar output widget for JupyterLab
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/jupyterlab-sidecar
Source:         https://files.pythonhosted.org/packages/source/s/sidecar/sidecar-%{mainver}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-jupyter-builder}
BuildRequires:  %{python_module hatch-nodejs-version}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module ipywidgets >= 8 with %python-ipywidgets < 9}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyter_core-filesystem
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-sidecar-jupyterlab = %{labver}
Requires:       (python-ipywidgets >= 8 with python-ipywidgets < 9)
BuildArch:      noarch

%python_subpackages

%description
A sidecar output widget for JupyterLab.

This package provides the python interface.

%package     -n jupyter-sidecar-jupyterlab
Summary:        A sidecar output widget for JupyterLab
Group:          Development/Languages/Python
Version:        %{labver}
Release:        0
Requires:       jupyter-jupyterlab >= 3.0.0
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(sidecar) = %{shortver}
Suggests:       python3-sidecar

%description -n jupyter-sidecar-jupyterlab
A sidecar output widget for JupyterLab.

This package provides the JupyterLab extension.

%prep
%autosetup -p1 -n sidecar-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand find %{buildroot}%{$python_sitelib} -name '*.py' -exec sed -i '1{/^#!.*env/ d}' {} \;
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}
find %{buildroot}%{_prefix} -path '*/sidecar-%{mainver}.dist-info/licenses' -exec cp -r {} ./ ';'

#%%check
# Tests need online connection using jlpm

%files %{python_files}
%license licenses/*
%{python_sitelib}/sidecar-%{mainver}.dist-info/
%{python_sitelib}/sidecar/

%files -n jupyter-sidecar-jupyterlab
%license licenses/*
%dir %{_jupyter_prefix}/labextensions
%dir %{_jupyter_prefix}/labextensions/@jupyter-widgets
%{_jupyter_prefix}/labextensions/@jupyter-widgets/jupyterlab-sidecar

%changelog
