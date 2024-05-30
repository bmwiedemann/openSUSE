#
# spec file for package python-azure-appconfiguration-provider
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
Name:           python-azure-appconfiguration-provider
Version:        1.2.0
Release:        0
Summary:        Microsoft App Configuration Provider Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk
Source:         https://files.pythonhosted.org/packages/source/a/azure-appconfiguration-provider/azure-appconfiguration-provider-%{version}.tar.gz
BuildRequires:  %{python_module azure-core >= 1.28.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-azure-appconfiguration >= 1.4.0 with python-azure-appconfiguration < 2.0.0)
Requires:       (python-azure-core >= 1.28.0 with python-azure-core < 2.0.0)
Requires:       (python-azure-keyvault-secrets >= 4.3.0 with python-azure-keyvault-secrets < 5.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-appconfiguration-provider < 1.1.0
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure App Configuration is a managed service that helps developers centralize their
application configurations simply and securely. This provider adds additional
functionality above the azure-sdk-for-python.

Using the provider enables loading sets of configurations from an Azure App
Configuration store in a managed way.

%prep
%setup -q -n azure-appconfiguration-provider-%{version}

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
%dir %{python_sitelib}/azure/appconfiguration
%{python_sitelib}/azure/appconfiguration/provider
%{python_sitelib}/azure_appconfiguration_provider-*.dist-info

%changelog
