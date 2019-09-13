#
# spec file for package python-pyjwkest
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
Name:           python-pyjwkest
Version:        1.4.0
Release:        0
Summary:        Python implementation of JWT, JWE, JWS and JWK
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/rohe/pyjwkest
Source:         https://github.com/rohe/pyjwkest/archive/v1.4.0.tar.gz#/pyjwkest-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
Requires:       python-pycryptodomex
Requires:       python-requests
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module pytest-runner}
%python_subpackages

%description
Python implementation of JWT, JWE, JWS and JWK.

%prep
%setup -q -n pyjwkest-%{version}
# https://github.com/rohe/pyjwkest/pull/1
chmod a+x script/gen_symkey.py
sed -i '1 {s:^#!:#!/usr/bin/env python:}' script/gen_symkey.py

sed -i '1 {/^#!/d}' src/jwkest/*.py
# This interferes with pytest collection, and is unused.
rm debug/A256KW/jwe_test.py

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
%python_exec setup.py pytest

%post
%python_install_alternative gen_symkey.py jwdecrypt.py jwenc.py jwpeek.py jwk_create.py jwk_export.py jwkutil.py

%postun
%python_uninstall_alternative gen_symkey.py jwdecrypt.py jwenc.py jwpeek.py jwk_create.py jwk_export.py jwkutil.py

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/pyjwkest*
%{python_sitelib}/jwkest
%python_alternative %{_bindir}/gen_symkey.py
%python_alternative %{_bindir}/jwdecrypt.py
%python_alternative %{_bindir}/jwenc.py
%python_alternative %{_bindir}/jwpeek.py
%python_alternative %{_bindir}/jwk_create.py
%python_alternative %{_bindir}/jwk_export.py
%python_alternative %{_bindir}/jwkutil.py

%changelog
