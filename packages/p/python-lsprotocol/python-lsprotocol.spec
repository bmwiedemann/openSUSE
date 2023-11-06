#
# spec file for package python-lsprotocol
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


Name:           python-lsprotocol
Version:        2023.0.0b1
Release:        0
Summary:        Python implementation of the Language Server Protocol
License:        MIT
URL:            https://github.com/microsoft/lsprotocol
Source:         https://files.pythonhosted.org/packages/source/l/lsprotocol/lsprotocol-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 21.3.0}
BuildRequires:  %{python_module cattrs}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 21.3.0
Requires:       python-cattrs
BuildArch:      noarch
%python_subpackages

%description
lsprotocol is a python implementation of object types used in the
Language Server Protocol (LSP). This repository contains the code
generator and the generated types for LSP.

LSP is used by editors to communicate with various tools to
enables services like code completion, documentation on hover,
formatting, code analysis, etc. The intent of this library is
to allow you to build on top of the types used by LSP. This
repository will be kept up to date with the latest version of LSP
as it is updated.

%prep
%autosetup -p1 -n lsprotocol-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No tests available

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/lsprotocol
%{python_sitelib}/lsprotocol-%{version}*-info

%changelog
