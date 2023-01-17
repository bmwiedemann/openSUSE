#
# spec file for package python-pytest-httpx
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


Name:           python-pytest-httpx
Version:        0.21.2
Release:        0
Summary:        Send responses to httpx
License:        MIT
URL:            https://colin-b.github.io/pytest_httpx/
Source:         https://github.com/Colin-b/pytest_httpx/archive/refs/tags/v%{version}.tar.gz#/pytest_httpx-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module httpx >= 0.23.0}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.20.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-httpx >= 0.23.0
Requires:       python-pytest >= 6.0
BuildArch:      noarch
%python_subpackages

%description
Send responses to httpx.

%prep
%setup -q -n pytest_httpx-%{version}
# unpin exact version
sed -i '/install_requires/ s/httpx==0.23.\*/httpx/' setup.py
sed -i '/install_requires/ s/pytest>=6.*,<8.\*/pytest/' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/pytest_httpx
%{python_sitelib}/pytest_httpx-%{version}*-info

%changelog
