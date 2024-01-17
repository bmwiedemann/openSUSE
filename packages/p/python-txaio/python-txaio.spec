#
# spec file for package python-txaio
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


Name:           python-txaio
Version:        23.1.1
Release:        0
Summary:        WebSocket and WAMP in Python for Twisted and asyncio
License:        MIT
URL:            https://github.com/crossbario/txaio
Source:         https://files.pythonhosted.org/packages/source/t/txaio/txaio-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-Twisted >= 20.3.0
Recommends:     python-zope.interface >= 5.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted >= 20.3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface >= 5.2}
# /SECTION
%python_subpackages

%description
WebSocket allows bidirectional real-time messaging on the Web and WAMP adds
asynchronous Remote Procedure Calls and Publish & Subscribe on top of WebSocket.

%prep
%setup -q -n txaio-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_sdist'

%files %{python_files}
%license LICENSE
%{python_sitelib}/txaio
%{python_sitelib}/txaio-%{version}*-info

%changelog
