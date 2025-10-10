#
# spec file for package CSXCAD
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           CSXCAD
%define octpkg  csxcad
Version:        0.6.3
Release:        0
%define so_ver  0
%define libname lib%{name}%{so_ver}
Summary:        A C++ library to describe geometrical objects and their properties
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://openems.de
Source0:        https://github.com/thliebig/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         boost.patch
# PATCH-FIX-OPENSUSE CSXCAD-octave-AppCSXCAD-load.patch -- Fix AppCSXCAD.sh load
Patch3:         CSXCAD-octave-AppCSXCAD-load.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cgal-devel
BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  fparser-devel
BuildRequires:  gcc-c++
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  lzma-devel
BuildRequires:  octave-devel
BuildRequires:  python-rpm-macros
BuildRequires:  tinyxml-devel
BuildRequires:  vtk-devel
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
%define python_subpackage_only 1
%python_subpackages

%description
CSXCAD is a C++ library to describe geometrical objects and their physical
or non-physical properties.

%package -n     %{libname}
Summary:        A C++ library to describe geometrical objects and their properties
Group:          System/Libraries

%description -n %{libname}
CSXCAD is a C++ library to describe geometrical objects and their physical
or non-physical properties.

%package        -n %{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    -n %{name}-devel
CSXCAD is a C++ library to describe geometrical objects and their physical
or non-physical properties.

This package contains libraries and header files for developing
applications that use %{name}.

%package -n     octave-%{name}
Summary:        Octave interface for openEMS
Group:          Productivity/Scientific/Physics
Requires:       octave-cli
BuildArch:      noarch

%description -n octave-%{name}
CSXCAD is a C++ library to describe geometrical objects and their physical
or non-physical properties.

This package provides Octave interface for CSXCAD.

%package -n     %{name}-matlab
Summary:        MATLAB interface for openEMS
Group:          Productivity/Scientific/Physics
BuildArch:      noarch

%description -n %{name}-matlab
CSXCAD is a C++ library to describe geometrical objects and their physical
or non-physical properties.

This package provides MATLAB interface for CSXCAD.

%package -n     python-%{name}
Summary:        Python %{python_version} bindings for CSXCAD
Group:          Development/Libraries/Python
Requires:       python-matplotlib
Requires:       python-numpy

%description -n python-%{name}
This package contains Python %{python_version} bindings for the CSXCAD
library.

%prep
%setup -q
%autopatch -p1

echo "Name: %{octpkg}" >> DESCRIPTION
echo "Version: %{version}" >> DESCRIPTION
echo "Date: 2015-10-10" >> DESCRIPTION
echo "Author: Thorsten Liebig" >> DESCRIPTION
echo "Maintainer: Thorsten Liebig" >> DESCRIPTION
echo "Title: Describing geometrical objects and their properties" >> DESCRIPTION
echo "Description: CSXCAD is a library to describe geometrical objects and their physical or non-physical properties." >> DESCRIPTION
echo "Categories: openEMS" >> DESCRIPTION

mkdir octave_build
cp -r matlab octave_build
pushd octave_build/matlab
    mkdir src
    mkdir inst
    mv *.m inst/
    mv private inst/
    cp ../../COPYING .
    mv ../../DESCRIPTION .
    cd ..
    %octave_pkg_src
popd

%build
%cmake \
    -DFPARSER_ROOT_DIR=%{_prefix} \
    %{nil}
%cmake_build

cd ..
pushd octave_build
    %octave_pkg_build
popd

pushd python
    mkdir -p "%{_builddir}/include"
    ln -s "%{_builddir}/%{name}-%{version}/src" "%{_builddir}/include/CSXCAD"
    cat >> setup.cfg << EOF
[build_ext]
include_dirs = %{_builddir}/include
library_dirs = %{_builddir}/%{name}-%{version}/build/src
EOF
    %pyproject_wheel
popd

%install
%cmake_install

pushd octave_build
    %octave_pkg_install
popd

pushd python
    %pyproject_install
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n octave-%{name}
%octave --eval "pkg rebuild"

%postun -n octave-%{name}
%octave --eval "pkg rebuild"

%files -n %{libname}
%license COPYING
%doc NEWS README
%{_libdir}/lib%{name}.so.*

%files -n %{name}-devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%files -n octave-%{name}
%{octpackages_dir}/%{octpkg}-%{version}

%files -n %{name}-matlab
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/matlab/

%files %{python_files CSXCAD}
%license COPYING
%{python_sitearch}/CSXCAD
%{python_sitearch}/csxcad-*.dist-info

%changelog
