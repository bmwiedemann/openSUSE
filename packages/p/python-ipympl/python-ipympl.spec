#
# spec file for package python-ipympl
#
# Copyright (c) 2024 SUSE LLC
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


%define skip_python39 1
%define pyver   0.9.4
%define jsver   0.11.4
%bcond_with     test
Name:           python-ipympl
Version:        %{pyver}
Release:        0
Summary:        Matplotlib Jupyter Extension
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/matplotlib/ipympl
Source0:        https://files.pythonhosted.org/packages/source/i/ipympl/ipympl-%{pyver}.tar.gz
# package-lock.json file generated with command:
# npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source2:        package-lock.json
# node_modules generated using "osc service mr" with the https://github.com/openSUSE/obs-service-node_modules
Source3:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module hatch-jupyter-builder}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module ipython < 9}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module ipywidgets >= 7.6.0 with %python-ipywidgets < 9}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module matplotlib >= 3.4.0 with %python-matplotlib < 4}
BuildRequires:  %{python_module matplotlib-web}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module traitlets < 6}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-matplotlib = %{jsver}
Requires:       python-Pillow
Requires:       python-ipython < 9
Requires:       python-ipython_genutils
Requires:       python-matplotlib-web
Requires:       python-numpy
Requires:       python-traitlets < 6
Requires:       (python-ipywidgets >= 7.6.0 with python-ipywidgets < 9)
Requires:       (python-matplotlib >= 3.4.0 with python-matplotlib < 4)
Suggests:       python-jupyterlab
Suggests:       python-notebook
Provides:       python-jupyter_ipympl = %{pyver}
Obsoletes:      python-jupyter_ipympl < %{pyver}
BuildArch:      noarch
%python_subpackages

%description
Jupyter extension to display matplotlib plots in a widget.

This package provides the python interface.

%package     -n jupyter-matplotlib
Version:        %{jsver}
Summary:        Matplotlib Jupyter Extension
Group:          Development/Languages/Python
Requires:       jupyter-notebook
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipympl) = %{pyver}
Suggests:       python3-ipympl
Provides:       jupyter-ipympl = %{jsver}
Obsoletes:      jupyter-ipympl < %{jsver}

%description -n jupyter-matplotlib
Jupyter extension to display matplotlib plots in a widget.

This package provides the jupyter notebook extension.

%package     -n jupyter-matplotlib-jupyterlab
Version:        %{jsver}
Release:        0
Summary:        Matplotlib JupyterLab Extension
Group:          Development/Languages/Python
Requires:       jupyter-jupyterlab
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipympl) = %{pyver}
Suggests:       python3-ipympl
Provides:       jupyter-ipympl-jupyterlab = %{jsver}
Obsoletes:      jupyter-ipympl-jupyterlab < %{jsver}

%description -n jupyter-matplotlib-jupyterlab
Jupyter extension to display matplotlib plots in a widget.

This package provides the JupyterLab extension.

%prep
%autosetup -p1 -n ipympl-%{pyver}
# Replace usage of "jlpm" with "npm"
sed -i 's/npm = \["jlpm"\]/npm = ["npm"]/g' pyproject.toml
sed -i 's/jlpm/npm run/g' package.json
sed -i '/prepublish/d' package.json
local-npm-registry %{_sourcedir} install --include=dev --include=peer

%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
%pytest --nbval docs/examples/full-example.ipynb

%files %{python_files}
%license LICENSE
%{python_sitelib}/ipympl/
%{python_sitelib}/ipympl-%{pyver}.dist-info

%files -n jupyter-matplotlib
%license LICENSE
%{_jupyter_nbextension_dir}/jupyter-matplotlib
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/jupyter-matplotlib.json

%files -n jupyter-matplotlib-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir3}/jupyter-matplotlib

%changelog
