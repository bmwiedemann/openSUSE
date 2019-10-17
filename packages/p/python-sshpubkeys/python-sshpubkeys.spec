#
# spec file for package python-sshpubkeys
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-sshpubkeys
Version:        3.1.0
Release:        0
Summary:        SSH public key parser
License:        BSD-3-Clause
URL:            https://github.com/ojarva/python-sshpubkeys
Source:         https://github.com/ojarva/python-sshpubkeys/archive/v%{version}.tar.gz
BuildRequires:  %{python_module cryptography >= 2.6.1}
BuildRequires:  %{python_module ecdsa >= 0.13}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module yapf >= 0.21.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.6.1
Requires:       python-ecdsa >= 0.13
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
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
