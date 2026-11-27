#
# spec file for package python-pypresence
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-pypresence
Version:        4.6.2
Release:        0
Summary:        Discord RPC and Rich Presence client
License:        MIT
URL:            https://github.com/qwertyquerty/pypresence
# PyPI sdist lacks tests/conftest.py, use the GitHub tarball
Source:         %{url}/archive/v%{version}/pypresence-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Discord IPC and Rich Presence client library for Python, with both
synchronous and asyncio interfaces.

%prep
%autosetup -p1 -n pypresence-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pypresence
%{python_sitelib}/pypresence-%{version}.dist-info

%changelog
