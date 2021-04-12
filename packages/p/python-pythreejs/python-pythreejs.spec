#
# spec file for package python-pythreejs
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
%define mainver 2.2.1
%define labver  2.2.0
Name:           python-pythreejs
Version:        %{mainver}
Release:        0
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/pythreejs
# Get examples for testing from GitHub
Source0:        https://github.com/jupyter-widgets/pythreejs/archive/%{version}.tar.gz#/pythreejs-%{version}-gh.tar.gz
# but install from wheel for bundles js stuff
Source1:        https://files.pythonhosted.org/packages/py2.py3/p/pythreejs/pythreejs-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Recommends:     jupyter-pythreejs-jupyterlab = %{labver}
Requires:       jupyter-pythreejs = %{version}
Requires:       python-ipydatawidgets >= 1.1.1
Requires:       python-ipywidgets >= 7.2.1
Requires:       python-numpy >= 1.14
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipydatawidgets >= 1.1.1}
BuildRequires:  %{python_module ipywebrtc}
BuildRequires:  %{python_module ipywidgets >= 7.2.1}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module numpy >= 1.14}
BuildRequires:  %{python_module pytest-check-links}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the python interface.

%package     -n jupyter-pythreejs
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
Group:          Development/Languages/Python
Requires:       jupyter-ipydatawidgets >= 1.1.1
Requires:       jupyter-ipywidgets >= 7.2.1
Requires:       jupyter-notebook
Requires:       python3-pythreejs = %{mainver}

%description -n jupyter-pythreejs
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the jupyter notebook extension.

%package     -n jupyter-pythreejs-jupyterlab
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
Group:          Development/Languages/Python
Version:        %{labver}
Release:        0
Requires:       jupyter-ipydatawidgets-jupyterlab >= 1.1.1
Requires:       jupyter-jupyterlab
Requires:       python3-pythreejs = %{mainver}

%description -n jupyter-pythreejs-jupyterlab
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the JupyterLab extension.

%prep
%setup -q -n pythreejs-%{mainver}

%build
# Not Needed

%install
%{python_expand mkdir -p build/; cp -a %{SOURCE1} build/}
%pyproject_install
%python_expand sed -i 's/\r$//' %{buildroot}%{$python_sitelib}/pythreejs/*.py
%python_expand sed -i -e '/^#!\//, 1d' %{buildroot}%{$python_sitelib}/pythreejs/*.py
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%jupyter_move_config
cp %{buildroot}%{python3_sitelib}/pythreejs-%{mainver}.dist-info/LICENSE .
%fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}

%check
# these require packages from the NEP 29 family (Python > 3.6)
python36_donttest="Examples.ipynb or Picker.ipynb or superellipsoid.ipynb"
%pytest -l --nbval-lax --current-env examples ${$python_donttest:+ -k "not (${$python_donttest})"}

%files %{python_files}
%license LICENSE
%{python_sitelib}/pythreejs/
%{python_sitelib}/pythreejs-%{mainver}.dist-info/

%files -n jupyter-pythreejs
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/jupyter-threejs.json
%{_jupyter_nbextension_dir}/jupyter-threejs/

%files -n jupyter-pythreejs-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir}/jupyter-threejs-%{labver}.tgz

%changelog
