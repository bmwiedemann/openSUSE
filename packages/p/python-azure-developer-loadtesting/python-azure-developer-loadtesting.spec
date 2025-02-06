#
# spec file for package python-azure-developer-loadtesting
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-azure-developer-loadtesting
Version:        1.0.1
Release:        0
Summary:        Microsoft Azure Developer LoadTesting Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk
Source:         https://files.pythonhosted.org/packages/source/a/azure_developer_loadtesting/azure_developer_loadtesting-%{version}.tar.gz
BuildRequires:  %{python_module azure-core >= 1.26.2}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module isodate >= 0.6.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-core >= 1.26.2
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.1
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-developer-loadtesting < 1.0.0
%endif
BuildArch:      noarch

%python_subpackages

%description
Microsoft Azure Developer LoadTesting Client Library for Python

%prep
%setup -q -n azure_developer_loadtesting-%{version}

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
%{python_sitelib}/azure/developer/loadtesting
%{python_sitelib}/azure_developer_loadtesting-*.dist-info

%changelog
