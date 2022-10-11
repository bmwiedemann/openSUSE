#
# spec file for package python-pytest-aiohttp
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
%define skip_python2 1
%define pyname pytest-aiohttp
Name:           python-pytest-aiohttp
Version:        1.0.4
Release:        0
Summary:        Python pytest plugin for aiohttp support
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/pytest-aiohttp
Source:         https://files.pythonhosted.org/packages/source/p/pytest-aiohttp/pytest-aiohttp-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.8.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 2.3.5
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
The library allows to use aiohttp pytest plugin without need for implicitly loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%prep
%setup -q -n %{pyname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# there are no tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
