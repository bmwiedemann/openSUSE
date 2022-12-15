#
# spec file for package python-fido2
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


Name:           python-fido2
Version:        1.1.0
Release:        0
Summary:        Python-based FIDO 2.0 library
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Yubico/python-fido2
Source0:        https://github.com/Yubico/python-fido2/releases/download/%{version}/fido2-%{version}.tar.gz
Source1:        https://github.com/Yubico/python-fido2/releases/download/%{version}/fido2-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module cryptography >= 2.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0}
BuildRequires:  %{python_module pyfakefs >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.6
BuildArch:      noarch
%python_subpackages

%description
This library supports the FIDO U2F and FIDO 2.0 protocols for communicating
with a USB authenticator via the Client-to-Authenticator Protocol (CTAP 1 and 2).
In addition to this low-level device access, classes defined in the fido2.client
implement higher level device operations.

%prep
%autosetup -p1 -n fido2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc NEWS* README*
%license COPYING*
%{python_sitelib}/fido2
%{python_sitelib}/fido2-%{version}*-info

%changelog
