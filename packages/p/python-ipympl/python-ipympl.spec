#
# spec file for package python-ipympl
#
# Copyright (c) 2020 SUSE LLC
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
%define labver  0.7.4
%define mainver 0.5.8
%bcond_with     test
Name:           python-ipympl
Version:        %{mainver}
Release:        0
Summary:        Matplotlib Jupyter Extension
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/matplotlib/ipympl
Source:         https://files.pythonhosted.org/packages/source/i/ipympl/ipympl-%{mainver}.tar.gz
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets >= 7.5.0}
BuildRequires:  %{python_module matplotlib >= 2.0.0}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  npm
BuildRequires:  python-rpm-macros
Requires:       python-ipykernel >= 4.7
Requires:       python-ipython
Requires:       python-ipywidgets >= 7.5.0
Requires:       python-matplotlib >= 2.0.0
Provides:       python-jupyter_ipympl = %{mainver}
Obsoletes:      python-jupyter_ipympl < %{mainver}
Provides:       jupyter-ipympl = %{mainver}
BuildArch:      noarch
%python_subpackages

%description
Jupyter extension to display matplotlib plots in a widget.

This package provides the python interface.

%package     -n jupyter-ipympl
Summary:        Matplotlib Jupyter Extension
Group:          Development/Languages/Python
Requires:       jupyter-notebook
Requires:       python3-ipympl = %{mainver}

%description -n jupyter-ipympl
Jupyter extension to display matplotlib plots in a widget.

This package provides the jupyter notebook extension.

%package     -n jupyter-ipympl-jupyterlab
Version:        %{labver}
Release:        0
Summary:        Matplotlib JupyterLab Extension
Group:          Development/Languages/Python
Requires:       jupyter-jupyterlab
Requires:       python3-ipympl = %{mainver}
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

%jupyter_move_config
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
