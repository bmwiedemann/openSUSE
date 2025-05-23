#
# spec file for package python-aiohttp-jinja2
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
Name:           python-aiohttp-jinja2
Version:        1.6
Release:        0
Summary:        Jinja2 template renderer for aiohttp.web
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/aiohttp-jinja2
Source:         https://github.com/aio-libs/aiohttp-jinja2/archive/v%{version}.tar.gz#/aiohttp-jinja2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 3.0
Requires:       python-aiohttp
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 3.0}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
%python_subpackages

%description
Jinja2 template renderer for aiohttp.web.

%prep
%autosetup -p1 -n aiohttp-jinja2-%{version}

# for unwanted pytest extra configuration
rm setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/aiohttp_jinja2
%{python_sitelib}/aiohttp_jinja2-%{version}*-info

%changelog
