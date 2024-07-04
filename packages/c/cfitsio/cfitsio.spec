#
# spec file for package cfitsio
#
# Copyright (c) 2024 SUSE LLC
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


%define so_ver 10
%define __builder ninja
Name:           cfitsio
Version:        4.4.0
Release:        0
Summary:        Library for manipulating FITS data files
License:        NASA-1.3
URL:            https://heasarc.gsfc.nasa.gov/fitsio/
Source0:        https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM cfitsio-cmake-allow-user-specified-incdir.patch badshah400@gmail.com -- Allow user-specified include dir
Patch0:         cfitsio-cmake-allow-user-specified-incdir.patch
# PATCH-FIX-UPSTREAM cfitsio-cmake-devel-scripts-destination.patch badshah400@gmail.com -- Fix installation dir for pkgconfig and cmake scripts
Patch1:         cfitsio-cmake-devel-scripts-destination.patch
# PATCH-FIX-UPSTREAM cfitsio-cmake-lowercase-util-names.patch badshah400@gmail.com -- Use lowercase name for utility binaries when building using cmake (same as autotools)
Patch2:         cfitsio-cmake-lowercase-util-names.patch
# PATCH-FIX-UPSTREAM cfitsio-cmake-match-autotools-soversion.patch badshah400@gmail.com -- Use same so version when building with cmake as when done using autotools
Patch3:         cfitsio-cmake-match-autotools-soversion.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)

%description
CFITSIO is a library of C and Fortran subroutines for reading and writing data
files in FITS (Flexible Image Transport System) data format. CFITSIO provides
simple high-level routines for reading and writing FITS files that insulate the
programmer from the internal complexities of the FITS format. CFITSIO also
provides many advanced features for manipulating and filtering the information
in FITS files.

This package contains some FITS image compression and decompression utilities.

%package devel
Summary:        Headers required when building programs against cfitsio library
Requires:       libcfitsio%{so_ver} = %{version}
Suggests:       cfitsio-devel-doc = %{version}
# libcfitsio-devel was last used in openSUSE 13.1 (version 3.350)
Obsoletes:      libcfitsio-devel <= 3.350

%description devel
This package contains headers required when building programs against cfitsio
library.

%package devel-doc
Summary:        Documentation for the cfitsio library
# libcfitsio-doc was last used in openSUSE 12.1 (version 3.280)
Obsoletes:      libcfitsio-doc <= 3.280
# libcfitsio-devel-doc was last used in openSUSE 13.1 (version 3.350)
Provides:       libcfitsio-devel-doc = %{version}
Obsoletes:      libcfitsio-devel-doc <= 3.350
BuildArch:      noarch

%description devel-doc
This package contains documentation for the cfitsio library.

%package -n libcfitsio%{so_ver}
Summary:        Library for manipulating FITS data files

%description -n libcfitsio%{so_ver}
CFITSIO is a library of C and Fortran subroutines for reading and writing data
files in FITS (Flexible Image Transport System) data format. CFITSIO provides
simple high-level routines for reading and writing FITS files that insulate the
programmer from the internal complexities of the FITS format. CFITSIO also
provides many advanced features for manipulating and filtering the information
in FITS files.

%prep
%autosetup -p1

%build
%cmake \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/cfitsio \
  -DUSE_BZIP2=ON \
  -DTESTS=ON \
  -DUTILS=ON \
%ifarch x86_64
  -DUSE_SSE2=ON \
%endif
  %{nil}

%cmake_build

%install
%cmake_install

%check
# testsuite
%ctest

%ldconfig_scriptlets -n libcfitsio%{so_ver}

%files
%doc README.md docs/{changes.txt,fpackguide.pdf}
%license licenses/NASA_Open_Source_Agreement_1.3.txt
%{_bindir}/fitscopy
%{_bindir}/fitsverify
%{_bindir}/fpack
%{_bindir}/funpack

%files devel
%license licenses/NASA_Open_Source_Agreement_1.3.txt
%{_includedir}/%{name}/
%{_libdir}/libcfitsio.so
%{_libdir}/pkgconfig/cfitsio.pc
%{_libdir}/cmake/%{name}/
%{_libdir}/%{name}-%{version}/

%files devel-doc
%doc docs/{cfitsio.ps,cfortran.doc,fitsio.doc,fitsio.ps,quick.ps}

%files -n libcfitsio%{so_ver}
%license licenses/NASA_Open_Source_Agreement_1.3.txt
%{_libdir}/libcfitsio.so.%{so_ver}*

%changelog
