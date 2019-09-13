#
# spec file for package python-plyvel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-plyvel
Version:        1.1.0
Release:        0
Summary:        Python interface to LevelDB
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            https://plyvel.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/p/plyvel/plyvel-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.17}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  leveldb-devel >= 1.20
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Plyvel is a Python interface to LevelDB.

In addition to basic features like getting, putting and deleting
data, Plyvel allows you to use write batches, database snapshots,
very flexible iterators, prefixed databases, bloom filters, custom
cache sizes, custom comparators.

%prep
%setup -q -n plyvel-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}

%check
%python_exec setup.py test
%pytest

%files %{python_files}
%license LICENSE.rst
%doc doc NEWS.rst README.rst
%{python_sitearch}/*

%changelog
