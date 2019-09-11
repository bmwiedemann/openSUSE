#
# spec file for package python-jupyter_latex_envs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with     test
Name:           python-jupyter_latex_envs
Version:        1.4.6
Release:        0
Summary:        LaTeX environments for Jupyter notebook
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/jfbercher/jupyter_latex_envs
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_latex_envs/jupyter_latex_envs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  jupyter-notebook >= 4.0
%if %{with test}
BuildRequires:  %{python_module entrypoints >= 0.2.2}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module notebook >= 4.0}
BuildRequires:  %{python_module traitlets >= 4.1}
%endif
Requires:       python-jupyter_core
Requires:       python-ipython
Requires:       python-nbconvert
Requires:       python-notebook >= 4.0
Requires:       python-traitlets >= 4.1
Requires:       jupyter-jupyter_latex_envs = %{version}
BuildArch:      noarch

%python_subpackages

%description
Jupyter notebook extension which supports (some) LaTeX environments
within markdown cells. Also provides support for labels and
crossreferences, document wide numbering, bibliography, and more.

This package provides the python interface.

%package     -n jupyter-jupyter_latex_envs
Summary:        LaTeX environments for Jupyter notebook
Requires:       jupyter-jupyter_core
Requires:       jupyter-nbconvert
Requires:       jupyter-notebook >= 4.0
Requires:       python3-jupyter_latex_envs = %{version}
Requires(post): jupyter-notebook
Requires(preun): jupyter-notebook
Requires(post): python3-jupyter_latex_envs = %{version}
Requires(preun): python3-jupyter_latex_envs = %{version}

%description -n jupyter-jupyter_latex_envs
Jupyter notebook extension which supports (some) LaTeX environments
within markdown cells. Also provides support for labels and
crossreferences, document wide numbering, bibliography, and more.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_latex_envs-%{version}
rm -r src/latex_envs/static/doc/.ipynb_checkpoints
chmod a-x src/latex_envs/static/doc/IEEEtran.bst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{jupyter_nbextension_install latex_envs}
%{fdupes %{buildroot}%{python3_sitelib} %{buildroot}%{_jupyter_nbextension_dir}}

%post -n jupyter-jupyter_latex_envs
%{jupyter_nbextension_enable latex_envs}

%preun -n jupyter-jupyter_latex_envs
%{jupyter_nbextension_disable latex_envs}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/latex_envs
%{python_sitelib}/jupyter_latex_envs-%{version}-py*.egg-info

%files -n jupyter-jupyter_latex_envs
%license LICENSE.txt
%{_jupyter_nbextension_dir}/latex_envs/

%changelog
