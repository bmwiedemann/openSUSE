#
# spec file for package python-jupyter-require
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyter-require
Version:        0.6.1
Release:        0
Summary:        Jupyter nbextension for loading non-python dependencies in Jupyter notebooks
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/CermakM/jupyter-require
Source:         https://files.pythonhosted.org/packages/py2.py3/j/jupyter-require/jupyter_require-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module csscompressor}
BuildRequires:  %{python_module daiquiri}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter-contrib-nbextensions}
BuildRequires:  %{python_module jupyter-nbutils}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyter_core-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyter-require = %{version}
Requires:       python-csscompressor
Requires:       python-daiquiri
Requires:       python-ipykernel
Requires:       python-ipython
Requires:       python-jupyter-contrib-nbextensions
Requires:       python-jupyter-nbutils
BuildArch:      noarch

%python_subpackages

%description
Jupyter nbextension for JavaScript execution and managing linked libraries and
CSS stylesheets in Jupyter notebooks.

This package provides the python interface.

%package     -n jupyter-jupyter-require
Summary:        Jupyter nbextension for loading non-python dependencies in Jupyter notebooks
Group:          Development/Languages/Python
Requires:       jupyter-ipykernel
Requires:       jupyter-ipython
Requires:       jupyter-jupyter-contrib-nbextensions
Requires:       python3-jupyter-require = %{version}

%description -n jupyter-jupyter-require
Jupyter nbextension for JavaScript execution and managing linked libraries and
CSS stylesheets in Jupyter notebooks.

This package provides the jupyter components.

%prep
%setup -q -c -T

%build
# Not needed

%install
%{python_expand mkdir build; cp -a %{SOURCE0} build/}
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
cp %{buildroot}%{python3_sitelib}/jupyter_require-%{version}.dist-info/LICENSE .

#%%check
# There are no tests

%files %{python_files}
%license LICENSE
%{python_sitelib}/jupyter_require-%{version}.dist-info/
%{python_sitelib}/jupyter_require/

%files -n jupyter-jupyter-require
%license LICENSE
%config %{_jupyter_nb_notebook_confdir}/jupyter-require.json
%{_jupyter_nbextension_dir}/jupyter-require/

%changelog
