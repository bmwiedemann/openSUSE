#
# spec file for package python-securesystemslib
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


Name:           python-securesystemslib
Version:        1.1.0
Release:        0
License:        MIT
Summary:        Cryptographic and general routines for Secure Systems Lab
URL:            https://github.com/secure-systems-lab/securesystemslib
Source:         securesystemslib-%{version}.tar.xz
BuildRequires:  %{python_module PyKCS11}
BuildRequires:  %{python_module asn1crypto}
BuildRequires:  %{python_module cryptography >= 3.3.2}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-asn1crypto
Suggests:       python-cryptography
Suggests:       python-PyKCS11

BuildArch:      noarch
%python_subpackages

%description
Cryptographic and general-purpose routines for Secure Systems Lab projects at NYU

%prep
%autosetup -p1 -n securesystemslib-%version
# Remove exec permission from python scripts
find . -type f -name *.py -exec chmod 0644 {} \;

%build
%pyproject_wheel

%install
%pyproject_install
# Remove not needed files
%{python_expand #
rm -rf %{buildroot}%{$python_sitelib}/securesystemslib/_vendor/ed25519/.gitignore
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# spinhcs+ key support requires the pyspx library
donttest="test_sphincs"
# remove the ed25519 tests, the module is "Not Recommended For New Applications: Use pynacl Instead"
rm securesystemslib/_vendor/ed25519/test_ed25519.py
%pytest -k "not ($donttest)"

%files %{python_files}
%{python_sitelib}/securesystemslib
%{python_sitelib}/securesystemslib-%{version}*info

%changelog
