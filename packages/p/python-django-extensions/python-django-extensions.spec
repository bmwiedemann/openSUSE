#
# spec file for package python-django-extensions
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


%{?sle15_python_module_pythons}
Name:           python-django-extensions
Version:        4.1
Release:        0
Summary:        Extensions for Django
License:        BSD-3-Clause
URL:            https://github.com/django-extensions/django-extensions
Source:         https://github.com/django-extensions/django-extensions/archive/%{version}.tar.gz#/django-extensions-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-Django >= 4.2
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
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module aiosmtpd}
BuildRequires:  %{python_module django-json-widget}
BuildRequires:  %{python_module djangorestframework >= 3.0.0}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pygraphviz}
BuildRequires:  %{python_module pytest-cov}
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

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export DJANGO_SETTINGS_MODULE=tests.testapp.settings
export PYTHONPATH=${PWD}

skips="(PipCheckerTests and not test_pipchecker_when_requirements_file_does_not_exist)"
# test_no_models_dot_py fails to generate a .dot file
skips="$skips or test_no_models_dot_py"
# missing fixtures in sdist
skips="$skips or test_validate_templates"

# test_should_colorize_noclasses_with_default_lexer can sometimes fail with minor html output differences
# when pygments is updated.  Uncomment this when that occurs, and raise an issue upstream.
#skips="$skips or test_should_colorize_noclasses_with_default_lexer"

# many DumpScriptTests fail with pytest 8 https://github.com/django-extensions/django-extensions/issues/1877
skips="$skips or DumpScriptTests"

%pytest -rs -v -k "not ($skips)"

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst docs/*.rst
%{python_sitelib}/django_extensions
%{python_sitelib}/django_extensions-%{version}.dist-info

%changelog
