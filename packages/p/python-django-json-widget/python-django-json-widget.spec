#
# spec file for package python-django-json-widget
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
%define skip_python36 1
Name:           python-django-json-widget
Version:        1.1.1
Release:        0
Summary:        Django JSON widget for editing the Django jsonfield
License:        MIT
URL:            https://github.com/jmrivas86/django-json-widget
Source:         https://github.com/jmrivas86/django-json-widget/archive/v%{version}.tar.gz#/django-json-widget-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-future
BuildArch:      noarch
%python_subpackages

%description
Django json widget is an alternative widget that makes it easy to edit the
jsonfield field of django.

%prep
%setup -q -n django-json-widget-%{version}
chmod a-x django_json_widget/static/dist/img/*.* django_json_widget/static/dist/*.* django_json_widget/static/css/*.*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
%python_expand django-admin-%{$python_bin_suffix} test --settings=tests.settings

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
