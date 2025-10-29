#
# spec file for package python-pony
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# not compatible: https://github.com/ponyorm/pony/blob/v0.7.17/setup.py#L112
%define skip_python313 1
%define skip_python314 1
Name:           python-pony
Version:        0.7.19
Release:        0
Summary:        Pony Object-Relational Mapper
License:        Apache-2.0
URL:            https://ponyorm.com
Source:         https://files.pythonhosted.org/packages/source/p/pony/pony-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlite3}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
Pony ORM is a object-relational mapper for Python. Using Pony, users
can create and maintain database-oriented software applications. Pony
is able to write queries to the database using generator expressions.
Pony then analyzes the abstract syntax tree of a generator and
translates it to its SQL equivalent.

%prep
%autosetup -p1 -n pony-%{version}
rm -rf pony/thirdparty/compiler
dos2unix README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/pony/*/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_json fails with sqlite 3.45 gh#ponyorm/pony#704
rm pony/orm/tests/test_json.py
%pyunittest discover -v pony/orm/tests -p 'test_*.py'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pony
%{python_sitelib}/pony-%{version}.dist-info

%changelog
