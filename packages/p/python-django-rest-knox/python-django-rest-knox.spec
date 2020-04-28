#
# spec file for package python-django-rest-knox
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-django-rest-knox
Version:        4.1.0
Release:        0
Summary:        Authentication for Django REST framework
License:        MIT
URL:            https://github.com/James1345/django-rest-knox
Source:         https://github.com/James1345/django-rest-knox/archive/%{version}.tar.gz#/django-rest-knox-%{version}.tar.gz
Patch0:         django3.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-cryptography
Requires:       python-djangorestframework
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module django-nose}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module freezegun}
# /SECTION
%python_subpackages

%description
Authentication for Django REST framework.

%prep
%setup -q -n django-rest-knox-%{version}
%patch0 -p1
# knox does not use pyOpenSSL; it uses cryptography.
# pyOpenSSL is a proxy for cryptography in 3.6.0,
# and replaced by cryptography in 4.0.0
sed -i "s/'pyOpenSSL'/'cryptography'/" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=knox_project.settings
%python_expand $python manage.py test -v 2

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
