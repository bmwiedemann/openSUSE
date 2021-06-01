#
# spec file for package python-Ming
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Ming
Version:        0.10.3
Release:        0
Summary:        Database mapping layer for MongoDB on Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/TurboGears/Ming
Source:         https://files.pythonhosted.org/packages/source/M/Ming/Ming-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/TurboGears/Ming/master/LICENSE.txt
BuildRequires:  %{python_module FormEncode >= 1.2.1}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module mock >= 0.8.0}
BuildRequires:  %{python_module pymongo >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz
Requires:       python-six >= 1.6.1
Recommends:     python-FormEncode >= 1.2.1
BuildArch:      noarch
%python_subpackages

%description
Database mapping layer for MongoDB on Python.
Includes schema enforcement and some facilities for schema migration.

%prep
%setup -q -n Ming-%{version}
cp %{SOURCE1} .

# gridfs fails
rm ming/tests/test_gridfs.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Real tests require running mongo instance
%pytest -rs -k 'not (TestMappingReal or TestRealBasicMapping or TestRealMongoRelation)'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
