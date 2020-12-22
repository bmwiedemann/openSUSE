#
# spec file for package libfsext
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


%define lname	libfsext1
%define timestamp 20201107
Name:           libfsext
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tools to access the Extended File System
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfsext/wiki
Source:         https://github.com/libyal/libfsext/releases/download/%timestamp/%{name}-experimental-%{timestamp}.tar.gz

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
libfsext is a library to access the Extended File System (ext).

Read-only supported ext formats:

* ext2 (version 2)
* ext3 (version 3)
* ext4 (version 4)

Supported ext format features:

* ext4 inline data

Unsupported ext format features:

* ext (version 1)
* compression
* encryption

%package -n %{lname}
Summary:        Library to access the Extended File System (ext)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libfsext is a library to access the Extended File System (ext).

Read-only supported ext formats:

* ext2 (version 2)
* ext3 (version 3)
* ext4 (version 4)

Supported ext format features:

* ext4 inline data

Unsupported ext format features:

* ext (version 1)
* compression
* encryption

%package tools
Summary:        Tools to access the Extended File System (ext)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to access the Extended File System.  See libfsext for additional details.

%package devel
Summary:        Development files for libfsext, Extended File System (ext) library 
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libfsext is a library to access the extended file system (ext) format.  see libfsext for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libfsext.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfsext, a extended file system (ext) parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
Provides:       pyfsext

%description -n python3-%{name}
libfsext is a library to access extended file system (ext) format. See libfsext for details.

This package contains Python 3 bindings for libfsext.

%prep
%setup -q -n libfsext-%{timestamp}

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
%{_libdir}/libfsext.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/fsext*
%{_mandir}/man1/fsext*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{_includedir}/libfsext.h
%{_includedir}/libfsext/
%{_libdir}/libfsext.so
%{_libdir}/pkgconfig/libfsext.pc
%{_mandir}/man3/libfsext.3*

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{python3_sitearch}/pyfsext.so

%changelog
