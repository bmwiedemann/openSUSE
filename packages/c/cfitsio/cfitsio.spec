#
# spec file for package cfitsio
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


%define so_ver 10
Name:           cfitsio
Version:        4.2.0
Release:        0
Summary:        Library for manipulating FITS data files
License:        ISC
URL:            https://heasarc.gsfc.nasa.gov/fitsio/
Source0:        https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/%{name}-%{version}.tar.gz
BuildRequires:  gcc-fortran
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bzip2)

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
%setup -q
# Disable build of static library
sed -i -e 's/\(.*:.*\)lib${PACKAGE}.a/\1/' Makefile.in

%build
%configure \
  --enable-reentrant \
  --includedir=%{_includedir}/cfitsio \
  --with-bzip2 \
%ifarch x86_64
  --enable-sse2 \
%endif
  %{nil}

%make_build shared
%make_build fpack funpack fitscopy

%install
%make_install

%check
# testsuite
%make_build testprog
LD_LIBRARY_PATH=. ./testprog > testprog.lis
diff testprog.lis testprog.out
cmp testprog.fit testprog.std ; echo $?

%post -n libcfitsio%{so_ver} -p /sbin/ldconfig
%postun -n libcfitsio%{so_ver} -p /sbin/ldconfig

%files
%doc README docs/{changes.txt,fpackguide.pdf}
%license License.txt
%{_bindir}/fitscopy
%{_bindir}/fpack
%{_bindir}/funpack

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcfitsio.so
%{_libdir}/pkgconfig/cfitsio.pc

%files devel-doc
%doc docs/{cfitsio.ps,cfortran.doc,fitsio.doc,fitsio.ps,quick.ps}

%files -n libcfitsio%{so_ver}
%{_libdir}/libcfitsio.so.%{so_ver}*

%changelog
