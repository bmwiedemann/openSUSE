#
# spec file for package python-drf-jwt-knox
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-drf-jwt-knox
Version:        0.1.1
Release:        0
Summary:        Django REST JWT authentication with server-side tokens
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ssaavedra/drf-jwt-knox
Source:         https://github.com/ssaavedra/drf-jwt-knox/archive/v%{version}.tar.gz#/drf-jwt-knox-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 1.6
Requires:       python-django-rest-knox >= 3.1
Requires:       python-djangorestframework >= 3.8
Requires:       python-six >= 1.11
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyJWT >= 1.6}
BuildRequires:  %{python_module django-rest-knox >= 3.1}
BuildRequires:  %{python_module djangorestframework >= 3.8}
BuildRequires:  %{python_module pytest-django >= 3.2.1}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module six >= 1.11}
# /SECTION
%python_subpackages

%description
Django REST Framework JWT-based authentication with server-side tokens
with a Knox-powered database backend.

%prep
%setup -q -n drf-jwt-knox-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
