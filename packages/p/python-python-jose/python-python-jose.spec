#
# spec file for package python-python-jose
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test-backend-cryptography"
%define psuffix -%{flavor}
%bcond_without test
%bcond_without testcryptography
%bcond_with    testnative
%endif
%if "%{flavor}" == "test-backend-native"
%define psuffix -%{flavor}
%bcond_without test
%bcond_with    testcryptography
%bcond_without testnative
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with    test
%bcond_with    testcryptography
%bcond_with    testnative
%endif

%{?sle15_python_module_pythons}
Name:           python-python-jose%{psuffix}
Version:        3.5.0
Release:        0
Summary:        JOSE implementation in Python
License:        MIT
URL:            https://github.com/mpdavis/python-jose
Source:         https://files.pythonhosted.org/packages/source/p/python-jose/python_jose-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ecdsa >= 0.16
Requires:       python-pyasn1
Requires:       python-rsa
BuildArch:      noarch
%if %{with test}
# pycryptodome is needed just for one test added in CVE-2024-33663.
# This package is not in Leap, so do not require for other versions.
%if 0%{?suse_version} >= 1699
BuildRequires:  %{python_module pycryptodome}
%endif
BuildRequires:  %{python_module pytest}
%if %{with testcryptography}
BuildRequires:  %{python_module python-jose-cryptography = %{version}}
%endif
%if %{with testnative}
BuildRequires:  %{python_module python-jose = %{version}}
%endif
%endif
# /SECTION
%python_subpackages

%description
A JavaScript Object Signing and Encryption (JOSE) technologies
implementation in Python.

python-jose implements different cryptographic backends.
Consuming python packages must select the backend as an extra
when installing python-jose. RPM packages must select the
corresponding rpm subpackage. If no backend is selected, the
main package uses the native-python backend.

%package cryptography
Summary:        JOSE implementation in Python, cryptography extra
Requires:       %{name} = %{version}-%{release}
Requires:       python-cryptography >= 3.4.0

%description cryptography
A JavaScript Object Signing and Encryption (JOSE) technologies
implementation in Python.

python-jose implements three different cryptographic backends.
This package provides the python-jose[cryptography] extra.

%prep
%autosetup -p1 -n python_jose-%{version}

%if ! %{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# https://github.com/mpdavis/python-jose/pull/396 test_incorrect_public_key_hmac_signing fails with cryptography 46
%pytest -rsEf -k "not test_incorrect_public_key_hmac_signing"
%endif

%if ! %{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/python_jose-%{version}.dist-info
%{python_sitelib}/jose

%files %{python_files cryptography}
%doc README.rst
%license LICENSE
%endif

%changelog
