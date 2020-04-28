#
# spec file for package python-django-oidc-provider
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
Name:           python-django-oidc-provider
Version:        0.7.0
Release:        0
Summary:        OpenID Connect Provider implementation for Django
License:        MIT
URL:            https://github.com/juanifioren/django-oidc-provider
Source:         https://github.com/juanifioren/django-oidc-provider/archive/v%{version}.tar.gz#/django-oidc-provider-%{version}.tar.gz
Patch0:         django3.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-pyjwkest >= 1.3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pyjwkest >= 1.3.0}
BuildRequires:  %{python_module pytest >= 3.6.4}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
OpenID Connect Provider implementation for Django.

%prep
%setup -q -n django-oidc-provider-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
