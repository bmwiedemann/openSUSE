#
# spec file for package python-diskcache
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
%global skip_python2 1
Name:           python-diskcache
Version:        5.0.3
Release:        0
Summary:        Disk and file backed cache
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.grantjenks.com/docs/diskcache/
Source:         https://github.com/grantjenks/python-diskcache/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
DiskCache: Disk Backed Cache

DiskCache is a disk and file backed cache library, written
in pure Python, and compatible with Django.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i '/-n auto/d' tox.ini
rm tests/test_djangocache.py
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
