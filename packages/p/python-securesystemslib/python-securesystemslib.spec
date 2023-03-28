#
# spec file for package python-securesystemslib
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


Name:           python-securesystemslib
Version:        0.21.0
Release:        0
License:        MIT
Summary:        Cryptographic and general routines for Secure Systems Lab
URL:            https://github.com/secure-systems-lab/securesystemslib
Source:         securesystemslib-%{version}.tar.xz
# PATCH-FIX-UPSTREAM Contained in debian/patches directory
Patch0:         use_python3_interpreter_in_tests.diff
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module asn1crypto}
BuildRequires:  %{python_module cryptography >= 3.3.2}
BuildRequires:  %{python_module ed25519}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyNaCl
Requires:       python-asn1crypto
Requires:       python-colorama
Requires:       python-cryptography >= 3.3.2

BuildArch:      noarch
%python_subpackages

%description
Cryptographic and general-purpose routines for Secure Systems Lab projects at NYU

%prep
%autosetup -p1 -n securesystemslib-%version

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (test_ed25519_kat or test_checkparams)'

%files %{python_files}
%{python_sitelib}/securesystemslib
%{python_sitelib}/securesystemslib-%{version}*info

%changelog
