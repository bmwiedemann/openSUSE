#
# spec file for package python-siosocks
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
Name:           python-siosocks
Version:        0.1.0
Release:        0
Summary:        Sans-io socks proxy client/server with couple io backends
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pohmelie/siosocks
Source:         https://files.pythonhosted.org/packages/source/s/siosocks/siosocks-%{version}.tar.gz
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module trio}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-trio
BuildArch:      noarch
%python_subpackages

%description
Sans-io (https://sans-io.readthedocs.io/) socks 4/5 client/server library/framework.

# Reasons
* No one-shot socks servers
* Sans-io
* asyncio-ready twunnel3 (https://github.com/jvansteirteghem/twunnel3) is dead
* aiosocks (https://github.com/nibrag/aiosocks) do not mimic `asyncio.open_connection` arguments (maybe dead too)
* Fun

# Features
* Only tcp connect (no bind, no udp)
* Both client and server
* Socks versions: 4, 4a, 5
* Socks5 auth: no auth, username/password
* Couple io backends: asyncio, trio, socketserver
* One-shot socks server (`python -m siosocks`)

%prep
%setup -q -n siosocks-%{version}

%build
%python_build

%check
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc readme.md
%license license.txt
%{python_sitelib}/*

%changelog
