#
# spec file for package python-psycopg-c
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


%{?sle15_python_module_pythons}
Name:           python-psycopg-c
# This needs to upgraded in lockstep with python-psycopg
Version:        3.2.3
Release:        0
Summary:        PostgreSQL database adapter for Python -- C optimisation distribution
License:        LGPL-3.0-only
URL:            https://psycopg.org/psycopg3/
Source:         https://files.pythonhosted.org/packages/source/p/psycopg-c/psycopg_c-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 49.2.0}
BuildRequires:  %{python_module tomli >= 2.0.1}
BuildRequires:  %{python_module wheel >= 0.37}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  postgresql17-server-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
PostgreSQL database adapter for Python -- C optimisation distribution

%prep
%autosetup -p1 -n psycopg_c-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Tested in python-psycopg

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/psycopg_c
%{python_sitearch}/psycopg_c-%{version}.dist-info

%changelog
