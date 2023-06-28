#
# spec file for package python-libusbsio
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


%{?sle15_python_module_pythons}
Name:           python-libusbsio
Version:        2.1.11
Release:        0
Summary:        Python wrapper around NXP LIBUSBSIO library
License:        BSD-3-Clause
URL:            https://www.nxp.com/design/software/development-software/library-for-windows-macos-and-ubuntu-linux:LIBUSBSIO
Source:         https://files.pythonhosted.org/packages/source/l/libusbsio/libusbsio-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  libudev1
BuildRequires:  libusb
# /SECTION
BuildRequires:  %{python_module setuptools >= 42.0}
BuildRequires:  %{python_module wheel >= 0.36.2}
BuildRequires:  fdupes
BuildRequires:  dos2unix
%python_subpackages

%description
Python wrapper around NXP LIBUSBSIO library

%prep
%setup -q -n libusbsio-%{version}

%build
%pyproject_wheel
dos2unix README.md

%install
%pyproject_install
# remove shebangs
%python_expand find %{buildroot}%{$python_sitelib} -iname "*.py" -exec sed -i '1{/env python/d;}' {} +
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
IGNORED_CHECKS="test_Error"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetDeviceInfo"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetDeviceInfo"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetLastError"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetMaxDataSize"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetNumGPIOPorts"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetNumI2CPorts"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetNumPorts"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetNumSPIPorts"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GetVersion"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_OpenClose"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_SPI_OpenClose"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_SPI_Reset"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_SPI_Transfer_Echo_long"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_SPI_Transfer_Echo_longer"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_SPI_Transfer_Echo_short"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_SPI_Transfer_Echo_single"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_OpenClose"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_Reset"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_Transfer_Echo_long"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_Transfer_Echo_short"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_Transfer_Echo_single"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_Transfer_Echo_long"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_Transfer_Echo_short"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_I2C_Transfer_Echo_single"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_ReadPort"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_SetClearPin_GetPin"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_SetClearPin_ReadPort"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_SetClearPort_ReadPort"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_SetClearTogglePin_ReadPort"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_SetPortDir_GetPortDir"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_WritePort_ReadBack"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_GPIO_WritePort_ReadPort"

%pytest -k "not (${IGNORED_CHECKS})"

%files %{python_files}
%doc README.md
%license license license/BSD-3-clause.txt license/LICENSE-hidapi-bsd.txt license/SoftwareContentRegister.txt
%{python_sitelib}/libusbsio
%{python_sitelib}/libusbsio-%{version}.dist-info/

%changelog
