#
# spec file for package python-azure-mgmt-networkcloud
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
Name:           python-azure-mgmt-networkcloud
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Networkcloud Management Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-mgmt-networkcloud/azure-mgmt-networkcloud-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-mgmt-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-mgmt-nspkg >= 3.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0.0)
Requires:       (python-azure-mgmt-core >= 1.3.2 with python-azure-mgmt-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-mgmt-networkcloud < 1.0.0
%endif
BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Networkcloud Management Client Library.

This package has been tested with Python 3.7+.

%prep
%setup -q -n azure-mgmt-networkcloud-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-mgmt-networkcloud-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/mgmt/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/mgmt/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/mgmt/networkcloud
%{python_sitelib}/azure_mgmt_networkcloud-*.dist-info

%changelog
