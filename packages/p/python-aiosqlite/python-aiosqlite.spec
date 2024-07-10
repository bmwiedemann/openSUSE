#
# spec file for package python-aiosqlite
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019 Matthias Fehring <buschmann23@opensuse.org>
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
Name:           python-aiosqlite
Version:        0.20.0
Release:        0
Summary:        AsyncIO Bridge to the Standard Python sqlite3 Module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jreese/aiosqlite
Source:         https://files.pythonhosted.org/packages/source/a/aiosqlite/aiosqlite-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
aiosqlite replicates the standard sqlite3 module, but with async versions of all
the standard connection and cursor methods, and context managers for
automatically closing connections.

%prep
%autosetup -p1 -n aiosqlite-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python_sitelib}/aiosqlite
%{python_sitelib}/aiosqlite-%{version}.dist-info

%changelog
