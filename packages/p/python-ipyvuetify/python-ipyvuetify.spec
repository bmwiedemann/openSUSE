#
# spec file for package python-ipyvuetify
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
Name:           python-ipyvuetify
Version:        1.9.1
Release:        0
Summary:        Jupyter widgets based on vuetify UI components
License:        MIT
URL:            https://github.com/mariobuikhuizen/ipyvuetify
Source0:        https://files.pythonhosted.org/packages/source/i/ipyvuetify/ipyvuetify-%{version}.tar.gz
Source1:        https://github.com/widgetti/ipyvuetify/raw/v%{version}/examples/Examples.ipynb
# PATCH-FIX-OPENSUSE avoid-npm.patch code@bnavigator.de
Patch0:         avoidnpm.patch
BuildRequires:  %{python_module jupyter-packaging >= 0.7.9}
BuildRequires:  %{python_module jupyterlab >= 3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       (python-ipyvue >= 1.7 with python-ipyvue < 2)
Recommends:     jupyter-ipyvuetify-nbextension = %{version}
Recommends:     jupyter-jupyterlab-ipyvuetify = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipyvue >= 1.7 with %python-ipyvue < 2}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Jupyter widgets based on vuetify UI components

%package     -n jupyter-ipyvuetify-nbextension
Summary:        Jupyter widgets based on vuetify UI components - nbextension
Requires:       jupyter-notebook
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipyvuetify) = %{version}
Suggests:       python3-ipyvuetify

%description -n jupyter-ipyvuetify-nbextension
Jupyter widgets based on vuetify UI components

This package provides the jupyter notebook extension.

%package     -n jupyter-jupyterlab-ipyvuetify
Summary:        Jupyter widgets based on vuetify UI components - labextension
Requires:       jupyter-jupyterlab
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(ipyvuetify) = %{version}
Suggests:       python3-ipyvuetify

%description -n jupyter-jupyterlab-ipyvuetify
Jupyter widgets based on vuetify UI components

This package provides the jupyterlab extension.

%prep
%autosetup -p1 -n ipyvuetify-%{version}
chmod -x prefix/share/jupyter/labextensions/jupyter-vuetify/package.json \
         prefix/etc/nbconfig/notebook.d/jupyter-vuetify.json \
         README.md

%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
%pytest --nbval %{SOURCE1}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipyvuetify
%{python_sitelib}/ipyvuetify-%{version}.dist-info

%files -n jupyter-ipyvuetify-nbextension
%license LICENSE
%_jupyter_config %{_jupyter_nb_notebook_confdir}/jupyter-vuetify.json
%{_jupyter_nbextension_dir}/jupyter-vuetify

%files -n jupyter-jupyterlab-ipyvuetify
%license LICENSE
%{_jupyter_labextensions_dir3}/jupyter-vuetify

%changelog
