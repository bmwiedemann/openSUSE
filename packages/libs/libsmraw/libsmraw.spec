#
# spec file for package libsmraw
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


Name:           libsmraw
%define lname	libsmraw1
%define timestamp 20181227
Version:        0~%timestamp
Release:        0
Summary:        Library and tools to access the (split) RAW image format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libsmraw/wiki
Source:         https://github.com/libyal/libsmraw/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20120426
BuildRequires:  pkgconfig(libcdata) >= 20120425
BuildRequires:  pkgconfig(libcerror) >= 20170101
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20120701
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20120701
BuildRequires:  pkgconfig(libfcache) >= 20120425
BuildRequires:  pkgconfig(libfdata) >= 20120425
BuildRequires:  pkgconfig(libfvalue) >= 20120428
BuildRequires:  pkgconfig(libhmac) >= 20120425
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libsmraw is a library to access the storage media RAW format.
The library supports both RAW and split RAW.

%package -n %lname
Summary:        Library and tools to access the (split) RAW image format
Group:          System/Libraries

%description -n %lname
libsmraw is a library to access the storage media RAW format.
The library supports both RAW and split RAW.

%package devel
Summary:        Development files for libsmraw, a (split) RAW image file library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libsmraw is a library to access the storage media RAW format.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmraw.

%package tools
Summary:        Utilities for reading and writing storage media (split) RAW files
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libsmraw to
acquire, export, query and verify storage media (split) RAW files.

%package -n python2-%name
Summary:        Python 2 bindings for libsmraw
Group:          Development/Languages/Python
Requires:       %lname = %version
Requires:       python
Obsoletes:      python-%{name}

%description -n python2-%name
Python 2 bindings for libsmraw, which provides functionality to work
with (split) RAW files.

%package -n python3-%name
Summary:        Python 3 bindings for libsmraw
Group:          Development/Languages/Python
Requires:       %lname = %version
Requires:       python3

%description -n python3-%name
Python 3 bindings for libsmraw, which provides functionality to work
with (split) RAW files.

%prep
%setup -qn libsmraw-%timestamp

%build
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find "%buildroot" -name "*.la" -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%_libdir/libsmraw.so.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%_includedir/libsmraw*
%_libdir/libsmraw.so
%_libdir/pkgconfig/libsmraw.pc
%_mandir/man3/libsmraw.3*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%_bindir/smrawverify
%_bindir/smrawmount
%_mandir/man1/smrawmount.1*

%files -n python2-%name
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%python_sitearch/pysmraw.so

%files -n python3-%name
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%python3_sitearch/pysmraw.so

%changelog
