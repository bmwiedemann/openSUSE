#
# spec file for package python-django-guardian
#
# Copyright (c) 2025 SUSE LLC
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
Version:        2.4.0
Release:        0
Summary:        Implementation of per object permissions for Django
License:        BSD-3-Clause
URL:            https://github.com/lukaszb/django-guardian
Source:         https://files.pythonhosted.org/packages/source/d/django-guardian/django-guardian-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-environ}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
django-guardian is implementation of per object permissions as
authorization backend.

%prep
%setup -q -n django-guardian-%{version}
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
%doc CHANGES README.rst
%{python_sitelib}/guardian
%{python_sitelib}/django_guardian-%{version}.dist-info

%changelog
