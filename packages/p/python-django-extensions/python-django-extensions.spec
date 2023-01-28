#
# spec file for package python-django-extensions
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


%define skip_python2 1
%define skip_python36 1
Name:           python-django-extensions
Version:        3.2.1
Release:        0
Summary:        Extensions for Django
License:        BSD-3-Clause
URL:            https://github.com/django-extensions/django-extensions
Source:         https://github.com/django-extensions/django-extensions/archive/%{version}.tar.gz#/django-extensions-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-Django >= 3.2
Recommends:     python-Pygments
Recommends:     python-Werkzeug
Recommends:     python-django-json-widget
Recommends:     python-djangorestframework >= 3.0.0
Recommends:     python-python-dateutil
Suggests:       python-pip >= 20.1
Suggests:       python-pydot
Suggests:       python-pygraphviz
Suggests:       python-requests
Suggests:       python-shortuuid
BuildArch:      noarch
# SECTION test requirements
# See https://github.com/django-extensions/django-extensions/issues/1617
# for optional dependency django-pdb
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module django-json-widget}
BuildRequires:  %{python_module djangorestframework >= 3.0.0}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pygraphviz}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module shortuuid}
BuildRequires:  %{python_module vobject}
# /SECTION test
%python_subpackages

%description
Django-extensions bundles several useful
additions for Django projects.

%prep
%autosetup -p1 -n django-extensions-%{version}
rm setup.cfg

# Most PipCheckerTests tests fail when using network to connect to PyPI
sed -i 's/djangorestframework==[0-9.]*/djangorestframework/g;s/pip==[0-9.]*/pip/g' tests/management/commands/test_pipchecker.py

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
export PYTHONPATH=${PWD}

skips="(PipCheckerTests and not test_pipchecker_when_requirements_file_does_not_exist)"
# test_should_colorize_noclasses_with_default_lexer - minor html output differences
skips="$skips or test_should_colorize_noclasses_with_default_lexer"
# test_no_models_dot_py fails to generate a .dot file
skips="$skips or test_no_models_dot_py"
# missing fixtures in sdist
skips="$skips or test_migration_is_last_applied or test_syncdata or test_validate_templates"
# https://github.com/django-extensions/django-extensions/issues/1795
skips="$skips or test_should_highlight_bash_syntax_without_name"

# test_export_emails, test_set_fake_emails and test_set_fake_emails fail in setup due to missing fixtures in sdist
%pytest -rs -v -k "not ($skips)" --ignore tests/management/commands/test_set_fake_passwords.py --ignore tests/management/commands/test_set_fake_emails.py --ignore tests/management/commands/test_export_emails.py

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst docs/*.rst
%{python_sitelib}/*django[-_]extensions*/

%changelog
