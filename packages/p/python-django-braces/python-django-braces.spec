#
# spec file for package python-django-braces
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


Name:           python-django-braces
Version:        1.16.0
Release:        0
Summary:        Reusable, generic mixins for Django
License:        BSD-3-Clause
URL:            https://github.com/brack3t/django-braces/
Source:         https://files.pythonhosted.org/packages/source/d/django_braces/django_braces-%{version}.tar.gz
Patch1:         testhack.patch
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
Reusable, generic mixins for Django.

%prep
%setup -q -n django_braces-%{version}
%autopatch -p1
# do not mess with the test setup and rely on pytest defaults
rm conftest.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
PYTHONPATH=.
# test_outdated_login gh#brack3t/django-braces#309
%pytest -k "not test_outdated_login"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/braces
%{python_sitelib}/django_braces-%{version}*info

%changelog
