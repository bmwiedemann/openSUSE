#
# spec file for package python-pythreejs
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


%define mainver 2.4.1
%define jupver  2.4.0
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
Source1:        https://files.pythonhosted.org/packages/py3/p/pythreejs/pythreejs-%{version}-py3-none-any.whl
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Recommends:     jupyter-threejs-jupyterlab = %{jupver}
Requires:       jupyter-threejs = %{jupver}
Requires:       python-ipydatawidgets >= 1.1.1
Requires:       python-ipywidgets >= 7.2.1
Requires:       python-numpy >= 1.14
Requires:       python-traitlets
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
BuildRequires:  %{python_module traitlets}
# /SECTION
%python_subpackages

%description
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the python interface.

%package     -n jupyter-threejs
Version:        %{jupver}
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
Group:          Development/Languages/Python
Requires:       jupyter-ipydatawidgets >= 1.1.1
Requires:       jupyter-ipywidgets >= 7.2.1
Requires:       jupyter-notebook
Requires:       python3-pythreejs = %{mainver}
Provides:       jupyter-pythreejs = %{jupver}-%{release}
Obsoletes:      jupyter-pythreejs < %{jupver}-%{release}

%description -n jupyter-threejs
Interactive 3d graphics for the Jupyter notebook,
using Three.js from Jupyter interactive widgets.

This package provides the jupyter notebook extension.

%package     -n jupyter-threejs-jupyterlab
Summary:        A Python/ThreeJS bridge utilizing the Jupyter widget infrastructure
Group:          Development/Languages/Python
Version:        %{jupver}
Release:        0
Requires:       jupyter-ipydatawidgets-jupyterlab >= 1.1.1
Requires:       jupyter-jupyterlab
Requires:       python3-pythreejs = %{mainver}
Provides:       jupyter-pythreejs-jupyterlab = %{jupver}-%{release}
Obsoletes:      jupyter-pythreejs-jupyterlab < %{jupver}-%{release}

%description -n jupyter-threejs-jupyterlab
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
%pytest -l --nbval-lax --current-env examples

%files %{python_files}
%license LICENSE
%{python_sitelib}/pythreejs/
%{python_sitelib}/pythreejs-%{mainver}.dist-info/

%files -n jupyter-threejs
%license LICENSE
%_jupyter_config %{_jupyter_nb_notebook_confdir}/jupyter-threejs.json
%{_jupyter_nbextension_dir}/jupyter-threejs/

%files -n jupyter-threejs-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir}/jupyter-threejs-%{jupver}.tgz
%{_jupyter_labextensions_dir3}/jupyter-threejs/

%changelog
