#
# spec file for package python-ipyscales
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


%{?!python_module:%define python_module() python3-%{**}}
%define mainver 0.6.0
%define labver  3.2.0
%define         skip_python2 1
Name:           python-ipyscales
Version:        %{mainver}
Release:        0
Summary:        A widget library for scales
License:        BSD-3-Clause
URL:            https://github.com/vidartf/ipyscales
Source0:        https://files.pythonhosted.org/packages/py2.py3/i/ipyscales/ipyscales-%{mainver}-py2.py3-none-any.whl
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyscales = %{version}
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-numpy
Recommends:     python-ipydatawidgets
Provides:       python-jupyter_ipyscales = %{version}-%{release}
Obsoletes:      python-jupyter_ipyscales < %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.6}
BuildRequires:  %{python_module ipydatawidgets >= 4.2}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Jupyter/IPython widget library for scales.

This package provides the python interface.

%package     -n jupyter-ipyscales
Summary:        A Jupyter widget library for scales
Requires:       jupyter-ipyscales = %{version}
Requires:       jupyter-notebook >= 4.0.0
Requires(post): jupyter-notebook
Requires(post): jupyter-ipywidgets >= 7.0.0
Requires(preun):jupyter-notebook
Requires(preun):jupyter-ipywidgets >= 7.0.0
Conflicts:      python3-jupyter_ipyscales < 0.4.0

%description -n jupyter-ipyscales
A Jupyter/IPython widget library for scales.

This package provides the jupyter notebook extension.

%package     -n jupyter-jupyterlab-ipyscales
Version:        %{labver}
Summary:        A JupyterLab widget library for scales
Requires:       jupyter-jupyterlab
Requires:       python3-ipyscales = %{mainver}
Provides:       python3-jupyter_ipyscales_jupyterlab = %{labver}-%{release}
Obsoletes:      python3-jupyter_ipyscales_jupyterlab < %{labver}-%{release}

%description -n jupyter-jupyterlab-ipyscales
A Jupyter/IPython widget library for scales.

This package provides the Jupyterlab widget

After installation you must run:
jupyter labextension install @jupyter-widgets/jupyterlab-manager

%prep
%setup -q -c -T

%build

%install
%pyproject_install %{SOURCE0}
%{python_expand #
find %{buildroot}%{$python_sitelib} -name '*.py' \
  -exec dos2unix '{}' ';' \
  -exec sed -i '1{/env python/ d}' '{}' ';'
%fdupes %{buildroot}%{$python_sitelib}
}

%{jupyter_move_config}
cp %{buildroot}%{python3_sitelib}/ipyscales-%{mainver}.dist-info/LICENSE.txt .
%fdupes %{buildroot}%{_jupyter_prefix}

%check
%pytest --pyargs ipyscales

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/ipyscales
%{python_sitelib}/ipyscales-%{mainver}.dist-info/

%files -n jupyter-ipyscales
%license LICENSE.txt
%{_jupyter_nbextension_dir}/jupyter-scales/
%_jupyter_config %{_jupyter_nb_notebook_confdir}/jupyter-scales.json

%files -n jupyter-jupyterlab-ipyscales
%license LICENSE.txt
%{_jupyter_labextensions_dir}/jupyter-scales-%{labver}.tgz
%{_jupyter_labextensions_dir3}/jupyter-scales

%changelog
