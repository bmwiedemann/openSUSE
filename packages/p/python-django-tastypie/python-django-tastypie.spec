#
# spec file for package python-django-tastypie
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
Name:           python-django-tastypie
Version:        0.14.3
Release:        0
Summary:        A webservice API framework layer for Django
License:        BSD-3-Clause
URL:            https://github.com/django-tastypie/django-tastypie
Source:         https://github.com/django-tastypie/django-tastypie/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM merged_pr_1624_chunk.patch -- based on PR 1624
Patch0:         merged_pr_1624_chunk.patch
BuildRequires:  %{python_module Django >= 1.11.0}
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
Requires:       python-Django >= 1.11.0
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
%patch0 -p1
# https://github.com/django-tastypie/django-tastypie/issues/1617
sed -Ei 's/(test_apikey_and_authentication_enforce_user|test_is_authenticated)/_\1/' tests/core/tests/authentication.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The tests are doing what is specified in tox.ini
%{python_expand export PYTHONPATH=${PWD}:${PWD}/tests/
django-admin.py-%{$python_bin_suffix} test -p '*' core.tests --settings=settings_core
django-admin.py-%{$python_bin_suffix} test basic.tests --settings=settings_basic
django-admin.py-%{$python_bin_suffix} test related_resource.tests --settings=settings_related
django-admin.py-%{$python_bin_suffix} test alphanumeric.tests --settings=settings_alphanumeric
django-admin.py-%{$python_bin_suffix} test authorization.tests --settings=settings_authorization
django-admin.py-%{$python_bin_suffix} test content_gfk.tests --settings=settings_content_gfk
django-admin.py-%{$python_bin_suffix} test customuser.tests --settings=settings_customuser
django-admin.py-%{$python_bin_suffix} test namespaced.tests --settings=settings_namespaced
django-admin.py-%{$python_bin_suffix} test slashless.tests --settings=settings_slashless
django-admin.py-%{$python_bin_suffix} test validation.tests --settings=settings_validation
}

%files %{python_files}
%license LICENSE
%doc AUTHORS *.rst docs/*.rst docs/release_notes/ docs/code/
%{python_sitelib}/*

%changelog
