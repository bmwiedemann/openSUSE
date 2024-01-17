#
# spec file for package python-pony
#
# Copyright (c) 2023 SUSE LLC
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


%global skip_python2 1
Name:           python-pony
Version:        0.7.16
Release:        0
Summary:        Pony Object-Relational Mapper
License:        Apache-2.0
URL:            https://ponyorm.com
Source:         https://files.pythonhosted.org/packages/source/p/pony/pony-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-311.patch gh#ponyorm/pony#671
Patch0:         python-311.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
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
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/pony/*/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v pony/orm/tests -p 'test_*.py'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pony
%{python_sitelib}/pony-%{version}*-info

%changelog
