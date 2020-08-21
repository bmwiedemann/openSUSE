#
# spec file for package python-slackclient
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
Name:           python-slackclient
Version:        2.8.0
Release:        0
Summary:        Slack API clients for Web API and RTM API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/slackapi/python-slackclient
Source:         https://github.com/slackapi/python-slackclient/archive/v%{version}.tar.gz#/slackclient-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp
Requires:       python-requests >= 2.11
Requires:       python-six >= 1.10
Requires:       python-websocket-client >= 0.35
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module requests >= 2.11}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module six >= 1.10}
BuildRequires:  %{python_module websocket-client >= 0.35}
# /SECTION
%python_subpackages

%description
A client for Slack, which supports the Slack Web API and Real Time Messaging (RTM) API.

Whether you're building a custom app for your team, or integrating a third
party service into your Slack workflows, Slack Developer Kit for Python allows
you to leverage the flexibility of Python to get your project up and running as
quickly as possible.

%prep
%setup -q -n python-slackclient-%{version}
chmod -x README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Despite the mocks, some tests still attempt to access Slack servers
PYTHONPATH=${PWD}
%pytest -k 'not (test_server_connect or test_reconnect_flag or test_rtm_reconnect or test_rtm_max_reconnect_timeout or test_start_raises_an_error_if_rtm_ws_url_is_not_returned)' tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
