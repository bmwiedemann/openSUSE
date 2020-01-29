#
# spec file for package python-jupyter_console
#
# Copyright (c) 2020 SUSE LLC.
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
Name:           python-jupyter_console
Version:        6.1.0
Release:        0
Summary:        Jupyter terminal console
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/jupyter/jupyter_console
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_console/jupyter_console-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module prompt_toolkit >= 2}
BuildRequires:  %{python_module pyzmq}
# /SECTION
Requires:       python-jupyter-client
Requires:       python-ipykernel
Requires:       python-ipython
Requires:       python-prompt_toolkit >= 2
Requires:       python-pyzmq
Requires:       jupyter-jupyter_console = %{version}
BuildArch:      noarch

%python_subpackages

%description
A terminal-based console frontend for Jupter kernels.
This code is based on the single-process IPython terminal.

This package provides the python components.

%package     -n jupyter-jupyter_console
Summary:        Jupyter terminal console
Requires:       python3-jupyter_console = %{version}
Provides:       jupyter-jupyter_console-doc = %{version}
Obsoletes:      jupyter-jupyter_console-doc < %{version}

%description -n jupyter-jupyter_console
A terminal-based console frontend for Jupter kernels.
This code is based on the single-process IPython terminal.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_console-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix} jupyter_console

%files %{python_files}
%doc CONTRIBUTING.md README.md
%license COPYING.md 
%{python_sitelib}/*

%files -n jupyter-jupyter_console
%license COPYING.md

%changelog
