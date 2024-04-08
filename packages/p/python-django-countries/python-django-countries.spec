#
# spec file for package python-django-countries
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-django-countries
Version:        7.6.1
Release:        0
Summary:        Provides a country field for Django models
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/SmileyChris/django-countries/
Source:         https://files.pythonhosted.org/packages/source/d/django-countries/django-countries-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-typing-extensions
Recommends:     python-djangorestframework
Recommends:     python-graphene-django
Recommends:     python-pyuca
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module graphene-django}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyuca}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
%python_subpackages

%description
Provides a country field for Django models, including
support for Django REST Framework.

%prep
%setup -q -n django-countries-%{version}
sed -i '1{/^#!/d}' django_countries/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/django_countries/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export DJANGO_SETTINGS_MODULE=django_countries.tests.settings
export PYTHONPATH=${PWD}
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/django_countries
%{python_sitelib}/django_countries-%{version}.dist-info

%changelog
