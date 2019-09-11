#
# spec file for package python-django-model-utils
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-django-model-utils
Version:        3.2.0
Release:        0
Summary:        Django model mixins and utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/carljm/django-model-utils/
Source:         https://github.com/jazzband/django-model-utils/archive/%{version}.tar.gz#/django-model-utils-%{version}.tar.gz
# PATCH-FIX-SUSE switch to sqlite from pgsql during testing
Patch0:         use-sqlite.patch
BuildRequires:  %{python_module Django >= 1.4.2}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-Django >= 1.4.2
BuildArch:      noarch
%python_subpackages

%description
Django model mixins and utilities.

%prep
%setup -q -n django-model-utils-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip JoinManagerTest tests as they need proper DB (pgsql/mysql)
%pytest -k 'not JoinManagerTest'

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.rst CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
