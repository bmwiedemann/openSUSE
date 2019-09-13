#
# spec file for package exodusii
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           exodusii
Version:        6.09
%define libver	5.14.0
%define libusc	5_14_0
Release:        0
Summary:        Library to store and retrieve transient finite element data
Group:          Productivity/Scientific/Math
License:        BSD-3-Clause
Url:            http://sourceforge.net/projects/exodusii/
Source:         http://distfiles.gentoo.org/distfiles/exodus-%{version}.tar.gz
Patch1:         sovers.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  cmake
BuildRequires:  netcdf-devel
BuildRequires:  zlib-devel

%description
EXODUS II is a model developed to store and retrieve data for finite element
analyses. It is used for preprocessing (problem definition), postprocessing
(results visualization), as well as code to code data transfer. An EXODUS II
data file is a random access, machine independent, binary file that is written
and read via C, C++, or Fortran library routines which comprise the
Application Programming Interface (API).

%package -n libexodus-%libusc
Summary:        ExodusII C library
Group:          Productivity/Scientific/Math
Provides:       libexoIIv2c-%libusc < %{version}

%description -n libexodus-%libusc
EXODUS II is a model developed to store and retrieve data for finite element
analyses. It is used for preprocessing (problem definition), postprocessing
(results visualization), as well as code to code data transfer. An EXODUS II
data file is a random access, machine independent, binary file that is written
and read via C, C++, or Fortran library routines which comprise the
Application Programming Interface (API).

This package contains the C library for exodusII.

%package -n libexoIIv2for-%libusc
Summary:        ExodusII Fortran library
Group:          Productivity/Scientific/Math

%description -n libexoIIv2for-%libusc
EXODUS II is a model developed to store and retrieve data for finite element
analyses. It is used for preprocessing (problem definition), postprocessing
(results visualization), as well as code to code data transfer. An EXODUS II
data file is a random access, machine independent, binary file that is written
and read via C, C++, or Fortran library routines which comprise the
Application Programming Interface (API).

This package contains the Fortran library for exodusII.

%package devel
Summary:    Development headers and libraries for exodusII
Group:      Development/Libraries/C and C++
Requires:   libexodus-%libusc = %{version}
Requires:   libexoIIv2for-%libusc = %{version}
Requires:   netcdf-devel

%description devel
EXODUS II is a model developed to store and retrieve data for finite element
analyses. It is used for preprocessing (problem definition), postprocessing
(results visualization), as well as code to code data transfer. An EXODUS II
data file is a random access, machine independent, binary file that is written
and read via C, C++, or Fortran library routines which comprise the
Application Programming Interface (API).

This package contains development headers and libraries for exodusII.

%prep
%setup -n exodus-%{version} -q
%patch -P 1 -p1

%build
cd exodus
%if %{undefined cmake}
%define cmake cmake
mkdir build
cd build
%endif
%{cmake} \
 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_SKIP_RPATH:BOOL=ON \
 -DPYTHON=false \
 -DBUILD_SHARED=ON \
 ..
make %{?_smp_mflags}

%install
cd exodus
cd build
make install DESTDIR=%{buildroot}
[[ %{_lib} = lib ]] || mv %{buildroot}/%{_prefix}/{lib,%{_lib}}
ln -s libexodus-%{libver}.so "%buildroot/%_libdir/libexodus.so"
ln -s libexoIIv2for-%{libver}.so "%buildroot/%_libdir/libexoIIv2for.so"
find %buildroot
 
%post -n libexodus-%libusc -p /sbin/ldconfig
%post -n libexoIIv2for-%libusc -p /sbin/ldconfig
%postun -n libexodus-%libusc -p /sbin/ldconfig
%postun -n libexoIIv2for-%libusc -p /sbin/ldconfig

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libexodus.so
%{_libdir}/libexoIIv2for.so

%files -n libexodus-%libusc
%defattr(-,root,root)
%{_libdir}/libexodus-%libver.so

%files -n libexoIIv2for-%libusc
%defattr(-,root,root)
%{_libdir}/libexoIIv2for-%libver.so
 
%changelog
