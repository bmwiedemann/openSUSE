#
# spec file for package python-apsw
#
# Copyright (c) 2020 SUSE LLC
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
%define tarver  3.33.0-r1
Name:           python-apsw
Version:        3.33.0_r1
Release:        0
Summary:        Another Python SQLite Wrapper
License:        Zlib
Group:          Development/Libraries/Python
URL:            https://github.com/rogerbinns/apsw/
Source:         https://github.com/rogerbinns/apsw/archive/%{tarver}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(sqlite3) >= 3.30
%python_subpackages

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%prep
%setup -q -n apsw-%{tarver}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install

%check
export CFLAGS="%{optflags} -fno-strict-aliasing"
%{python_expand $python setup.py build_ext --inplace
$python setup.py test
$python setup.py clean
}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
