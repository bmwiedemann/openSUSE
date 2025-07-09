#
# spec file for package python-nitrokey
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-nitrokey
Version:        0.3.2
Release:        0
Summary:        Nitrokey Python SDK
License:        Apache-2.0
URL:            https://github.com/Nitrokey/nitrokey-sdk-py
Source0:        https://files.pythonhosted.org/packages/source/n/nitrokey/nitrokey-%{version}.tar.gz
Source99:       python-nitrokey.rpmlintrc
BuildRequires:  %{python_module base >= 3.9.2}
BuildRequires:  %{python_module fido2 >= 1.1.2 with %python-fido2 < 3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-crcmod
Requires:       python-cryptography
Requires:       python-hidapi
Requires:       python-protobuf
Requires:       python-pyserial
Requires:       python-requests
Requires:       python-semver
Requires:       python-tlv8
Requires:       (python-fido2 >= 1.1.2 with python-fido2 < 3)
BuildArch:      noarch
%python_subpackages

%description
The Nitrokey Python SDK can be used to use and configure Nitrokey devices.

%prep
%autosetup -p1 -n nitrokey-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSES/Apache-2.0.txt LICENSES/MIT.txt
%{python_sitelib}/nitrokey
%{python_sitelib}/nitrokey-%{version}.dist-info

%changelog
