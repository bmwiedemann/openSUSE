#
# spec file for package libqcow
#
# Copyright (c) 2021 SUSE LLC
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


%define lname	libqcow1
Name:           libqcow
Version:        20210419
Release:        0
Summary:        Library and tooling to access the QEMU Copy-On-Write (QCOW) image format
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libqcow
Source:         %{name}-%{version}.tar.xz
Source2:        QEMU_Copy-On-Write_file_format.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcaes) >= 20201012
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib) >= 1.2.5

%description
Library and tooling to access the QEMU Copy-On-Write (QCOW) image format.

Read supported QCOW formats:

version 1
version 2
Supported QCOW format features:

compression
encryption
QCOW format features not supported at the moment:

backing file-based snapshots
in-image snapshots
Work in progress:

Python bindings
Dokan library support
Planned:

version 3 support
Multi-threading support

%package -n %{lname}
Summary:        Library to access the QEMU Copy-On-Write (QCOW) image format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to access the QEMU Copy-On-Write (QCOW) image format.

Read supported QCOW formats:

version 1
version 2
Supported QCOW format features:

compression
encryption
QCOW format features not supported at the moment:

backing file-based snapshots
in-image snapshots

%package tools
Summary:        Tools to access the QEMU Copy-On-Write (QCOW) image format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools to access the QEMU Copy-On-Write (QCOW) image format.

Read supported QCOW formats:

version 1
version 2
Supported QCOW format features:

compression
encryption
QCOW format features not supported at the moment:

backing file-based snapshots
in-image snapshots

%package devel
Summary:        Development files for libqcow
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libqcow is a library to access the QEMU Copy-On-Write (QCOW) image format.

This subpackage contains libraries and header files for developing
applications that want to make use of libqcow.

%package -n python3-%{name}
Summary:        Python 3 bindings for libqcow
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description -n python3-%{name}
Python 3 bindings for libqcow, which can access the QEMU Copy-On-Write (QCOW) image format

%prep
%autosetup -p1
cp "%{SOURCE2}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libqcow.so.*

%files tools
%license COPYING*
%{_bindir}/qcow*
%{_mandir}/man1/qcow*.1*

%files devel
%doc QEMU_Copy-On-Write_file_format.pdf
%license COPYING*
%{_includedir}/libqcow.h
%{_includedir}/libqcow/
%{_libdir}/libqcow.so
%{_libdir}/pkgconfig/libqcow.pc
%{_mandir}/man3/libqcow.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyqcow.so

%changelog
