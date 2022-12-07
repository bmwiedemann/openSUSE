#
# spec file for package python-pycryptodomex
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global skip_python2 1
Name:           python-pycryptodomex
Version:        3.16.0
Release:        0
Summary:        Cryptographic library for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://www.pycryptodome.org
Source:         https://github.com/Legrandin/pycryptodome/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if !0%{?_no_weakdeps}
# PyCryptodomex uses gmp via cffi as runtime optimization
# would be better, if libgmp* would provide gmp
Suggests:       libgmp10
Suggests:       python-cffi
%endif
%python_subpackages

%description
PyCryptodomex is a self-contained Python package of low-level
cryptographic primitives.

Unlike PyCryptodome, it resides in its own namespace `Cryptodome`.

PyCryptodome is a fork of PyCrypto. It brings several enhancements
with respect to the last official version of PyCrypto (2.6.1),
for instance:

* Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
* Accelerated AES on Intel platforms via AES-NI
* First class support for PyPy
* Elliptic curves cryptography (NIST P-256 curve only)
* Better and more compact API (`nonce` and `iv` attributes for
  ciphers, automatic generation of random nonces and IVs, simplified
  CTR cipher mode, and more)
* SHA-3 (including SHAKE XOFs), SHA-512/t and BLAKE2 hash algorithms
* Salsa20 and ChaCha20 stream ciphers
* Poly1305 MAC
* ChaCha20-Poly1305 authenticated cipher
* scrypt and HKDF
* Deterministic (EC)DSA
* Password-protected PKCS#8 key containers
* Shamir's Secret Sharing scheme
* Random numbers get sourced directly from the OS (and not from a
  CSPRNG in userspace)
* Simplified install process, including better support for Windows
* Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
* Major clean ups and simplification of the code base

PyCryptodomex is not a wrapper to a separate C library like *OpenSSL*.
To the largest possible extent, algorithms are implemented in pure
Python. Only the pieces that are extremely critical to performance
(e.g. block ciphers) are implemented as C extensions.

%prep
%setup -q -n pycryptodome-%{version}
touch .separate_namespace

%build
export LC_ALL=en_US.UTF-8
export CFLAGS="%{optflags}"
%python_build

%install
export LC_ALL=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LC_ALL=en_US.UTF-8
%{python_expand pushd %{buildroot}%{$python_sitearch}
PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m Cryptodome.SelfTest
popd}

%files %{python_files}
%license LICENSE.rst
%doc AUTHORS.rst Changelog.rst README.rst
%{python_sitearch}/Cryptodome/
%{python_sitearch}/pycryptodomex-%{version}-py*.egg-info

%changelog
