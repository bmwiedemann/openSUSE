#
# spec file for package python-msoffcrypto-tool
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
Name:           python-msoffcrypto-tool
Version:        4.10.2
Release:        0
Summary:        Library for decrypting MS Office files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/nolze/msoffcrypto-tool
Source:         https://files.pythonhosted.org/packages/source/m/msoffcrypto-tool/msoffcrypto-tool-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.3
Requires:       python-olefile >= 0.45
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module cryptography >= 2.3}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module olefile >= 0.45}
# /SECTION
%python_subpackages

%description
A Python tool and library for decrypting MS Office
files with passwords or other keys.

%prep
%setup -q -n msoffcrypto-tool-%{version}
# Delete empty file as of v4.10.0
wc -c msoffcrypto/method/xor_obfuscation.py | sed -n '/^0/{s/^0\s//;p}' | xargs rm

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/msoffcrypto-tool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose --with-doctest

%post
%python_install_alternative msoffcrypto-tool

%postun
%python_uninstall_alternative msoffcrypto-tool

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/msoffcrypto-tool
%{python_sitelib}/*

%changelog
