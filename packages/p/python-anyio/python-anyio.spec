#
# spec file for package python-anyio
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-anyio
Version:        2.2.0
Release:        0
Summary:        High level compatibility layer for asynchronous event loop implementations
License:        MIT
URL:            https://github.com/agronholm/anyio
Source:         https://files.pythonhosted.org/packages/source/a/anyio/anyio-%{version}.tar.gz
BuildRequires:  %{python_module async_generator if %python-base < 3.7}
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module idna >= 2.8}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sniffio >= 1.1}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.8}
BuildRequires:  python-rpm-macros >= 20210127.3a18043
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 4.0}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module trio >= 0.16}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module uvloop}
# Note to packagers: future versions will drop curio (https://github.com/agronholm/anyio/pull/182)
BuildRequires:  %{python_module curio >= 1.4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-idna >= 2.8
Requires:       python-sniffio >= 1.1
%if 0%{?python_version_nodots} < 38
Requires:       python-typing_extensions
%endif
%if 0%{?python_version_nodots} < 37
Requires:       python-async_generator
Requires:       python-dataclasses
%endif
Suggests:       python-trio >= 0.1
# See note above
Suggests:       python-curio >= 1.4
BuildArch:      noarch
%python_subpackages

%description
Asynchronous compatibility API that allows applications and libraries written 
against it to run unmodified on asyncio, curio and trio.

%prep
%setup -q -n anyio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# bind and resolution failures inside OBS
donttest+=" or (TestTCPStream and (ipv4 or ipv6))"
donttest+=" or (TestTCPListener and (ipv4 or ipv6))"
donttest+=" or (TestConnectedUDPSocket and (ipv4 or ipv6))"
donttest+=" or (TestUDPSocket and (ipv4 or ipv6))"
# wrong localhost address
donttest+=" or (TestTCPStream and test_happy_eyeballs)"
donttest+=" or (TestTCPStream and test_connection_refused)"
donttest+=" or test_getaddrinfo"
%pytest -k "not (${donttest:4})" -ra

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/anyio
%{python_sitelib}/anyio-%{version}*-info

%changelog
