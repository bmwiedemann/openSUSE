#
# spec file for package python-django-celery-beat
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-django-celery-beat
Version:        2.6.0
Release:        0
Summary:        Database-backed Periodic Tasks
License:        BSD-3-Clause
URL:            https://github.com/celery/django-celery-beat
Source:         https://files.pythonhosted.org/packages/source/d/django-celery-beat/django-celery-beat-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module celery >= 5.2.3}
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module case >= 1.3.1}
BuildRequires:  %{python_module cron-descriptor >= 1.2.32}
BuildRequires:  %{python_module django-timezone-field >= 5.0}
BuildRequires:  %{python_module ephem}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytest-django >= 4.5.2}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module python-crontab >= 2.3.4}
BuildRequires:  %{python_module tzdata}
BuildRequires:  timezone
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 3.2
Requires:       python-celery >= 5.2.3
Requires:       python-cron-descriptor >= 1.2.32
Requires:       python-django-timezone-field >= 5.0
Requires:       python-python-crontab >= 2.3.4
Requires:       python-tzdata
Suggests:       python-importlib-metadata < 5.0
Suggests:       python-backports.zoneinfo
BuildArch:      noarch
%python_subpackages

%description
Database-backed Periodic Tasks.

%prep
%autosetup -p1 -n django-celery-beat-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=t.proj.settings
# test_run_task, test_run_tasks: I see ghosts in the buildlog https://github.com/celery/django-celery-beat/issues/665
%pytest -k "not test_run_task"

%files %{python_files}
%doc AUTHORS Changelog README.rst
%license LICENSE
%{python_sitelib}/django_celery_beat
%{python_sitelib}/django_celery_beat-%{version}.dist-info

%changelog
