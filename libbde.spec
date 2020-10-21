#
# spec file for package libbde
#
# Copyright (c) 2020 SUSE LLC
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
%define timestamp 20200724
Name:           libbde
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tools to access Microsoft Bitlocker Disk Encrypted partitions
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libbde/wiki
Source:         https://github.com/libyal/libbde/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
Source2:        BitLocker_Drive_Encryption_BDE_format.pdf
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcaes) >= 20130331
BuildRequires:  pkgconfig(libcdata) >= 20130904
BuildRequires:  pkgconfig(libcerror) >= 20120425
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfdatetime) >= 20120522
BuildRequires:  pkgconfig(libfguid) >= 20120426
BuildRequires:  pkgconfig(libfvalue) >= 20120428
BuildRequires:  pkgconfig(libhmac) >= 20130714
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)
# fails to build with factory package, use internal  - verified 2/16/2017
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       %{lname} = %{version}

%description tools
Tools to access the BitLocker Drive Encryption (BDE) format. The BDE format is used by Windows, as of Vista, to encrypt data on a storage media volume.

%package devel
Summary:        Development files for libbde, used to access Bitlocker Drive Encrypted Volumes
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
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
Requires:       %{lname} = %{version}
Requires:       python3

%description -n python3-%{name}
Python 3 bindings for libbde, which can access Bitlocker Drive Encrypted volumes

%prep
%setup -q -n libbde-%{timestamp}
cp "%{SOURCE2}" .

%build
# I haven't tested the usefullness of these args yet
%configure --disable-static --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
# we have static libs for some reason, trash them
find %{buildroot} -name "*.a" -delete

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%license COPYING*
%doc AUTHORS ChangeLog
%{_libdir}/libbde.so.*

%files tools
%defattr(-,root,root)
%license COPYING*
%doc AUTHORS README ChangeLog
%{_bindir}/bde*
%{_mandir}/man1/bde*.1*

%files devel
%defattr(-,root,root)
%license COPYING*
%doc AUTHORS README ChangeLog
%doc BitLocker_Drive_Encryption_*.pdf
%{_includedir}/libbde.h
%{_includedir}/libbde/
%{_libdir}/libbde.so
%{_libdir}/pkgconfig/libbde.pc
%{_mandir}/man3/libbde.3*

%files -n python3-%{name}
%defattr(-,root,root)
%license COPYING*
%doc AUTHORS README ChangeLog
%{python3_sitearch}/pybde.so

%changelog
