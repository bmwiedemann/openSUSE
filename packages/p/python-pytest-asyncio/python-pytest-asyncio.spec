#
# spec file for package python-pytest-asyncio
#
# Copyright (c) 2020 SUSE LLC
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
%{?!python_module:%define python_module() python3-%{**}}
Name:           python-pytest-asyncio
Version:        0.12.0
Release:        0
Summary:        Pytest support for asyncio
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source:         https://github.com/pytest-dev/pytest-asyncio/archive/v%{version}.tar.gz#./pytest-asyncio-%{version}.tar.gz
BuildRequires:  %{python_module async_generator >= 1.3}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module hypothesis >= 5.7.1}
BuildRequires:  %{python_module pytest >= 5.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 5.4.0
BuildArch:      noarch
%python_subpackages

%description
pytest-asyncio is a Python library used for testing asyncio code with pytest.

asyncio code is usually written in the form of coroutines, which makes it
slightly more difficult to test using normal testing tools. pytest-asyncio
provides useful fixtures and markers to make testing easier.

%prep
%setup -q -n pytest-asyncio-%{version}
sed -ie '1i# -*- coding: utf-8 -*-' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# remove pytest config to not error out on deprecations
rm setup.cfg
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
