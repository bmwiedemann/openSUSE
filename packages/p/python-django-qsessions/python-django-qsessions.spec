#
# spec file for package python-django-qsessions
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
%define skip_python2 1
%define skip_python36 1
Name:           python-django-qsessions
Version:        1.1.3
Release:        0
Summary:        Extended session backends for Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/QueraTeam/django-qsessions
Source:         https://files.pythonhosted.org/packages/source/d/django-qsessions/django-qsessions-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.10
Requires:       python-django-ipware >= 2.0.0
Requires:       python-user-agents >= 1.1.0
Suggests:       python-geoip2 >= 3.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.10}
BuildRequires:  %{python_module django-ipware >= 2.0.0}
BuildRequires:  %{python_module geoip2 >= 3.0.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module user-agents >= 1.1.0}
# /SECTION
%python_subpackages

%description
Extended session backends for Django.

%prep
%setup -q -n django-qsessions-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export DJANGO_SETTINGS_MODULE=tests.settings_db
export PYTHONPATH=${PWD}
%pytest

%files %{python_files}
%doc README.rst CHANGELOG.md
%license LICENSE.txt
%{python_sitelib}/*qsessions*/

%changelog
