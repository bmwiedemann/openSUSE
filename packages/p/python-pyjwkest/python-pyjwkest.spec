#
# spec file for package python-pyjwkest
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
%define commit 9ed11b406911dde70b281b2473a976ec88afd1a9
Name:           python-pyjwkest
Version:        1.4.2
Release:        0
Summary:        Python implementation of JWT, JWE, JWS and JWK
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com//IdentityPython/pyjwkest
#Source:         https://files.pythonhosted.org/packages/source/p/pyjwkest/pyjwkest-%%{version}.tar.gz
# 1.4.2, released on PyPI is untagged on GitHub, but we need the tests
Source:         https://github.com/IdentityPython/pyjwkest/archive/%{commit}.tar.gz#/pyjwkest-%{version}-gh.tar.gz
# PATCH-FIX-OPENSUSE (upstream is unmaintained) -- py 3.9 compatibility. Works for all of py3.
Patch0:         py39-tobytes.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
Requires:       python-pycryptodomex
Requires:       python-requests
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
%python_subpackages

%description
Python implementation of JWT, JWE, JWS and JWK.
(JSON web signarure)

Note: This library is NOT actively maintained anymore.

%prep
%autosetup -p1 -n pyjwkest-%{commit}
# https://github.com/rohe/pyjwkest/pull/1
chmod a+x script/gen_symkey.py
sed -i '1 {s:^#!:#!/usr/bin/env python:}' script/gen_symkey.py

sed -i '1 {/^#!/d}' src/jwkest/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# The peek.py script is very tiny, so avoid it reserving 'peek.py' as
# upstream 'peek' may relinquish it https://github.com/dcramer/peek/issues/1
mv %{buildroot}%{_bindir}/peek.py %{buildroot}%{_bindir}/jwpeek.py

%python_clone -a %{buildroot}%{_bindir}/gen_symkey.py
%python_clone -a %{buildroot}%{_bindir}/jwdecrypt.py
%python_clone -a %{buildroot}%{_bindir}/jwenc.py
%python_clone -a %{buildroot}%{_bindir}/jwpeek.py
%python_clone -a %{buildroot}%{_bindir}/jwk_create.py
%python_clone -a %{buildroot}%{_bindir}/jwk_export.py
%python_clone -a %{buildroot}%{_bindir}/jwkutil.py

%check
%pytest

%post
%python_install_alternative gen_symkey.py jwdecrypt.py jwenc.py jwpeek.py jwk_create.py jwk_export.py jwkutil.py

%postun
%python_uninstall_alternative gen_symkey.py jwdecrypt.py jwenc.py jwpeek.py jwk_create.py jwk_export.py jwkutil.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pyjwkest-%{version}*-info
%{python_sitelib}/jwkest
%python_alternative %{_bindir}/gen_symkey.py
%python_alternative %{_bindir}/jwdecrypt.py
%python_alternative %{_bindir}/jwenc.py
%python_alternative %{_bindir}/jwpeek.py
%python_alternative %{_bindir}/jwk_create.py
%python_alternative %{_bindir}/jwk_export.py
%python_alternative %{_bindir}/jwkutil.py

%changelog
