#
# spec file for package python-pykeepass
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-pykeepass
Version:        4.0.0
Release:        0
Summary:        Low-level library to interact with keepass databases
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/libkeepass/pykeepass
Source:         https://github.com/libkeepass/pykeepass/archive/%{version}.tar.gz#/pykeepass-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-pykeepass-fix-version.patch badshah400@gmail.com -- Fix version so that egg-infos don't end up with the wrong version; patch taken from upstream commit
Patch0:         python-pykeepass-fix-version.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-argon2-cffi
Requires:       python-construct >= 2.10.54
Requires:       python-future
Requires:       python-lxml
Requires:       python-pycryptodomex >= 3.6.2
Requires:       python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module construct >= 2.10.54}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pycryptodomex >= 3.6.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
This library allows you to write entries to a KeePass database

%prep
%autosetup -p1 -n pykeepass-%{version}
sed -i '1{/^#!.*env python/d}' pykeepass/pykeepass.py pykeepass/kdbx_parsing/kdbx*.py

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
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
