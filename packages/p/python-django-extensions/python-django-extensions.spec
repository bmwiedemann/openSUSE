#
# spec file for package python-django-extensions
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


Name:           python-django-extensions
Version:        2.2.1
Release:        0
Summary:        Extensions for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/django-extensions/django-extensions
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
Recommends:     python-python-dateutil
Recommends:     python-djangorestframework
Suggests:       python-pip
Suggests:       python-shortuuid
Suggests:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
Django-extensions bundles several useful
additions for Django projects. See the project page for more information:
http://github.com/django-extensions/django-extensions

%prep
%setup -q -n django-extensions-%{version}

# See https://github.com/django-extensions/django-extensions/issues/1123
rm tests/test_encrypted_fields.py

# pip checks not possible in rpmbuild,
# and also not particularly useful when packaged.
rm tests/management/commands/test_pipchecker.py

# tests are completely borked and the keyczar module is deprecated
#rm tests/db/fields/test_encrypted.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.testapp.settings

%if 0%{?have_python2} && ! 0%{?skip_python2}
# It is not possible to use %%pytest here, as it expands to py.test-3.7
# which causes /usr/bin to be in the PYTHONPATH.
# django_extensions/management/commands/mail_debug.py imports smtpd,
# and python2-base adds smtpd.py to /usr/bin, so the import fails on
# Python 3.

python2 -m pytest
%endif
%if 0%{?have_python3} && ! 0%{?skip_python3}
# Test collection exception ValueError: wrapper loop when unwrapping call
python3 -m pytest \
    --ignore tests/test_logging_filters.py \
    --ignore tests/management/commands/test_reset_db.py \
    --ignore tests/management/commands/test_reset_schema.py
%endif

%files %{python_files}
%license LICENSE
%doc README.rst docs/*.*
%{python_sitelib}/*

%changelog
