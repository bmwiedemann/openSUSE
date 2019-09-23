#
# spec file for package python-ipyscales
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
%define mainver 0.4.0
%define labver  3.0.0
%define         skip_python2 1
Name:           python-ipyscales
Version:        %{mainver}
Release:        0
Summary:        A widget library for scales
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vidartf/ipyscales
Source:         https://files.pythonhosted.org/packages/py2.py3/i/ipyscales/ipyscales-%{mainver}-py2.py3-none-any.whl
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipyscales = %{version}
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-numpy
Recommends:     python-ipydatawidgets
Provides:       python-jupyter_ipyscales = %{version}
Obsoletes:      python-jupyter_ipyscales < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module ipydatawidgets}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Jupyter/IPython widget library for scales.

This package provides the python interface.

%package     -n jupyter-ipyscales
Summary:        A Jupyter widget library for scales
Requires:       jupyter-notebook >= 4.0.0
Requires:       jupyter-ipyscales = %{version}
Requires(post): jupyter-notebook
Requires(post): jupyter-ipywidgets >= 7.0.0
Requires(preun): jupyter-notebook
Requires(preun): jupyter-ipywidgets >= 7.0.0
Conflicts:      python3-jupyter_ipyscales < 0.4.0

%description -n jupyter-ipyscales
A Jupyter/IPython widget library for scales.

This package provides the jupyter notebook extension.

%package     -n jupyter-jupyterlab-ipyscales
Version:        %{labver}
Summary:        A JupyterLab widget library for scales
Requires:       jupyter-jupyterlab
Requires:       python3-ipyscales = %{mainver}
Provides:       python3-jupyter_ipyscales_jupyterlab = %{labver}
Obsoletes:      python3-jupyter_ipyscales_jupyterlab < %{labver}

%description -n jupyter-jupyterlab-ipyscales
A Jupyter/IPython widget library for scales.

This package provides the Jupyterlab widget

After installation you must run:
jupyter labextension install @jupyter-widgets/jupyterlab-manager

%prep
%setup -q -c -T

%build
# Not Needed

%install
%{python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}
find %{buildroot}%{$python_sitelib}/ipyscales/ -name '*.py' -exec sed -i 's/\r$//' {} \;
find %{buildroot}%{$python_sitelib}/ipyscales/ -name '*.py' -exec sed -i sed -i -e '/^#!\//, 1d'  {} \;
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/ipyscales/
}

%{jupyter_move_config}
cp %{buildroot}%{python3_sitelib}/ipyscales-%{mainver}.dist-info/LICENSE.txt .
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}


%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix} -l --pyargs ipyscales
}

%files %{python_files}
%license %{python_sitelib}/ipyscales-%{mainver}.dist-info/LICENSE.txt
%{python_sitelib}/ipyscales/
%{python_sitelib}/ipyscales-%{mainver}.dist-info/

%files -n jupyter-ipyscales
%license LICENSE.txt
%{_jupyter_nbextension_dir}/jupyter-scales/
%config %{_jupyter_nb_notebook_confdir}/jupyter-scales.json

%files -n jupyter-jupyterlab-ipyscales
%license LICENSE.txt
%{_jupyter_labextensions_dir}/jupyter-scales-%{labver}.tgz

%changelog
