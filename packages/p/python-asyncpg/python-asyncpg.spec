#
# spec file for package python-asyncpg
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-asyncpg
Version:        0.22.0
Release:        0
Summary:        Python asyncio PosgtreSQL driver
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/MagicStack/asyncpg
Source:         https://files.pythonhosted.org/packages/source/a/asyncpg/asyncpg-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.28}
BuildRequires:  %{python_module devel >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libpq5 >= 9.4
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module uvloop >= 0.14.0}
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-server
# /SECTION
%python_subpackages

%description
A fast PostgreSQL Database Client Library for Python/asyncio.

**asyncpg** is a database interface library designed specifically for
PostgreSQL and Python/asyncio with clean implementation

%prep
%setup -q -n asyncpg-%{version}

%build
%python_build

%install
%python_install
%{python_expand find %{buildroot}%{$python_sitearch} -name '*.[ch]' -delete
%fdupes %{buildroot}%{$python_sitearch}
}

%check
# Needed to avoid asyncpg.cluster.ClusterError:
#                 could not find pg_config executable
export PGINSTALLATION=%{_bindir}

mv asyncpg .asyncpg
%pytest_arch -rs
mv .asyncpg asyncpg

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
