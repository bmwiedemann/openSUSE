#
# spec file for package python-django-treebeard
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


%define skip_python2 1
Name:           python-django-treebeard
Version:        4.5.1
Release:        0
Summary:        Efficient tree implementations for Django
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/django-treebeard/django-treebeard/
Source:         https://files.pythonhosted.org/packages/source/d/django-treebeard/django-treebeard-%{version}.tar.gz
# PATCH-FIX-UPSTREAM update-tests.patch gh#django-treebeard/django-treebeard#241 mcepl@suse.com
# update tests to work with the modern versions of libraries
Patch0:         update-tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module pytest-django >= 4.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
django-treebeard is a library that implements three efficient tree implementations
for the Django Web Framework:

- Adjacency List
- Materialized Path
- Nested Sets

%prep
%autosetup -p1 -n django-treebeard-%{version}

sed -i 's/\r//' CHANGES.md README.md UPDATING

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/treebeard/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
cat << EOF >>pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = treebeard.tests.settings
python_files = tests.py test_*.py *_tests.py
django_find_project = false
markers =
    django_db
EOF
%python_expand cp -r treebeard/tests/ %{buildroot}%{$python_sitelib}/treebeard/

export DJANGO_SETTINGS_MODULE=treebeard.tests.settings
PYTHONPATH=.
%pytest

%python_expand rm -r %{buildroot}%{$python_sitelib}/treebeard/tests/

%files %{python_files}
%doc CHANGES.md README.md UPDATING
%license LICENSE
%{python_sitelib}/treebeard
%{python_sitelib}/django_treebeard-%{version}*-info

%changelog
