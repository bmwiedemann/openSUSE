#
# spec file for package python-django-filter
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
Name:           python-django-filter
Version:        25.2
Release:        0
Summary:        Reusable Django app to allow users to filter queryset dynamically
License:        BSD-3-Clause
URL:            https://github.com/carltongibson/django-filter
Source:         https://files.pythonhosted.org/packages/source/d/django_filter/django_filter-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module django-crispy-forms}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytz}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
BuildArch:      noarch
%python_subpackages

%description
Django-filter is a reusable Django application for allowing users to filter queryset dynamically.
For usage and installation instructions, consult the docs directory.

%prep
%setup -q -n django_filter-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py -v 2

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES.rst README.rst docs/{*.txt,ref/*.txt}
%{python_sitelib}/django_filters
%{python_sitelib}/django_filter-%{version}.dist-info

%changelog
