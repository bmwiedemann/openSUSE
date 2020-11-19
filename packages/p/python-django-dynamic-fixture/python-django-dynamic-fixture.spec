#
# spec file for package python-django-dynamic-fixture
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
Name:           python-django-dynamic-fixture
Version:        3.1.1
Release:        0
Summary:        Python library to create dynamic model instances for testing purposes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/paulocheque/django-dynamic-fixture
Source:         https://github.com/paulocheque/django-dynamic-fixture/archive/%{version}.tar.gz#/django-dynamic-fixture-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Conflicts:      python-ddf
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module django-nose}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Python library to create dynamic model instances for testing purposes.

%prep
%setup -q -n django-dynamic-fixture-%{version}
sed -i '1{/^#!/d}' django_dynamic_fixture/models_test.py

# test_ddf_geo imports modules which dont exist on older Django
rm django_dynamic_fixture/tests/test_ddf_geo.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
%pytest --ds=settings_sqlite django_dynamic_fixture/tests/

%files %{python_files}
%doc README.mkd
%license LICENSE.txt
%{python_sitelib}/*

%changelog
