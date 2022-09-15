#
# spec file for package libmsym
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


# At least python3 is required
%define skip_python2 1
%if 0%{suse_version} >= 1550
# On Factory numpy does not support python36 anymore
%define skip_python36 1
%endif

%define sonum   0_2
Name:           libmsym
Version:        0.2.3
Release:        0
Summary:        Molecular point group symmetry library
License:        MIT
Group:          System/Libraries
URL:            https://github.com/mcodev31/libmsym
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros

%define python_subpackage_only 1
%python_subpackages

%description
A C library dealing with point group symmetry in molecules.

%package -n %{name}%{sonum}
Summary:        Molecular point group symmetry library
Group:          System/Libraries

%description -n %{name}%{sonum}
A C library dealing with point group symmetry in molecules.

%package devel
Summary:        Development files for libmsym
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sonum} = %{version}

%description devel
This package contains all necessary include files and libraries
needed to develop applications that require libmsym.

%package -n python-%{name}
Summary:        Python bindings for libmsym
BuildArch:      noarch

%description -n python-%{name}
This package contains the python bindings needed to develop
python applications that require libmsym.

%prep
%setup -q

%build
%cmake \
  -DINSTALL_LIB_DIR=%{_libdir} \
  -DINSTALL_CMAKE_DIR=%{_libdir}/cmake/libmsym
%make_build
pushd ../bindings/python
%python_build
popd

%install
%cmake_install
pushd bindings/python
%python_install
popd

%post   -n %{name}%{sonum} -p /sbin/ldconfig
%postun -n %{name}%{sonum} -p /sbin/ldconfig

%files  -n %{name}%{sonum}
%license LICENSE
%{_libdir}/libmsym.so.*

%files devel
%doc README.md
%{_libdir}/cmake/libmsym/
%{_includedir}/libmsym/
%{_libdir}/libmsym.so

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%files %{python_files %name}
%{python_sitelib}/*
%else

%files %{python_files}
%{python_sitelib}/*
%endif

%changelog
