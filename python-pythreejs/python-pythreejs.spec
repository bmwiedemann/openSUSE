#
# spec file for package python-pythreejs
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pythreejs
%define mainver 2.1.1
%define labver  2.1.1
%define         skip_python2 1
Version:        %{mainver}
Release:        0
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/pythreejs
Source:         https://files.pythonhosted.org/packages/py2.py3/p/pythreejs/pythreejs-%{mainver}-py2.py3-none-any.whl
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-pythreejs = %{mainver}
Requires:       python-ipywidgets >= 7.2.1
Requires:       python-ipydatawidgets >= 1.1.1
Requires:       python-numpy >= 1.14
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.2.1}
BuildRequires:  %{python_module ipydatawidgets >= 1.1.1}
BuildRequires:  %{python_module numpy >= 1.14}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pytest-check-links}
# /SECTION
%python_subpackages

%description
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the python interface.

%package     -n jupyter-pythreejs
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
Requires:       jupyter-ipywidgets >= 7.2.1
Requires:       jupyter-ipydatawidgets >= 1.1.1
Requires:       jupyter-notebook
Requires:       python3-pythreejs = %{mainver}

%description -n jupyter-pythreejs
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the jupyter notebook extension.

%package     -n jupyter-pythreejs-jupyterlab
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
Version:        %{labver}
Requires:       jupyter-ipydatawidgets-jupyterlab >= 1.1.1
Requires:       jupyter-jupyterlab
Requires:       python3-pythreejs = %{mainver}

%description -n jupyter-pythreejs-jupyterlab
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the JupyterLab extension.

%prep
%setup -q -c -T

%build
# Not Needed

%install
%python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}
%python_expand sed -i 's/\r$//' %{buildroot}%{$python_sitelib}/pythreejs/*.py
%python_expand sed -i -e '/^#!\//, 1d' %{buildroot}%{$python_sitelib}/pythreejs/*.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{jupyter_move_config}
cp %{buildroot}%{python3_sitelib}/pythreejs-%{mainver}.dist-info/LICENSE .
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%files %{python_files}
%{python_sitelib}/pythreejs/
%{python_sitelib}/pythreejs-%{mainver}.dist-info/
%license %{python_sitelib}/pythreejs-%{mainver}.dist-info/LICENSE

%files -n jupyter-pythreejs
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/jupyter-threejs.json
%{_jupyter_nbextension_dir}/jupyter-threejs/

%files -n jupyter-pythreejs-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir}/jupyter-threejs-%{labver}.tgz

%changelog
