#
# spec file for package cgns
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


%define libname libcgns4_3
Name:           cgns
Version:        4.3.0
Release:        0
Summary:        CFD General Notation System
License:        Zlib
Group:          Development/Libraries/Other
URL:            https://cgns.github.io/index.html
Source0:        https://github.com/CGNS/CGNS/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  f2c
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5-devel
BuildRequires:  libxml2-devel

%description
The CFD General Notation System (CGNS) provides a general, portable,
and extensible standard for the storage and retrieval of computational
fluid dynamics (CFD) analysis data.

%package -n %{libname}
Summary:        CFD General Notation System library
Group:          System/Libraries
Provides:       lib%{name} = %{version}
Obsoletes:      lib%{name} < %{version}

%description -n %{libname}
The CFD General Notation System (CGNS) provides a general, portable,
and extensible standard for the storage and retrieval of computational
fluid dynamics (CFD) analysis data.

%package devel
Summary:        CFD General Notation System library
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}
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
%if %{__isa_bits} == 64
      -DCGNS_ENABLE_64BIT:BOOL=ON \
%endif
      -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
      -DCGNS_ENABLE_HDF5:BOOL=ON \
      -DCGNS_ENABLE_LEGACY:BOOL=ON \
      -DCGNS_ENABLE_FORTRAN:BOOL=ON \
      -DHDF5_NEED_ZLIB:BOOL=ON \

# Parallel build fails, see https://cgnsorg.atlassian.net/browse/CGNS-204
%cmake_build -j1

%install
%cmake_install

%if "%_lib" != "lib"
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/*

%files -n %{libname}
%license license.txt
%doc release_docs/RELEASE.txt
%{_libdir}/libcgns.so.*

%files devel
%{_includedir}/*.h
%{_includedir}/cgns.mod
%{_includedir}/cgnsBuild.defs
%{_libdir}/libcgns.so
%{_libdir}/cmake/cgns

%files devel-static
%{_libdir}/libcgns.a

%changelog
