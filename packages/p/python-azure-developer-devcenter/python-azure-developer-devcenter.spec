#
# spec file for package python-azure-developer-devcenter
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
Name:           python-azure-developer-devcenter
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Developer DevCenter Service Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk
Source:         https://files.pythonhosted.org/packages/source/a/azure-developer-devcenter/azure-developer-devcenter-%{version}.tar.gz
BuildRequires:  %{python_module azure-core < 2.0.0}
BuildRequires:  %{python_module azure-core >= 1.28.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module isodate < 1.0.0}
BuildRequires:  %{python_module isodate >= 0.6.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-typing_extensions >= 4.6.0
Requires:       (python-azure-core >= 1.30.0 with python-azure-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-developer-devcenter < 1.0.0~b3
%endif
BuildArch:      noarch

%python_subpackages

%description
The Azure DevCenter package provides access to manage resources for Microsoft Dev Box
and Azure Deployment Environments. This SDK enables managing developer machines and
environments in Azure.

Use the package for Azure DevCenter to:

Create, access, manage, and delete Dev Box resources Create,
deploy, manage, and delete Environment resources

%prep
%setup -q -n azure-developer-devcenter-%{version}

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
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{python_sitelib}/azure/developer
%{python_sitelib}/azure/developer/devcenter
%{python_sitelib}/azure_developer_devcenter-*.dist-info

%changelog
