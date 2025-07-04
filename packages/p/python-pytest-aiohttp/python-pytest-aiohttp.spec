#
# spec file for package python-pytest-aiohttp
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
Name:           python-pytest-aiohttp
Version:        1.1.0
Release:        0
Summary:        Python pytest plugin for aiohttp support
License:        Apache-2.0
URL:            https://github.com/aio-libs/pytest-aiohttp
Source:         https://files.pythonhosted.org/packages/source/p/pytest-aiohttp/pytest_aiohttp-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.8.1}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.1.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.20.2}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.8.1
Requires:       python-pytest >= 6.1.0
Requires:       python-pytest-asyncio >= 0.20.2
BuildArch:      noarch
%python_subpackages

%description
A library that provides fixtures for creation test aiohttp server and client.

%prep
%autosetup -p1 -n pytest_aiohttp-%{version}
cat >pytest.ini <<EOF
[pytest]
asyncio_mode=auto
asyncio_default_fixture_loop_scope=function
EOF

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_aiohttp
%{python_sitelib}/pytest_aiohttp-%{version}.dist-info

%changelog
