#
# spec file for package python-azure-mixedreality-authentication
#
# Copyright (c) 2021 SUSE LLC
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
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-mixedreality-authentication
Version:        1.0.0b1
Release:        0
Summary:        Microsoft Azure Mixed Reality Authentication Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-mixedreality-authentication/azure-mixedreality-authentication-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-mixedreality-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.4.0
Requires:       python-msrest >= 0.5.0
Requires:       python-azure-mixedreality-nspkg >= 1.0.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
Mixed Reality services, like Azure Spatial Anchors, Azure Remote Rendering, and
others, use the Mixed Reality security token service (STS) for authentication.

This package supports exchanging Mixed Reality account credentials for an access
token from the STS that can be used to access Mixed Reality services.

%prep
%setup -q -n azure-mixedreality-authentication-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-mixedreality-authentication-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/mixedreality/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/mixedreality/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/mixedreality/authentication
%{python_sitelib}/azure_mixedreality_authentication-*.egg-info

%changelog
