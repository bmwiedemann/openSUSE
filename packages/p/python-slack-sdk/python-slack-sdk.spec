#
# spec file for package python-slack-sdk
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-slack-sdk
Version:        3.19.3
Release:        0
Summary:        Python SDKs for the Slack API
License:        MIT
URL:            https://github.com/slackapi/python-slack-sdk
Source:         https://github.com/slackapi/python-slack-sdk/archive/v%{version}.tar.gz#/slack-sdk-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      python-slackclient < %{version}
Provides:       python-slackclient = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sqlalchemy}
BuildRequires:  %{python_module websockets}
# /SECTION
%python_subpackages

%description
The Slack platform offers several APIs to build apps. Each Slack API delivers
part of the capabilities from the platform, so that you can pick just those
that fit for your needs. This SDK offers a corresponding package for each of
Slack’s APIs. They are small and powerful when used independently, and work
seamlessly when used together, too.

%prep
%setup -q -n python-slack-sdk-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No flask_sockets in Tumbleweed; TestRTMClient requires network
%pytest --ignore-glob '*/socket_mode/*' -k 'not TestRTMClient' tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
