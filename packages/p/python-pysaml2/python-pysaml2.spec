#
# spec file for package python-pysaml2
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


%global modname pysaml2
%{?sle15_python_module_pythons}
Name:           python-pysaml2
Version:        7.5.2
Release:        0
Summary:        Python implementation of SAML Version 2 to be used in a WSGI environment
License:        Apache-2.0
URL:            https://github.com/IdentityPython/pysaml2
Source:         https://github.com/IdentityPython/pysaml2/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM use-cryptography.patch https://github.com/IdentityPython/pysaml2/issues/879
Patch0:         use-cryptography.patch
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module cryptography >= 40.0}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pymongo >= 3.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 1.0.0}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module xmlschema >= 2}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
# This is needed as xmlsec itself does not pull any backend by default
# Will be fixed in future xmlsec releases
BuildRequires:  libxmlsec1-openssl1
BuildRequires:  python-rpm-macros
BuildRequires:  update-alternatives
BuildRequires:  xmlsec1
Requires:       python-Paste
Requires:       python-cryptography >= 3.1
Requires:       python-defusedxml
Requires:       python-pyOpenSSL
Requires:       python-pymongo >= 3.5
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-requests >= 1.0.0
Requires:       python-xmlschema >= 1.2.1
Requires:       python-zope.interface
Requires(post): update-alternatives
Requires(postun): update-alternatives
# We need to have arch build to make ifarch condition below working
# BuildArch:      noarch
%python_subpackages

%description
PySAML2 is a pure python implementation of SAML2.
It contains all necessary pieces for building a
SAML2 service provider or an identity provider.

%prep
%autosetup -p1 -n %{modname}-%{version}

# delete shebang of files not in executable path
find src/ -name '*.py' -print0 | xargs -0 sed -i '1s/#!.*$//'
# remove tests that poll internet
rm -f tests/test_30_mdstore*.py

%build
%pyproject_wheel

%install
%pyproject_install
for exec in make_metadata parse_xsd2 mdexport merge_metadata ; do
%python_clone -a %{buildroot}%{_bindir}/$exec
done
%python_expand rm -r %{buildroot}%{$python_sitelib}/saml2test
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/IdentityPython/pysaml2/issues/858
sed -i 's:import mock:from unittest import mock:' tests/test_41_response.py
sed -i 's:mock.mock:unittest.mock:' tests/test_52_default_sign_alg.py
# Excluded tests for i586 gh#IdentityPython/pysaml2#682 and gh#IdentityPython/pysaml2#759
# Exclude broken namespace test (https://github.com/IdentityPython/pysaml2/issues/921)
%ifarch %{ix86}
%pytest -k "not (test_namespace_processing or test_assertion_consumer_service or test_swamid_sp or test_swamid_idp or test_other_response or test_mta or test_unknown_subject or test_filter_ava_registration_authority_1)" tests
%else
%pytest -k "not test_namespace_processing" tests
%endif

%post
%python_install_alternative make_metadata parse_xsd2 mdexport merge_metadata

%postun
%python_uninstall_alternative make_metadata parse_xsd2 mdexport merge_metadata

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%python_alternative %{_bindir}/make_metadata
%python_alternative %{_bindir}/parse_xsd2
%python_alternative %{_bindir}/mdexport
%python_alternative %{_bindir}/merge_metadata
%{python_sitelib}/saml2
%{python_sitelib}/pysaml2-%{version}.dist-info

%changelog
