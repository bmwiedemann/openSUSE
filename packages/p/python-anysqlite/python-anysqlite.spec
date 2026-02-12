#
# spec file for package python-anysqlite
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-anysqlite
Version:        0.0.5
Release:        0
Summary:        Anysqlite provides an async/await interface to the standard sqlite3 library
License:        BSD-3-Clause
URL:            https://github.com/karosis88/anysqlite
Source:         https://github.com/karpetrosyan/anysqlite/archive/refs/tags/v%{version}.tar.gz#/anysqlite-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %pythons
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module anyio > 3.4.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-anyio > 3.4.0
BuildArch:      noarch
%python_subpackages

%description
Anysqlite provides an `async/await` interface to the standard
`sqlite3` library and supports both `trio` and `asyncio` backends
using the power of Anyio.

%prep
%autosetup -p1 -n anysqlite-%{version}

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
%{python_sitelib}/anysqlite
%{python_sitelib}/anysqlite-%{version}.dist-info

%changelog
