#
# spec file for package python-pysaml2
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
%global modname pysaml2
Name:           python-pysaml2
Version:        4.8.0
Release:        0
Summary:        Python implementation of SAML Version 2 to be used in a WSGI environment
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/IdentityPython/pysaml2
Source:         https://github.com/IdentityPython/pysaml2/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Paste
Requires:       python-cryptography >= 1.4
Requires:       python-defusedxml
Requires:       python-pyOpenSSL
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-repoze.who
Requires:       python-requests >= 1.0.0
Requires:       python-six
Requires:       python-zope.interface
BuildArch:      noarch
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module cryptography >= 1.4}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module repoze.who}
BuildRequires:  %{python_module requests >= 1.0.0}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module zope.interface}
# This is needed as xmlsec itself does not pull any backend by default
# Will be fixed in future xmlsec releases
BuildRequires:  libxmlsec1-openssl1
BuildRequires:  python2-gdbm
BuildRequires:  python3-dbm
BuildRequires:  xmlsec1
%python_subpackages

%description
PySAML2 is a pure python implementation of SAML2.
It contains all necessary pieces for building a
SAML2 service provider or an identity provider.

%prep
%setup -q -n %{modname}-%{version}
# delete shebang of files not in executable path
find src/ -name '*.py' -print0 | xargs -0 sed -i '1s/#!.*$//'
# remove tests that poll internet
rm -f tests/test_30_mdstore*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%python3_only %{_bindir}/make_metadata.py
%python3_only %{_bindir}/parse_xsd2.py
%python3_only %{_bindir}/mdexport.py
%python3_only %{_bindir}/merge_metadata.py
%{python_sitelib}/*

%changelog
