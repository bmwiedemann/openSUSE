#
# spec file for package python-slycot
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
%define skip_python36 1
%define eggversion 0.4.0
Name:           python-slycot
Version:        0.4.0.0
Release:        0
Summary:        A wrapper for the SLICOT control and systems library
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/python-control/Slycot
Source:         https://files.pythonhosted.org/packages/source/s/slycot/slycot-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  blas-devel
BuildRequires:  cmake >= 3.11
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy
%python_subpackages

%description
Slycot is a wrapper for the SLICOT control and systems library.

%prep
%setup -q -n slycot-%{version}

%build
export CFLAGS="%{optflags}"
# openblas-devel is pulled in by numpy-devel, but we link against the
# generic BLAS/LAPACK binaries so that update-alternatives can choose
# the implementation for runtime.
%python_build --generator "Unix Makefiles" -DBLA_VENDOR="Generic"

%install
# scikit-build installs into sitelib instead of platlib
%python_expand %{$python_install} --install-lib %{$python_sitearch} --generator "Unix Makefiles"
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG="en_US.UTF-8"
%ifarch ppc64 ppc64le
  %define skiptest -k "not (test_tb05ad_ or test_sg03ad_ex)"
%endif
%pytest_arch --pyargs slycot %{?skiptest}

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitearch}/slycot
%{python_sitearch}/slycot-%{eggversion}*-info

%changelog
