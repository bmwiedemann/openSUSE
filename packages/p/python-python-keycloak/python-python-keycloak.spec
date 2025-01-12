#
# spec file for package python-python-keycloak
#
# Copyright (c) 2025 SUSE LLC
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


%global modname python-keycloak
Name:           python-%{modname}
Version:        3.7.0
Release:        0
Summary:        Python package providing access to the Keycloak API
License:        MIT
URL:            https://github.com/marcospereirampj/python-keycloak
Source:         https://github.com/marcospereirampj/python-keycloak/archive/refs/tags/v%{version}.tar.gz#/python-keycloak-%{version}.tar.gz
Patch0:         fix-version.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module deprecation}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module httmock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-deprecation
Requires:       python-python-jose >= 1.4.0
Requires:       python-requests >= 2.20.0
Requires:       python-requests-toolbelt
BuildArch:      noarch
%python_subpackages

%description
Python package providing access to the Keycloak API

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}

%check
# Certain parts of the testsuite requiring a running keycloak service. However
# the code is absolutely dependant on these variables being in the environment
. tox.env
export KEYCLOAK_HOST=localhost
export KEYCLOAK_ADMIN KEYCLOAK_ADMIN_PASSWORD KEYCLOAK_PORT
%pytest --ignore tests/test_keycloak_admin.py --ignore tests/test_keycloak_openid.py --ignore tests/test_keycloak_uma.py

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{python_sitelib}/keycloak
%{python_sitelib}/python_keycloak-%{version}.dist-info

%changelog
