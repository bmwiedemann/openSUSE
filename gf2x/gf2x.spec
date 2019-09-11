#
# spec file for package gf2x
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gf2x
%define lname	libgf2x-1_2
Version:        1.2
Release:        0
Summary:        Library for multiplication over the GF(2) field
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            https://gforge.inria.fr/projects/gf2x/

# Caution: the filename does not matter - the ID (36934) determines which source you get.
Source:         https://gforge.inria.fr/frs/download.php/36934/%name-%version.tar.gz
Patch1:         0001-build-fix-version-info-for-libgf2x-after-ABI-break.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  libtool

%description
gf2x is a library for multiplication of polynomials over the
GF(2) binary field.

%package -n %lname
Summary:        Library for multiplication over the GF(2) field
Group:          System/Libraries

%description -n %lname
gf2x is a library for multiplication of polynomials over the
GF(2) binary field.

%package devel
Summary:        Development headers for libgf2x
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
gf2x is a library for fast multiplication of polynomials over the
GF(2) binary field.

This package contains the interface definitions for the gf2x library.
 
%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fi
# SSE2 may not be available on all x86_32 machines.
# PCLMUL may not be available on all machines.
%configure --disable-static \
%ifarch %ix86
	--disable-sse2 \
%endif
	--disable-pclmul
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libgf2x-1.2.so
%doc COPYING

%files devel
%defattr(-,root,root)
%_includedir/gf2x*
%_libdir/libgf2x.so

%changelog
