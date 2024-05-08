#
# spec file for package python-azure-devops
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


%define realversion 7.1.0b4

%{?sle15_python_module_pythons}
Name:           python-azure-devops
Version:        7.1.0~b4
Release:        0
Summary:        Python wrapper around the Azure DevOps 5x APIs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Microsoft/vsts-python-api
Source:         https://files.pythonhosted.org/packages/source/a/azure-devops/azure-devops-%{realversion}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module msrest >= 0.7.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-msrest >= 0.7.1 with python-msrest < 0.8.0)
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-devops < 7.1.0~b4
Obsoletes:      python3-vsts <= 0.1.25
Obsoletes:      python3-vsts-cd-manager <= 1.0.2
%endif
BuildArch:      noarch

%python_subpackages

%description
Python wrapper around the Azure DevOps 5.x APIs

%prep
%setup -q -n azure-devops-%{realversion}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/azure/devops
%{python_sitelib}/azure_devops-*.dist-info

%changelog
