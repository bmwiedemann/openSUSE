#
# spec file for package python-ecdsa
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
Name:           python-ecdsa
Version:        0.18.0
Release:        0
Summary:        ECDSA cryptographic signature library (pure python)
License:        MIT
URL:            https://github.com/tlsfuzzer/python-ecdsa
Source:         https://files.pythonhosted.org/packages/source/e/ecdsa/ecdsa-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9.0
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
# unfortunate hypothesis fuzzing (gh#warner/python-ecdsa#307):
donttest="(test_ecdsa and test_sig_verify)"
donttest="$donttest or (test_jacobi and test_add and scale_points)"
donttest="$donttest or (test_ellipticcurve and test_p192_mult_tests)"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc NEWS README.md
%{python_sitelib}/ecdsa
%{python_sitelib}/ecdsa-%{version}*-info

%changelog
