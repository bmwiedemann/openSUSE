#
# spec file for package python-pykeepass
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
Name:           python-pykeepass
Version:        3.0.3
Release:        0
Summary:        Low-level library to interact with keepass databases
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/pschmitt/pykeepass
Source:         https://github.com/pschmitt/pykeepass/archive/%{version}.tar.gz#/pykeepass-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-argon2-cffi
Requires:       python-construct >= 2.9.31
Requires:       python-future
Requires:       python-lxml
Requires:       python-pycryptodome
Requires:       python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module construct >= 2.9.31}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
This library allows you to write entries to a KeePass database

%prep
%setup -q -n pykeepass-%{version}
sed -i '1{/^#!.*env python/d}' pykeepass/pykeepass.py pykeepass/kdbx_parsing/kdbx*.py

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
# python2 seg faults after 65 successful tests
python3 setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
