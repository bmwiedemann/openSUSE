#
# spec file for package libdmtx
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libdmtx
Version:        0.7.5
Release:        0
Summary:        Software for reading and writing Data Matrix barcodes
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            http://libdmtx.sourceforge.net/
Source:         https://github.com/dmtx/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         libdmtx-0.7.4.diff
# PATCH-FIX-UPSTREAM libdmtx-DmtxPropRowPadBytes.patch
Patch1:         libdmtx-DmtxPropRowPadBytes.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libdmtx is open source software for reading and writing Data Matrix barcodes.
At its core libdmtx is a native shared library, allowing C/C++ programs to use
its capabilities without extra restrictions or overhead.

%package -n libdmtx0
Summary:        Software for reading and writing Data Matrix barcodes
Group:          System/Libraries

%description -n libdmtx0
libdmtx is open source software for reading and writing Data Matrix barcodes.
At its core libdmtx is a native shared library, allowing C/C++ programs to use
its capabilities without extra restrictions or overhead.

%package devel
Summary:        Software for reading and writing Data Matrix barcodes
Group:          Development/Libraries/C and C++
Requires:       libdmtx0 = %{version}

%description devel
libdmtx is open source software for reading and writing Data Matrix barcodes.
At its core libdmtx is a native shared library, allowing C/C++ programs to use
its capabilities without extra restrictions or overhead.

%prep
%autosetup -p1
./autogen.sh

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%post -n libdmtx0 -p /sbin/ldconfig
%postun -n libdmtx0 -p /sbin/ldconfig

%files -n libdmtx0
%license LICENSE
%doc AUTHORS ChangeLog KNOWNBUG README
%{_mandir}/man?/*dmtx*
%{_libdir}/libdmtx.so.*

%files devel
%{_includedir}/dmtx.h
%{_libdir}/libdmtx.so
%{_libdir}/pkgconfig/libdmtx.pc

%changelog
