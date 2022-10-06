#
# spec file for package python-django-opentracing
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-opentracing
Version:        1.1.0
Release:        0
Summary:        OpenTracing support for Django applications
License:        BSD-3-Clause
URL:            https://github.com/opentracing-contrib/python-django/
Source:         https://github.com/opentracing-contrib/python-django/archive/%{version}.tar.gz#/django_opentracing-%{version}.tar.gz
# c.f. https://github.com/opentracing-contrib/python-django/issues/71
Patch0:         dj41.patch
BuildRequires:  %{python_module django-codemod}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module opentracing >= 2.0}
BuildRequires:  %{python_module six}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django
Requires:       python-opentracing >= 2.0
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
OpenTracing support for Django applications.

%prep
%setup -q -n python-django-%{version}
%patch0 -p1
djcodemod run --removed-in 4.0 tests/test_site/urls.py
sed -i 's/import mock/from unittest import mock as mock/' tests/test_site/test_middleware.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
cd tests
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python manage.py test
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*django[-_]opentracing*/

%changelog
