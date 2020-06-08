#
# spec file for package libEMF
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libEMF
Version:        1.0.12
Release:        0
Summary:        Library for Manipulation with Enhanced MetaFile (EMF, ECMA-234)
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/Libraries
URL:            http://libemf.sourceforge.net/
Source:         http://downloads.sourceforge.net/libemf/libemf-%{version}.tar.gz
Patch2:         ppc64le-support.patch
BuildRequires:  gcc-c++
# taken from includes/wine/winnt.h
ExclusiveArch:  alpha %{arm} aarch64 %{ix86} mips ppc ppc64 ppc64le sparc s390 s390x x86_64

%description
LibEMF is a C/C++ library that provides a drawing toolkit based on
ECMA-234. The general purpose of this library is to create vector
graphics files on POSIX systems that can be imported into StarOffice or
OpenOffice. The Enhanced MetaFile (EMF) is one of the two color vector
graphics format that is "vectorially" understood by SO and OO. The EMF
format also has the additional advantage that it can be "broken" into
its constituent components and edited like any other SO or OO graphics
object.

%package -n libEMF1
Summary:        Library for manipulation with Enhanced MetaFile (EMF, ECMA-234)
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libEMF1
LibEMF is a C/C++ library which provides a drawing toolkit based on
ECMA-234. The general purpose of this library is to create vector
graphics files on POSIX systems which can be imported into
StarOffice/OpenOffice. The Enhanced MetaFile (EMF) is one of the two
color vector graphics format which is "vectorially" understood by
SO/OO. The EMF format also has the additional advantage that it can be
"broken" into its constituent components and edited like any other
SO/OO graphics object.

%package utils
Summary:        Library for manipulation with Enhanced MetaFile (EMF, ECMA-234)
# split-provides for upgrade from openSUSE <= 12.1 and SLE <= 11
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
Provides:       %{name}:%{_bindir}/printemf

%description utils
LibEMF is a C/C++ library which provides a drawing toolkit based on
ECMA-234. The general purpose of this library is to create vector
graphics files on POSIX systems which can be imported into
StarOffice/OpenOffice. The Enhanced MetaFile (EMF) is one of the two
color vector graphics format which is "vectorially" understood by
SO/OO. The EMF format also has the additional advantage that it can be
"broken" into its constituent components and edited like any other
SO/OO graphics object.

%package devel
Summary:        Library for manipulation with Enhanced MetaFile (EMF, ECMA-234)
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libEMF1 = %{version}

%description devel
LibEMF is a C/C++ library which provides a drawing toolkit based on
ECMA-234. The general purpose of this library is to create vector
graphics files on POSIX systems which can be imported into
StarOffice/OpenOffice. The Enhanced MetaFile (EMF) is one of the two
color vector graphics format which is "vectorially" understood by
SO/OO. The EMF format also has the additional advantage that it can be
"broken" into its constituent components and edited like any other
SO/OO graphics object.

%prep
%setup -q -n libemf-%{version}
%patch2 -p1

%build
%configure\
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n libEMF1 -p /sbin/ldconfig
%postun -n libEMF1 -p /sbin/ldconfig

%files -n libEMF1
%license COPYING.LIB
%{_libdir}/*.so.*

%files utils
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*

%files devel
%doc doc/html
%{_includedir}/libEMF
%{_libdir}/*.so

%changelog
