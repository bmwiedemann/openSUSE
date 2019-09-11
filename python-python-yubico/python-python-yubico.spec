#
# spec file for package python-yubico
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-python-yubico
# there are three repos:
#               https://pypi.org/project/python-yubico/ (1.3.3)
#               https://pypi.org/project/yubico/        (1.6.2) IIUC for protocol version 2.0
#               https://pypi.org/project/yubico-client/ (1.10.0) for 2.0, too, just renamed
Version:        1.3.3
Release:        0
Summary:        Python code for talking to Yubico's YubiKeys
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://developers.yubico.com/python-yubico/Releases/
Source:         https://developers.yubico.com/python-yubico/Releases/python-yubico-%{version}.tar.gz
Source1:        https://developers.yubico.com/python-yubico/Releases/python-yubico-%{version}.tar.gz.sig
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module usb}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-usb
BuildArch:      noarch
Provides:       python-yubico = %{version}
Obsoletes:      python-yubico < %{version}
%python_subpackages

%description
The YubiKey is a hardware token for authentication. The main mode of the YubiKey
is entering a one time password (or a strong static password) by acting as a USB HID device,
but there are things one can do with bi-directional communication:

 1. Configuration. The yubikey_config class should be a feature-wise complete implementation
    of everything that can be configured on YubiKeys version 1.3 to 3.x (besides deprecated
    functions in YubiKey 1.x). See examples/configure_nist_test_key for an example.
 2. Challenge-response. YubiKey 2.2 and later supports HMAC-SHA1 or Yubico challenge-response
    operations. See examples/nist_challenge_response for an example.

%prep
%setup -q -n python-yubico-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# needs the hardware
rm -r test/usb
%python_exec setup.py test

%files %{python_files}
%license COPYING
%doc README NEWS
%{python_sitelib}/*

%changelog
