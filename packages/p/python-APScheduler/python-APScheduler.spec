#
# spec file for package python-APScheduler
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-APScheduler
Version:        3.9.1.post1
Release:        0
Summary:        In-process task scheduler with Cron-like capabilities
License:        MIT
URL:            https://github.com/agronholm/apscheduler
Source:         https://files.pythonhosted.org/packages/source/A/APScheduler/APScheduler-%{version}.tar.gz
BuildRequires:  %{python_module SQLAlchemy >= 0.8}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-tornado}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools >= 36.2.7}
BuildRequires:  %{python_module setuptools_scm >= 1.7.0}
BuildRequires:  %{python_module six >= 1.4.0}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module tzlocal >= 2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz
Requires:       python-six >= 1.4.0
Requires:       python-tzlocal >= 2.0
Recommends:     python-SQLAlchemy >= 0.8
Recommends:     python-Twisted
Recommends:     python-gevent
Suggests:       python-kazoo
Suggests:       python-pymongo >= 3.0
Suggests:       python-redis
Suggests:       python-tornado >= 4.3
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-funcsigs
BuildRequires:  python-futures
BuildRequires:  python-mock
BuildRequires:  python-trollius
%endif
%ifpython2
Requires:       python-funcsigs
Requires:       python-futures
Requires:       python-trollius
%endif
%python_subpackages

%description
Advanced Python Scheduler (APScheduler) is an in-process task
scheduler that lets you schedule jobs (functions or any python callables) to be
executed at any time of your choosing.

This can be an alternative to externally run cron scripts for
long-running applications (e.g. web applications), as it is platform neutral
and can access the application's variables and functions.

APscheduler provides multiple job stores.

* Configurable scheduling mechanisms (triggers):
  * Cron-like scheduling
  * Delayed scheduling of single run jobs (like the UNIX "at" command)
  * Interval-based (run a job at specified time intervals)
* Multiple, simultaneously active job stores:
  * RAM
  * File-based simple database (shelve)
  * SQLAlchemy (any supported RDBMS works)
  * MongoDB

%prep
%setup -q -n APScheduler-%{version}
sed -i 's/--cov//' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/agronholm/apscheduler/issues/601
%pytest -k 'not test_broken_pool'

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%doc examples/
%{python_sitelib}/apscheduler
%{python_sitelib}/APScheduler-%{version}*-info

%changelog
