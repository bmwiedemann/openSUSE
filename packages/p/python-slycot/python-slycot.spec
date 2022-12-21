#
# spec file for package python-slycot
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


Name:           python-slycot
Version:        0.5.3
Release:        0
Summary:        A wrapper for the SLICOT control and systems library
License:        BSD-3-Clause AND GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/python-control/Slycot
Source0:        https://files.pythonhosted.org/packages/source/s/slycot/slycot-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build >= 0.15}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 7.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  blas-devel
BuildRequires:  cmake >= 3.14
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Slycot is a wrapper for the SLICOT control and systems library.

%prep
%setup -q -n slycot-%{version}
cp slycot/src/SLICOT-Reference/LICENSE LICENSE-SLICOT

%build
export CFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
export CMAKE_GENERATOR="Unix Makefiles"
# openblas-devel is pulled in by numpy-devel, but we link against the
# generic BLAS/LAPACK binaries so that update-alternatives can choose
# the implementation for runtime.
export BLA_VENDOR="Generic"
%{python_expand # give the pep517 build the correct f2py flavor as "f2py3"
mkdir -p build/buildbin
ln -s %{_bindir}/f2py-%{$python_bin_suffix} build/buildbin/f2py3
}
export PATH=$PWD/build/buildbin:$PATH
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG="en_US.UTF-8"
%ifarch ppc64 ppc64le
  %define skiptest -k "not (test_tb05ad_ or test_sg03ad_ex)"
%endif
%pytest_arch --pyargs slycot %{?skiptest}

%files %{python_files}
%doc README.rst
%license COPYING LICENSE-SLICOT
%{python_sitearch}/slycot
%{python_sitearch}/slycot-%{version}.dist-info

%changelog
