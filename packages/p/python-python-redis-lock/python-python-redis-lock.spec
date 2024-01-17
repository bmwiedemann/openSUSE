#
# spec file for package python-python-redis-lock
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
Name:           python-python-redis-lock
Version:        4.0.0
Release:        0
Summary:        Lock context manager implemented via redis SETNX/BLPOP
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/python-redis-lock
Source:         https://files.pythonhosted.org/packages/source/p/python-redis-lock/python-redis-lock-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-redis >= 2.10.0
Recommends:     python-django-redis >= 3.8.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module django-redis >= 3.8.0}
BuildRequires:  %{python_module process-tests}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 2.10.0}
# /SECTION
%python_subpackages

%description
Lock context manager implemented via redis SETNX/BLPOP.

%prep
%autosetup -p1 -n python-redis-lock-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests temporarily switched off gh#ionelmc/python-redis-lock#107
# # redis-server is in sbin
# export PATH=$PATH:%%{_sbindir}
# export PYTHONPATH=$(pwd)/tests
# export DJANGO_SETTINGS_MODULE=test_project.settings
# # gh#ionelmc/python-redis-lock#86
# %%pytest -k 'not test_no_overlap2'

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/redis_lock
%{python_sitelib}/python_redis_lock-%{version}*-info

%changelog
