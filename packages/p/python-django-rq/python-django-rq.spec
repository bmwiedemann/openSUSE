#
# spec file for package python-django-rq
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-rq
Version:        2.6.0
Release:        0
Summary:        Simple app that provides django integration for RQ (Redis Queue)
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rq/django-rq
Source:         https://github.com/rq/django-rq/archive/v%{version}/django-rq-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.0
Requires:       python-rq >= 1.2
Recommends:     python-django-redis >= 3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module django-redis >= 3.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module rq >= 1.2}
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
Django integration with RQ, a Redis based Python queuing library.
Django-RQ is a simple app that allows you to configure your queues
in django's settings.py and easily use them in your project.

%prep
%setup -q -n django-rq-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/django_rq/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{_sbindir}/redis-server &
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=django_rq.tests.settings
%pytest -k 'not (test_job_details or test_jobs)'

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/django[-_]rq*/

%changelog
