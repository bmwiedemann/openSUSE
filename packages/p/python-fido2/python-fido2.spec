#
# spec file for package python-fido2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-fido2
Version:        0.9.1
Release:        0
Summary:        Python-based FIDO 2.0 library
License:        BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Yubico/python-fido2
Source0:        %{URL}/releases/download/%{version}/fido2-%{version}.tar.gz
Source1:        %{URL}/releases/download/%{version}/fido2-%{version}.tar.gz.sig
# PATCH-FIX-UPSTREAM 0001-Don-t-use-enum.auto-Python-2.patch -- https://github.com/Yubico/python-fido2/commit/ce19ba598a077dd09d164c2bef05169e01b69eaf
Patch0:         0001-Don-t-use-enum.auto-Python-2.patch
# PATCH-FIX-UPSTREAM 0001-Skip-tests-on-older-Cryptography-versions.patch -- https://github.com/Yubico/python-fido2/commit/2e3224d7a8be8625b05e88c10efdbf57b646107c
Patch1:         0001-Skip-tests-on-older-Cryptography-versions.patch
BuildRequires:  %{python_module cryptography >= 1.5}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module pyfakefs >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 1.5
Requires:       python-six
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-enum34
%endif
%ifpython2
Requires:       python2-enum34
%endif
%python_subpackages

%description
This library supports the FIDO U2F and FIDO 2.0 protocols for communicating
with a USB authenticator via the Client-to-Authenticator Protocol (CTAP 1 and 2).
In addition to this low-level device access, classes defined in the fido2.client
implement higher level device operations.

%prep
%autosetup -p1 -n fido2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# %%pyunittest
%python_expand $python -m unittest

%files %{python_files}
%doc NEWS* README*
%license COPYING*
%{python_sitelib}/*

%changelog
