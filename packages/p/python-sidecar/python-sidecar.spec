#
# spec file for package python-sidecar
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
%define         skip_python2 1
Name:           python-sidecar
%define mainver 0.2.0
%define labver  0.3.0
Version:        %{mainver}
Release:        0
License:        BSD-3-Clause
Summary:        A sidecar output widget for JupyterLab
Url:            https://github.com/jupyter-widgets/jupyterlab-sidecar
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/py2.py3/s/sidecar/sidecar-%{mainver}-py2.py3-none-any.whl 
BuildRequires:  python-rpm-macros
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-check-links}
# /SECTION
BuildRequires:  fdupes
Requires:       python-ipywidgets >= 7.0.0
Requires:       jupyter-jupyterlab
Requires:       jupyter-sidecar-jupyterlab = %{labver}
BuildArch:      noarch

%python_subpackages

%description
A sidecar output widget for JupyterLab.

This package provides the python interface.

%package     -n jupyter-sidecar-jupyterlab
Summary:        A sidecar output widget for JupyterLab
Version:        %{labver}
Requires:       jupyter-jupyterlab
Requires:       python3-sidecar = %{mainver}

%description -n jupyter-sidecar-jupyterlab
A sidecar output widget for JupyterLab.

This package provides the JupyterLab extension.

%prep
%setup -q -c -T

%build
# Not needed

%install
%python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}
cp %{buildroot}%{python3_sitelib}/sidecar-%{mainver}.dist-info/LICENSE.txt .

%files %{python_files}
%license %{python_sitelib}/sidecar-%{mainver}.dist-info/LICENSE.txt
%{python_sitelib}/sidecar-%{mainver}.dist-info/
%{python_sitelib}/sidecar/

%files -n jupyter-sidecar-jupyterlab
%license LICENSE.txt
%{_jupyter_labextensions_dir}/jupyter-widgets-jupyterlab-sidecar-%{labver}.tgz

%changelog
