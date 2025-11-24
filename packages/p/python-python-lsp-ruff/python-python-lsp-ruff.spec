#
# spec file for package python-python-lsp-ruff
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


Name:           python-python-lsp-ruff
Version:        2.3.0
Release:        0
Summary:        Ruff linting plugin for pylsp
License:        MIT
URL:            https://github.com/python-lsp/python-lsp-ruff
Source:         https://files.pythonhosted.org/packages/source/p/python_lsp_ruff/python_lsp_ruff-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cattrs
Requires:       python-lsprotocol >= 2023.0.1
Requires:       python-python-lsp-server
Requires:       python-ruff >= 0.2.0
Provides:       python-python_lsp_ruff = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cattrs}
BuildRequires:  %{python_module lsprotocol >= 2023.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lsp-server}
BuildRequires:  %{python_module ruff >= 0.2.0}
# /SECTION
%python_subpackages

%description
python-lsp-ruff is a plugin for python-lsp-server that adds linting,
code actions and formatting capabilities that are provided by ruff

%prep
%autosetup -p1 -n python_lsp_ruff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/pylsp_ruff
%{python_sitelib}/python_lsp_ruff-%{version}.dist-info

%changelog
