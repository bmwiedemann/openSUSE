#
# spec file for package python-django-guardian
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
%define pypi_package_name django-guardian
Name:           python-%{pypi_package_name}
Version:        3.3.1
Release:        0
Summary:        Implementation of per object permissions for Django
License:        BSD-2-Clause
URL:            https://github.com/django-guardian/django-guardian
Source:         https://files.pythonhosted.org/packages/source/d/django-guardian/django_guardian-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module django-environ >= 0.12.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django >= 4.9.0}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module typing-extensions >= 4.12.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
Requires:       python-typing-extensions >= 4.12.0
BuildArch:      noarch
%python_subpackages

%description
django-guardian is implementation of per object permissions as
authorization backend.

%prep
%setup -q -n django_guardian-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/guardian/testapp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/guardian
%{python_sitelib}/django_guardian-%{version}.dist-info

%changelog
