#
# spec file for package python-mitmproxy
#
# Copyright (c) 2025 SUSE LLC
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
# Upstream only supports Python 3.12+!
%define skip_python311 1
Name:           python-mitmproxy
Version:        11.1.2
Release:        0
Summary:        An interactive, SSL/TLS-capable intercepting proxy
License:        MIT
URL:            https://mitmproxy.org
Source:         https://github.com/mitmproxy/mitmproxy/archive/refs/tags/v%{version}.tar.gz#/mitmproxy-%{version}.tar.gz
BuildRequires:  %{python_module Brotli >= 1.0}
BuildRequires:  %{python_module Flask >= 3.0}
BuildRequires:  %{python_module aioquic >= 1.1.0}
BuildRequires:  %{python_module argon2-cffi >= 23.1.0}
BuildRequires:  %{python_module asgiref >= 3.2.10}
BuildRequires:  %{python_module certifi >= 2019.9.11}
BuildRequires:  %{python_module cryptography >= 42.0}
BuildRequires:  %{python_module h11 >= 0.11}
BuildRequires:  %{python_module h2 >= 4.1}
BuildRequires:  %{python_module hyperframe >= 6.0}
BuildRequires:  %{python_module hypothesis >= 5.8}
BuildRequires:  %{python_module kaitaistruct >= 0.10}
BuildRequires:  %{python_module ldap3 >= 2.8}
BuildRequires:  %{python_module mitmproxy-rs >= 0.11}
BuildRequires:  %{python_module msgpack >= 1.0.0}
BuildRequires:  %{python_module parver >= 0.1}
BuildRequires:  %{python_module passlib >= 1.6.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module publicsuffix2 >= 2.20190812}
BuildRequires:  %{python_module pyOpenSSL >= 22.1}
BuildRequires:  %{python_module pyparsing >= 2.4.2}
BuildRequires:  %{python_module pyperclip >= 1.9.0}
BuildRequires:  %{python_module pytest >= 6.1.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.17.0}
BuildRequires:  %{python_module requests >= 2.9.1}
BuildRequires:  %{python_module ruamel.yaml >= 0.16}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sortedcontainers >= 2.3}
BuildRequires:  %{python_module tornado >= 6.4}
BuildRequires:  %{python_module urwid >= 2.6.14}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module wsproto >= 1.0}
BuildRequires:  %{python_module zstandard >= 0.15}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli >= 1.0
Requires:       python-Flask >= 3.0
Requires:       python-aioquic >= 1.1.0
Requires:       python-argon2-cffi >= 23.1.0
Requires:       python-asgiref >= 3.2.10
Requires:       python-certifi >= 2019.9.11
Requires:       python-cryptography >= 42.0
Requires:       python-h11 >= 0.11
Requires:       python-h2 >= 4.1
Requires:       python-hyperframe >= 6.0
Requires:       python-kaitaistruct >= 0.10
Requires:       python-ldap3 >= 2.8
Requires:       python-mitmproxy-rs >= 0.11
Requires:       python-msgpack >= 1.0.0
Requires:       python-passlib >= 1.6.5
Requires:       python-publicsuffix2 >= 2.20190812
Requires:       python-pyOpenSSL >= 22.1
Requires:       python-pyparsing >= 2.4.2
Requires:       python-pyperclip >= 1.9.0
Requires:       python-ruamel.yaml >= 0.16
Requires:       python-sortedcontainers >= 2.3
Requires:       python-tornado >= 6.4
Requires:       python-urwid >= 2.6.14
Requires:       python-wsproto >= 1.0
Requires:       python-zstandard >= 0.15
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
mitmproxy is an interactive, SSL/TLS-capable intercepting proxy with a console
interface for HTTP/1, HTTP/2, and WebSockets.

mitmdump is the command-line version of mitmproxy. Think tcpdump for HTTP.

mitmweb is a web-based interface for mitmproxy.

%prep
%autosetup -p1 -n mitmproxy-%{version}
rm mitmproxy/contrib/kaitaistruct/make.sh

echo "
# increase test deadline for slow obs executions
import hypothesis
hypothesis.settings.register_profile(
    'obs',
    deadline=5000,
    suppress_health_check=[hypothesis.HealthCheck.too_slow]
)
" >> test/conftest.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/mitmdump
%python_clone -a %{buildroot}%{_bindir}/mitmproxy
%python_clone -a %{buildroot}%{_bindir}/mitmweb

%check
# test_refresh fails on i586... wrong timestamp type, maybe?
# test_rollback and test_output[None-expected_out0-expected_err0] just randomly fail on i586
# test_dns and test_name_servers require networking
# test_tun_mode requires root to create a TUN device
%pytest -k "not (test_refresh or test_rollback or test_output or test_name_servers or test_dns or test_tun_mode)" --hypothesis-profile="obs"

%post
%python_install_alternative mitmdump
%python_install_alternative mitmproxy
%python_install_alternative mitmweb

%postun
%python_uninstall_alternative mitmdump
%python_uninstall_alternative mitmproxy
%python_uninstall_alternative mitmweb

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/mitmproxy
%{python_sitelib}/mitmproxy-%{version}.dist-info
%python_alternative %{_bindir}/mitmdump
%python_alternative %{_bindir}/mitmproxy
%python_alternative %{_bindir}/mitmweb

%changelog
