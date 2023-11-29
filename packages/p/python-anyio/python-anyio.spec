#
# spec file for package python-anyio
#
# Copyright (c) 2023 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-anyio
Version:        3.7.1
Release:        0
Summary:        High level compatibility layer for asynchronous event loop implementations
License:        MIT
URL:            https://github.com/agronholm/anyio
Source:         https://files.pythonhosted.org/packages/source/a/anyio/anyio-%{version}.tar.gz
# PATCH-FIX-UPSTREAM see gh#agronholm/anyio#626
Patch2:         tests-test_fileio.py-don-t-follow-symlinks-in-dev.patch
BuildRequires:  %{python_module contextlib2 if %python-base < 3.7}
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module idna >= 2.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil >= 5.9}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module sniffio >= 1.1}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros >= 20210127.3a18043
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 4.0}
BuildRequires:  %{python_module mock >= 4.0 if %python-base < 3.8}
BuildRequires:  %{python_module pytest >= 7.0}
BuildRequires:  %{python_module pytest-mock >= 3.6.1}
BuildRequires:  %{python_module trio >= 0.16}
BuildRequires:  %{python_module trustme}
# /SECTION
BuildRequires:  fdupes
Requires:       python-idna >= 2.8
Requires:       python-sniffio >= 1.1
%if 0%{?python_version_nodots} < 38
Requires:       python-typing_extensions
%endif
%if 0%{?python_version_nodots} < 37
Requires:       python-contextvars
Requires:       python-dataclasses
%endif
Suggests:       python-trio >= 0.16
BuildArch:      noarch
%python_subpackages

%description
Asynchronous compatibility API that allows applications and libraries written
against it to run unmodified on asyncio, curio and trio.

%prep
%autosetup -p1 -n anyio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
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
%pytest -m "not network" -k "not (${donttest:4})" -ra

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/anyio
%{python_sitelib}/anyio-%{version}*-info

%changelog
