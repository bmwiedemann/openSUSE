#
# spec file for package ossim
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Angelos Tzotsos <tzotsos@opensuse.org>.
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


%define _release_name Islamorada
Name:           ossim
Version:        2.5.1
Release:        0
Summary:        Open Source Software Image Map (OSSIM)
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            http://trac.osgeo.org/ossim/
Source0:        https://github.com/ossimlabs/ossim/archive/%{_release_name}-%{version}.tar.gz#/%{name}-%{_release_name}-%{version}.tar.gz
# hdf5 1.10.2+ deprecate printError() virtual function by removing it
# Fix ossim code to use printErrorStack replacement
Patch0:         fix_hdf5_printErrorStack.patch
BuildRequires:  cmake >= 2.8.0
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  geos-devel
BuildRequires:  geotiff-devel
BuildRequires:  hdf5-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libOpenThreads-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel

%description
The OSSIM core utilities.
Open Source Software Image Map (OSSIM) is an engine for
remote sensing, image processing, geographical information systems and
photogrammetry.

%package devel
Summary:        Header files for the Open Source Software Image Map
Group:          Development/Libraries/C and C++
Requires:       lib%{name}1 = %{version}-%{release}
Provides:       lib%{name}-devel

%description devel
The OSSIM development files.
Open Source Software Image Map (OSSIM) is an engine for
remote sensing, image processing, geographical information systems and
photogrammetry.

%package -n lib%{name}1
Summary:        Open Source Software Image Map libraries
Group:          System/Libraries

%description -n lib%{name}1
The OSSIM shared library files.
Open Source Software Image Map (OSSIM) is an engine for
remote sensing, image processing, geographical information systems and
photogrammetry.

%package sample-data
Summary:        OSSIM data samples files
Group:          Development/Libraries/C and C++

%description sample-data
The OSSIM data samples files for tests.

%prep
%setup -q -n %{name}-%{_release_name}-%{version}
%patch0 -p1

%build
export CXXFLAGS=" -std=c++03"
%cmake \
  -DBUILD_OSSIM_FRAMEWORKS=ON \
  -DBUILD_OSSIM_FREETYPE_SUPPORT=ON \
  -DBUILD_OSSIM_MPI_SUPPORT=OFF \
  -DBUILD_OSSIM_ID_SUPPORT=ON \
  -DBUILD_OSSIM_APPS=ON \
  -DBUILD_OSSIM_CURL_APPS=OFF \
  -DBUILD_OSSIM_TESTS=ON \
  -DBUILD_OSSIM_HDF5_SUPPORT=ON \
  -DBUILD_SHARED_LIBS=ON \
  -DGEOS_C_LIB=%{_libdir}/libgeos_c.so \
  -DGEOS_INCLUDE_DIR=%{_includedir}/geos \
  -DGEOS_LIB=%{_libdir}/libgeos.so \
  -DGEOS_LIBRARY=%{_libdir}/libgeos.so \
  -DGEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \
  -DCMAKE_MODULE_PATH=$(CURDIR)/CMakeModules \
  -DFREETYPE_INCLUDE_DIRS=%{_includedir}/freetype2 \
  -DGEOTIFF_LIBRARY=%{_libdir}/libgeotiff.so

make %{?_smp_mflags}

%install
%cmake_install

# Fix lib folder for 32-bits
# Beware don't let spec-cleaner playing with this
%if "%{_lib}" == "lib"
mkdir -p %{buildroot}/usr/lib
mv %{buildroot}/usr/lib64/* %{buildroot}/usr/lib/
%endif

%fdupes %{buildroot}/%{_prefix}

%post -n lib%{name}1 -p /sbin/ldconfig

%postun -n lib%{name}1 -p /sbin/ldconfig

%files -n lib%{name}1
%defattr(644,root,root,755)
%{_libdir}/*.so.*

%files
%defattr(-,root,root,-)
%{_bindir}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so

%files sample-data
%dir %{_datadir}/ossim
%{_datadir}/ossim/*

%changelog
