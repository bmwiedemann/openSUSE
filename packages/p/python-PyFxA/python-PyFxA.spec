#
# spec file for package python-PyFxA
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-PyFxA
Version:        0.7.9
Release:        0
Summary:        Firefox Accounts client library for Python
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mozilla/PyFxA
Source:         https://files.pythonhosted.org/packages/source/P/PyFxA/pyfxa-%{version}.tar.gz
BuildRequires:  %{python_module PyBrowserID}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hawkauthlib}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyotp}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.4.2}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyBrowserID
Requires:       python-PyJWT
Requires:       python-cryptography
Requires:       python-hawkauthlib
Requires:       python-requests >= 2.4.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is python library for interacting with the Firefox Accounts ecosystem.

%prep
%autosetup -p1 -n pyfxa-%{version}
sed -i -e '/^#!\/usr\/bin\/env python/d' fxa/__main__.py
find ./ -type f -exec chmod -x {} +

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/fxa
%{python_sitelib}/pyfxa-%{version}.dist-info

%changelog
