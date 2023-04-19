#
# spec file for package python-azure-devops
#
# Copyright (c) 2023 SUSE LLC
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

%define realversion 7.1.0b1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-devops
Version:        7.1.0~b1
Release:        0
Summary:        Python wrapper around the Azure DevOps 5x APIs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Microsoft/vsts-python-api
Source:         https://files.pythonhosted.org/packages/source/a/azure-devops/azure-devops-%{realversion}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module msrest >= 0.7.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest < 0.8.0
Requires:       python-msrest >= 0.7.1
Provides:       python-vsts = %{realversion}
Obsoletes:      python-vsts < %{realversion}

BuildArch:      noarch

%python_subpackages

%description
Python wrapper around the Azure DevOps 5.x APIs

%prep
%setup -q -n azure-devops-%{realversion}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%check
# Don't import namespace from build root
rm -f azure/__init__.py
%pyunittest discover -v

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/azure/devops
%{python_sitelib}/azure_devops-*.egg-info

%changelog
