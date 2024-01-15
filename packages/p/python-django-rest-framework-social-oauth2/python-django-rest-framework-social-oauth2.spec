#
# spec file for package python-django-rest-framework-social-oauth2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-rest-framework-social-oauth2
Version:        1.2.0
Release:        0
License:        MIT
Summary:        Django rest framework support for python-social-auth and oauth2
URL:            https://github.com/PhilipGarnero/django-rest-framework-social-oauth2
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/django-rest-framework-social-oauth2/django-rest-framework-social-oauth2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-django-braces >= 1.11.0
Requires:       python-django-oauth-toolkit >= 1.0.0
Requires:       python-djangorestframework >= 3.0.1
Requires:       python-social-auth-app-django >= 0.1.0
BuildArch:      noarch

%python_subpackages

%description
python-social-auth and oauth2 support for django-rest-framework.

%prep
%setup -q -n django-rest-framework-social-oauth2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
