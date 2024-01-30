#
# spec file for package python-pyOpenSSL
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
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-pyOpenSSL%{psuffix}
Version:        24.0.0
Release:        0
Summary:        Python wrapper module around the OpenSSL library
License:        Apache-2.0
URL:            https://github.com/pyca/pyopenssl
Source:         https://files.pythonhosted.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip-networked-test.patch gh#pyca/pyopenssl#68 mcepl@suse.com
# Mark tests requiring network access
Patch0:         skip-networked-test.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cffi
Requires:       (python-cryptography >= 41.0.5 with python-cryptography < 43)
Provides:       pyOpenSSL = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module cryptography >= 41.0.5 with %python-cryptography < 43}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pyOpenSSL >= %version}
BuildRequires:  %{python_module pytest >= 3.0.1}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  openssl
%endif
%python_subpackages

%description
pyOpenSSL is a set of Python bindings for OpenSSL.  It includes some low-level
cryptography APIs but is primarily focused on providing an API for using the
TLS protocol from Python.

pyOpenSSL is now a pure-Python project with a dependency on a new project,
cryptography (<https://github.com/pyca/cryptography>), which provides (among
other things) a cffi-based interface to OpenSSL.

%prep
%autosetup -p1 -n pyOpenSSL-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
SKIPPED_TESTS="network"
%if %{__isa_bits} == 32
SKIPPED_TESTS="(network or test_verify_with_time)"
%endif
export LC_ALL=en_US.UTF-8
%pytest -k "not $SKIPPED_TESTS"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc *.rst
%{python_sitelib}/OpenSSL/
%{python_sitelib}/pyOpenSSL-%{version}*-info
%endif

%changelog
