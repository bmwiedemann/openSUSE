#
# spec file for package python-django-extra-views
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
Name:           python-django-extra-views
Version:        0.13.0
Release:        0
Summary:        Extra class-based views for Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/AndrewIngram/django-extra-views
Source:         https://github.com/AndrewIngram/django-extra-views/archive/%{version}.tar.gz#/django-extra-views-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-six >= 1.5.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module six >= 1.5.2}
# /SECTION
%python_subpackages

%description
Extra class-based views for Django.

%prep
%setup -q -n django-extra-views-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=extra_views_tests.settings
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
