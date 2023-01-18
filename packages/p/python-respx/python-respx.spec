#
# spec file for package python-respx
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-respx
Version:        0.20.1
Release:        0
Summary:        Mock HTTPX with request patterns and response side effects
License:        BSD-3-Clause
URL:            https://github.com/lundberg/respx
Source0:        https://github.com/lundberg/respx/archive/refs/tags/%{version}.tar.gz#/respx-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python library to mock httpx with request patterns and responses

%prep
%autosetup -p1 -n respx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --asyncio-mode=auto

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/respx-%{version}-py*.egg-info
%{python_sitelib}/respx

%changelog
