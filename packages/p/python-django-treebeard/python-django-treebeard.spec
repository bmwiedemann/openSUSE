#
# spec file for package python-django-treebeard
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
%define skip_python2 1
Name:           python-django-treebeard
Version:        4.3.1
Release:        0
Summary:        Efficient tree implementations for Django
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/django-treebeard/django-treebeard/
Source:         https://files.pythonhosted.org/packages/source/d/django-treebeard/django-treebeard-%{version}.tar.gz
Patch0:         https://github.com/django-treebeard/django-treebeard/commit/50489e63.patch#/merged_50489e63.patch
Patch1:         https://github.com/django-treebeard/django-treebeard/commit/d6f117f0.patch#/merged_d6f117f0.patch
Patch2:         https://github.com/django-treebeard/django-treebeard/commit/56121dca.patch#/merged_56121dca.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.8}
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
%setup -q -n django-treebeard-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/treebeard/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_expand cp -r treebeard/tests/ %{buildroot}%{$python_sitelib}/treebeard/

export DJANGO_SETTINGS_MODULE=treebeard.tests.settings
%pytest

%python_expand rm -r %{buildroot}%{$python_sitelib}/treebeard/tests/

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
