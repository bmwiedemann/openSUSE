#
# spec file for package python-nitrokey
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        0.4.2
Release:        0
Summary:        Nitrokey Python SDK
License:        Apache-2.0
URL:            https://github.com/Nitrokey/nitrokey-sdk-py
Source0:        https://files.pythonhosted.org/packages/source/n/nitrokey/nitrokey-%{version}.tar.gz
Source99:       python-nitrokey.rpmlintrc
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  %{python_module wheel}
# Runtime dependencies
BuildRequires:  %{python_module cryptography >= 41}
BuildRequires:  %{python_module crcmod >= 1.7 with %python-crcmod < 2}
BuildRequires:  %{python_module fido2 >= 1.1.2 with %python-fido2 < 3}
BuildRequires:  %{python_module hidapi >= 0.14 with %python-hidapi < 0.15}
BuildRequires:  %{python_module protobuf >= 5.26 with %python-protobuf < 7}
BuildRequires:  %{python_module pyserial >= 3.5 with %python-pyserial < 4}
BuildRequires:  %{python_module requests >= 2 with %python-requests < 3}
BuildRequires:  %{python_module semver >= 3 with %python-semver < 4}
BuildRequires:  %{python_module tlv8 >= 0.10 with %python-tlv8 < 0.11}
BuildRequires:  %{python_module wrapt}
#
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 41
Requires:       python-wrapt
Requires:       (python-crcmod >= 1.7 with python-crcmod < 2)
Requires:       (python-fido2 >= 1.1.2 with python-fido2 < 3)
Requires:       (python-hidapi >= 0.14 with python-hidapi < 0.15)
Requires:       (python-protobuf >= 5.26 with python-protobuf < 7)
Requires:       (python-pyserial >= 3.5 with python-pyserial < 4)
Requires:       (python-requests >= 2 with python-requests < 3)
Requires:       (python-semver >= 3 with python-semver < 4)
Requires:       (python-tlv8 >= 0.10 with python-tlv8 < 0.11)
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
