#
# spec file for package python-PyFxA
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2018 The openSUSE Project.
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
Name:           python-PyFxA
Version:        0.7.7
Release:        0
Summary:        Firefox Accounts client library for Python
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mozilla/PyFxA
Source:         https://files.pythonhosted.org/packages/source/P/PyFxA/PyFxA-%{version}.tar.gz
BuildRequires:  %{python_module PyBrowserID}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module hawkauthlib}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyotp}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.4.2}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.14}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyBrowserID
Requires:       python-cryptography
Requires:       python-requests >= 2.4.2
Requires:       python-six >= 1.14
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython3
Requires:       python-setuptools
%endif
%python_subpackages

%description
This is python library for interacting with the Firefox Accounts ecosystem.

%prep
%setup -q -n PyFxA-%{version}
sed -i -e '/^#!\/usr\/bin\/env python/d' fxa/__main__.py
find ./ -type f -exec chmod -x {} +

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/fxa-client
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Exclude tests which require network connection +
# deprecated test_monkey_patch_for_gevent
includedTests="\
  not TestAuthClientAuthorizeToken and\
  not TestAuthClientVerifyCode and\
  not TestCachedClient and\
  not TestCoreClient and\
  not TestCoreClientSession and\
  not TestJwtToken and\
  not test_monkey_patch_for_gevent"
%pytest -k "${includedTests}" fxa/tests/

%post
%python_install_alternative fxa-client

%postun
%python_uninstall_alternative fxa-client

%files %{python_files}
%doc CHANGES.txt README.rst
%python_alternative %{_bindir}/fxa-client
%{python_sitelib}/*

%changelog
