#
# spec file for package python-django-axes
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-django-axes
Version:        5.40.1
Release:        0
License:        MIT
Summary:        Keep track of failed login attempts in Django-powered sites
URL:            https://github.com/jazzband/django-axes
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/django-axes/django-axes-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-ipware >= 3}
BuildRequires:  %{python_module pytest-django}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 2.2
Requires:       python-django-ipware >= 3
BuildArch:      noarch

%python_subpackages

%description
Keep track of failed login attempts in Django-powered sites.

%prep
%setup -q -n django-axes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
rm pyproject.toml
# see https://github.com/jazzband/django-axes/issues/1012
%pytest -k 'not test_log_data_truncated'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/axes/
%{python_sitelib}/django[_-]axes*/

%changelog
