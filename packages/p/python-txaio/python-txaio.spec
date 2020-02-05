#
# spec file for package python-txaio
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-txaio
Version:        20.1.1
Release:        0
Summary:        WebSocket and WAMP in Python for Twisted and asyncio
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/crossbario/txaio
Source:         https://files.pythonhosted.org/packages/source/t/txaio/txaio-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
Requires:       python-six
Recommends:     python-Twisted >= 12.1.0
Recommends:     python-zope.interface >= 3.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted >= 12.1.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
WebSocket allows bidirectional real-time messaging on the Web and WAMP adds
asynchronous Remote Procedure Calls and Publish & Subscribe on top of WebSocket.

%prep
%setup -q -n txaio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_sdist'

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
