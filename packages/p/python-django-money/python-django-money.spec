#
# spec file for package python-django-money
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


Name:           python-django-money
Version:        3.5.4
Release:        0
Summary:        Django support for using money and currency fields
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django-money/django-money
Source:         https://github.com/django-money/django-money/archive/%{version}.tar.gz#/django-money-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-py-moneyed >= 2.0
Requires:       python-setuptools
Recommends:     python-certifi
Suggests:       python-django-reversion
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-reversion}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py-moneyed >= 2.0}
BuildRequires:  %{python_module pytest >= 8.2}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
Django money and currency fields in models and forms.

%prep
%autosetup -p1 -n django-money-%{version}

sed -i -e '/^addopts/d' pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=$(pwd -P)
# we don't have python-mixer and it is needed only for tests
%pytest -k "not mixer"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/djmoney
%{python_sitelib}/django_money-%{version}*-info

%changelog
