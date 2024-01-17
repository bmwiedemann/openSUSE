#
# spec file for package python-django-model-utils
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
%define skip_python36 1
Name:           python-django-model-utils
Version:        4.3.1
Release:        0
Summary:        Django model mixins and utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-model-utils
Source:         https://files.pythonhosted.org/packages/source/d/django-model-utils/django-model-utils-%{version}.tar.gz
# Upstreamed to https://github.com/jazzband/django-model-utils/pull/516
Patch0:         use-sqlite.patch
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-Django >= 2.0
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
export PYTHONPATH=.
export SQLITE=1
%pytest -k 'not JoinManagerTest'

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.rst CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
