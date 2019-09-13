#
# spec file for package python-jupytext
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-jupytext
%define mainver 1.2.1
%define labver  1.0.2
Version:        %{mainver}
Release:        0
License:        MIT
Summary:        Tool to convert Jupyter notebooks to other formats
Url:            https://github.com/mwouts/jupytext
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jupytext/jupytext-%{mainver}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nbformat >= 4.0.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module testfixtures}
# /SECTION
BuildRequires:  fdupes
Requires:       python-nbformat >= 4.0.0
Requires:       python-notebook
Requires:       python-PyYAML
Requires:       jupyter-jupytext = %{mainver}
BuildArch:      noarch

%python_subpackages

%description
Jupytext can save Jupyter notebooks as:

   * Markdown and R Markdown documents,
   * Julia, Python, R, Bash, Scheme, Clojure, Matlab, Octave, C++ and q/kdb+ scripts.
interactive computing.

This package provides the python interface.

%package     -n jupyter-jupytext
Summary:        Tool to convert Jupyter notebooks to other formats
Requires:       jupyter-nbformat >= 4.0.0
Requires:       jupyter-notebook
Requires:       python3-jupytext = %{mainver}

%description -n jupyter-jupytext
Jupytext can save Jupyter notebooks as:

   * Markdown and R Markdown documents,
   * Julia, Python, R, Bash, Scheme, Clojure, Matlab, Octave, C++ and q/kdb+ scripts.
interactive computing.

This package provides the exectuables and jupyter components.

%package     -n jupyter-jupytext-jupyterlab
Summary:        Tool to convert Jupyter notebooks to other formats
Version:        %{labver}
Requires:       jupyter-jupyterlab
Requires:       python3-jupytext = %{mainver}

%description -n jupyter-jupytext-jupyterlab
Jupytext can save Jupyter notebooks as:

   * Markdown and R Markdown documents,
   * Julia, Python, R, Bash, Scheme, Clojure, Matlab, Octave, C++ and q/kdb+ scripts.

This package provides the JupyterLab extension.

%prep
%setup -q -n jupytext-%{mainver}
sed -i 's/\r$//' README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%jupyter_move_config

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupytext-%{mainver}-py*.egg-info
%{python_sitelib}/jupytext/

%files -n jupyter-jupytext
%license LICENSE
%{_bindir}/jupytext
%config %{_jupyter_server_confdir}/jupytext.json
%config %{_jupyter_servextension_confdir}/jupytext.json
%config %{_jupyter_nb_notebook_confdir}/jupytext.json
%{_jupyter_nbextension_dir}/jupytext/

%files -n jupyter-jupytext-jupyterlab
%license LICENSE
%{_jupyter_labextensions_dir}/jupyterlab-jupytext-%{labver}.tgz

%changelog
