#
# spec file for package python-azure-synapse-artifacts
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-synapse-artifacts
Version:        0.15.0
Release:        0
Summary:        Microsoft Azure Synapse Artifacts Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-synapse-artifacts/azure-synapse-artifacts-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-synapse-nspkg >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.24.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-azure-synapse-nspkg >= 1.0.0
Requires:       python-msrest >= 0.7.1
Provides:       python-azure-synapse = 0.1.0
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Obsoletes:      python-azure-synapse < 0.1.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Synapse Artifacts Client Library.

This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8.

%prep
%setup -q -n azure-synapse-artifacts-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-synapse-artifacts-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/synapse/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/synapse/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/tests/
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/synapse/artifacts
%{python_sitelib}/azure_synapse_artifacts-*.egg-info

%changelog
