#
# spec file for package libqcow
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


%define lname	libqcow1
%define timestamp 20181227
Name:           libqcow
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tooling to access the QEMU Copy-On-Write (QCOW) image format
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libqcow/wiki
Source:         https://github.com/libyal/libqcow/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
Source2:        QEMU_Copy-On-Write_file_format.pdf
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcaes) >= 20140731
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  pkgconfig(zlib) >= 1.2.5
# using these packages from factory breaks the build, verified 2/25/2107
#BuildRequires:  pkgconfig(libcpath) > 20170108
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       %{lname} = %{version}

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
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
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
Requires:       python3
BuildRequires:  pkgconfig(python3)
Requires:       %{lname} = %{version}

%description -n python3-%{name}
Python 3 bindings for libqcow, which can access the QEMU Copy-On-Write (QCOW) image format

%prep
%setup -q -n libqcow-%{timestamp}
cp "%{SOURCE2}" .

%build
%configure --disable-static --enable-wide-character-type --enable-python3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%{_libdir}/libqcow.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%{_bindir}/qcow*
%{_mandir}/man1/qcow*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%doc QEMU_Copy-On-Write_file_format.pdf
%license COPYING 
%{_includedir}/libqcow.h
%{_includedir}/libqcow/
%{_libdir}/libqcow.so
%{_libdir}/pkgconfig/libqcow.pc
%{_mandir}/man3/libqcow.3*

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING 
%{python3_sitearch}/pyqcow.so

%changelog
