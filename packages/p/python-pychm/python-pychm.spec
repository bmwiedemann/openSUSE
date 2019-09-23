#
# spec file for package python-pychm
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python3 1
%define pkgname pychm
Name:           python-%{pkgname}
Version:        0.8.4.1
Release:        0
Summary:        Python package to handle CHM files
License:        GPL-2.0+
Group:          Development/Libraries/Python
Url:            https://github.com/dottedmag/pychm
Source0:        https://files.pythonhosted.org/packages/source/p/pychm/pychm-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  chmlib-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  swig
%ifpython2
Provides:       python-PyCHM = %{version}
Provides:       python-pychm = %{version}
Obsoletes:      python-PyCHM <= %{version}
Obsoletes:      python-pychm <= %{version}
%endif
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
%python_build

%install
%python_install
%fdupes %{buildroot}

%files %{python_files}
%doc COPYING README
%{python_sitearch}/*

%changelog
