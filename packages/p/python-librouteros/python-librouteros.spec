#
# spec file for package python-librouteros
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017-2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-librouteros
Version:        3.4.1
Release:        0
Summary:        Python implementation of MikroTik RouterOS API
License:        GPL-2.0-or-later
URL:            https://github.com/luqasz/librouteros
Source:         https://github.com/luqasz/librouteros/archive/%{version}.tar.gz#/librouteros-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
# /SECTION
Requires:       python-toml
%python_subpackages

%description
Python implementation of MikroTik RouterOS API.
http://wiki.mikrotik.com/wiki/API

%prep
%autosetup -p1 -n librouteros-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Broken test upstream
%pytest -k 'not test_rawCmd_calls_writeSentence' tests/unit

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/librouteros
%{python_sitelib}/librouteros-%{version}.dist-info

%changelog
