#
# spec file for package python-django-tastypie
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
Name:           python-django-tastypie
Version:        0.14.5
Release:        0
Summary:        A webservice API framework layer for Django
License:        BSD-3-Clause
URL:            https://github.com/django-tastypie/django-tastypie
Source:         https://github.com/django-tastypie/django-tastypie/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module biplist}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module lxml}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The tests are doing what is specified in tox.ini
%{python_expand export PYTHONPATH=${PWD}:${PWD}/tests/
django-admin-%{$python_bin_suffix} test -v 3 -p '*' core.tests --settings=settings_core
django-admin-%{$python_bin_suffix} test -v 3 basic.tests --settings=settings_basic
django-admin-%{$python_bin_suffix} test -v 3 related_resource.tests --settings=settings_related
django-admin-%{$python_bin_suffix} test -v 3 alphanumeric.tests --settings=settings_alphanumeric
django-admin-%{$python_bin_suffix} test -v 3 authorization.tests --settings=settings_authorization
django-admin-%{$python_bin_suffix} test -v 3 content_gfk.tests --settings=settings_content_gfk
django-admin-%{$python_bin_suffix} test -v 3 customuser.tests --settings=settings_customuser
django-admin-%{$python_bin_suffix} test -v 3 namespaced.tests --settings=settings_namespaced
django-admin-%{$python_bin_suffix} test -v 3 slashless.tests --settings=settings_slashless
django-admin-%{$python_bin_suffix} test -v 3 validation.tests --settings=settings_validation
}

%files %{python_files}
%license LICENSE
%doc AUTHORS *.rst docs/*.rst docs/release_notes/ docs/code/
%{python_sitelib}/*tastypie*/

%changelog
