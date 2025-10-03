#
# spec file for package openEMS
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


Name:           openEMS
%define octpkg  openems
Version:        0.0.36
Release:        0
Summary:        Electromagnetic field solver using the EC-FDTD method
License:        GPL-3.0-only
Group:          Productivity/Scientific/Physics
URL:            https://openems.de/start
# source - openEMS component only, not openEMS-Project
Source0:        https://github.com/thliebig/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE openEMS-octave-openEMS-load.patch -- Fix openEMS.sh load
Patch2:         0002-Fix-openEMS.sh-load.patch
# PATCH-FIX-OPENSUSE openEMS-octave-nf2ff-load.patch -- Fix nf2ff load
Patch3:         0003-Fix-nf2ff-load.patch
# PATCH-FIX-OPENSUSE openEMS-readme-octave-package.patch -- Add correct instruction about Octave and MATLAB packages
Patch4:         0004-Add-correct-instruction-about-Octave-and-MATLAB-pack.patch
# PATCH-FIX-UPSTREAM 0001-fix-cython-import.patch -- fix cython import
Patch5:         0001-fix-cython-import.patch
Patch6:         boost.patch
BuildRequires:  %{python_module CSXCAD}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  CSXCAD-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  octave-devel
BuildRequires:  python-rpm-macros
BuildRequires:  tinyxml-devel
BuildRequires:  vtk-devel
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(fparser)
BuildRequires:  pkgconfig(python3)
ExcludeArch:    %{ix86} s390x
%define python_subpackage_only 1
%python_subpackages

%description
Electromagnetic field solver using the EC-FDTD method.

%package -n     libnf2ff0
Summary:        Near-field to far-field transformation library
Group:          System/Libraries

%description -n libnf2ff0
Near-field to far-field transformation library.

%package -n     libopenEMS0
Summary:        Electromagnetic field solver library
Group:          System/Libraries

%description -n libopenEMS0
Electromagnetic field solver using the EC-FDTD method library.

%package -n     %{name}-devel
Summary:        Development files for openEMS
Group:          Development/Libraries/C and C++
Requires:       libnf2ff0 = %{version}
Requires:       libopenEMS0 = %{version}

%description -n %{name}-devel
This package contains libraries for developing applications
that use %{name}.

%package -n     octave-%{name}
Summary:        Octave interface for openEMS
Group:          Productivity/Scientific/Physics
Requires:       %{name} = %{version}
Requires:       AppCSXCAD
Requires:       octave-CSXCAD
Requires:       octave-cli

%description -n octave-%{name}
Electromagnetic field solver using the EC-FDTD method.

This package provides Octave interface for openEMS.

%package -n     %{name}-matlab
Summary:        MATLAB interface for openEMS
Group:          Productivity/Scientific/Physics
Requires:       %{name} = %{version}
Requires:       AppCSXCAD
Requires:       CSXCAD-matlab

%description -n %{name}-matlab
Electromagnetic field solver using the EC-FDTD method.

This package provides MATLAB interface for openEMS.

%package -n     python-%{name}
Summary:        Python %{python_version} bindings for openEMS
Group:          Development/Libraries/Python
Requires:       python-CSXCAD
Requires:       python-h5py
Requires:       python-matplotlib
Requires:       python-numpy

%description -n python-%{name}
This package contains Python %{python_version} bindings for the openEMS
library.

%prep
%setup -q
%autopatch -p1

echo "Name: %{octpkg}" >> DESCRIPTION
echo "Version: %{version}" >> DESCRIPTION
echo "Date: 2015-10-10" >> DESCRIPTION
echo "Author: Thorsten Liebig" >> DESCRIPTION
echo "Maintainer: Thorsten Liebig" >> DESCRIPTION
echo "Title: Electromagnetic field solver using the EC-FDTD method" >> DESCRIPTION
echo "Description: Electromagnetic field solver using the EC-FDTD method." >> DESCRIPTION
echo "Categories: openEMS" >> DESCRIPTION
echo "Depends: csxcad" >> DESCRIPTION
echo "Autoload: yes" >> DESCRIPTION

cat > Makefile-octave << 'EOF'
MKOCTFILE := mkoctfile

all: h5readatt_octave.oct

%.oct: %.cc
	$(MKOCTFILE) -lhdf5 -DH5_USE_16_API -s $<

clean: ; rm *.o *.oct
EOF

rm matlab/setup.m

mkdir octave_build
cp -r matlab octave_build
pushd octave_build/matlab
    mkdir src
    mv *.cc src/
    mv ../../Makefile-octave src/Makefile
    mkdir inst
    mv *.m inst/
    mv {private,examples,Tutorials} inst/
    cp ../../COPYING .
    mv ../../DESCRIPTION .
    cd ..
    %octave_pkg_src
popd

%build
%ifarch %ix86
# Required for XMM intrinsics
export CFLAGS="%{optflags} -msse"
export CXXFLAGS="%{optflags} -msse"
%endif
%ifnarch %ix86 x86_64
# Always handle subnormals according to IEEE754 (gradual underflow),
# as the code for enabling Flush-To-Zero is x86 specific. This may have
# a performance impact, arch specific code for non-x86 should be used.
export CXXFLAGS="%{optflags} -DSSE_CORRECT_DENORMALS"
%endif
%cmake

%cmake_build

cd ..
pushd octave_build
    %octave_pkg_build
popd

pushd python
    mkdir -p "%{_builddir}/include/openEMS"
    cp "%{_builddir}/%{name}-%{version}/openems.h" "%{_builddir}/include/openEMS"
    cp "%{_builddir}/%{name}-%{version}/openems_global.h" "%{_builddir}/include/openEMS"
    cp "%{_builddir}/%{name}-%{version}/nf2ff/nf2ff.h" "%{_builddir}/include/openEMS"
    cat >> setup.cfg << EOF
[build_ext]
include_dirs = %{_builddir}/include
library_dirs = %{_builddir}/%{name}-%{version}/build:%{_builddir}/%{name}-%{version}/build/nf2ff
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

%post -n libnf2ff0 -p /sbin/ldconfig

%postun -n libnf2ff0 -p /sbin/ldconfig

%post -n libopenEMS0 -p /sbin/ldconfig

%postun -n libopenEMS0 -p /sbin/ldconfig

%post -n octave-%{name}
%octave --eval "pkg rebuild -auto %{octpkg}"

%postun -n octave-%{name}
%octave --eval "pkg rebuild"

%files -n %{name}
%license COPYING
%doc NEWS README
%{_bindir}/*

%files -n libnf2ff0
%{_libdir}/libnf2ff.so.*

%files -n libopenEMS0
%{_libdir}/libopenEMS.so.*

%files -n %{name}-devel
%dir %{_prefix}/include/%{name}
%{_prefix}/include/%{name}/*
%{_libdir}/libnf2ff.so
%{_libdir}/libopenEMS.so

%files -n octave-%{name}
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%files -n %{name}-matlab
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/matlab/

%files %{python_files openEMS}
%license COPYING
%{python_sitearch}/openEMS
%{python_sitearch}/openems-*.dist-info

%changelog
