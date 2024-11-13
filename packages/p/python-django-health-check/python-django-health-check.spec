#
# spec file for package python-django-health-check
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


%{?sle15_python_module_pythons}
Name:           python-django-health-check
Version:        3.18.3
Release:        0
Summary:        Run checks on Django and is dependent services
License:        MIT
URL:            https://github.com/revsys/django-health-check
Source:         https://github.com/revsys/django-health-check/archive/%{version}.tar.gz#/django-health-check-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module celery}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# Additional test requirements
BuildRequires:  %{python_module django-storages}
BuildRequires:  %{python_module boto3}
#
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
BuildArch:      noarch
%python_subpackages

%description
This project checks for various conditions and provides reports when anomalous
behavior is detected.

Services checked include databases, caches, queue servers, celery processes, etc.

%prep
%autosetup -p1 -n django-health-check-%{version}
# setuptools-scm fails for GitHub archives
sed -i 's/use_scm_version=True/version="%{version}"/' setup.py

# Hot fix: include sub-packages (and a template in %%install)
# https://github.com/KristianOellegaard/django-health-check/issues/268
sed -i 's/packages = health_check/packages = find:/' setup.cfg

# do not nedlessly pull extra deps
sed -i -e '/sphinx/d;/pytest-runner/d;/--cov[-=]/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand # https://github.com/KristianOellegaard/django-health-check/issues/268
rm -rf %{buildroot}%{$python_sitelib}/tests/
if [[ -f %{buildroot}%{$python_sitelib}/health_check/templates/health_check/index.html ]]; then false; fi
ls %{buildroot}%{$python_sitelib}/health_check/cache/
mkdir -p %{buildroot}%{$python_sitelib}/health_check/templates/health_check
cp health_check/templates/health_check/index.html %{buildroot}%{$python_sitelib}/health_check/templates/health_check
%fdupes %{buildroot}%{$python_sitelib}
}

%check
rm -rf /tmp/testenv
mkdir /tmp/testenv
mv tests /tmp/testenv
cd /tmp/testenv
PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=tests.testapp.settings
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/health_check
%{python_sitelib}/django_health_check-%{version}.dist-info

%changelog
