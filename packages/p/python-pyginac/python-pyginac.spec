#
# spec file for package python-pyginac
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


# The specfile is prepared for multiple python flavors, but the boost library
# is only available for the primary python3.
%define pythons python3
%global modname pyginac
Name:           python-pyginac
Version:        1.5.5
Release:        0
Summary:        Python bindings for ginac - a symbolic manipulation library
License:        GPL-2.0-only
URL:            http://moebinv.sourceforge.net/pyGiNaC.html
Source:         https://download.sf.net/pyginac.moebinv.p/%{modname}_%{version}.orig.tar.gz
# PATCH-FEATURE-OPENSUSE pyginac-opensusepaths.patch badshah400@gmail.com, code@bnavigator.de -- Enable build with multiple python versions, patch adapted from upstream (commit b4848e)
Patch1:         pyginac-opensusepaths.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ginac-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
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
cp -ar site-packages site-packages0
%{python_expand # build for flavor and place into shuffled build/ dir
%make_build PYTHON=$python
mkdir build
mv site-packages build/
# get clean state for next build
cp -ar site-packages0 site-packages
}

%install
%{python_expand # install into flavor sitearch
rm -r site-packages
cp -ar build/site-packages ./
%make_install PYTHON=$python prefix=%{_prefix} libdir=%{$python_sitearch} docdir=%{_docdir}/%{$python_prefix}-pyginac
}
%{python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitearch}
if [[ "%{_lib}" != 'lib' ]]; then
  mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_libdir}/
fi

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python bin/checkall.py
}

%files %{python_files}
%license COPYING
%doc AUTHORS debian/changelog README.md
%doc %{_docdir}/%{python_prefix}-pyginac
%{python_sitearch}/ginac/
%{python_sitearch}/*.so

%files %{python_files devel}
%{_includedir}/*.hpp
%{_libdir}/pkgconfig/*.pc

%changelog
