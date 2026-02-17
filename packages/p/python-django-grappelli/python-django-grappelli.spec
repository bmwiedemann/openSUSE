#
# spec file for package python-django-grappelli
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
Name:           python-django-grappelli
Version:        4.0.3
Release:        0
Summary:        A skin for the Django Admin-Interface
License:        BSD-2-Clause AND LGPL-2.1-or-later
URL:            https://github.com/sehmaschine/django-grappelli
Source:         https://github.com/sehmaschine/django-grappelli/archive/%{version}.tar.gz#/django-grappelli-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 5.0}
BuildRequires:  %{python_module pytest-django >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
A jazzy skin for the Django Admin-Interface.

%prep
%autosetup -p1 -n django-grappelli-%{version}

find grappelli/templates/ -type f | xargs chmod -R a-x
find grappelli/static/grappelli/stylesheets/ -type f | xargs chmod -R a-x

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/grappelli/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
PYTHONPATH=.
export PYTHONDONTWRITEBYTECODE=1
export DJANGO_SETTINGS_MODULE=test_project.settings
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/grappelli
%{python_sitelib}/django_grappelli-%{version}.dist-info

%changelog
