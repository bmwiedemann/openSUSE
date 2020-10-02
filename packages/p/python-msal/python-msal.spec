#
# spec file for package python-msal
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
Name:           python-msal
Version:        1.5.0
Release:        0
Summary:        Microsoft Authentication Library (MSAL) for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python
Source:         https://files.pythonhosted.org/packages/source/m/msal/msal-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 1.0.0
Requires:       python-requests >= 2.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyJWT >= 1.0.0}
BuildRequires:  %{python_module requests >= 2.0.0}
# /SECTION
%python_subpackages

%description
The Microsoft Authentication Library (MSAL) for Python library enables your app
to access the Microsoft Cloud by supporting authentication of users with Microsoft
Azure Active Directory accounts (AAD) and Microsoft Accounts (MSA) using industry
standard OAuth2 and OpenID Connect.

%prep
%setup -q -n msal-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
