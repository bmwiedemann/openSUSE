#
# spec file for package python-autobahn
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


%ifarch %arm aarch64 riscv64
%bcond_with nvx_support
%else
%bcond_without nvx_support
%endif

Name:           python-autobahn
Version:        26.7.1
Release:        0
Summary:        WebSocket and WAMP in Python for Twisted and asyncio
License:        MIT
URL:            https://github.com/crossbario/autobahn-python
Source:         https://files.pythonhosted.org/packages/source/a/autobahn/autobahn-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support s390x intrinics
Patch0:         intrin-arch.patch
# PATCH-FIX-OPENSUSE Do not ship flatc wrapper
Patch1:         no-flatc-entrypoint.patch
BuildRequires:  %{python_module PyNaCl >= 1.4.0}
BuildRequires:  %{python_module Twisted >= 24.3.0}
BuildRequires:  %{python_module argon2-cffi >= 20.1.0}
BuildRequires:  %{python_module attrs >= 20.3.0}
BuildRequires:  %{python_module base58 >= 2.1.1}
BuildRequires:  %{python_module cbor2 >= 5.2.0}
BuildRequires:  %{python_module cffi >= 2.0.0}
BuildRequires:  %{python_module cryptography >= 3.4.6}
BuildRequires:  %{python_module devel >= 3.11}
BuildRequires:  %{python_module ecdsa >= 0.19.1}
BuildRequires:  %{python_module flatbuffers >= 22.12.6}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hyperlink >= 21.0.0}
BuildRequires:  %{python_module msgpack >= 1.0.2}
BuildRequires:  %{python_module passlib >= 1.7.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL >= 20.0.1}
BuildRequires:  %{python_module pytest >= 2.8.6}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytrie >= 0.4.0}
BuildRequires:  %{python_module qrcode >= 7.3.1}
BuildRequires:  %{python_module service_identity >= 18.1.0}
BuildRequires:  %{python_module txaio >= 25.12.2}
BuildRequires:  %{python_module ujson >= 4.0.2}
BuildRequires:  %{python_module wsaccel >= 0.6.3}
BuildRequires:  %{python_module zope.interface >= 5.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cbor2 >= 5.2.0
Requires:       python-cffi >= 2.0.0
Requires:       python-cryptography >= 3.4.6
Requires:       python-hyperlink >= 21.0.0
Requires:       python-msgpack >= 1.0.2
Requires:       python-txaio >= 25.12.2
Requires:       python-ujson >= 4.0.2
# Because not vendored
Requires:       python-flatbuffers >= 22.12.6
# [twisted]
Suggests:       python-Twisted >= 24.3.0
Suggests:       python-attrs >= 20.3.0
Suggests:       python-zope.interface >= 5.2.0
# [accelerate]
Suggests:       python-wsaccel >= 0.6.3
# [encryption]
Suggests:       python-PyNaCl >= 1.4.0
Suggests:       python-pyOpenSSL >= 20.0.1
Suggests:       python-service_identity >= 18.1.0
Suggests:       python-pytrie >= 0.4.0
Suggests:       python-base58 >= 2.1.1
Suggests:       python-ecdsa >= 0.19.1
Suggests:       python-qrcode >= 7.3.1
# [scram]
Suggests:       python-argon2-cffi >= 20.1.0
Suggests:       python-passlib >= 1.7.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
WebSocket allows bidirectional real-time messaging on the Web and WAMP adds
asynchronous Remote Procedure Calls and Publish & Subscribe on top of WebSocket.

%prep
%autosetup -p1 -n autobahn-%{version}

# this test relies too much on rng that can behave randomly in obs
rm src/autobahn/test/test_rng.py

%build
%if %{with nvx_support}
export AUTOBAHN_USE_NVX=1
%endif
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%if %{with nvx_support}
export AUTOBAHN_USE_NVX=1
%endif
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/wamp
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%if %{with nvx_support}
export AUTOBAHN_USE_NVX=1
%else
export AUTOBAHN_USE_NVX=0
%endif
export USE_ASYNCIO=1
export PY_IGNORE_IMPORTMISMATCH=1
# We need to ignore twisted tests here
export PYTEST_ADDOPTS="--ignore=src/autobahn/twisted --ignore=examples"
%pytest_arch
# And then run them here
unset USE_ASYNCIO
export USE_TWISTED=1
%{python_expand # line continues
    pushd %{buildroot}%{$python_sitearch}
    $python -m twisted.trial --no-recurse \
        autobahn.test \
        autobahn.twisted.test \
        autobahn.websocket.test \
        autobahn.rawsocket.test \
        autobahn.wamp.test \
        autobahn.nvx.test
    rm -r _trial_temp
    rm -f twisted/plugins/dropin.cache
    popd
}

%post
%python_install_alternative wamp

%postun
%python_uninstall_alternative wamp

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/_nvx_*cpython-*-linux-gnu*.so
%{python_sitearch}/autobahn
%{python_sitearch}/twisted
%{python_sitearch}/autobahn-%{version}.dist-info
%python_alternative %{_bindir}/wamp

%changelog
