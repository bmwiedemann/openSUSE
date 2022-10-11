#
# spec file for package python-django-mptt
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-django-mptt
Version:        0.14
Release:        0
Summary:        Modified Preorder Tree Traversal for Django Models
License:        MIT
URL:            https://github.com/django-mptt/django-mptt
Source:         https://github.com/django-mptt/django-mptt/archive/refs/tags/%{version}.tar.gz#/django-mptt-%{version}.0.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-django-js-asset
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-js-asset}
BuildRequires:  %{python_module model-bakery}
# /SECTION
%python_subpackages

%description
Utilities for implementing Modified Preorder Tree Traversal with your Django Models and working with trees of Model instances.

%prep
%setup -q -n django-mptt-%{version}
sed -i 's/from model_mommy import mommy/from model_bakery import baker as mommy/' tests/myapp/tests.py
sed -i 's/test_create_by_mommy_exception/_test_create_by_mommy_exception/' tests/myapp/tests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
%python_expand $python tests/manage.py test -v2 --keepdb

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/mptt/
%{python_sitelib}/django[-_]mptt*/

%changelog
