#
# spec file for package python-openTSNE
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
Name:           python-openTSNE
Version:        1.0.2
Release:        0
Summary:        Extensible, parallel implementations of t-SNE
License:        BSD-3-Clause
URL:            https://github.com/pavlin-policar/openTSNE
# tests are not packaged in the PyPI sdist, use GitHub instead
Source:         %{url}/archive/v%{version}.tar.gz#/openTSNE-%{version}-gh.tar.gz
Patch0:         python-openTSNE-disable-CPU-autodetection.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel >= 1.16.6}
BuildRequires:  %{python_module scikit-learn >= 0.20}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-numpy >= 1.16.6
Requires:       python-scikit-learn >= 0.20
Requires:       python-scipy
Suggests:       python-hnswlib
Suggests:       python-pynndescent
Provides:       python-fastTSNE = %{version}
Obsoletes:      python-fastTSNE < %{version}
%python_subpackages

%description
Extensible, parallel implementations of t-SNE

%prep
%autosetup -p1 -n openTSNE-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%ifarch %ix86 %arm32 aarch64 riscv64 s390x
# precision errors
%define donttest -k "not TestTSNECorrectnessUsingPrecomputedDistanceMatrix"
%endif
%pytest_arch --import-mode append %{?donttest}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/openTSNE
%{python_sitearch}/openTSNE-%{version}*-info

%changelog
