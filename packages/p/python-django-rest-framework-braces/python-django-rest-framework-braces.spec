#
# spec file for package python-django-rest-framework-braces
#
# Copyright (c) 2022 SUSE LLC
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


%global skip_python36 1
Name:           python-django-rest-framework-braces
Version:        0.3.4
Release:        0
Summary:        Django REST Framework (DRF) utilities
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dealertrack/django-rest-framework-braces
Source:         https://files.pythonhosted.org/packages/source/d/django-rest-framework-braces/django-rest-framework-braces-%{version}.tar.gz
Patch0:         pr_34.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-dateutils
Requires:       python-djangorestframework
Requires:       python-pytz
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module dateutils}
BuildRequires:  %{python_module django-extensions}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Collection of utilities for working with Django REST Framework (DRF).

%prep
%setup -q -n django-rest-framework-braces-%{version}
%patch0 -p1
sed -i 's/from collections import Mapping/from collections.abc import Mapping/' drf_braces/renderers.py

sed -i '/argparse/d' setup.* requirements*
sed -i '/\.admin/d' tests/settings.py
sed -i 's/^import mock/from unittest import mock/' drf_braces/tests/test_mixins.py drf_braces/tests/*/test_*.py
# NullBooleanField is removed from django gh#dealertrack/django-rest-framework-braces#36
sed -i "s/'NullBooleanField',//" drf_braces/fields/_fields.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/dealertrack/django-rest-framework-braces/issues/29
PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest -k 'not test_to_python_not_iso8601'

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE.rst
%{python_sitelib}/drf_braces
%{python_sitelib}/django_rest_framework_braces-%{version}*-info

%changelog
