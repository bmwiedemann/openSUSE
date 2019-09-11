#
# spec file for package python-scikit-umfpack
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Group:          Development/Languages/Python
Url:            https://github.com/scikit-umfpack/scikit-umfpack
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-umfpack/scikit-umfpack-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.14.3}
BuildRequires:  %{python_module scikits.example}
BuildRequires:  %{python_module scipy >= 1.0.0rc1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  openblas-devel
BuildRequires:  python-rpm-macros
BuildRequires:  suitesparse-devel
BuildRequires:  swig
# SECTION test requirements
BuildRequires:  %{python_module nose}
# /SECTION
ExcludeArch:    aarch64 ppc64 ppc64le
Requires:       python-numpy >= 1.14.3
Requires:       python-scikits.example
Requires:       python-scipy >= 1.0.0rc1
%ifpython2
Provides:       %{oldpython}-scikits-umfpack = %{version}
Obsoletes:      %{oldpython}-scikits-umfpack < %{version}
%endif

%python_subpackages

%description
The scikit-umfpack package provides wrapper of UMFPACK sparse direct solver to SciPy.

%prep
%setup -q -n scikit-umfpack-%{version}
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
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitearch}/scikits/
%{python_sitearch}/scikits/umfpack/
%{python_sitearch}/scikit_umfpack-%{version}-py*.egg-info

%changelog
