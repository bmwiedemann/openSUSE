#
# spec file for package python-pykeepass
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


Name:           python-pykeepass
Version:        4.0.4
Release:        0
Summary:        Low-level library to interact with keepass databases
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/libkeepass/pykeepass
Source:         https://github.com/libkeepass/pykeepass/archive/refs/tags/v%{version}.tar.gz#/pykeepass-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-argon2-cffi >= 20.1.0
Requires:       python-construct >= 2.10.54
Requires:       python-future
Requires:       python-lxml >= 4.6.1
Requires:       python-pycryptodomex >= 3.10.1
Requires:       python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module argon2-cffi >= 20.1.0}
BuildRequires:  %{python_module construct >= 2.10.54}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module lxml >= 4.6.1}
BuildRequires:  %{python_module pycryptodomex >= 3.10.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
This library allows you to write entries to a KeePass database

%prep
%autosetup -p1 -n pykeepass-%{version}
sed -i '1{/^#!.*env python/d}' pykeepass/{pykeepass,deprecated,kdbx_parsing/kdbx*}.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONDONTWRITEBYTECODE=1
%python_exec tests/tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pykeepass/
%{python_sitelib}/pykeepass-%{version}-py%{python_version}.egg-info/

%changelog
