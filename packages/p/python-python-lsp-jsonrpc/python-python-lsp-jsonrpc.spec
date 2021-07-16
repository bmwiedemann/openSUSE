#
# spec file for package python-python-lsp-jsonrpc
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-python-lsp-jsonrpc
Version:        1.0.0
Release:        0
Summary:        JSON RPC 2.0 server library
License:        MIT
URL:            https://github.com/python-lsp/python-lsp-jsonrpc
Source:         https://files.pythonhosted.org/packages/source/p/python-lsp-jsonrpc/python-lsp-jsonrpc-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module ujson >= 3.0.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-ujson >= 3.0.0
BuildArch:      noarch
%python_subpackages

%description
A Python 3.6+ server implementation of the JSON RPC 2.0 protocol.
This library has been pulled out of the Python Language Server project.


%prep
%setup -q -n python-lsp-jsonrpc-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Remove pytest addopts
rm setup.cfg
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pylsp_jsonrpc
%{python_sitelib}/python_lsp_jsonrpc-%{version}*-info

%changelog
