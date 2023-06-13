#
# spec file for package python-jupyter-lsp
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

%define python3dist python3dist
%define shortversion 2.2
Name:           python-jupyter-lsp
Version:        2.2.0
Release:        0
Summary:        LSP for Jupyter Notebook/Lab server
License:        BSD-3-Clause
URL:            https://github.com/jupyter-lsp/jupyterlab-lsp/tree/master/python_packages/jupyter_lsp
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-lsp/jupyter-lsp-%{version}.tar.gz
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module jupyter_server >= 1.1.2}
BuildRequires:  %{python_module importlib_metadata >= 4.8.3 if %python-base < 3.10}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jupyter_server >= 1.1.2
Requires:       (python-importlib_metadata >= 4.8.3 if python-base < 3.10)
Requires:       jupyter-lsp = %{version}
Provides:       python-jupyter_lsp = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server

%package -n jupyter-lsp
Summary: LSP for Jupyter Notebook/Lab server - Config
Requires: %python3dist(jupyter-lsp) = %{shortversion}

%description -n jupyter-lsp
Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server
Jupyter config

%prep
%autosetup -p1 -n jupyter-lsp-%{version}

%build
%pyproject_wheel
sed -e /cov/d -e /--flake8/d -i setup.cfg

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no R language server
donttest="test_r_package_detection"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupyter_lsp
%{python_sitelib}/jupyter_lsp-%{version}.dist-info

%files -n jupyter-lsp
%doc README.md
%license LICENSE
%_jupyter_config %_jupyter_servextension_confdir/jupyter-lsp-notebook.json
%_jupyter_config %_jupyter_server_confdir/jupyter-lsp-jupyter-server.json

%changelog
