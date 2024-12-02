#
# spec file for package python-esptool
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
Name:           python-esptool
Version:        4.8.1
Release:        0
Summary:        A serial utility to communicate & flash code to Espressif ESP8266 & ESP32 chips
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/espressif/esptool
Source:         https://github.com/espressif/esptool/archive/v%{version}.tar.gz#/esptool-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module bitstring >= 3.1.6}
BuildRequires:  %{python_module ecdsa >= 0.16.0}
BuildRequires:  %{python_module intelhex}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyelftools}
BuildRequires:  %{python_module pyserial >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module reedsolo >= 1.5.3}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-bitstring >= 3.1.6
Requires:       python-cryptography >= 2.1.4
Requires:       python-ecdsa >= 0.16.0
Requires:       python-intelhex
Requires:       python-pyserial >= 3.0
Requires:       python-reedsolo >= 1.5.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?python_version_nodots} < 37
BuildRequires:  %{python_module cryptography}
%endif
%python_subpackages

%description
A command line utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32 microcontrollers.

Allows flashing firmware, reading back firmware, querying chip parameters, etc.

%prep
%setup -q -n esptool-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/espefuse.py
%python_clone -a %{buildroot}%{_bindir}/espsecure.py
%python_clone -a %{buildroot}%{_bindir}/esptool.py
%python_clone -a %{buildroot}%{_bindir}/esp_rfc2217_server.py
%python_expand rm -rf %{buildroot}%{$python_sitelib}/__pycache__/*.pyc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# there are more tests but upstream runs only those in .travis.yml
%pytest test/test_imagegen.py
# requires python-pkcs11 which isn't packaged
rm -v test/test_espsecure.py test/test_espsecure_hsm.py
%pytest -m host_test

%post
%python_install_alternative espefuse.py
%python_install_alternative espsecure.py
%python_install_alternative esptool.py
%python_install_alternative esp_rfc2217_server.py

%postun
%python_uninstall_alternative espefuse.py
%python_uninstall_alternative espsecure.py
%python_uninstall_alternative esptool.py
%python_uninstall_alternative esp_rfc2217_server.py

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/esptool.py
%python_alternative %{_bindir}/espsecure.py
%python_alternative %{_bindir}/espefuse.py
%python_alternative %{_bindir}/esp_rfc2217_server.py
%{python_sitelib}/esptool-%{version}.dist-info
%{python_sitelib}/esptool
%{python_sitelib}/esp_rfc2217_server
%{python_sitelib}/espsecure
%{python_sitelib}/espefuse

%changelog
