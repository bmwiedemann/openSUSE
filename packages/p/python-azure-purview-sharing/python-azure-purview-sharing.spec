#
# spec file for package python-azure-purview-sharing
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

%define realversion 1.0.0b1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-purview-sharing
Version:        1.0.0~b1
Release:        0
Summary:        Microsoft Azure Purview Sharing Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-purview-sharing/azure-purview-sharing-%{realversion}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-purview-nspkg >= 2.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.24.0
Requires:       python-azure-purview-nspkg >= 2.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.1
Requires:       python-isodate < 1.0.0
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
Microsoft Purview Share is a fully managed cloud service.

%prep
%setup -q -n azure-purview-sharing-%{realversion}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-purview-sharing-%{realversion}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/purview/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/purview/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/purview/sharing
%{python_sitelib}/azure_purview_sharing-*.egg-info

%changelog
