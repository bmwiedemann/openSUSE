#
# spec file for package python-autobahn
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} %{!?skip_python3:python3-%{**}}}
%define skip_python2 1
Name:           python-autobahn
Version:        20.6.1
Release:        0
Summary:        WebSocket and WAMP in Python for Twisted and asyncio
License:        MIT
URL:            https://github.com/crossbario/autobahn-python
Source:         https://files.pythonhosted.org/packages/source/a/autobahn/autobahn-%{version}.tar.gz
Patch0:         respect-cflags.patch
BuildRequires:  %{python_module PyNaCl >= 1.0.1}
BuildRequires:  %{python_module PyQRCode >= 1.1}
BuildRequires:  %{python_module Twisted >= 20.3.0}
BuildRequires:  %{python_module argon2-cffi >= 18.1.0}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module cbor >= 1.0.0}
BuildRequires:  %{python_module cbor2 >= 4.1.2}
BuildRequires:  %{python_module cffi >= 1.11.5}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module flatbuffers >= 1.10}
BuildRequires:  %{python_module lz4 >= 0.7.0}
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module msgpack >= 0.6.1}
BuildRequires:  %{python_module passlib >= 1.7.1}
BuildRequires:  %{python_module py-ubjson >= 0.8.4}
BuildRequires:  %{python_module pyOpenSSL >= 16.2.0}
BuildRequires:  %{python_module pytest >= 2.8.6}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytrie >= 0.2}
BuildRequires:  %{python_module service_identity >= 16.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module txaio >= 18.8.1}
BuildRequires:  %{python_module ujson >= 1.35}
BuildRequires:  %{python_module wsaccel >= 0.6.2}
BuildRequires:  %{python_module zope.interface >= 3.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python3-PyNaCl >= 1.0.1
Requires:       python3-PyQRCode >= 1.1
Requires:       python3-Twisted >= 20.3.0
Requires:       python3-argon2-cffi >= 18.1.0
Requires:       python3-cbor >= 1.0.0
Requires:       python3-cbor2 >= 4.1.2
Requires:       python3-cffi >= 1.11.5
Requires:       python3-flatbuffers >= 1.10
Requires:       python3-lz4 >= 0.7.0
Requires:       python3-msgpack >= 0.6.1
Requires:       python3-passlib >= 1.7.1
Requires:       python3-py-ubjson >= 0.8.4
Requires:       python3-pyOpenSSL >= 16.2.0
Requires:       python3-pytrie >= 0.2
Requires:       python3-service_identity >= 16.0.0
Requires:       python3-txaio >= 18.8.1
Requires:       python3-ujson >= 1.35
Requires:       python3-wsaccel >= 0.6.2
Requires:       python3-zope.interface >= 3.6.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
WebSocket allows bidirectional real-time messaging on the Web and WAMP adds
asynchronous Remote Procedure Calls and Publish & Subscribe on top of WebSocket.

%prep
%setup -q -n autobahn-%{version}
%patch0 -p1

# this test relies too much on rng that can behave randomly in obs
rm autobahn/test/test_rng.py

%build
export AUTOBAHN_USE_NVX=true
export CFLAGS="%{optflags}"
%python_build

%install
export AUTOBAHN_USE_NVX=true
%python_install
%python_clone -a %{buildroot}%{_bindir}/wamp
%python_clone -a %{buildroot}%{_bindir}/xbrnetwork
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export USE_ASYNCIO=true
export AUTOBAHN_USE_NVX=true
export PYTHONDONTWRITEBYTECODE=1
export PY_IGNORE_IMPORTMISMATCH=1
%pytest_arch

%post
%python_install_alternative wamp xbrnetwork

%postun
%python_uninstall_alternative wamp xbrnetwork

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*
%python_alternative %{_bindir}/wamp
%python_alternative %{_bindir}/xbrnetwork

%changelog
