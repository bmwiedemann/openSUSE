#
# spec file for package cgns
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define libname libcgns3_4

Name:           cgns
Version:        3.4.0
Release:        1
Source0:        https://github.com/CGNS/CGNS/archive/v3.4.0.tar.gz#/cgnslib_%{version}.tar.gz
Source1:        %name-rpmlintrc
Summary:        CFD General Notation System
License:        Zlib
Group:          Development/Libraries/Other
Url:            http://cgns.org/
BuildRequires:  cmake
BuildRequires:  f2c
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5-devel
BuildRequires:  libxml2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
The CFD General Notation System (CGNS) provides a general, portable,
and extensible standard for the storage and retrieval of computational
fluid dynamics (CFD) analysis data.

%package -n %libname
Summary:        CFD General Notation System library
Group:          System/Libraries
Provides:       lib%{name} = %{version}
Obsoletes:      lib%{name} < %{version}

%description -n %libname
The CFD General Notation System (CGNS) provides a general, portable,
and extensible standard for the storage and retrieval of computational
fluid dynamics (CFD) analysis data.

%package devel
Summary:        CFD General Notation System library
Group:          Development/Libraries/Other
Requires:       %libname = %{version}
Provides:       lib%{name}-devel = %{version}
Obsoletes:      lib%{name}-devel < %{version}

%description devel
Files required to develop applications using CGNS (CFD General notation system).

%package devel-static
Summary:        CFD General Notation System library
Group:          Development/Libraries/Other
Requires:       %{name}-devel = %{version}

%description devel-static
Static CGNS (CFD General notation system) library.


%prep
%setup -q -n CGNS-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

%cmake \
%ifarch x86_64 ppc64 ppc64le aarch64
      -DCGNS_ENABLE_64BIT:BOOL=ON \
%endif
      -DCGNS_ENABLE_HDF5:BOOL=ON \
      -DCGNS_ENABLE_LEGACY:BOOL=ON \
      -DCGNS_ENABLE_FORTRAN:BOOL=ON \
      -DHDF5_NEED_ZLIB:BOOL=ON \

make %{?_smp_mflags}

%install
%cmake_install

%ifarch x86_64 ppc64 ppc64le aarch64
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%{_bindir}/*

%files -n %libname
%license license.txt
%doc release_docs/Release.txt
%{_libdir}/libcgns.so.*

%files devel
%{_includedir}/*.h
%{_includedir}/cgns.mod
%{_includedir}/cgnsBuild.defs
%{_libdir}/libcgns.so

%files devel-static
%{_libdir}/libcgns.a

%changelog
