#
# spec file for package python-pyginac
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


%define skip_python2 1
%global modname pyginac
Name:           python-pyginac
Version:        1.5.5
Release:        0
Summary:        Python bindings for ginac - a symbolic manipulation library
License:        GPL-2.0-only
URL:            http://moebinv.sourceforge.net/pyGiNaC.html
Source:         https://download.sf.net/pyginac.moebinv.p/%{modname}_%{version}.orig.tar.gz
# PATCH-FEATURE-OPENSUSE pyginac-makefile-fix.patch badshah400@gmail.com -- In the lack of a proper configuring tool, we patch the Makefile appropriately to fix installation paths
Patch0:         pyginac-makefile-fix.patch
# PATCH-FIX-UPSTREAM pyginac-python38.patch badshah400@gmail.com -- Fix build with python 3.8, patch taken from upstream (commit b4848e)
Patch1:         pyginac-python38.patch
BuildRequires:  gcc-c++
BuildRequires:  ginac-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module Cython}

%python_subpackages

%description
PyGiNaC is a Python package that provides an interface to the C++ library
GiNaC, which is an open framework for symbolic computation within C++. PyGiNaC
is implemented with the help of the Boost.Python library.

%package devel
Summary:        Headers and pkgconfig file for pyginac
Requires:       python-%{modname} = %{version}

%description devel
PyGiNaC is a Python package that provides an interface to the C++ library
GiNaC, which is an open framework for symbolic computation within C++. PyGiNaC
is implemented with the help of the Boost.Python library.

This package provides the header and pkgconfig file used when developing against
pyginac.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%make_build

%install
%make_install

mv %{buildroot}%{_prefix}/lib/python3 %{buildroot}%{_prefix}/lib/python%{python_version}
if [[ "%{_lib}" != 'lib' ]]
then
  mkdir -p %{buildroot}%{_libdir}
  mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}/
fi

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python_sitearch}
%python_exec bin/checkall.py

%files %{python_files}
%license COPYING
%doc AUTHORS debian/changelog README.md
%doc %{_docdir}/%{python_flavor}-%{modname}
%{python_sitearch}/ginac/
%{python_sitearch}/*.so

%files %{python_files devel}
%{_includedir}/*.hpp
%{_libdir}/pkgconfig/*.pc

%changelog
