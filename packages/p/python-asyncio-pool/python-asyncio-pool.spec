#
# spec file for package python-asyncio-pool
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


Name:           python-asyncio-pool
Version:        0.6.0
Release:        0
Summary:        Pool of asyncio coroutines with familiar interface
License:        MIT
URL:            https://github.com/gistart/asyncio-pool
Source:         https://github.com/gistart/asyncio-pool/archive/refs/tags/v%{version}/asyncio-pool-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PyPI tarball does not include tests and license
#Source:         https://files.pythonhosted.org/packages/source/a/asyncio_pool/asyncio_pool-%%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Pool of asyncio coroutines with familiar interface. Supports python 3.5+ (including PyPy 6+, which is also 3.5 atm)

AioPool makes sure _no more_ and _no less_ (if possible) than `size` spawned coroutines are active at the same time. _spawned_ means created and scheduled with one of the pool interface methods, _active_ means coroutine function started executing it's code, as opposed to _waiting_ -- which waits for pool space without entering coroutine function.

%prep
%setup -q -n asyncio-pool-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/asyncio_pool
%{python_sitelib}/asyncio_pool-%{version}.dist-info
%doc examples

%changelog
