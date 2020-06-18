#
# spec file for package python-mitmproxy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-mitmproxy
Version:        5.1.1
Release:        0
Summary:        An interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets
License:        MIT
Group:          Development/Languages/Python
URL:            https://mitmproxy.org
Source:         https://github.com/mitmproxy/mitmproxy/archive/v%{version}.tar.gz#/mitmproxy-%{version}.tar.gz
# upstream likes to pin dependencies too aggressively
Patch0:         unpin.patch
BuildRequires:  %{python_module Brotli >= 1.0}
BuildRequires:  %{python_module Flask >= 1.1.1}
BuildRequires:  %{python_module asynctest >= 0.12.0}
BuildRequires:  %{python_module beautifulsoup4 >= 4.4.1}
BuildRequires:  %{python_module blinker >= 1.4}
BuildRequires:  %{python_module certifi >= 2019.9.11}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module cryptography >= 2.9}
BuildRequires:  %{python_module h2 >= 3.2.0}
BuildRequires:  %{python_module hyperframe >= 5.1.0}
BuildRequires:  %{python_module hypothesis >= 5.8}
BuildRequires:  %{python_module kaitaistruct >= 0.7}
BuildRequires:  %{python_module ldap3 >= 2.6.1}
BuildRequires:  %{python_module parver >= 0.1}
BuildRequires:  %{python_module passlib >= 1.6.5}
BuildRequires:  %{python_module protobuf >= 3.6.0}
BuildRequires:  %{python_module publicsuffix2 >= 2.20190812}
BuildRequires:  %{python_module pyOpenSSL >= 19.1.0}
BuildRequires:  %{python_module pyasn1 >= 0.3.1}
BuildRequires:  %{python_module pyparsing >= 2.4.2}
BuildRequires:  %{python_module pyperclip >= 1.6.0}
BuildRequires:  %{python_module pytest >= 5.1.3}
BuildRequires:  %{python_module pytest-asyncio >= 0.10.0}
BuildRequires:  %{python_module requests >= 2.9.1}
BuildRequires:  %{python_module ruamel.yaml >= 0.16}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sortedcontainers >= 2.1.0}
BuildRequires:  %{python_module tornado >= 4.3}
BuildRequires:  %{python_module urwid >= 2.1.0}
BuildRequires:  %{python_module wsproto >= 0.14}
BuildRequires:  %{python_module zstandard >= 0.11}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli >= 1.0
Requires:       python-Flask >= 1.1.1
Requires:       python-blinker >= 1.4
Requires:       python-certifi >= 2019.9.11
Requires:       python-click >= 7.0
Requires:       python-cryptography >= 2.9
Requires:       python-h2 >= 3.2.0
Requires:       python-hyperframe >= 5.1.0
Requires:       python-kaitaistruct >= 0.7
Requires:       python-ldap3 >= 2.6.1
Requires:       python-passlib >= 1.6.2
Requires:       python-protobuf >= 3.6.0
Requires:       python-publicsuffix2 >= 2.20190812
Requires:       python-pyOpenSSL >= 19.1.0
Requires:       python-pyasn1 >= 0.3.1
Requires:       python-pyparsing >= 2.4.2
Requires:       python-pyperclip >= 1.6.0
Requires:       python-ruamel.yaml >= 0.16
Requires:       python-sortedcontainers >= 2.1.0
Requires:       python-tornado >= 4.3
Requires:       python-urwid >= 2.1.0
Requires:       python-wsproto >= 0.14
Requires:       python-zstandard >= 0.11
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-beautifulsoup4 >= 4.4.1
BuildArch:      noarch
%python_subpackages

%description
This repository contains the **mitmproxy** and **pathod** projects.

mitmproxy is an interactive, SSL/TLS-capable intercepting proxy with a console
interface for HTTP/1, HTTP/2, and WebSockets.

mitmdump is the command-line version of mitmproxy. Think tcpdump for HTTP.

mitmweb is a web-based interface for mitmproxy.

pathoc and pathod are perverse HTTP client and server applications
designed to let you craft almost any conceivable HTTP request, including ones
that creatively violate the standards.

%prep
%setup -q -n mitmproxy-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/mitmdump
%python_clone -a %{buildroot}%{_bindir}/mitmproxy
%python_clone -a %{buildroot}%{_bindir}/mitmweb
%python_clone -a %{buildroot}%{_bindir}/pathoc
%python_clone -a %{buildroot}%{_bindir}/pathod

%check
# test_refresh fails on i586... wrong timestamp type, maybe?
# test_rollback and test_output[None-expected_out0-expected_err0] just randomly fail on i586
%pytest -k "not (test_refresh or test_rollback or test_output)"

%post
%python_install_alternative mitmdump
%python_install_alternative mitmproxy
%python_install_alternative mitmweb
%python_install_alternative pathoc
%python_install_alternative pathod

%postun
%python_uninstall_alternative mitmdump
%python_uninstall_alternative mitmproxy
%python_uninstall_alternative mitmweb
%python_uninstall_alternative pathoc
%python_uninstall_alternative pathod

%files %{python_files}
%doc README.rst CHANGELOG
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/mitmdump
%python_alternative %{_bindir}/mitmproxy
%python_alternative %{_bindir}/mitmweb
%python_alternative %{_bindir}/pathoc
%python_alternative %{_bindir}/pathod

%changelog
