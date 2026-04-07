#
# spec file for package python-django-registration
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
Name:           python-django-registration
Version:        5.2.1
Release:        0
Summary:        An extensible user-registration application for Django
License:        BSD-3-Clause
URL:            https://github.com/ubernostrum/django-registration/
Source:         https://files.pythonhosted.org/packages/source/d/django-registration/django_registration-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module confusable-homoglyphs >= 3.0}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-confusable-homoglyphs >= 3.0
BuildArch:      noarch
%python_subpackages

%description
This is a user registration application for Django. It requires a
functional installation of Django, but has no other
dependencies.

%prep
%autosetup -p1 -n django_registration-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python runtests.py

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/django_registration
%{python_sitelib}/django_registration-%{version}*-info

%changelog
