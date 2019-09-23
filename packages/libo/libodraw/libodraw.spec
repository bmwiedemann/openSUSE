#
# spec file for package libodraw
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


Name:           libodraw
%define lname	libodraw1
%define timestamp 20190118
Version:        0~%timestamp
Release:        0
Summary:        Library and tools to access to optical disc (split) RAW image files
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libodraw/wiki 
Source:         https://github.com/libyal/libodraw/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
Source2:        CUE_sheet_format.pdf
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20120426
BuildRequires:  pkgconfig(libcdata) >= 20120425
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20140105
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20120701
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libuna) >= 20120425
#use internal package, factory version causes build failure
# verified 1/11/2015
#BuildRequires:  pkgconfig(libcsystem) >= 20120425
#BuildRequires:  pkgconfig(libcerror) >= 20120425
#BuildRequires:  pkgconfig(libcstring) >= 20120425
#BuildRequires:  pkgconfig(libhmac)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libodraw is a library to access optical disc (split) RAW images such
as BIN/ISO/CUE.

%package -n %lname
Summary:        Library to access to optical disc (split) RAW image files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libodraw is a library to access optical disc (split) RAW images such
as BIN/ISO/CUE.

%package devel
Summary:        Development files for libodraw, a disc image file library
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libodraw is a library to access optical disc (split) RAW images such
as BIN/ISO/CUE.

This subpackage contains libraries and header files for developing
applications that want to make use of libodraw.

%package tools
Summary:        Utilities for reading BIN/ISO/CUE image files through libodraw
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
This subpackage contains the utility programs from libodraw, which
can read optical disc (split) RAW image files such as BIN/ISO/CUE.

%prep
%setup -qn libodraw-%timestamp
cp "%{S:2}" .

%build
%configure --disable-static --enable-wide-character-type
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%_libdir/libodraw.so.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%doc CUE_*.pdf
%_includedir/libodraw*
%_libdir/libodraw.so
%_libdir/pkgconfig/libodraw.pc
%_mandir/man3/libodraw.3*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%_bindir/odrawverify
%_bindir/odrawinfo
%_mandir/man1/odrawinfo.1*

%changelog
