#
# spec file for package python-factory_boy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-factory_boy
Version:        3.3.3
Release:        0
Summary:        Python test fixtures
License:        MIT
URL:            https://github.com/rbarrois/factory_boy
Source:         https://files.pythonhosted.org/packages/source/f/factory_boy/factory_boy-%{version}.tar.gz
BuildRequires:  %{python_module Faker >= 0.7.0}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 0.8}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{suse_version} >= 1699
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
# Fix wrong version
sed -i -e 's|"3.2.1.dev0"|"3.3.0"|g' tests/test_version.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/factory
%{python_sitelib}/factory_boy-%{version}.dist-info

%changelog
