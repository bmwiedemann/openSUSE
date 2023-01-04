#
# spec file for package python-django-grappelli
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-django-grappelli
Version:        3.0.4
Release:        0
Summary:        A skin for the Django Admin-Interface
License:        BSD-2-Clause AND LGPL-2.1-or-later
URL:            https://github.com/sehmaschine/django-grappelli
Source:         https://github.com/sehmaschine/django-grappelli/archive/%{version}.tar.gz#/django-grappelli-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module py >= 1.8}
BuildRequires:  %{python_module pytest >= 5.0}
BuildRequires:  %{python_module pytest-django >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
A jazzy skin for the Django Admin-Interface.

%prep
%setup -q -n django-grappelli-%{version}
find grappelli/templates/ -type f | xargs chmod -R a-x
find grappelli/static/grappelli/stylesheets/ -type f | xargs chmod -R a-x

%build
%python_build

%install
%python_install
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
%{python_sitelib}/*grappelli*/

%changelog
