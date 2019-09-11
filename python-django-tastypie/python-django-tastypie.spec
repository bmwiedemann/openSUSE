#
# spec file for package python-django-tastypie
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
Name:           python-django-tastypie
Version:        0.14.2
Release:        0
Summary:        A webservice API framework layer for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django-tastypie/django-tastypie
Source:         https://github.com/django-tastypie/django-tastypie/archive/v%{version}.tar.gz
# https://github.com/django-tastypie/django-tastypie/pull/1562
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module biplist}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module python-mimeparse >= 0.1.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
Requires:       python-python-dateutil >= 2.1
Requires:       python-python-mimeparse >= 0.1.4
Recommends:     python-PyYAML
Recommends:     python-biplist
Recommends:     python-defusedxml
Recommends:     python-lxml
BuildArch:      noarch
%python_subpackages

%description
Tastypie is a webservice API framework for Django. It provides a
customizable abstraction for creating REST-style interfaces.

%prep
%setup -q -n django-tastypie-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The tests are doing what is specified in tox.ini
%{python_expand export PYTHONPATH=./tests/
$python -m django test -p '*' core.tests --settings=settings_core
$python -m django test basic.tests --settings=settings_basic
$python -m django test related_resource.tests --settings=settings_related
$python -m django test alphanumeric.tests --settings=settings_alphanumeric
$python -m django test authorization.tests --settings=settings_authorization
$python -m django test content_gfk.tests --settings=settings_content_gfk
$python -m django test customuser.tests --settings=settings_customuser
$python -m django test namespaced.tests --settings=settings_namespaced
$python -m django test slashless.tests --settings=settings_slashless
$python -m django test validation.tests --settings=settings_validation
}

%files %{python_files}
%license LICENSE
%doc AUTHORS *.rst docs/*.rst docs/release_notes/ docs/code/
%{python_sitelib}/*

%changelog
