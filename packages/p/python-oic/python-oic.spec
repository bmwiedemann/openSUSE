#
# spec file for package python-oic
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global modname oic
Name:           python-oic
Version:        1.0.1
Release:        0
Summary:        A complete OpenID Connect implementation in Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/OpenIDC/pyoidc
Source:         https://github.com/OpenIDC/pyoidc/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module ldap}
BuildRequires:  %{python_module mock}
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
BuildRequires:  python3-dbm
Requires:       python-Beaker
Requires:       python-Mako
Requires:       python-cryptography
Requires:       python-defusedxml
Requires:       python-future
Requires:       python-pycryptodomex
Requires:       python-pyjwkest >= 1.3.6
Requires:       python-requests
Requires:       python-typing
Requires:       python-typing_extensions
Suggests:       python-ldap
BuildArch:      noarch
%ifpython3
Requires:       python3-dbm
%endif
%python_subpackages

%description
This is a complete Python implementation of OpenID Connect as specified in
the OpenID Connect Core specification. As a side effect, this is a complete
implementation of OAuth2.0 too.

%prep
%setup -q -n pyoidc-%{version}
find src -type f -exec sed -i '1 {/#!/d}' {} +

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=src
%pytest -k 'not network'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*
%{_bindir}/oic-client-management

%changelog
