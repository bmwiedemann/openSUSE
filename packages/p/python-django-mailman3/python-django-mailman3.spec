#
# spec file for package python-django-mailman3
#
# Copyright (c) 2021 SUSE LLC
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
# mailman is built only for primary python3 flavor
%define pythons python3
Name:           python-django-mailman3
Version:        1.3.5
Release:        0
Summary:        Django library to help interaction with Mailman
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/django-mailman3
Source:         https://files.pythonhosted.org/packages/source/d/django-mailman3/django-mailman3-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-django-allauth
Requires:       python-django-gravatar2 >= 1.0.6
Requires:       python-mailmanclient
Requires:       python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module django-allauth}
BuildRequires:  %{python_module django-gravatar2 >= 1.0.6}
BuildRequires:  %{python_module mailmanclient}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytz}
# /SECTION
%if 0%{python3_version_nodots} == 38
# help in replacing any previously installed multiflavor package back to the primary python3 package
Provides:       python38-django-mailman3 = %{version}-%{release}
Obsoletes:      python38-django-mailman3 < %{version}-%{release}
%endif
%python_subpackages

%description
Django library to help interaction with Mailman

%prep
%setup -q -n django-mailman3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH='.' $python %{_bindir}/django-admin.py test --settings=django_mailman3.tests.settings_test

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/*

%changelog
