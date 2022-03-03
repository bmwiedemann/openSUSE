#
# spec file for package python-pytest-httpx
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
Name:           python-pytest-httpx
Version:        0.20.0
Release:        0
Summary:        Send responses to httpx
License:        MIT
URL:            https://colin-b.github.io/pytest_httpx/
Source:         https://github.com/Colin-b/pytest_httpx/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module httpx >= 0.22.0}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.14.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-httpx >= 0.22.0
Requires:       python-pytest >= 6.0
BuildArch:      noarch
%python_subpackages

%description
Send responses to httpx.

%prep
%setup -q -n pytest_httpx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/*

%changelog
