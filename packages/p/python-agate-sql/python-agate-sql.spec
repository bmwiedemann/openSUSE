#
# spec file for package python-agate-sql
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
Name:           python-agate-sql
Version:        0.7.2
Release:        0
Summary:        SQL read/write support for agate
License:        MIT
Group:          Development/Languages/Python
URL:            https://agate-sql.readthedocs.org/
Source:         https://github.com/wireservice/agate-sql/archive/%{version}.tar.gz
# we do not have crate dialect
Patch0:         python-agate-sql-no-crate.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy
Requires:       python-agate >= 1.5.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Agate-sql adds SQL read/write support to agate.

%prep
%autosetup -p1 -n agate-sql-%{version}

sed -i -e '/^#!\//, 1d' agatesql/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst CHANGELOG.rst
%license COPYING
%{python_sitelib}/agatesql
%{python_sitelib}/agate_sql-%{version}.dist-info

%changelog
