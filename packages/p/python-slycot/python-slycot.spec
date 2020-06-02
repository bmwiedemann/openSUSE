#
# spec file for package python-slycot
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


%if 0%{?sle_version} == 120300 && !0%{?is_opensuse}
  %bcond_with openblas
%else
 %ifarch armv6l s390 s390x m68k riscv64
  %bcond_with openblas
 %else
  %bcond_without openblas
 %endif
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
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
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-fortran
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-configparser
%endif
%if %{with openblas}
BuildRequires:  openblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%endif
Requires:       python-numpy
%python_subpackages

%description
Slycot is a wrapper for the SLICOT control and systems library.

%prep
%setup -q -n slycot-%{version}

%build
export CFLAGS="%{optflags}"
%python_build --generator "Unix Makefiles"

%install
%python_expand %{$python_install} --install-lib %{$python_sitearch} --generator "Unix Makefiles"
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG="en_US.UTF-8"
# avoid leading empty path entry introduced by %%pytest_arch
export PYTHONPATH=/nonexistent
%pytest_arch --pyargs slycot

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitearch}/slycot
%{python_sitearch}/slycot-%{eggversion}-py*.egg-info

%changelog
