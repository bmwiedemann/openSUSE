#
# spec file for package python-ecdsa
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
Name:           python-ecdsa
Version:        0.16.0
Release:        0
Summary:        ECDSA cryptographic signature library (pure python)
License:        MIT
URL:            https://github.com/warner/python-ecdsa
Source:         https://files.pythonhosted.org/packages/source/e/ecdsa/ecdsa-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       python-six
Suggests:       python-gmpy
Suggests:       python-gmpy2
BuildArch:      noarch
%python_subpackages

%description
This is an easy-to-use implementation of ECDSA cryptography (Elliptic Curve
Digital Signature Algorithm), implemented purely in Python, released under
the MIT license. With this library, you can quickly create keypairs (signing
key and verifying key), sign messages, and verify the signatures. The keys
and signatures are very short, making them easy to handle and incorporate
into other protocols.

%prep
%setup -q -n ecdsa-%{version}

%build
%python_build
#remove shebang from all non executable files
find ./ -type f -name "*.py" -perm 644 -exec sed -i -e '1{\@^#! %{_bindir}/env python@d}' {} \;

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc NEWS README.md
%{python_sitelib}/*

%changelog
