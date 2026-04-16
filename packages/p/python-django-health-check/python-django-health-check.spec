#
# spec file for package python-django-health-check
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-django-health-check
Version:        4.3.0
Release:        0
Summary:        Run checks on Django and is dependent services
License:        MIT
URL:            https://github.com/codingjoe/django-health-check
Source:         https://github.com/codingjoe/django-health-check/archive/%{version}.tar.gz#/django-health-check-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 5.2}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module celery >= 5.0.0}
BuildRequires:  %{python_module django-storages}
BuildRequires:  %{python_module dnspython >= 2.0.0}
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module flit-scm}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 4.2.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
#
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 5.2
Requires:       python-dnspython >= 2.0.0
Requires:       python-feedparser
BuildArch:      noarch
%python_subpackages

%description
This project checks for various conditions and provides reports when anomalous
behavior is detected.

Services checked include databases, caches, queue servers, celery processes, etc.

%prep
%autosetup -p1 -n django-health-check-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -rf /tmp/testenv
mkdir /tmp/testenv
mv tests /tmp/testenv
cd /tmp/testenv
PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=tests.testapp.settings
%pytest -k "not (test_run_check__dns_working or TestDNSExceptionHandling or test_feed_url)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/health_check
%{python_sitelib}/django_health_check-%{version}.dist-info

%changelog
