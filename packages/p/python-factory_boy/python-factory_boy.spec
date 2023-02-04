#
# spec file for package python-factory_boy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-factory_boy
Version:        3.2.1
Release:        0
Summary:        Python test fixtures
License:        MIT
URL:            https://github.com/rbarrois/factory_boy
Source:         https://files.pythonhosted.org/packages/source/f/factory_boy/factory_boy-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE  tests-skip-django-py36.patch -- don't test django on python36: no python36-Django 4, code@bnavigator.de
Patch0:         tests-skip-django-py36.patch
BuildRequires:  %{python_module Faker >= 0.7.0}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module setuptools >= 0.8}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{suse_version} >= 1550
BuildRequires:  %{python_module Django}
%endif
Requires:       python-Faker >= 0.7.0
BuildArch:      noarch
%python_subpackages

%description
A test fixtures replacement based on thoughtbot's factory_girl for Ruby.

%prep
%autosetup -p1 -n factory_boy-%{version}
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
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/factory
%{python_sitelib}/factory_boy-%{version}*-info

%changelog
