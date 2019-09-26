#
# spec file for package python-autobahn
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


%{?!python_module:%define python_module() python-%{**} %{!?skip_python3:python3-%{**}}}
Name:           python-autobahn
Version:        19.9.2
Release:        0
Summary:        WebSocket and WAMP in Python for Twisted and asyncio
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/crossbario/autobahn-python
Source:         https://files.pythonhosted.org/packages/source/a/autobahn/autobahn-%{version}.tar.gz
Patch0:         respect-cflags.patch
BuildRequires:  %{python_module PyNaCl >= 1.0.1}
BuildRequires:  %{python_module PyQRCode >= 1.1}
BuildRequires:  %{python_module Twisted >= 12.1.0}
BuildRequires:  %{python_module argon2-cffi >= 18.1.0}
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
BuildRequires:  %{python_module pytrie >= 0.2}
BuildRequires:  %{python_module service_identity >= 16.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  %{python_module txaio >= 18.8.1}
BuildRequires:  %{python_module ujson >= 1.35}
BuildRequires:  %{python_module wsaccel >= 0.6.2}
BuildRequires:  %{python_module zope.interface >= 3.6.0}
BuildRequires:  fdupes
BuildRequires:  python-futures >= 3.0.4
BuildRequires:  python-rpm-macros
BuildRequires:  python2-trollius
BuildRequires:  python3-pytest-aiohttp
BuildRequires:  python3-pytest-asyncio
Requires:       python-PyNaCl >= 1.0.1
Requires:       python-PyQRCode >= 1.1
Requires:       python-Twisted >= 12.1.0
Requires:       python-argon2-cffi >= 18.1.0
Requires:       python-cbor >= 1.0.0
Requires:       python-cbor2 >= 4.1.2
Requires:       python-cffi >= 1.11.5
Requires:       python-flatbuffers >= 1.10
Requires:       python-lz4 >= 0.7.0
Requires:       python-msgpack >= 0.6.1
Requires:       python-passlib >= 1.7.1
Requires:       python-py-ubjson >= 0.8.4
Requires:       python-pyOpenSSL >= 16.2.0
Requires:       python-pytrie >= 0.2
Requires:       python-service_identity >= 16.0.0
Requires:       python-six >= 1.11.0
Requires:       python-txaio >= 18.8.1
Requires:       python-ujson >= 1.35
Requires:       python-wsaccel >= 0.6.2
Requires:       python-zope.interface >= 3.6.0
%ifpython2
Requires:       python-futures >= 3.0.4
Requires:       python-trollius >= 2.0
%endif
%python_subpackages

%description
WebSocket allows bidirectional real-time messaging on the Web and WAMP adds
asynchronous Remote Procedure Calls and Publish & Subscribe on top of WebSocket.

%prep
%setup -q -n autobahn-%{version}
%patch0 -p1

%build
export AUTOBAHN_USE_NVX=true
export CFLAGS="%{optflags}"
%python_build

%install
export AUTOBAHN_USE_NVX=true
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export USE_ASYNCIO=true
export AUTOBAHN_USE_NVX=true
export PYTHONDONTWRITEBYTECODE=1
export PY_IGNORE_IMPORTMISMATCH=1
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*
%python3_only /usr/bin/wamp

%changelog
