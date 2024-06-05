#
# spec file for package python-azure-maps-geolocation
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


%define realversion 1.0.0b1

%{?sle15_python_module_pythons}
Name:           python-azure-maps-geolocation
Version:        1.0.0~b1
Release:        0
Summary:        Microsoft Azure Maps Geolocation Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-maps-geolocation/azure-maps-geolocation-%{realversion}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.21
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0)
Requires:       (python-azure-mgmt-core >= 1.3.0 with python-azure-mgmt-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch

%python_subpackages

%description
This package contains a Python SDK for Azure Maps Services for Geolocation.

%prep
%setup -q -n azure-maps-geolocation-%{realversion}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-maps-geolocation-%{realversion}
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
%license LICENSE.txt
%{python_sitelib}/azure/maps/
%{python_sitelib}/azure_maps_geolocation-*.dist-info

%changelog
