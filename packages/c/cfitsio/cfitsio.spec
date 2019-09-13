#
# spec file for package cfitsio
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define tar_ver 3450
%define so_ver 7
Name:           cfitsio
Version:        3.450
Release:        0
Summary:        Library for manipulating FITS data files
License:        ISC
Group:          Productivity/Scientific/Other
URL:            http://heasarc.nasa.gov/fitsio/
Source0:        ftp://heasarc.gsfc.nasa.gov/software/fitsio/c/%{name}%{tar_ver}.tar.gz
# PATCH-FIX-OPENSUSE cfitsio-zlib.patch asterios.dramis@gmail.com -- Use system zlib, link programs to shared libcfitsio (based on patches from Fedora and Debian)
Patch0:         cfitsio-zlib.patch
BuildRequires:  gcc-fortran
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

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
Group:          Development/Libraries/Other
Requires:       libcfitsio%{so_ver} = %{version}
Requires:       pkgconfig
Suggests:       cfitsio-devel-doc = %{version}
# libcfitsio-devel was last used in openSUSE 13.1 (version 3.350)
Provides:       libcfitsio-devel = %{version}
Obsoletes:      libcfitsio-devel <= 3.350

%description devel
This package contains headers required when building programs against cfitsio
library.

%package devel-doc
Summary:        Documentation for the cfitsio library
Group:          Documentation/Other
# libcfitsio-doc was last used in openSUSE 12.1 (version 3.280)
Obsoletes:      libcfitsio-doc <= 3.280
# libcfitsio-devel-doc was last used in openSUSE 13.1 (version 3.350)
Provides:       libcfitsio-devel-doc = %{version}
Obsoletes:      libcfitsio-devel-doc <= 3.350

%description devel-doc
This package contains documentation for the cfitsio library.

%package -n libcfitsio%{so_ver}
Summary:        Library for manipulating FITS data files
Group:          System/Libraries

%description -n libcfitsio%{so_ver}
CFITSIO is a library of C and Fortran subroutines for reading and writing data
files in FITS (Flexible Image Transport System) data format. CFITSIO provides
simple high-level routines for reading and writing FITS files that insulate the
programmer from the internal complexities of the FITS format. CFITSIO also
provides many advanced features for manipulating and filtering the information
in FITS files.

%prep
%setup -q -n %{name}
%patch0 -p1

# Remove bundled zlib
pushd zlib
rm -f adler32.c crc32.c crc32.h deflate.c deflate.h infback.c inffast.c \
 inffast.h inffixed.h inflate.c inflate.h inftrees.c inftrees.h trees.c trees.h \
 uncompr.c zconf.h zlib.h zutil.c zutil.h
popd

%build
# lines bellow contain fixes for pkgconfig file bnc#546004, some of them are already fixed by upstream
# so please drop them if they are not needed (in next round of updates)
# Add include dir, multithreading support, zlib dependency
sed -i 's|Cflags: -I${includedir}|Cflags: -D_REENTRANT -I${includedir} -I${includedir}/%{name}|' cfitsio.pc.in
sed -i 's|Libs: -L${libdir} -lcfitsio @LIBS@|Libs: -L${libdir} -lcfitsio|' cfitsio.pc.in
sed -i 's|Libs.private: -lm|Libs.private: @LIBS@ -lz -lm|' cfitsio.pc.in

%configure --enable-reentrant
make shared %{?_smp_mflags}
make fpack %{?_smp_mflags}
make funpack %{?_smp_mflags}

%check
# testsuite
make testprog %{?_smp_mflags}
LD_LIBRARY_PATH=. ./testprog > testprog.lis
diff testprog.lis testprog.out
cmp testprog.fit testprog.std ; echo $?

%install
make DESTDIR=%{buildroot} CFITSIO_INCLUDE=%{buildroot}%{_includedir}/%{name} install

# Remove static libraries
rm -f %{buildroot}%{_libdir}/libcfitsio.a

%post -n libcfitsio%{so_ver} -p /sbin/ldconfig
%postun -n libcfitsio%{so_ver} -p /sbin/ldconfig

%files
%doc README docs/{changes.txt,fpackguide.pdf}
%license License.txt
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
