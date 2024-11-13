#
# spec file for package python-psycopg
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
Name:           python-psycopg
# This needs to upgraded in lockstep with python-psycopg-c
Version:        3.2.3
Release:        0
Summary:        PostgreSQL database adapter for Python
License:        LGPL-3.0-only
URL:            https://psycopg.org/psycopg3/
Source:         https://github.com/psycopg/psycopg/archive/refs/tags/%{version}.tar.gz#/psycopg-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 49.2.0}
BuildRequires:  %{python_module wheel >= 0.37}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module typing-extensions >= 4.1}
BuildRequires:  %{python_module psycopg-c == %{version}}
# psycopg-pool has a different release schedule, version number is likely
# different
BuildRequires:  %{python_module psycopg-pool}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-psycopg-c == %{version}
Requires:       python-typing-extensions >= 4.1
Suggests:       python-dnspython >= 2.1
Suggests:       python-psycopg-pool
BuildArch:      noarch
%python_subpackages

%description
PostgreSQL database adapter for Python

%prep
%autosetup -p1 -n psycopg-%{version}

%build
pushd psycopg
%pyproject_wheel
popd

%install
pushd psycopg
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/psycopg
%{python_sitelib}/psycopg-%{version}.dist-info

%changelog
