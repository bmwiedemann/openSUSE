#
# spec file for package python-sshpubkeys
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-sshpubkeys
Version:        3.3.1
Release:        0
Summary:        SSH public key parser
License:        BSD-3-Clause
URL:            https://github.com/ojarva/python-sshpubkeys
Source:         https://github.com/ojarva/python-sshpubkeys/archive/%{version}.tar.gz
BuildRequires:  %{python_module cryptography >= 3.2}
BuildRequires:  %{python_module ecdsa >= 0.13.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 3.2
Requires:       python-ecdsa >= 0.13.3
BuildArch:      noarch
%python_subpackages

%description
OpenSSH Public Key Parser for Python

%prep
%setup -q -n python-sshpubkeys-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
