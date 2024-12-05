#
# spec file for package python-django-q
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
Name:           python-django-q
Version:        1.3.9
Release:        0
Summary:        Multiprocessing Distributed Task Queue for Django
License:        MIT
URL:            https://django-q.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/d/django-q/django-q-%{version}.tar.gz
# pkg_resources is broken since the flufl.lock update in Factory
Patch:          gh-pr-737_importlib.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-arrow
Requires:       python-blessed
Requires:       python-django-picklefield
Requires:       python-redis
Requires:       (python-Django >= 2.2 with python-Django < 5)
Suggests:       python-croniter
Suggests:       python-django-q-rollbar >= 0.1
Suggests:       python-django-q-sentry >= 0.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2 with %python-Django < 5}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module blessed}
BuildRequires:  %{python_module croniter}
BuildRequires:  %{python_module django-picklefield}
BuildRequires:  %{python_module django-redis}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  dos2unix
BuildRequires:  psmisc
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
This package provides a multiprocessing distributed task queue for Django.

%prep
%setup -n django-q-%{version}
# wrong line endings prevent patching
dos2unix django_q/conf.py
%autopatch -p1

# Fix permissions
find -name "*.po" | xargs chmod a-x
find -name "*.py" | xargs chmod a-x
chmod a-x README.rst CHANGELOG.md LICENSE

# Fix encoding
dos2unix README.rst

# Use real redis server
sed -i '/HiredisParser/d' django_q/tests/settings.py

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/django_q/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv django_q/tests .
sed -i 's/django_q.tests/tests/g' tests/*.py
sed -i 's/brokers.redis_broker/django_q.brokers.redis_broker/' tests/test_brokers.py

export DJANGO_SETTINGS_MODULE=tests.settings

export PYTHONPATH=${PWD}

timeout 20m %{_sbindir}/redis-server &
# Mongo & Disque servers not installed
# test_max_rss assertions fail
%pytest -k 'not (mongo or disque or test_max_rss)'
killall redis-server

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/django_q
%{python_sitelib}/django_q-%{version}*-info

%changelog
