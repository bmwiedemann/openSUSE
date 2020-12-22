#
# spec file for package libfshfs
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


%define lname	libfshfs1
%define timestamp 20201104
Name:           libfshfs
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tools to access the Mac OS Hierarchical File System (HFS)
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfshfs/wiki
Source:         https://github.com/libyal/libfshfs/releases/download/%timestamp/%{name}-experimental-%{timestamp}.tar.gz

BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20170101
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfguid) >= 20130317
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libhmac)
BuildRequires:  pkgconfig(python3)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Read-only supported HFS formats:

* HFS+, Mac OS 10.3 and later (Unicode 3.2 case-insensitive)
* HFSX, Mac OS 10.3 and later (Unicode 3.2 case-sensitive)

Unsupported HFS formats:

* (traditional) HFS
* HFS+, Mac OS 8.1 through 10.2 (Unicode 2.1 case-insensitive)
* HFSX, Mac OS 8.1 through 10.2 (Unicode 2.1 case-sensitive)

Supported HFS format features:

* ZLIB (DEFLATE) compression
* LZVN compression

Unsupported HFS format features:

* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10

Planned:

* Complete resource fork support
* Complete named fork (extended attributes) support

%package -n %{lname}
Summary:        Library and tools to access the Mac OS Hierarchical File System (HFS)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Read-only supported HFS formats:

* HFS+, Mac OS 10.3 and later (Unicode 3.2 case-insensitive)
* HFSX, Mac OS 10.3 and later (Unicode 3.2 case-sensitive)

Unsupported HFS formats:

* (traditional) HFS
* HFS+, Mac OS 8.1 through 10.2 (Unicode 2.1 case-insensitive)
* HFSX, Mac OS 8.1 through 10.2 (Unicode 2.1 case-sensitive)

Supported HFS format features:

* ZLIB (DEFLATE) compression
* LZVN compression

Unsupported HFS format features:

* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10

Planned:

* Complete resource fork support
* Complete named fork (extended attributes) support


%package tools
Summary:        Tools to access the Mac OS Hierarchical File System (HFS) 
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to access the Mac OS Hierarchical File System (HFS).  See libfshfs for additional details.

%package devel
Summary:        Development files for libfshfs, Mac OS Hierarchical File System (HFS) library 
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libfshfs is a library to access the Mac OS Hierarchical File System (HFS) format.  see libfshfs for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libfshfs.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfshfs, a Mac OS Hierarchical FIle System (HFS) parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
Provides:       pyfshfs

%description -n python3-%{name}
libfshfs is a library to access Mac OS Hierarchical File System (HFS) format. See libfshfs for details.

This package contains Python 3 bindings for libfshfs.

%prep
%setup -q -n libfshfs-%{timestamp}

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
%{_libdir}/libfshfs.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/fshfs*
%{_mandir}/man1/fshfs*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{_includedir}/libfshfs.h
%{_includedir}/libfshfs/
%{_libdir}/libfshfs.so
%{_libdir}/pkgconfig/libfshfs.pc
%{_mandir}/man3/libfshfs.3*

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{python3_sitearch}/pyfshfs.so

%changelog
