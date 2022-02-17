#
# spec file for package python-matrix-nio
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-matrix-nio
Version:        0.19.0
Release:        0
Summary:        A Python Matrix client library, designed according to sans I/O principles
License:        ISC
URL:            https://github.com/poljar/matrix-nio
Source:         https://files.pythonhosted.org/packages/source/m/matrix-nio/matrix-nio-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module aiofiles >= 0.6.0}
BuildRequires:  %{python_module aiohttp >= 3.7.4}
BuildRequires:  %{python_module aiohttp-socks >= 0.7.0}
BuildRequires:  %{python_module future >= 0.18.2}
BuildRequires:  %{python_module h11 >= 0.12.0}
BuildRequires:  %{python_module h2 >= 4.0.0}
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module Logbook >= 1.5.3}
BuildRequires:  %{python_module pycryptodome >= 3.10.1}
BuildRequires:  %{python_module unpaddedbase64 >= 2.1.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-aiofiles >= 0.6.0
Requires:       python-aiohttp >= 3.7.4
Requires:       python-aiohttp-socks >= 0.7.0
Requires:       python-future >= 0.18.2
Requires:       python-h11 >= 0.12.0
Requires:       python-h2 >= 4.0.0
Requires:       python-jsonschema >= 3.2.0
Requires:       python-Logbook >= 1.5.3
Requires:       python-pycryptodome >= 3.10.1
Requires:       python-unpaddedbase64 >= 2.1.0
Suggests:       python-dataclasses >= 0.7
Suggests:       python-python-olm >= 3.1.3
Suggests:       python-peewee >= 3.14.4
Suggests:       python-cachetools >= 4.2.1
Suggests:       python-atomicwrites >= 1.4.0
BuildArch:      noarch
%python_subpackages

%description
A Python Matrix client library, designed according to sans I/O principles.

%prep
%autosetup -p1 -n matrix-nio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
