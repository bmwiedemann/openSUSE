#
# spec file for package python-oic
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


%define skip_python2 1
%global modname oic
Name:           python-oic
Version:        1.5.0
Release:        0
Summary:        A complete OpenID Connect implementation in Python
License:        Apache-2.0
URL:            https://github.com/OpenIDC/pyoidc
Source:         https://github.com/OpenIDC/pyoidc/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-scheme-message.patch gh#OpenIDC/pyoidc@6fa769a59b8b
Patch0:         fix-scheme-message.patch
BuildRequires:  %{python_module Beaker}
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module ldap}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pyjwkest >= 1.3.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Beaker
Requires:       python-Mako
Requires:       python-cryptography
Requires:       python-dbm
Requires:       python-defusedxml
Requires:       python-pycryptodomex
Requires:       python-pyjwkest >= 1.3.6
Requires:       python-requests
Requires:       python-typing
Requires:       python-typing_extensions
Suggests:       python-ldap
BuildArch:      noarch
%python_subpackages

%description
This is a complete Python implementation of OpenID Connect as specified in
the OpenID Connect Core specification. As a side effect, this is a complete
implementation of OAuth2.0 too.

%prep
%autosetup -p1 -n pyoidc-%{version}
find src -type f -exec sed -i '1 {/#!/d}' {} +
sed -i 's/--color=yes//' tox.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/oic-client-management

%post
%python_install_alternative oic-client-management

%postun
%python_uninstall_alternative oic-client-management

%check
export PYTHONPATH=src
%pytest -k 'not network'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/oic
%{python_sitelib}/oic-%{version}*-info
%python_alternative %{_bindir}/oic-client-management

%changelog
