#
# spec file for package python-pychm
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


%define pkgname pychm
%{?sle15_python_module_pythons}
Name:           python-%{pkgname}
Version:        0.8.6
Release:        0
Summary:        Python package to handle CHM files
License:        GPL-2.0-or-later
URL:            https://github.com/dottedmag/pychm
Source0:        https://files.pythonhosted.org/packages/source/p/pychm/pychm-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  chmlib-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  swig
%python_subpackages

%description
The chm package provides three modules, chm, chmlib and extra, which
provide access to the API implemented by the C library chmlib and some
additional classes and functions. They are used to access MS-ITSS encoded
files - Compressed Html Help files (.chm).

%prep
%setup -q -n %{pkgname}-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}

%files %{python_files}
%license COPYING
%doc README
%{python_sitearch}/chm
%{python_sitearch}/pychm-%{version}*-info

%changelog
