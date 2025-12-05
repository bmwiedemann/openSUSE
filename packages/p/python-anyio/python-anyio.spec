#
# spec file for package python-anyio
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-anyio%{psuffix}
Version:        4.11.0
Release:        0
Summary:        High level compatibility layer for asynchronous event loop implementations
License:        MIT
URL:            https://github.com/agronholm/anyio
Source:         https://files.pythonhosted.org/packages/source/a/anyio/anyio-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros >= 20210127.3a18043
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module anyio = %{version}}
BuildRequires:  %{python_module blockbuster}
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module hypothesis >= 4.0}
BuildRequires:  %{python_module psutil >= 5.9}
BuildRequires:  %{python_module pytest >= 7.0}
BuildRequires:  %{python_module pytest-mock >= 3.6.1}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module trio >= 0.31.0}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module truststore}
BuildRequires:  %{python_module uvloop}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-idna >= 2.8
Requires:       python-sniffio >= 1.1
%if 0%{?python_version_nodots} < 313
Requires:       python-typing_extensions >= 4.5
%endif
%if 0%{?python_version_nodots} < 311
Requires:       python-exceptiongroup
%endif
Suggests:       python-trio >= 0.31.0
BuildArch:      noarch
%python_subpackages

%description
Asynchronous compatibility API that allows applications and libraries written
against it to run unmodified on asyncio, curio and trio.

%prep
%autosetup -p1 -n anyio-%{version}
# Fix license field in pyproject.toml for older setuptools
%if 0%{?suse_version} <= 1500
sed -i 's/license = "MIT"/license = { text = "MIT" }/' pyproject.toml
%endif

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# increase timeout in test_keyboardinterrupt_during_test
sed -i 's/timeout=3/timeout=8/' tests/test_pytest_plugin.py

sed -i '/filterwarnings/,/^]/ { /"error"/ d}' pyproject.toml
# bind and resolution failures inside OBS
donttest+=" or (TestTCPStream and (ipv4 or ipv6))"
donttest+=" or (TestTCPListener and (ipv4 or ipv6))"
donttest+=" or (TestConnectedUDPSocket and (ipv4 or ipv6))"
donttest+=" or (TestUDPSocket and (ipv4 or ipv6))"
# wrong localhost address
donttest+=" or (TestTCPStream and test_happy_eyeballs)"
donttest+=" or (TestTCPStream and test_connection_refused)"
donttest+=" or test_bind_link_local"
# does not raise an exception
donttest+=" or (TestTLSStream and test_ragged_eofs)"
%if 0%{?suse_version} < 1550
donttest+=" or (test_send_eof_not_implemented)"
%endif
donttest+=" or (test_exception_group and trio)"
# Fail with python 3.12
donttest+=" or (test_properties and trio)"
donttest+=" or (test_properties and asyncio)"
# Flaky test in i586
donttest+=" or test_keyboardinterrupt_during_test"
# Fails with pytest 9
donttest+=" or test_anyio_fixture_adoption_does_not_persist"

%pytest -m "not network" -k "not (${donttest:4})" -ra
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/anyio
%{python_sitelib}/anyio-%{version}.dist-info
%endif

%changelog
