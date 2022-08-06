#
# spec file for package python-django-q
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-django-q
Version:        1.3.9
Release:        0
Summary:        Multiprocessing Distributed Task Queue for Django
License:        MIT
URL:            https://django-q.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/d/django-q/django-q-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-arrow
Requires:       python-blessed
Requires:       python-django-picklefield
Requires:       python-redis
Suggests:       python-croniter
Suggests:       python-django-q-rollbar >= 0.1
Suggests:       python-django-q-sentry >= 0.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module blessed}
BuildRequires:  %{python_module croniter}
BuildRequires:  %{python_module django-picklefield}
BuildRequires:  %{python_module django-redis}
BuildRequires:  %{python_module hiredis}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  dos2unix
# /SECTION
%python_subpackages

%description
This package provides a multiprocessing distributed task queue for Django.

%prep
%autosetup -n django-q-%{version} -p1

# Fix permissions
find -name "*.po" | xargs chmod a-x
chmod a-x README.rst CHANGELOG.md LICENSE

# Fix encoding
dos2unix README.rst

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/django_q/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# Tests require a docker container to run

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/django_q
%{python_sitelib}/django_q-%{version}*-info

%changelog
