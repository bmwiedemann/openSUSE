#
# spec file for package python-nest-asyncio2
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


Name:           python-nest-asyncio2
Version:        1.7.4
Release:        0
Summary:        Patch asyncio to allow nested event loops
License:        BSD-2-Clause
URL:            https://github.com/Chaoses-Ib/nest-asyncio2
Source:         https://files.pythonhosted.org/packages/source/n/nest_asyncio2/nest_asyncio2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-nest_asyncio2 = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
By design asyncio does not allow its event loop to be nested. This presents a practical problem:
When in an environment where the event loop is already running it's impossible to run tasks and
wait for the result. Trying to do so will give the error "RuntimeError: This event loop is already
running".

The issue pops up in various environments, such as web servers, GUI applications and in Jupyter
notebooks.

This module patches asyncio to allow nested use of asyncio.run and loop.run_until_complete.

%prep
%autosetup -p1 -n nest_asyncio2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/nest_asyncio2.py
%pycache_only %{python_sitelib}/__pycache__/nest_asyncio2.*.pyc
%{python_sitelib}/nest_asyncio2[_-]%{version}.dist-info

%changelog
