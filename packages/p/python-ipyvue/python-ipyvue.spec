#
# spec file for package python-ipyvue
#
# Copyright (c) 2023 SUSE LLC
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


# This is important for versions ending in .0
%define python3dist_version 1.10.1
Name:           python-ipyvue
Version:        1.10.1
Release:        0
Summary:        Jupyter widgets base for Vue libraries
License:        MIT
URL:            https://github.com/widgetti/ipyvue
# Use sdist for static js but github archive for test files
Source0:        https://files.pythonhosted.org/packages/source/i/ipyvue/ipyvue-%{version}.tar.gz
Source1:        https://github.com/widgetti/ipyvue/archive/refs/tags/v%{version}.tar.gz#/ipyvue-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-ipywidgets >= 7.0.0
Recommends:     jupyter-ipyvue-nbextension = %{version}
Recommends:     jupyter-jupyterlab-ipyvue = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Jupyter widgets base for Vue libraries

%package     -n jupyter-ipyvue-nbextension
Summary:        Jupyter widgets base for Vue libraries - nbextension
Requires:       jupyter-notebook
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipyvue) = %{python3dist_version}
Suggests:       python3-ipyvue

%description -n jupyter-ipyvue-nbextension
Jupyter widgets base for Vue libraries

This package provides the jupyter notebook extension.

%package     -n jupyter-jupyterlab-ipyvue
Summary:        Jupyter widgets base for Vue libraries - labextension
Requires:       jupyter-jupyterlab
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipyvue) = %{python3dist_version}
Suggests:       python3-ipyvue

%description -n jupyter-jupyterlab-ipyvue
Jupyter widgets base for Vue libraries

This package provides the jupyterlab extension.

%prep
%setup -q -n ipyvue-%{version}
chmod -x ipyvue/labextension/package.json README.md
tar -x --strip-components=1 -f %{SOURCE1}  ipyvue-%{version}/tests/

%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
# no playwright
ignoretestfiles="--ignore tests/ui"
%pytest $ignoretestfiles

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipyvue
%{python_sitelib}/ipyvue-%{version}.dist-info

%files -n jupyter-ipyvue-nbextension
%license LICENSE
%_jupyter_config %{_jupyter_nb_notebook_confdir}/jupyter-vue.json
%{_jupyter_nbextension_dir}/jupyter-vue

%files -n jupyter-jupyterlab-ipyvue
%license LICENSE
%{_jupyter_labextensions_dir}/jupyter-vue-%{version}.tgz
%{_jupyter_labextensions_dir3}/jupyter-vue

%changelog
