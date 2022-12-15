#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-%{modname}
Version:        2.6.0
Release:        0
Summary:        Python package providing access to the Keycloak API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/marcospereirampj/python-keycloak
Source:         https://files.pythonhosted.org/packages/source/p/python-keycloak/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module httmock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-jose >= 1.4.0
Requires:       python-requests >= 2.20.0
Requires:       python-setuptools
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
%pyunittest discover -v

%files %{python_files}
%doc README.md
%doc %{python_sitelib}/CHANGELOG.md
%doc %{python_sitelib}/CONTRIBUTING.md
%doc %{python_sitelib}/CODEOWNERS
%license %{python_sitelib}/LICENSE
%{python_sitelib}/keycloak
%{python_sitelib}/python_keycloak-%{version}*-info

%changelog
