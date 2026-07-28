#
# spec file for package python-bqscales
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-bqscales
Version:        0.3.7
Release:        0
Summary:        Grammar of Graphics in Python
License:        Apache-2.0
URL:            https://github.com/bqplot/bqscales
Source0:        https://files.pythonhosted.org/packages/source/b/bqscales/bqscales-%{version}.tar.gz
# package-lock.json file generated with command:
# npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source2:        package-lock.json
# node_modules generated using "osc service mr" with the https://github.com/openSUSE/obs-service-node_modules
Source3:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
# PATCH-FIX-OPENSUSE remove-hatch-build-scripts-dep.patch
Patch0:         remove-hatch-build-scripts-dep.patch
# PATCH-FIX-OPENSUSE use-npm.patch
Patch1:         use-npm.patch
BuildRequires:  %{python_module hatch-jupyter-builder}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hatch}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem >= 20211114
BuildRequires:  jupyter-rpm-macros
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
Requires:       python-ipywidgets >= 8.0.1
Requires:       python-numpy >= 1.10.4
Requires:       python-traitlets >= 4.3.0
Requires:       python-traittypes >= 0.0.6
# TEST
BuildRequires:  %{python_module ipywidgets >= 8.0.1}
BuildRequires:  %{python_module numpy >= 1.10.4}
BuildRequires:  %{python_module traitlets >= 4.3.0}
BuildRequires:  %{python_module traittypes >= 0.0.6}
BuildRequires:  %{python_module nbclassic}
# /TEST
BuildArch:      noarch
%python_subpackages

%description
Grammar of Graphics in Python for bqplot and other Jupyter widgets
libraries

%package     -n jupyter-bqscales-jupyterlab
Version:        %{version}
Summary:        Grammar of Graphics in Python for Jupyterlab
Group:          Development/Languages/Python
Requires:       jupyter-notebook
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(bqscales) = %{version}
Suggests:       python3-bqscales

%package     -n jupyter-bqscales-notebook
Version:        %{version}
Summary:        Grammar of Graphics in Python for Classic Jupyter Notebooks
Requires:       jupyter-nbclassic
Requires:       python3dist(bqscales) = %{version}
Suggests:       python3-bqscales

%description -n jupyter-bqscales-notebook
Grammar of Graphics in Python for bqplot and other Jupyter widgets
libraries

This package provides the jupyter notebook extension.

%description -n jupyter-bqscales-jupyterlab
Grammar of Graphics in Python for bqplot and other Jupyter widgets
libraries

This package provides the jupyter lab extension.

%prep
%autosetup -p1 -n bqscales-%{version}
cp %{SOURCE2} .
local-npm-registry %{_sourcedir} install --legacy-peer-deps
sed -i '1{/env python/d}' bqscales/*.py bqscales/nbextension/*.py

%build
export SKIP_JUPYTER_BUILDER=1
npm run build
%pyproject_wheel

%install
export SKIP_JUPYTER_BUILDER=1
%jupyter_move_config
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
export JUPYTER_CONFIG_DIR=%{buildroot}%{_jupyter_confdir}
%{python_expand # no $python tests available
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import bqscales'
jupyter-%{$python_bin_suffix} nbclassic-extension list 2>&1 | grep -ie "bqscales/extension.*enabled"
jupyter-%{$python_bin_suffix} labextension list 2>&1 | grep -ie "bqscales.*enabled.*ok"
}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/bqscales
%{python_sitelib}/bqscales-%{version}.dist-info

%files -n jupyter-bqscales-notebook
%license LICENSE
%{_jupyter_nbextension_dir}/bqscales/
%{_jupyter_config} %{_jupyter_nb_notebook_confdir}/bqscales.json

%files -n jupyter-bqscales-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir3}/bqscales/

%changelog
