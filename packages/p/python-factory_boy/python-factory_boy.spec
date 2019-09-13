#
# spec file for package python-factory_boy
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
Name:           python-factory_boy
Version:        2.12.0
Release:        0
Summary:        A test fixtures replacement
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/rbarrois/factory_boy
Source:         https://github.com/FactoryBoy/factory_boy/archive/%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Faker >= 0.7.0}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools >= 0.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-ipaddress
Requires:       python-Faker >= 0.7.0
BuildArch:      noarch
%python_subpackages

%description
A test fixtures replacement based on thoughtbot's factory_girl for Ruby.

%prep
%setup -q -n factory_boy-%{version}
# needs running mongo
rm tests/test_mongoengine.py
sed -i -e '/test_mongoengine/d' tests/__init__.py
# sqlalchemy hickups a lot
rm tests/test_alchemy.py
sed -i -e '/test_alchemy/d' tests/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
