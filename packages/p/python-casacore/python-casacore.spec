#
# spec file for package python-casacore
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


# libboost_python3-devel (libbost_python-py3-*) is for the primary python3 flavor only
%define pythons python3
%global modname casacore
Name:           python-casacore
Version:        3.5.1
Release:        0
Summary:        A wrapper around CASACORE, the radio astronomy library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/casacore/python-casacore
Source:         https://github.com/casacore/python-casacore/archive/refs/tags/v%{version}.tar.gz#/python-casacore-%{version}-gh.tar.gz
BuildRequires:  %{python_module configargparse}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  casacore-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_python3-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(wcslib)
Requires:       python-configargparse
Requires:       python-future
Requires:       python-numpy
Requires:       python-six
ExcludeArch:    %ix86
%python_subpackages

%description
A python wrapper around CASACORE, the radio astronomy library

%prep
%setup -q -n python-casacore-%{version}
# empty file masking the module directory
rm pyrap/images.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# old python-rpm-macros for SLE/Leap: don't import casacore from current source dir
mv casacore casacore.tmp
# TestImage needs to use data files that are no longer available upstream
# TestTable tries to write to tmp dir and fails during build due to perm issues
%pytest_arch -k 'not (TestImage or TestTable)'
mv casacore.tmp casacore

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/%{modname}/
%{python_sitearch}/pyrap/
%{python_sitearch}/python_%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
