#
# spec file for package python-django-axes
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-django-axes
Version:        5.6.0
Release:        0
License:        MIT
Summary:        Keep track of failed login attempts in Django-powered sites
Url:            https://github.com/jazzband/django-axes
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/django-axes/django-axes-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module django-appconf >= 1.0.3}
BuildRequires:  %{python_module django-ipware >= 2.0.2}
BuildRequires:  %{python_module pytest-django}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 1.11
Requires:       python-django-appconf >= 1.0.3
Requires:       python-django-ipware >= 2.0.2
BuildArch:      noarch

%python_subpackages

%description
Keep track of failed login attempts in Django-powered sites.

%prep
%setup -q -n django-axes-%{version}
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=axes.tests.settings
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
