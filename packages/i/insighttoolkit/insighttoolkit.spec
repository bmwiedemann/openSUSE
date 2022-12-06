#
# spec file for package insighttoolkit
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2016 Angelos Tzotsos <tzotsos@opensuse.org>.
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


%global __builder ninja
%define tarname ITK
%define libname lib%{name}5_3-1

# Do not use system eigen on aarch64 until fixed upstream:
# https://github.com/InsightSoftwareConsortium/ITK/issues/2903
%ifarch aarch64
%bcond_with system_eigen
%else
%bcond_without system_eigen
%endif

# Python bindings must be turned off until https://github.com/InsightSoftwareConsortium/ITK/issues/3782 is resolved
%if 0%{?suse_version} >= 1550
%bcond_with python
%else
%bcond_without python
%endif

Name:           insighttoolkit
Version:        5.3.0
Release:        0
Summary:        Toolkit for scientific image processing, segmentation, and registration
License:        Apache-2.0
URL:            https://www.itk.org
Source:         https://github.com/InsightSoftwareConsortium/ITK/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  CastXML-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  dcmtk-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gdcm-devel
BuildRequires:  gtest
BuildRequires:  hdf5-devel
BuildRequires:  libnsl-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  vtk-devel
BuildRequires:  vtk-qt
BuildRequires:  xz
BuildRequires:  cmake(double-conversion)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  swig >= 4.0
%endif
%if %{with system_eigen}
BuildRequires:  pkgconfig(eigen3)
%endif

%description
The Insight Toolkit (ITK) is a toolkit for N-dimensional scientific
image processing, segmentation, and registration.

%package devel
Summary:        Development files for ITK
Requires:       %{libname} = %{version}-%{release}
Requires:       dcmtk-devel
Requires:       double-conversion-devel
Requires:       fftw3-threads-devel
Requires:       hdf5-devel
Requires:       vtk-devel
Requires:       pkgconfig(expat)
Requires:       pkgconfig(fftw3)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libpcrecpp)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(libtiff-4)
Requires:       pkgconfig(libxml-2.0)
Requires:       pkgconfig(zlib)
Provides:       lib%{name}-devel

%description devel
The Insight Toolkit (ITK) is a toolkit for N-dimensional scientific
image processing, segmentation, and registration.

This package provides development files for the ITK library.

%package -n %{libname}
Summary:        Toolkit for scientific image processing, segmentation, and registration
Conflicts:      libinsighttoolkit5

%description -n %{libname}
The Insight Toolkit (ITK) is a toolkit for N-dimensional scientific
image processing, segmentation, and registration.

This package provides shared libraries for ITK.

%package -n python3-itk
Summary:        Python bindings for ITK
Requires:       python3-numpy

%description -n python3-itk
The Insight Toolkit (ITK) is a toolkit for N-dimensional scientific
image processing, segmentation, and registration.

This package provides the modules for ITK's python bindings.

%prep
%autosetup -p1 -n %{tarname}-%{version}

%build
# Tests disabled because no KWStyle pkg for openSUSE
%cmake \
  -DITK_INSTALL_LIBRARY_DIR:PATH=%{_lib}/ \
  -DITK_INSTALL_INCLUDE_DIR:PATH=include/%{name}/ \
  -DITK_INSTALL_PACKAGE_DIR:PATH=%{_lib}/cmake/%{name}/ \
  -DITK_INSTALL_RUNTIME_DIR:PATH=%{_bindir} \
  -DITK_INSTALL_DOC_DIR=share/doc/packages/%{name}/ \
  -DBUILD_EXAMPLES:BOOL=ON \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBUILD_TESTING:BOOL=OFF \
  -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON \
  -DITK_USE_FFTWD:BOOL=ON \
  -DITK_USE_FFTWF:BOOL=ON \
  -DITK_USE_SYSTEM_LIBRARIES:BOOL=ON \
  -DITK_USE_SYSTEM_CASTXML:BOOL=ON \
  -DITK_USE_SYSTEM_GDCM:BOOL=ON \
%if %{without system_eigen}
  -DITK_USE_SYSTEM_EIGEN:BOOL=OFF \
%endif
  -DITK_USE_SYSTEM_SWIG:BOOL=ON \
  -DITK_USE_SYSTEM_VXL:BOOL=OFF \
  -DVXL_BUILD_CORE_NUMERICS:BOOL=OFF \
  -DVCL_INCLUDE_CXX_0X:BOOL=ON \
  -DITK_FORBID_DOWNLOADS=ON \
  -DITK_WRAP_PYTHON:BOOL=%{?with_python:ON}%{!?with_python:OFF}

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}/%{_prefix}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE NOTICE
%{_libdir}/*.so.1

%files devel
%license LICENSE NOTICE
%{_includedir}/%{name}/
%{_libdir}/lib*.so
%{_libdir}/cmake/
%{_bindir}/itkTestDriver
%doc %{_docdir}/%{name}/

%if %{with python}
%files -n python3-itk
%license LICENSE NOTICE
%{python3_sitearch}/*.py
%{python3_sitearch}/itk/
%endif

%changelog
