#
# spec file for package python-social-auth-core
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Matthias Fehring <buschmann23@opensuse.org>
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
Name:           python-social-auth-core
Version:        3.2.0
Release:        0
Summary:        Python Social Auth Core
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-social-auth/social-core
Source:         https://files.pythonhosted.org/packages/source/s/social-auth-core/social-auth-core-%{version}.tar.gz
# Missing test data https://github.com/python-social-auth/social-core/pull/351
Source1:        https://raw.githubusercontent.com/python-social-auth/social-core/master/social_core/tests/backends/data/saml_config.json
Patch0:         remove-unittest2.patch
BuildRequires:  %{python_module PyJWT >= 1.4.0}
BuildRequires:  %{python_module coverage >= 3.6}
BuildRequires:  %{python_module cryptography >= 2.1.1}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose >= 1.2.1}
BuildRequires:  %{python_module oauthlib >= 1.0.3}
BuildRequires:  %{python_module python-jose >= 3.0.0}
BuildRequires:  %{python_module python3-saml}
BuildRequires:  %{python_module rednose >= 0.4.1}
BuildRequires:  %{python_module requests >= 2.9.1}
BuildRequires:  %{python_module requests-oauthlib >= 0.6.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-python-openid >= 2.2.5
BuildRequires:  python3 >= 3.4.0
BuildRequires:  python3-defusedxml >= 0.5.0
BuildRequires:  python3-python3-openid >= 3.0.10
Requires:       python-PyJWT >= 1.4.0
Requires:       python-cryptography >= 2.1.1
Requires:       python-oauthlib >= 1.0.3
Requires:       python-python-jose >= 3.0.0
Requires:       python-requests >= 2.9.1
Requires:       python-requests-oauthlib >= 0.6.1
Requires:       python-six >= 1.10.0
Suggests:       python-python3-saml
BuildArch:      noarch
%ifpython2
Requires:       python2-python-openid >= 2.2.5
%endif
%ifpython3
Requires:       python3 >= 3.4.0
Requires:       python3-defusedxml >= 0.5.0
Requires:       python3-python3-openid >= 3.0.10
%endif
%python_subpackages

%description
Python Social Auth is a social authentication/registration
mechanism with support for several frameworks and auth providers.

This is the core component of the python-social-auth ecosystem. It
implements the common interface to define new authentication backends to
third party services, implement integrations with web frameworks and
storage solutions.

%prep
%setup -q -n social-auth-core-%{version}
%patch0 -p1
cp %{SOURCE1} social_core/tests/backends/data/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand %{_bindir}/nosetests-%{$python_bin_suffix}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
