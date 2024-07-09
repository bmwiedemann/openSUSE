#
# spec file for package python-msal-extensions
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


%{?sle15_python_module_pythons}
Name:           python-msal-extensions
Version:        1.2.0
Release:        0
Summary:        Microsoft Authentication Library (MSAL) for Python Extensions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python
Source:         https://files.pythonhosted.org/packages/source/m/msal-extensions/msal_extensions-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-msal >= 1.29 with python-msal < 2.0)
Requires:       (python-portalocker >= 1.4 with python-portalocker < 3.0)
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-msal-extensions < 1.1.0
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module msal < 2.0}
BuildRequires:  %{python_module msal >= 1.29}
BuildRequires:  %{python_module portalocker < 3.0}
BuildRequires:  %{python_module portalocker >= 1.4}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The Microsoft Authentication Library (MSAL) for Python library enables your app
to access the Microsoft Cloud by supporting authentication of users with Microsoft
Azure Active Directory accounts (AAD) and Microsoft Accounts (MSA) using industry
standard OAuth2 and OpenID Connect.

This packages contains additional extensions.

%prep
%setup -q -n msal_extensions-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/msal_extensions
%{python_sitelib}/msal_extensions-*.dist-info

%changelog
