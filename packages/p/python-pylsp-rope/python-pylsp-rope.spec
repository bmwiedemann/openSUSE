#
# spec file for package python-pylsp-rope
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


%define skip_python2 1
Name:           python-pylsp-rope
Version:        0.1.11
Release:        0
Summary:        Extended refactoring capabilities for Python LSP Server using Rope
License:        MIT
URL:            https://github.com/python-rope/pylsp-rope
Source:         https://files.pythonhosted.org/packages/source/p/pylsp-rope/pylsp-rope-%{version}.tar.gz
# Source:         pylsp-rope-%%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRequires:  (python3-typing_extensions if python3-base <= 3.6)
# SECTION test requirements
BuildRequires:  %{python_module python-lsp-server}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rope}
# /SECTION
BuildRequires:  fdupes
Requires:       python-python-lsp-server
Requires:       python-rope
Suggests:       python-twine
BuildArch:      noarch
%python_subpackages

%description
Extended refactoring capabilities for Python LSP Server using Rope.

This is a plugin for Python LSP Server.

%prep
%autosetup -p1 -n pylsp-rope-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/test
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc AUTHORS.txt README.md
%license LICENSE
%{python_sitelib}/pylsp_rope
%{python_sitelib}/pylsp_rope-%{version}*-info

%changelog
