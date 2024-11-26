#
# spec file for package python-legacycrypt
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-legacycrypt
Version:        0.3
Release:        0
Summary:        Wrapper to the POSIX crypt library call and associated functionality
License:        Python-2.0
URL:            https://github.com/tiran/legacycrypt
Source:         https://files.pythonhosted.org/packages/source/l/legacycrypt/legacycrypt-%{version}.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The legacycrypt module is a standalone version of
https://docs.python.org/3/library/crypt.html

This module implements an interface to the crypt(3) routine, which is a
one-way hash function based upon a modified DES algorithm; see the Unix man
page for further details. Possible uses include storing hashed passwords so
you can check passwords without storing the actual password, or attempting
to crack Unix passwords with a dictionary.

Notice that the behavior of this module depends on the actual
implementation of the crypt(3) routine in the running system. Therefore,
any extensions available on the current implementation will also be
available on this module.

%prep
%autosetup -p1 -n legacycrypt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_types' tests.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/legacycrypt.py
%pycache_only %{python_sitelib}/__pycache__/legacycrypt.*.pyc
%{python_sitelib}/legacycrypt-%{version}.dist-info

%changelog
