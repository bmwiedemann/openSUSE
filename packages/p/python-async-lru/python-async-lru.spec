#
# spec file for package python-async-lru
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-async-lru
Version:        2.0.5
Release:        0
Summary:        Simple LRU cache for asyncio
License:        MIT
URL:            https://github.com/aio-libs/async-lru
Source:         https://files.pythonhosted.org/packages/source/a/async_lru/async_lru-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#aio-libs/async-lru#637
Patch0:         support-python-314.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-async_lru = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This package is a port of Python's built-in functools.lru_cache function for asyncio.
To better handle async behaviour, it also ensures multiple concurrent calls will only
result in 1 call to the wrapped function, with all awaits receiving the result of that
call when it completes.

%prep
%autosetup -p1 -n async_lru-%{version}
sed -i /addopts/d setup.cfg

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
%{python_sitelib}/async_lru
%{python_sitelib}/async_lru-%{version}.dist-info

%changelog
