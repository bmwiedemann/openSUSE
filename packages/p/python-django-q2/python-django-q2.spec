#
# spec file for package python-django-q2
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


Name:           python-django-q2
Version:        1.10.0
Release:        0
Summary:        A multiprocessing distributed task queue for Django
License:        MIT
URL:            https://github.com/django-q2/django-q2
Source:         https://files.pythonhosted.org/packages/source/d/django-q2/django_q2-%{version}.tar.gz
# PATCH-FIX-OPENSUSE str() more things inside qmonitor
Patch0:         str-more-things.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module blessed}
BuildRequires:  %{python_module croniter}
BuildRequires:  %{python_module django-picklefield >= 3.1}
BuildRequires:  %{python_module django-redis}
BuildRequires:  %{python_module pytest >= 7.1}
BuildRequires:  %{python_module pytest-django >= 4.5.2}
BuildRequires:  %{python_module redis}
BuildRequires:  redis
BuildRequires:  psmisc
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 4.2
Requires:       python-django-picklefield >= 3.1
Obsoletes:      python-django-q < %{version}
Provides:       python-django-q = %{version}
BuildArch:      noarch
%python_subpackages

%description
Django Q2 is a fork of Django Q. Big thanks to Ilan Steemers for starting this project. Unfortunately, development has stalled since June 2021. Django Q2 is the new updated version of Django Q, with dependencies updates, docs updates and several bug fixes.

%prep
%autosetup -p1 -n django_q2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
# Remove tests
rm -rv %{buildroot}%{$python_sitelib}/django_q/tests
}

%check
redis_dir=$(mktemp -d)
export PYTHONPATH=.
export REDIS_HOST=localhost
export DJANGO_SETTINGS_MODULE=django_q.tests.settings
timeout 10m %{_sbindir}/redis-server --dir $redis_dir &
# No mongo ... and broken tests on 3.14
# test_timeout variations are flaky on i568
%pytest -k 'not (test_mongo or test_recycle or test_max_rss or test_timeout)'
killall redis-server

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/django_q
%{python_sitelib}/django_q2-%{version}.dist-info

%changelog
