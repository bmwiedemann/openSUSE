#
# spec file for package python-aiohttp_cors
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-aiohttp_cors
Version:        0.8.1
Release:        0
Summary:        Asynchronous HTTP client/server framework
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp-cors
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp-cors/aiohttp_cors-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.9
Suggests:       %{name}-doc
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 3.9}
BuildRequires:  %{python_module pytest-aiohttp >= 0.3.0}
BuildRequires:  %{python_module pytest}
BuildArch:      noarch
%python_subpackages

%description
Asynchronous HTTP client/server framework for Python.

- Supports both the client and server side of HTTP protocol.
- Supports both client and server WebSockets out-of-the-box.
- Web-server has middleware and pluggable routing.

%prep
%autosetup -p1 -n aiohttp_cors-%{version}
# remove code coverage flags from pytest
sed -i '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --asyncio-mode=auto tests/unit

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/aiohttp_cors
%{python_sitelib}/aiohttp_cors-%{version}.dist-info

%changelog
