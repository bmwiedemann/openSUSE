#
# spec file for package libbde
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


%define lname	libbde1
Name:           libbde
Version:        20210605
Release:        0
Summary:        Library and tools to access Microsoft Bitlocker Disk Encrypted partitions
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libbde
Source:         https://github.com/libyal/libbde/releases/download/%version/libbde-alpha-%version.tar.gz
Source2:        BitLocker_Drive_Encryption_BDE_format.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcaes) >= 20201012
BuildRequires:  pkgconfig(libcdata) >= 20210625
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20210526
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
libbde is a library and tools to access the BitLocker Drive Encryption (BDE) format. The BDE format is used by Windows, as of Vista, to encrypt data on a storage media volume.

Supported BDE formats:

BitLocker Windows Vista
BitLocker Windows 7
BitLocker Windows 8 (Consumer Preview)
BitLocker To Go
Supported protection methods:

clear key
password
recovery password
start-up key
FKEV and/or TWEAK key data
Additional features:

support for partial encrypted volumes
zeros out the BDE metadata, matches behavior seen on Windows
Work in progress:

Dokan library support
Multi-threading support

%package -n %{lname}
Summary:        Library to access Microsoft Bitlocker Drive Encrypted volumes
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libbde is a library to access the BitLocker Drive Encryption (BDE) format. The BDE format is used by Windows, as of Vista, to encrypt data on a storage media volume.

%package tools
Summary:        Tools to access Microsoft Bitlocker Drive Encrypted volumes
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools to access the BitLocker Drive Encryption (BDE) format. The BDE format is used by Windows, as of Vista, to encrypt data on a storage media volume.

%package devel
Summary:        Development files for libbde, used to access Bitlocker Drive Encrypted Volumes
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libbde is a library to access the BitLocker Drive Encryption (BDE) format. The BDE format is used by Windows, as of Vista, to encrypt data on a storage media volume.

This subpackage contains libraries and header files for developing
applications that want to make use of libbde.

%package -n python3-%{name}
Summary:        Python 3 bindings for libbde, a Bitlocker Drive Encryption library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description -n python3-%{name}
Python 3 bindings for libbde, which can access Bitlocker Drive Encrypted volumes

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
# we have static libs for some reason, trash them
find %{buildroot} -name "*.a" -print -delete

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libbde.so.*

%files tools
%license COPYING*
%{_bindir}/bde*
%{_mandir}/man1/bde*.1*

%files devel
%license COPYING*
%doc BitLocker_Drive_Encryption_*.pdf
%{_includedir}/libbde.h
%{_includedir}/libbde/
%{_libdir}/libbde.so
%{_libdir}/pkgconfig/libbde.pc
%{_mandir}/man3/libbde.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pybde.so

%changelog
