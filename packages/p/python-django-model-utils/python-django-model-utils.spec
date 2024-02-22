#
# spec file for package python-django-model-utils
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


Name:           python-django-model-utils
Version:        4.4.0
Release:        0
Summary:        Django model mixins and utilities
License:        BSD-3-Clause
URL:            https://github.com/jazzband/django-model-utils
Source:         https://files.pythonhosted.org/packages/source/d/django-model-utils/django-model-utils-%{version}.tar.gz
# Upstreamed to https://github.com/jazzband/django-model-utils/pull/516
Patch0:         use-sqlite.patch
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-Django >= 2.0
BuildArch:      noarch
%python_subpackages

%description
Django model mixins and utilities.

%prep
%autosetup -p1 -n django-model-utils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip JoinManagerTest tests as they need proper DB (pgsql/mysql)
export PYTHONPATH=.
export SQLITE=1
%pytest -k 'not JoinManagerTest'

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.rst CHANGES.rst README.rst
%{python_sitelib}/model_utils
%{python_sitelib}/django_model_utils-%{version}.dist-info

%changelog
