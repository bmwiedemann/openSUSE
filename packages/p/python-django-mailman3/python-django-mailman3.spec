#
# spec file for package python-django-mailman3
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


%global django_min_version           4.2
%global django_max_version           5.1
%global mailmanclient_min_version    3.3.3
%global django_allauth_min_version   0.63
%global django_gravatar2_min_version 1.0.6

%{?sle15_python_module_pythons}
%define modname django_mailman3
Name:           python-django-mailman3
Version:        1.3.14
Release:        0
Summary:        Django library to help interaction with Mailman
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/django-mailman3
Source0:        %{url}/-/releases/v%{version}/downloads/%{modname}-%{version}.tar.gz
Source1:        %{url}/-/releases/v%{version}/downloads/%{modname}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{url}/-/raw/v%{version}/pytest.ini
BuildRequires:  %{python_module pdm}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-django-allauth >= %{django_allauth_min_version}
Requires:       python-django-gravatar2 >= %{django_gravatar2_min_version}
Requires:       python-mailmanclient >= %{mailmanclient_min_version}
Requires:       (python-Django >= %{django_min_version} with python-Django < %{django_max_version})
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= %{django_min_version}}
BuildRequires:  %{python_module django-allauth >= %{django_allauth_min_version}}
BuildRequires:  %{python_module django-gravatar2 >= %{django_gravatar2_min_version}}
BuildRequires:  %{python_module editables}
BuildRequires:  %{python_module mailmanclient >= %{mailmanclient_min_version}}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Django library to help interaction with Mailman.

%prep
%autosetup -p1 -n %{modname}-%{version}

cp %{SOURCE3} pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install

%{python_expand # remove for each python flavor
rm -f %{buildroot}%{$python_sitelib}/COPYING.txt
rm -f %{buildroot}%{$python_sitelib}/README.rst
rm -f %{buildroot}%{$python_sitelib}/pytest.ini
rm -f %{buildroot}%{$python_sitelib}/tox.ini
}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH="$(pwd)"
%pytest django_mailman3

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/%{modname}-%{version}.dist-info
%{python_sitelib}/%{modname}

%changelog
