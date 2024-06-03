#
# spec file for package python-python-jose
#
# Copyright (c) 2024 SUSE LLC
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
Version:        3.3.0
Release:        0
Summary:        JOSE implementation in Python
License:        MIT
URL:            https://github.com/mpdavis/python-jose
Source:         https://files.pythonhosted.org/packages/source/p/python-jose/python-jose-%{version}.tar.gz
Patch0:         unpin-deps.patch
# PATCH-FIX-UPSTREAM CVE-2024-33664.patch gh#mpdavis/python-jose#352
Patch1:         CVE-2024-33664.patch
# PATCH-FIX-UPSTREAM CVE-2024-33663.patch gh#mpdavis/python-jose#349
Patch2:         CVE-2024-33663.patch
# PATCH-FIX-UPSTREAM fix-tests-ecdsa-019.patch gh#mpdavis/python-jose#350
Patch3:         fix-tests-ecdsa-019.patch
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ecdsa >= 0.16
Requires:       python-pyasn1
Requires:       python-rsa
BuildArch:      noarch
%if %{with test}
# pycryptodome is needed just for one test added in CVE-2024-33663.
# This package is not in Leap, so do not require for other versions.
%if 0%{?suse_version} > 1600
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
%autosetup -p1 -n python-jose-%{version}

%if ! %{with test}
%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest -rsEf
%endif

%if ! %{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/python_jose-%{version}*-info
%{python_sitelib}/jose

%files %{python_files cryptography}
%doc README.rst
%license LICENSE
%endif

%changelog
