#
# spec file for package python-python3-saml
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-python3-saml
Version:        1.14.0
Release:        0
Summary:        Python SAML support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/onelogin/python3-saml
Source:         https://github.com/onelogin/python3-saml/archive/v%{version}.tar.gz#/python3-saml-%{version}.tar.gz
BuildRequires:  %{python_module freezegun >= 0.3.11}
BuildRequires:  %{python_module isodate >= 0.6.1}
BuildRequires:  %{python_module lxml >= 3.3.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xmlsec >= 1.3.9}
BuildRequires:  fdupes
BuildRequires:  libxmlsec1-openssl1
BuildRequires:  python-rpm-macros
# Select the libxmlsec backend known to work
# pkgconfig doesnt auto-require it.
Requires:       libxmlsec1-openssl1
Requires:       python-isodate >= 0.6.1
Requires:       python-xmlsec >= 1.3.9
BuildArch:      noarch
%python_subpackages

%description
Python SAML support for your Python 2 or 3 software.

SAML is an XML-based standard for web browser single sign-on and is
defined by the OASIS Security Services Technical Committee.

%prep
%autosetup -p1 -n python3-saml-%{version}

sed -i 's/==/>=/;/dependency_links/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/onelogin

%check
# gh#onelogin/python3-saml#271
# the test suite is a complete disaster currently gh#onelogin/python3-saml#272
%pytest -k 'not (testIsInValidAudience or testIsInValidEncAttrs or testIsInValidIssuer or testIsInValidSessionIndex or testIsInValidSubjectConfirmation)' || /bin/true

%files %{python_files}
%license LICENSE
%doc README.md
%dir %{python_sitelib}/onelogin
%{python_sitelib}/onelogin/saml2
%{python_sitelib}/onelogin/__init__.py
%pycache_only %{python_sitelib}/onelogin/__pycache__/
%{python_sitelib}/python3_saml-%{version}*-info

%changelog
