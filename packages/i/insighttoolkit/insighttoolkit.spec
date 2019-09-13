#
# spec file for package insighttoolkit
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define tarname InsightToolkit
%define baseversion 4.13
Name:           insighttoolkit
Version:        %{baseversion}.2
Release:        0
Summary:        Insight Segmentation and Registration Toolkit
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.itk.org
#Source0:        http://sourceforge.net/projects/itk/files/itk/%{baseversion}/%{tarname}-%{version}.tar.xz
Source:         https://netix.dl.sourceforge.net/project/itk/itk/%{baseversion}/%{tarname}-%{version}.tar.xz
Patch0:         dcmtk-cmake.patch
# PATCH-FIX-UPSTREAM proper linking against math library
Patch1:         nrrdio-linking.patch
# PATCH-FIX-UPSTREAM add support for GCC 9
Patch2:         add_gcc9_support.patch
# PATCH-FIX-UPSTREAM proper linking against math library
Patch3:         itklbfgs-linking.patch
BuildRequires:  cmake >= 2.8.0
BuildRequires:  dcmtk
BuildRequires:  dcmtk-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
# BuildRequires:  gdcm-devel
BuildRequires:  hdf5-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  python-devel
BuildRequires:  sed
BuildRequires:  swig
%if 0%{suse_version} > 1320
# Indirect DCMTK dep. Should DCMTK be fixed?
# tcpd-devel is needed for libwrap.so on Tumbleweed (> Leap 42.3)
BuildRequires:  tcpd-devel
BuildRequires:  libnsl-devel
%endif
BuildRequires:  vtk-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ITK is a suite of software tools for image analysis.

%package devel
Summary:        Development files for ITK
Group:          Development/Libraries/C and C++
Requires:       dcmtk-devel
Requires:       fftw3-devel
Requires:       fftw3-threads-devel
Requires:       hdf5-devel
Requires:       lib%{name}4 = %{version}
Requires:       libexpat-devel
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       libtiff-devel
Requires:       vtk-devel
Requires:       zlib-devel
Provides:       lib%{name}-devel

%description devel
Development files for the ITK library.
ITK is a suite of software tools for image analysis.

%package -n lib%{name}4
Summary:        Insight Segmentation and Registration Toolkit
Group:          System/Libraries

%description -n lib%{name}4
Shared ITK library.
ITK is a suite of software tools for image analysis.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake \
  -DBUILD_EXAMPLES:BOOL=ON \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBUILD_TESTING:BOOL=OFF \
  -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON \
  -DUSE_FFTWF=ON \
  -DITK_USE_FFTWD:BOOL=ON \
  -DITK_USE_FFTWF:BOOL=ON \
  -DITK_USE_SYSTEM_FFTW:BOOL=ON \
  -DITK_USE_STRICT_CONCEPT_CHECKING:BOOL=ON \
  -DITK_USE_SYSTEM_DOUBLECONVERSION:BOOL=OFF \
  -DITK_USE_SYSTEM_DCMTK:BOOL=ON \
  -DITK_USE_SYSTEM_GDCM:BOOL=OFF \
  -DITK_USE_SYSTEM_HDF5:BOOL=ON \
  -DITK_USE_SYSTEM_JPEG:BOOL=ON \
  -DITK_USE_SYSTEM_PNG:BOOL=ON \
  -DITK_USE_SYSTEM_TIFF:BOOL=ON \
  -DITK_USE_SYSTEM_VXL:BOOL=OFF \
  -DITK_USE_SYSTEM_ZLIB:BOOL=ON \
  -DITK_USE_SYSTEM_EXPAT:BOOL=ON \
  -DModule_ITKDCMTK:BOOL=ON \
  -DModule_ITKIOPhilipsREC:BOOL=OFF \
  -DModule_ITKLevelSetsv4Visualization:BOOL=OFF \
  -DModule_ITKReview:BOOL=OFF \
  -DModule_ITKVideoBridgeOpenCV:BOOL=OFF \
  -DModule_ITKVideoBridgeVXL:BOOL=OFF \
  -DModule_ITKVtkGlue:BOOL=OFF \
  -DModule_ITKDeprecated:BOOL=OFF \
  -DITKV3_COMPATIBILITY:BOOL=ON \
  -DVCL_INCLUDE_CXX_0X:BOOL=ON \
  -DITK_WRAPPING:BOOL=OFF \
  -DITK_WRAP_PYTHON:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING="Release"

make VERBOSE=1 %{?_smp_mflags}


%install
%cmake_install

%if "%{_lib}" == "lib64"
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_libexecdir}/* %{buildroot}%{_libdir}/
sed -i 's|/lib/|/lib64/|g' %{buildroot}%{_libdir}/cmake/ITK-%{baseversion}/ITKConfig.cmake
sed -i 's|/lib/|/lib64/|g' %{buildroot}%{_libdir}/cmake/ITK-%{baseversion}/ITKTargets.cmake
sed -i 's|/lib/|/lib64/|g' %{buildroot}%{_libdir}/cmake/ITK-%{baseversion}/ITKTargets-release.cmake
%endif
rm -rf %{buildroot}%{_libexecdir}/debug
# move files to a proper place
mv %{buildroot}%{_libdir}/*itk*.cmake %{buildroot}%{_libdir}/cmake/
# remove openjp2 file installation
rm -rf %{buildroot}/%{_includedir}/gdcmopenjpeg %{buildroot}%{_libdir}/gdcmopenjpeg-* %{buildroot}%{_libdir}/pkgconfig/libopenjp2.pc
rmdir %{buildroot}%{_libdir}/pkgconfig

%fdupes %{buildroot}/%{_prefix}

%post -n lib%{name}4 -p /sbin/ldconfig

%postun -n lib%{name}4 -p /sbin/ldconfig

%files -n lib%{name}4
%defattr(644,root,root,755)
%license LICENSE
%{_libdir}/*.so.1

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/
%{_bindir}/itkTestDriver
%{_datadir}/*

%changelog
