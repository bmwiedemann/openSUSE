#
# spec file for package python-autobahn
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


%ifarch %arm aarch64 riscv64
%bcond_with nvx_support
%else
%bcond_without nvx_support
%endif

Name:           python-autobahn
Version:        24.4.2
Release:        0
Summary:        WebSocket and WAMP in Python for Twisted and asyncio
License:        MIT
URL:            https://github.com/crossbario/autobahn-python
Source:         https://files.pythonhosted.org/packages/source/a/autobahn/autobahn-%{version}.tar.gz
Patch0:         respect-cflags.patch
Patch1:         intrin-arch.patch
# PATCH-FIX-UPSTREAM gh#crossbario/autobahn-python#1647
Patch2:         support-new-pytest-asyncio.patch
BuildRequires:  %{python_module PyNaCl >= 1.4.0}
BuildRequires:  %{python_module Twisted >= 24.3.0}
BuildRequires:  %{python_module argon2-cffi >= 20.1.0}
BuildRequires:  %{python_module attrs >= 20.3.0}
BuildRequires:  %{python_module cbor2 >= 5.2.0}
BuildRequires:  %{python_module cffi >= 1.14.5}
BuildRequires:  %{python_module cryptography >= 3.4.6}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module flatbuffers >= 22.12.6}
BuildRequires:  %{python_module hyperlink >= 21.0.0}
BuildRequires:  %{python_module msgpack >= 1.0.2}
BuildRequires:  %{python_module passlib >= 1.7.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py-ubjson >= 0.16.1}
BuildRequires:  %{python_module pyOpenSSL >= 20.0.1}
BuildRequires:  %{python_module pytest >= 2.8.6}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytrie >= 0.4.0}
BuildRequires:  %{python_module qrcode >= 7.3.1}
BuildRequires:  %{python_module service_identity >= 18.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module txaio >= 21.2.1}
BuildRequires:  %{python_module ujson >= 4.0.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module wsaccel >= 0.6.3}
BuildRequires:  %{python_module zope.interface >= 5.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyNaCl >= 1.4.0
Requires:       python-Twisted >= 24.3.0
Requires:       python-argon2-cffi >= 20.1.0
Requires:       python-attrs >= 20.3.0
Requires:       python-cbor2 >= 5.2.0
Requires:       python-cffi >= 1.14.5
Requires:       python-cryptography >= 3.4.6
Requires:       python-flatbuffers >= 22.12.6
Requires:       python-hyperlink >= 21.0.0
Requires:       python-msgpack >= 1.0.2
Requires:       python-passlib >= 1.7.4
Requires:       python-py-ubjson >= 0.16.1
Requires:       python-pyOpenSSL >= 20.0.1
Requires:       python-pytrie >= 0.4.0
Requires:       python-qrcode >= 7.3.1
Requires:       python-service_identity >= 18.1.0
Requires:       python-setuptools
Requires:       python-txaio >= 21.2.1
Requires:       python-ujson >= 4.0.2
Requires:       python-wsaccel >= 0.6.3
Requires:       python-zope.interface >= 5.2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
WebSocket allows bidirectional real-time messaging on the Web and WAMP adds
asynchronous Remote Procedure Calls and Publish & Subscribe on top of WebSocket.

%prep
%autosetup -p1 -n autobahn-%{version}

# this test relies too much on rng that can behave randomly in obs
rm autobahn/test/test_rng.py

%build
%if %{with nvx_support}
export AUTOBAHN_USE_NVX=true
%endif
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%if %{with nvx_support}
export AUTOBAHN_USE_NVX=true
%endif
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/wamp
%python_clone -a %{buildroot}%{_bindir}/xbrnetwork
%python_clone -a %{buildroot}%{_bindir}/xbrnetwork-ui
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with nvx_support}
# It tries to test NVX, even if disabled
%check
export USE_ASYNCIO=true
export AUTOBAHN_USE_NVX=true
export PYTHONDONTWRITEBYTECODE=1
export PY_IGNORE_IMPORTMISMATCH=1
%pytest_arch
%endif

%post
%python_install_alternative wamp xbrnetwork xbrnetwork-ui

%postun
%python_uninstall_alternative wamp xbrnetwork xbrnetwork-ui

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/_nvx_utf8validator.abi3.so
%{python_sitearch}/autobahn
%{python_sitearch}/twisted
%{python_sitearch}/autobahn-%{version}.dist-info
%python_alternative %{_bindir}/wamp
%python_alternative %{_bindir}/xbrnetwork
%python_alternative %{_bindir}/xbrnetwork-ui

%changelog
