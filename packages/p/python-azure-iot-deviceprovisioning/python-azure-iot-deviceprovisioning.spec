#
# spec file for package python-azure-iot-deviceprovisioning
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
Name:           python-azure-iot-deviceprovisioning
Version:        1.0.0~b1
Release:        0
Summary:        Microsoft Azure IoT Device Provisioning Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-iot-deviceprovisioning/azure-iot-deviceprovisioning-%{realversion}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-iot-nspkg >= 1.0.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-iot-nspkg >= 1.0.1
Requires:       (python-azure-core >= 1.24.0 with python-azure-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-iot-deviceprovisioning < 1.0.0~b1
%endif
BuildArch:      noarch
%python_subpackages

%description
The IoT Hub Device Provisioning Service (DPS) is a helper service for
IoT Hub that enables zero-touch, just-in-time provisioning to the right
IoT hub without requiring human intervention, allowing customers to
provision millions of devices in a secure and scalable manner.

This service SDK provides data plane operations for backend apps. You
can use this service SDK to create and manage individual enrollments
and enrollment groups, and to query and manage device registration records.

%prep
%setup -q -n azure-iot-deviceprovisioning-%{realversion}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-iot-deviceprovisioning-%{realversion}
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/azure/iot/deviceprovisioning
%{python_sitelib}/azure_iot_deviceprovisioning-*.dist-info

%changelog
