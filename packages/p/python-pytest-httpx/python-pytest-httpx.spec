#
# spec file for package python-pytest-httpx
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
Name:           python-pytest-httpx
Version:        0.35.0
Release:        0
Summary:        Send responses to httpx
License:        MIT
URL:            https://colin-b.github.io/pytest_httpx/
Source:         https://github.com/Colin-b/pytest_httpx/archive/refs/tags/v%{version}.tar.gz#/pytest_httpx-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module httpx >= 0.28.0 with %python-httpx < 0.29}
BuildRequires:  %{python_module pytest >= 8.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.24.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 8.0
Requires:       (python-httpx >= 0.28.0 with python-httpx < 0.29)
BuildArch:      noarch
%python_subpackages

%description
Send responses to httpx.

%prep
%setup -q -n pytest_httpx-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/pytest_httpx
%{python_sitelib}/pytest_httpx-%{version}.dist-info

%changelog
