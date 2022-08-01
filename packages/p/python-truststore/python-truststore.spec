#
# spec file for package python-truststore
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


%define skip_python2 1
%define skip_python38 1
%define skip_python39 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-truststore
Version:        0.4.0
Release:        0
Summary:        Verify certificates using OS trust stores
License:        MIT
URL:            https://github.com/sethmlarson/truststore
Source:         https://github.com/sethmlarson/truststore/archive/refs/tags/v%{version}.tar.gz#/truststore-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM no-network-testing.patch bsc#[0-9]+ mcepl@suse.com
# skip tests requiring network access
Patch0:         no-network-testing.patch
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Verify certificates using OS trust stores. Supports macOS,
Windows, and Linux (with OpenSSL). This project should be
considered experimental.

%prep
%autosetup -p1 -n truststore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -s -k 'not network'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/truststore
%{python_sitelib}/truststore-%{version}*-info

%changelog
