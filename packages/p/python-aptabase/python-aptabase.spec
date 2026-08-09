#
# spec file for package python-aptabase
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-aptabase
Version:        0.1.0
Release:        0
Summary:        Python SDK for Aptabase
License:        MIT
URL:            https://github.com/aptabase/aptabase-python
Source:         https://files.pythonhosted.org/packages/source/a/aptabase/aptabase-%{version}.tar.gz
Patch1:         fix-test-sdk-version.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-httpx}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  fdupes
Requires:       %{pythons}-base
Requires:       %{pythons}-httpx >= 0.28.1
BuildArch:      noarch
%python_subpackages

%description
Python SDK for Aptabase - privacy-first analytics for mobile, desktop and web applications.

%prep
%autosetup -p1 -n aptabase-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/aptabase
%{python_sitelib}/aptabase-%{version}.dist-info

%changelog
