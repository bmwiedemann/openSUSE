#
# spec file for package jupyter
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


%define plainpython python
Name:           jupyter
Version:        1.1.1
Release:        0
Summary:        Metapackage to install all the Jupyter components in one go
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://jupyter.org/
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter/jupyter-%{version}.tar.gz
Source99:       jupyter.rpmlintrc
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyter-console}
BuildRequires:  %{python_module jupyterlab}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-ipykernel
Requires:       python-ipywidgets
Requires:       python-jupyter-console
Requires:       python-jupyterlab
Requires:       python-nbconvert
Requires:       python-notebook
Suggests:       python-qtconsole
Requires:       %plainpython(abi) = %{python_version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter = %{version}-%{release}
Obsoletes:      jupyter < %{version}-%{release}
%endif
BuildArch:      noarch
%python_subpackages

%description
Jupyter is an environment for interactive computing in multiple languages.
It includes a console, a browser-based notebook format, and support for
dozens of languages through the use of language-specific kernels.

This is an empty metapackage for user convenience, only expressing
dependencies on multiple Jupyter packages. jupyter should not be used
as a dependency for any packages.

For more efficient installation of what you need, all Jupyter components
installed by pip install jupyter can be installed separately. For example:
  - %{python_flavor}-notebook - Jupyter Notebook
  - %{python_flavor}-jupyterlab - JupyterLab (added to metapackage v1.1)
  - %{python_flavor}-ipython - IPython (terminal)
  - %{python_flavor}-ipykernel - IPython Kernel for Jupyter
  - %{python_flavor}-jupyter-console - terminal Jupyter client
  - %{python_flavor}-nbconvert - convert notebooks between formats
  - %{python_flavor}-ipywidgets - interactive widgets package for IPython

No longer included as hard dependency, but still supported:

  - %{python_flavor}-qtconsole - Qt Console (removed in metapackage v1.1)

%prep
%setup -q -n jupyter-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %python_files
%license LICENSE
%doc README.md SECURITY.md
%{python_sitelib}/jupyter-%{version}.dist-info

%changelog
