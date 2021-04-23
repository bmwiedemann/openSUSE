#
# spec file for package python-python-sql
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
%define base_name python-sql
Name:           python-%{base_name}
Version:        1.2.0
Release:        0
Summary:        Library to write SQL queries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://pypi.io/project/python-sql
Source:         https://pypi.io/packages/source/p/%{base_name}/%{base_name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
python-sql is a library to write SQL queries in a pythonic way.

%prep
%setup -q -n %{base_name}-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%doc README
%{python_sitelib}/*

%changelog
