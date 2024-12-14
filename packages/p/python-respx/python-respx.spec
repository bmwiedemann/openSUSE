#
# spec file for package python-respx
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
Name:           python-respx
Version:        0.21.1
Release:        0
Summary:        Mock HTTPX with request patterns and response side effects
License:        BSD-3-Clause
URL:            https://github.com/lundberg/respx
Source0:        https://github.com/lundberg/respx/archive/refs/tags/%{version}.tar.gz#/respx-%{version}.tar.gz
# PATCH-FIX-UPSTREAM respx-pr267-httpx0.28.patch gh#lundberg/respx#267
Patch0:         respx-pr267-httpx0.28.patch
# PATCH-FIX-UPSTREAM respx-pr278-httpx0.28.patch gh#lundberg/respx#278
Patch1:         respx-pr278-httpx0.28.patch
BuildRequires:  %{python_module Flask}
# >= 0.28 for tests because of the Patches
BuildRequires:  %{python_module httpx >= 0.28}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpx >= 0.21
BuildArch:      noarch
%python_subpackages

%description
Python library to mock httpx with request patterns and responses

%prep
%autosetup -p1 -n respx-%{version}
sed -i '/--cov/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rfE

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/respx-%{version}.dist-info
%{python_sitelib}/respx

%changelog
