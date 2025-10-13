#
# spec file for package python-jupyter-lsp
#
# Copyright (c) 2025 SUSE LLC
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


%define pyversion 2.2.6
%define shortversion 2.2.6
%define jupversion 5.2.0
Name:           python-jupyter-lsp
Version:        %{pyversion}
Release:        0
Summary:        LSP for Jupyter Notebook/Lab server
License:        BSD-3-Clause
# SourceRepository: https://github.com/jupyter-lsp/jupyterlab-lsp
URL:            https://github.com/jupyter-lsp/jupyterlab-lsp/tree/main/python_packages/jupyter_lsp
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-lsp/jupyter_lsp-%{pyversion}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module importlib_metadata >= 4.8.3 if %python-base < 3.10}
BuildRequires:  %{python_module jupyter_server >= 1.1.2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module python-lsp-server}
# /SECTION
BuildRequires:  fdupes
Requires:       jupyter-lsp = %{jupversion}
Requires:       python-jupyter_server >= 1.1.2
Requires:       (python-importlib_metadata >= 4.8.3 if python-base < 3.10)
Provides:       python-jupyter_lsp = %{pyversion}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server

%package -n jupyter-lsp
Version:        %{jupversion}
Summary:        LSP for Jupyter Notebook/Lab server - Config
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(jupyter-lsp) = %{shortversion}
Suggests:       python3-jupyter-lsp

%description -n jupyter-lsp
Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server
Jupyter config

%prep
%autosetup -p1 -n jupyter_lsp-%{pyversion}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no R language server
donttest="test_r_package_detection"
# servers not installed
donttest="$donttest or languageserver-bin or language-server"
# Does not report stopped in time (?)
donttest="$donttest or test_start_known[pylsp]"
%pytest -k "not ($donttest)" -n auto

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupyter_lsp
%{python_sitelib}/jupyter_lsp-%{pyversion}.dist-info

%files -n jupyter-lsp
%doc README.md
%license LICENSE
%_jupyter_config %_jupyter_server_confdir/jupyter-lsp-jupyter-server.json

%changelog
