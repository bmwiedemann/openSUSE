#
# spec file for package python-psycopg2cffi
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-psycopg2cffi
Version:        2.9.0
Release:        0
Summary:        Implementation of the psycopg2 module using cffi
License:        LGPL-3.0-or-later
URL:            https://github.com/chtd/psycopg2cffi
Source:         https://files.pythonhosted.org/packages/source/p/psycopg2cffi/psycopg2cffi-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE allow-rc-versions.patch to allow 15rc2 pg version
Patch0:         allow-rc-versions.patch
BuildRequires:  %{python_module devel >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  postgresql-server-devel
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.0
Requires:       python-six
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
This is a implementation of the psycopg2 module using cffi.

%prep
%autosetup -p1 -n psycopg2cffi-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -r %{buildroot}%{$python_sitearch}/psycopg2cffi/tests
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
rm psycopg2cffi/tests/__init__.py
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/psycopg2cffi
%{python_sitearch}/psycopg2cffi-%{version}*-info

%changelog
