#
# spec file for package python-pyaes
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyaes
Version:        1.6.1
Release:        0
Summary:        Pure-Python Implementation of the AES block-cipher
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/ricmoo/pyaes/
Source:         https://files.pythonhosted.org/packages/source/p/pyaes/pyaes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pycrypto}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pycrypto

%python_subpackages

%description
A pure-Python implementation of the AES (FIPS-197) block-cipher algorithm and common modes of operation (CBC, CFB, CTR, ECB, OFB) with no dependencies beyond standard Python libraries. See README.md for API reference and details.

%prep
%setup -q -n pyaes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose

%files %python_files
%defattr(-,root,root,-)
%{python_sitelib}/*
%doc LICENSE.txt README.md

%changelog
