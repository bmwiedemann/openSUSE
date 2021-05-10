#
# spec file for package python-django-debug-toolbar
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-django-debug-toolbar
Version:        3.2.1
Release:        0
Summary:        A configurable set of panels that display various debug information
License:        BSD-3-Clause
URL:            https://github.com/jazzband/django-debug-toolbar
Source:         https://github.com/jazzband/django-debug-toolbar/archive/%{version}.tar.gz#/django-debug-toolbar-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-jinja}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlparse >= 0.2.0}
BuildRequires:  fdupes
Requires:       python-Django >= 2.2
Requires:       python-django-jinja
Requires:       python-sqlparse >= 0.2.0
BuildArch:      noarch
%python_subpackages

%description
The Django Debug Toolbar is a configurable set of panels that display various
debug information about the current request/response and when clicked, display
more details about the panel's content.

Currently, the following panels have been written and are working:
 - Django version
 - Request timer
 - A list of settings in settings.py
 - Common HTTP headers
 - GET/POST/cookie/session variable display
 - Templates and context used, and their template paths
 - SQL queries including time to execute and links to EXPLAIN each query
 - List of signals, their args and receivers
 - Logging output via Python's built-in logging, or via the logbook module

There is also one Django management command currently:
 - debugsqlshell: Outputs the SQL that gets executed as you work in the Python
   interactive shell.

%prep
%setup -q -n django-debug-toolbar-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
export DJANGO_SETTINGS_MODULE=tests.settings
export DB_BACKEND=sqlite3
export DB_NAME=":memory:"
%python_expand $python -m django test -v2 tests

%files %{python_files}
%license LICENSE
%doc README.rst docs/*.rst
%{python_sitelib}/*

%changelog
