#
# spec file for package python-pbkdf2
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pbkdf2
Version:        1.3
Release:        0
Summary:        PKCS#5 v2.0 PBKDF2 Module
License:        MIT
Group:          Development/Libraries/Python
URL:            http://www.dlitz.net/software/%{name}/
Source:         https://files.pythonhosted.org/packages/source/p/pbkdf2/pbkdf2-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pycrypto}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-pycrypto
BuildArch:      noarch
%python_subpackages

%description
This module implements the password-based key derivation function, PBKDF2, specified in RSA PKCS#5 v2.0.

%prep
%setup -q -n pbkdf2-%{version}
chmod a-x pbkdf2.py
sed -i '1d' pbkdf2.py

%build
%python_build

%install
%python_install

%check
%pytest

%files %{python_files}
%{python_sitelib}/*
%doc README.txt

%changelog
