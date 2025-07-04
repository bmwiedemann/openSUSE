#
# spec file for package python-oic
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


%global modname oic
Name:           python-oic
Version:        1.7.0
Release:        0
Summary:        A complete OpenID Connect implementation in Python
License:        Apache-2.0
URL:            https://github.com/OpenIDC/pyoidc
Source:         https://github.com/OpenIDC/pyoidc/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Beaker}
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module ldap}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pydantic-settings}
BuildRequires:  %{python_module pyjwkest >= 1.3.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Mako
Requires:       python-cryptography
Requires:       python-defusedxml
Requires:       python-pycryptodomex
Requires:       python-pydantic-settings
Requires:       python-pyjwkest >= 1.3.6
Requires:       python-requests
Suggests:       python-Beaker
Suggests:       python-ldap
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/oic-%{version}.dist-info
%python_alternative %{_bindir}/oic-client-management

%changelog
