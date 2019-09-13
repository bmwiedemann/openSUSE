#
# spec file for package python-pony
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
Name:           python-pony
Version:        0.7.10
Release:        0
Summary:        Pony Object-Relational Mapper
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://ponyorm.com
Source:         https://files.pythonhosted.org/packages/source/p/pony/pony-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  python2
%endif
%python_subpackages

%description
Pony ORM is a object-relational mapper for Python. Using Pony, users
can create and maintain database-oriented software applications. Pony
is able to write queries to the database using generator expressions.
Pony then analyzes the abstract syntax tree of a generator and
translates it to its SQL equivalent.

%prep
%setup -q -n pony-%{version}
dos2unix README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
