#
# spec file for package python-plyvel
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-plyvel
Version:        1.5.1
Release:        0
Summary:        Python interface to LevelDB
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            https://plyvel.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/p/plyvel/plyvel-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.17}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  leveldb-devel >= 1.21
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
mkdir tests

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}

%check
mv plyvel plyvel.hide
%pytest_arch

%files %{python_files}
%license LICENSE.rst
%doc doc NEWS.rst README.rst
%{python_sitearch}/plyvel
%{python_sitearch}/plyvel-%{version}*-info

%changelog
