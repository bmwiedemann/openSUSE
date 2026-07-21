#
# spec file for package python-openqa-async
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global         skip_python311 1
%global         skip_python312 1
Name:           python-openqa-async
Version:        1.0.0
Release:        0
Summary:        Client library for openQA with async support
License:        GPL-2.0-or-later
URL:            https://pypi.org/project/openqa-async/
Source:         https://github.com/mimi1vx/openqa-async/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.13}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6
Requires:       python-httpx >= 0.28.1
BuildArch:      noarch
BuildRequires:  %{python_module PyYAML >= 6}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module respx}

%python_subpackages

%description
A client for the openQA API based on httpx, providing both synchronous
and asynchronous interfaces.

%prep
%autosetup -p1 -n openqa-async-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitelib}/openqa_async
%{python_sitelib}/openqa_async-%{version}.dist-info

%changelog
