#
# spec file for package python-django-extensions
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


%define skip_python2 1
Name:           python-django-extensions
Version:        2.2.8
Release:        0
Summary:        Extensions for Django
License:        BSD-3-Clause
URL:            https://github.com/django-extensions/django-extensions
Source:         https://github.com/django-extensions/django-extensions/archive/%{version}.tar.gz#/django-extensions-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module django-json-widget}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module shortuuid}
BuildRequires:  %{python_module six >= 1.2}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module vobject}
BuildRequires:  fdupes
Requires:       python-Django
Requires:       python-six >= 1.2
Recommends:     python-Pygments
Recommends:     python-Werkzeug
Recommends:     python-django-json-widget
Recommends:     python-djangorestframework
Recommends:     python-python-dateutil
Suggests:       python-pip
Suggests:       python-python-dateutil
Suggests:       python-shortuuid
BuildArch:      noarch
%python_subpackages

%description
Django-extensions bundles several useful
additions for Django projects. See the project page for more information:
http://github.com/django-extensions/django-extensions

%prep
%setup -q -n django-extensions-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export DJANGO_SETTINGS_MODULE=tests.testapp.settings
# Test collection exception ValueError: wrapper loop when unwrapping call
# test_should_highlight_python_syntax_with_name - breaks ordering on py versions, fragile 
%python_expand $python -m pytest -v \
    --ignore tests/test_logging_filters.py \
    --ignore tests/management/commands/test_reset_db.py \
    --ignore tests/management/commands/test_reset_schema.py \
    --ignore tests/management/commands/test_pipchecker.py \
    -k 'not test_should_highlight_python_syntax_with_name'

%files %{python_files}
%license LICENSE
%doc README.rst docs/*.*
%{python_sitelib}/*

%changelog
