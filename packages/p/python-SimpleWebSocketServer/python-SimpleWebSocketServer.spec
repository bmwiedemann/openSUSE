#
# spec file for package python-SimpleWebSocketServer
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-SimpleWebSocketServer
Version:        0.1.1
Release:        0
Summary:        A Websocket server written in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dpallot/simple-websocket-server/
Source:         https://files.pythonhosted.org/packages/source/S/SimpleWebsocketServer/SimpleWebsocketServer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Websocket Server written in Python

- RFC 6455
- TLS/SSL out of the box
- Passes Autobahn's websocket testsuite
- Support for Python 2 and 3

%prep
%setup -q -n SimpleWebSocketServer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
