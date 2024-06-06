#
# spec file for package python-apsw
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-apsw
Version:        3.46.0.0
Release:        0
Summary:        Another Python SQLite Wrapper
License:        Zlib
Group:          Development/Libraries/Python
URL:            https://github.com/rogerbinns/apsw/
Source:         https://github.com/rogerbinns/apsw/archive/refs/tags/%{version}.tar.gz#/apsw-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(sqlite3) >= 3.44
%python_subpackages

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%prep
%autosetup -p1 -n apsw-%{version}

# See the discussion on gh#rogerbinns/apsw#462
cat << EOF >setup.apsw
[build_ext]
use_system_sqlite_config = true
EOF

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel
%python_exec setup.py build_test_extension

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# gh#rogerbinns/apsw#462
# We cannot use %%pyunittest_arch here, see the ticket for the discussion
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch} PYTHONDONTWRITEBYTECODE=1
$python -m apsw.tests -v
}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/apsw
%{python_sitearch}/apsw-%{version}*-info

%changelog
