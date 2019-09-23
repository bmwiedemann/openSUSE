#
# spec file for package python-ipympl
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
%define labver  0.4.2
%define mainver 0.3.3
%bcond_with     test
Name:           python-ipympl
Version:        %{mainver}
Release:        0
Summary:        Matplotlib Jupyter Extension
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/matplotlib/jupyter-matplotlib
Source:         https://files.pythonhosted.org/packages/source/i/ipympl/ipympl-%{mainver}.tar.gz
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module matplotlib >= 2.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  npm
BuildRequires:  python-backports.functools_lru_cache
BuildRequires:  python-notebook
BuildRequires:  python-rpm-macros
BuildRequires:  jupyter-jupyterlab-filesystem
Requires:       python-ipython
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-matplotlib >= 2.0.0
Requires:       python-six
Provides:       python-jupyter_ipympl = %{mainver}
Obsoletes:      python-jupyter_ipympl < %{mainver}
BuildArch:      noarch
%ifpython2
Requires:       python-backports.functools_lru_cache
Requires:       python3-ipympl = %{mainver}
%endif
%ifpython3
Provides:       jupyter-ipympl = %{mainver}
%endif
%python_subpackages

%description
Jupyter extension to display matplotlib plots in a widget.

This package provides the python interface.

%package     -n jupyter-ipympl
Summary:        Matplotlib Jupyter Extension
Requires:       python3-ipympl = %{mainver}
Requires:       jupyter-notebook

%description -n jupyter-ipympl
Jupyter extension to display matplotlib plots in a widget.

This package provides the jupyter notebook extension.

%package     -n jupyter-ipympl-jupyterlab
Version:        %{labver}
Summary:        Matplotlib JupyterLab Extension
Requires:       python3-ipympl = %{mainver}
Requires:       jupyter-jupyterlab
Provides:       python3-jupyter_ipympl_jupyterlab = %{labver}
Obsoletes:      python3-jupyter_ipympl_jupyterlab < %{labver}

%description -n jupyter-ipympl-jupyterlab
Jupyter extension to display matplotlib plots in a widget.

This package provides the JupyterLab extension.

After installation you must run:
jupyter labextension install @jupyter-widgets/jupyterlab-manager

%prep
%setup -q -n ipympl-%{mainver}

%build
%python_build

%install
%python_install

%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%files %{python_files}
%license LICENSE
%{python_sitelib}/ipympl/
%{python_sitelib}/ipympl-%{mainver}-py*.egg-info

%files -n jupyter-ipympl
%license LICENSE
%doc README.md
%{_jupyter_nbextension_dir}/jupyter-matplotlib
%config %{_jupyter_nb_notebook_confdir}/jupyter-matplotlib.json

%files -n jupyter-ipympl-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir}/jupyter-matplotlib-%{labver}.tgz

%changelog
