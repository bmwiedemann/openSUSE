#
# spec file for package python-django-js-asset
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

%{?sle15_python_module_pythons}
Name:           python-django-js-asset
Version:        2.2
%define intversion %{version}.0
Release:        0
Summary:        Script tag with additional attributes for django.formsMedia
License:        BSD-3-Clause
URL:            https://github.com/matthiask/django-js-asset/
Source:         https://github.com/matthiask/django-js-asset/archive/%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Insert a script tag via forms.Media containing additional
attributes (such as id and data-* for CSP-compatible data
injection.)

%prep
%setup -q -n django-js-asset-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec tests/manage.py test -v 2 testapp

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/js_asset/
%{python_sitelib}/django_js_asset-%{intversion}.dist-info

%changelog
