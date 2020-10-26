#
# spec file for package python-llvmlite
#
# Copyright (c) 2020 SUSE LLC
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


%define modname llvmlite
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         llvm_major 10
%if 0%{?suse_version} <= 1500
%define         llvm_major 7
%endif
%define skip_python2 1
Name:           python-llvmlite
Version:        0.32.0
Release:        0
Summary:        Lightweight wrapper around basic LLVM functionality
License:        BSD-2-Clause
URL:            http://llvmlite.pydata.org
Source:         https://github.com/numba/llvmlite/archive/v%{version}.tar.gz#/llvmlite-%{version}.tar.gz
Patch0:         support-clang9.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libstdc++-devel
BuildRequires:  llvm%{llvm_major}-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A lightweight LLVM python binding for writing JIT compilers

The old llvmpy  binding exposes a lot of LLVM APIs but the mapping of
C++-style memory management to Python is error prone. Numba_ and many JIT
compilers do not need a full LLVM API.  Only the IR builder, optimizer,
and JIT compiler APIs are necessary.

llvmlite is a project originally tailored for Numba's needs, using the
following approach:

* A small C wrapper around the parts of the LLVM C++ API we need that are
  not already exposed by the LLVM C API.
* A ctypes Python wrapper around the C API.
* A pure Python implementation of the subset of the LLVM IR builder that we
  need for Numba.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1

%build
export CPPFLAGS="-fPIC"
export LLVM_CONFIG=%{_bindir}/llvm-config
%python_build

%install
%python_expand $python setup.py install --prefix=%{_prefix} --root=%{buildroot} --install-lib=%{$python_sitearch}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir tester
pushd tester
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
rm -rf _build.* build
$python -m llvmlite.tests -vb
}
popd

%files %{python_files}
%license LICENSE
%doc README.rst
%doc examples/
%{python_sitearch}/llvmlite/
%{python_sitearch}/llvmlite-%{version}-*.egg-info

%changelog
