#
# spec file for package python-adal
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
Name:           python-adal
Version:        1.2.4
Release:        0
Summary:        Azure Active Directory library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/AzureAD/azure-activedirectory-library-for-python
Source:         https://files.pythonhosted.org/packages/source/a/adal/adal-%{version}.tar.gz
Source1:        HISTORY.txt
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 1.0.0
Requires:       python-cryptography >= 1.1.0
Requires:       python-python-dateutil >= 2.1.0
Requires:       python-requests >= 2.0.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
The ADAL for Python library makes it easy for python application to authenticate to
Azure Active Directory (AAD) in order to access AAD protected web resources.

%prep
%setup -q -n adal-%{version}
cp %{SOURCE1} HISTORY.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc HISTORY.txt README.md
%{python_sitelib}/*

%changelog
