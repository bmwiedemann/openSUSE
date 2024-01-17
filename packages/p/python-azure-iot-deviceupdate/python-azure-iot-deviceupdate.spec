#
# spec file for package python-azure-iot-deviceupdate
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-azure-iot-deviceupdate
Version:        1.0.0
Release:        0
Summary:        Azure Device Update for IoT Hub client library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-iot-deviceupdate/azure-iot-deviceupdate-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-iot-nspkg >= 1.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-iot-nspkg >= 1.0.1
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.24.0
Requires:       python-isodate < 1.0.0
Requires:       python-isodate >= 0.6.1
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
The library provides access to the Device Update for IoT Hub service that
enables customers to publish updates for their IoT devices to the cloud,
and then deploy these updates to their devices (approve updates to groups
of devices managed and provisioned in IoT Hub).

%prep
%setup -q -n azure-iot-deviceupdate-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-iot-deviceupdate-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/iot/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/iot/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/iot/deviceupdate
%{python_sitelib}/azure_iot_deviceupdate-*.egg-info

%changelog
