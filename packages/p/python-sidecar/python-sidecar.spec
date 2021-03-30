#
# spec file for package python-sidecar
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
Name:           python-sidecar
%define mainver 0.5.0
%define labver  0.6.0
Version:        %{mainver}
Release:        0
Summary:        A sidecar output widget for JupyterLab
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/jupyterlab-sidecar
Source:         https://files.pythonhosted.org/packages/py2.py3/s/sidecar/sidecar-%{mainver}-py2.py3-none-any.whl 
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module jupyterlab >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyter_core-filesystem
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-sidecar-jupyterlab = %{labver}
Requires:       python-ipywidgets >= 7.6.0
Requires:       python-jupyterlab >= 3.0.0
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
Requires:       python3-sidecar = %{mainver}

%description -n jupyter-sidecar-jupyterlab
A sidecar output widget for JupyterLab.

This package provides the JupyterLab extension.

%prep
%setup -q -c -T

%build
# Not needed

%install
%{python_expand mkdir build; cp -a %{SOURCE0} build/}
%pyproject_install
%python_expand find %{buildroot}%{$python_sitelib} -name '*.py' -exec sed -i '1{/^#!.*env/ d}' {} \;
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}
cp %{buildroot}%{python3_sitelib}/sidecar-%{mainver}.dist-info/LICENSE.txt .

#%%check
# Tests need online connection using jlpm

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/sidecar-%{mainver}.dist-info/
%{python_sitelib}/sidecar/

%files -n jupyter-sidecar-jupyterlab
%license LICENSE.txt
%dir %{_jupyter_prefix}/labextensions
%dir %{_jupyter_prefix}/labextensions/@jupyter-widgets
%{_jupyter_prefix}/labextensions/@jupyter-widgets/jupyterlab-sidecar

%changelog
