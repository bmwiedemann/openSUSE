#
# spec file for package python-azure-synapse-nspkg
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
Name:           python-azure-synapse-nspkg
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Synapse Namespace Package
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-synapse-nspkg/azure-synapse-nspkg-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-nspkg >= 3.0.0
Provides:       python-azure-synapse = 0.1.0
Obsoletes:      python-azure-synapse < 0.1.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Synapse namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure.synapse namespace.

%prep
%setup -q -n azure-synapse-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-synapse-nspkg-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/synapse
%{python_sitelib}/azure_synapse_nspkg-*.egg-info

%changelog
