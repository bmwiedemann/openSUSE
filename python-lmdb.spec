#
# spec file for package python-lmdb
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lmdb
Version:        1.4.0
Release:        0
Summary:        Universal Python binding for the LMDB 'Lightning' Database
License:        OLDAP-2.8
Group:          Development/Languages/Python
URL:            http://github.com/dw/py-lmdb/
Source:         https://files.pythonhosted.org/packages/source/l/lmdb/lmdb-%{version}.tar.gz
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  lmdb-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This is a universal Python binding for the LMDB 'Lightning' Database.

LMDB is a tiny database with the following properties:
  * Ordered map interface (keys are always lexicographically sorted).
  * Reader/writer transactions: readers don’t block writers,
    writers don’t block readers.
    Each environment supports one concurrent write transaction.
  * Cheap read transactions.
  * Environments may be opened by multiple processes on the same host.
  * Multiple named databases may be created with transactions covering
    all named databases.
  * Memory mapped, allowing for zero copy lookup and iteration.
    This is optionally exposed to Python using the buffer() interface.
  * Maintenance requires no external process or background threads.
  * No application-level caching is required:
    LMDB uses the operating system’s buffer cache.

%prep
%setup -q -n lmdb-%{version}

%build
export LMDB_FORCE_SYSTEM=1
%python_build

%check
%python_exec setup.py develop --user
%python_exec -c 'import lmdb.cpython'
%python_exec -m pytest -v tests

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc README.md ChangeLog
%{python_sitearch}/*

%changelog
