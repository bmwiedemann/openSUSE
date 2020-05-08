#
# spec file for package python-azure-search-nspkg
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
Name:           python-azure-search-nspkg
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Search Namespace Package
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-search-nspkg/azure-search-nspkg-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-nspkg >= 3.0.0
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
This is the Microsoft Azure Search namespace package. It isn't intended to be
installed directly. Search client libraries are located elsewhere:

* azure-search-documents

This package is for Python 2 only. It provides the necessary files for other packages
to extend the azure namespace. Python 3.x libraries use PEP420 instead.

%prep
%setup -q -n azure-search-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-search-nspkg-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mkdir -p %{buildroot}%{python2_sitelib}/azure/search
mkdir -p %{buildroot}%{python3_sitelib}/azure/search

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python2_only %{python2_sitelib}/azure/search
%python3_only %dir %{python3_sitelib}/azure/search
%python3_only %exclude %{python3_sitelib}/azure/search/*
%{python_sitelib}/azure_search_nspkg-*.egg-info

%changelog
