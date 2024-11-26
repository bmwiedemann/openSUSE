#
# spec file for package python-aiohttp-socks
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


%{?sle15_python_module_pythons}
Name:           python-aiohttp-socks
Version:        0.9.1
Release:        0
Summary:        SOCKS proxy connector for aiohttp
License:        Apache-2.0
URL:            https://github.com/romis2012/aiohttp-socks
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp_socks/aiohttp_socks-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 2.3.2
Requires:       python-attrs >= 19.2.0
Requires:       python-python-socks >= 2.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 2.3.2}
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module attrs >= 1.0.1}
BuildRequires:  %{python_module python-socks >= 2.0.0}
# /SECTION
%python_subpackages

%description
SOCKS proxy connector for aiohttp

%prep
%autosetup -p1 -n aiohttp_socks-%{version}
dos2unix README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests need access to the internet
#%%pytest

# so try at least a simple import
%python_exec -c 'from aiohttp_socks import ProxyConnector'

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/aiohttp_socks
%{python_sitelib}/aiohttp_socks-%{version}*-info

%changelog
