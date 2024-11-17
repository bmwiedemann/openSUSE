#
# spec file for package python-unyt
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
Name:           python-unyt
Version:        3.0.3
Release:        0
Summary:        A package for handling numpy arrays with units
License:        BSD-3-Clause
URL:            https://github.com/yt-project/unyt
Source:         https://files.pythonhosted.org/packages/source/u/unyt/unyt-%{version}.tar.gz
# PATCH-FIX-UPSTREAM unyt-pr512-np2.1.patch gh#yt-project/unyt#512
Patch0:         https://github.com/yt-project/unyt/pull/512.patch#/unyt-pr512-np2.1.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module dask-diagnostics}
BuildRequires:  %{python_module numpy >= 1.19.3 with %python-numpy < 3}
BuildRequires:  %{python_module packaging >= 20.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sympy >= 1.7}
# /SECTION
Requires:       (python-numpy >= 1.19.3 with python-numpy < 3)
Requires:       python-packaging > 20.9
Requires:       python-sympy >= 1.7
BuildArch:      noarch
%python_subpackages

%description
A package for handling numpy arrays with units.

Often writing code that deals with data that has units can be confusing. A
function might return an array but at least with plain NumPy arrays, there is no
way to easily tell what the units of the data are without somehow knowing *a
priori*.

%prep
%autosetup -p1 -n unyt-%{version}
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc *.rst
%license LICENSE
%{python_sitelib}/unyt
%{python_sitelib}/unyt-%{version}.dist-info

%changelog
