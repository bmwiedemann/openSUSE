#
# spec file for package python-raven-aiohttp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-raven-aiohttp
Version:        0.7.0
Release:        0
Summary:        Asyncio transport for raven-python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/raven-aiohttp
Source:         https://github.com/getsentry/raven-aiohttp/archive/%{version}.tar.gz#/raven-aiohttp-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 2.0
Requires:       python-raven >= 5.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 2.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module raven >= 5.4.0}
# /SECTION
%python_subpackages

%description
An asyncio transport for raven-python.

%prep
%setup -q -n raven-aiohttp-%{version}
rm setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
