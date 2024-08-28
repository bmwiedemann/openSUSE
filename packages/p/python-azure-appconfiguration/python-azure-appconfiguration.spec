#
# spec file for package python-azure-appconfiguration
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
Name:           python-azure-appconfiguration
Version:        1.7.1
Release:        0
Summary:        Microsoft App Configuration Data Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-appconfiguration/azure-appconfiguration-%{version}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.0
Requires:       (python-azure-core >= 1.28.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-appconfiguration < 1.5.0
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure App Configuration is a managed service that helps developers centralize
their application configurations simply and securely.

Modern programs, especially programs running in a cloud, generally have many
components that are distributed in nature. Spreading configuration settings
across these components can lead to hard-to-troubleshoot errors during an
application deployment. Use App Configuration to securely store all the
settings for your application in one place.

%prep
%setup -q -n azure-appconfiguration-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/tests/
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/appconfiguration
%{python_sitelib}/azure_appconfiguration-*.dist-info

%changelog
