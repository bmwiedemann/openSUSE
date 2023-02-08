#
# spec file for package python-ctypescrypto
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
Name:           python-ctypescrypto
Version:        0.5
Release:        0
Summary:        CTypes-based interface for some OpenSSL libcrypto features
License:        MIT
URL:            https://github.com/vbwagner/ctypescrypto
Source:         https://files.pythonhosted.org/packages/source/c/ctypescrypto/ctypescrypto-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python interface to some openssl function based on ctypes module.

%prep
%setup -q -n ctypescrypto-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests/testmac.py disabled since MAC tests require the openssl
#  GOST engine which openSUSE does not ship
rm tests/testmac.py
# tests/testx509.py disabled since we don't have the proper root CA
# available to check against
rm tests/testx509.py
# tests/testpkey.py disabled since the openssl version that's
# currently shipped on Tumbleweed is heavily patched.
# e.g. the default bit size for RSA keys was changed,...
%if 0%{?suse_version} >= 1550
rm tests/testpkey.py
%endif
# Run remaining tests
%python_exec -m unittest discover tests/ -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ctypescrypto
%{python_sitelib}/ctypescrypto-%{version}-py%{python_version}.egg-info

%changelog
