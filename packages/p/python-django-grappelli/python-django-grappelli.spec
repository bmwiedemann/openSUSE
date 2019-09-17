#
# spec file for package python-django-grappelli
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-django-grappelli
Version:        2.13.1
Release:        0
Summary:        A skin for the Django Admin-Interface
License:        BSD-2-Clause AND LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/sehmaschine/django-grappelli
Source:         https://github.com/sehmaschine/django-grappelli/archive/%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module py >= 1.7}
BuildRequires:  %{python_module pytest >= 3.9}
BuildRequires:  %{python_module pytest-django >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
A jazzy skin for the Django Admin-Interface.

%prep
%setup -q -n django-grappelli-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export DJANGO_SETTINGS_MODULE=test_project.settings
# test_related_lookup - uses unicode literals that break on py2
%pytest -k 'not test_related_lookup'

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/*

%changelog
