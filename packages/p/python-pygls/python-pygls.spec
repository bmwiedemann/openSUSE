#
# spec file for package python-pygls
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-pygls
Version:        2.0.0
Release:        0
Summary:        A pythonic generic language server
License:        Apache-2.0
URL:            https://github.com/openlawlibrary/pygls
Source:         https://github.com/openlawlibrary/pygls/archive/refs/tags/v%{version}.tar.gz#/pygls-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# For testing
BuildRequires:  %{python_module lsprotocol = 2025.0.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# Endif
Requires:       python-attrs >= 24.3.0
Requires:       python-cattrs >= 23.1.2
Requires:       python-lsprotocol = 2025.0.0
Requires:       python-websockets
BuildArch:      noarch
%python_subpackages

%description
pygls (pronounced like "pie glass") is a pythonic generic
implementation of the Language Server Protocol for use as a
foundation for writing your own Language Servers in just a few
lines of code.

%prep
%autosetup -p1 -n pygls-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/pygls
%{python_sitelib}/pygls-%{version}*-info

%changelog
