#
# spec file for package python-scikit-umfpack
#
# Copyright (c) 2022 SUSE LLC
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
%define         oldpython python
Name:           python-scikit-umfpack
Version:        0.3.2
Release:        0
Summary:        Python interface to UMFPACK sparse direct solver
License:        BSD-3-Clause
URL:            https://github.com/scikit-umfpack/scikit-umfpack
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-umfpack/scikit-umfpack-%{version}.tar.gz
Patch0:         do-not-use-numpy-decorators.patch
# PATCH-FIX-UPSTREAM scikit-umfpack-pr68-scipy-sparse-linalg.patch -- gh#scikit-umfpack/scikit-umfpack68
Patch1:         scikit-umfpack-pr68-scipy-sparse-linalg.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.14.3}
BuildRequires:  %{python_module scipy >= 1.0.0rc1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  openblas-devel
BuildRequires:  python-rpm-macros
BuildRequires:  suitesparse-devel
BuildRequires:  swig
Requires:       python-numpy >= 1.14.3
Requires:       python-scipy >= 1.0.0rc1
ExclusiveArch:  x86_64
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%ifpython2
Provides:       %{oldpython}-scikits-umfpack = %{version}
Obsoletes:      %{oldpython}-scikits-umfpack < %{version}
%endif
%python_subpackages

%description
The scikit-umfpack package provides wrapper of UMFPACK sparse direct solver to SciPy.

%prep
%setup -q -n scikit-umfpack-%{version}
%autopatch -p1
sed -i -e '/^#!\//, 1d' scikits/umfpack/setup.py
sed -i -e '/^#!\//, 1d' scikits/umfpack/tests/try_umfpack.py

%build
export LANG=en_US.UTF-8
export CFLAGS="%{optflags}"
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand rm %{buildroot}%{$python_sitearch}/scikits/__init__.py*
%python_expand rm %{buildroot}%{$python_sitearch}/MANIFEST.in
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG=en_US.UTF-8
export CFLAGS="%{optflags}"
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitearch}/scikits/
%{python_sitearch}/scikits/umfpack/
%{python_sitearch}/scikit_umfpack-%{version}*-info

%changelog
