#
# spec file for package python-django-nose
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-django-nose
Version:        1.4.6
Release:        0
Summary:        Django test runner that uses python-nose
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/django-nose/django-nose
Source:         https://files.pythonhosted.org/packages/source/d/django-nose/django-nose-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module dj-database-url}
BuildRequires:  %{python_module nose >= 1.2.1}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-nose >= 1.2.1
BuildArch:      noarch
%python_subpackages

%description
Django test runner that uses nose.

%prep
%setup -q -n django-nose-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec ./manage.py test testapp/tests.py

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst changelog.rst
%{python_sitelib}/*

%changelog
