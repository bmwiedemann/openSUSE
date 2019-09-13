#
# spec file for package libwrc
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


Name:           libwrc
%define lname	libwrc1
%define timestamp 20181203
Version:        0~%timestamp
Release:        0
Summary:        Library to support the Windows Resource Compiler format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libwrc/wiki
Source:         https://github.com/libyal/libwrc/releases/download/%timestamp/%name-experimental-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20120426
BuildRequires:  pkgconfig(libcdata) >= 20120425
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130904
BuildRequires:  pkgconfig(libexe) >= 20120405
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfdatetime) >= 20130317
BuildRequires:  pkgconfig(libfguid) >= 20130317
BuildRequires:  pkgconfig(libfvalue) >= 20120428
BuildRequires:  pkgconfig(libfwevt) >= 20120426
BuildRequires:  pkgconfig(libfwnt) >= 20120426
BuildRequires:  pkgconfig(libuna) >= 20130728
#  The following packages cause build failures if factory version is used, 
# verified 1/12/2015
#BuildRequires:  pkgconfig(libcerror) >= 20120425
#BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libwrc is a library to support the Windows Resource Compiler format.

%package -n %lname
Summary:        Library to support the Windows Resource Compiler format
Group:          System/Libraries

%description -n %lname
libwrc is a library to support the Windows Resource Compiler format.

%package devel
Summary:        Development files for libwrc, a Windows Resouce Compiler format support library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libwrc is a library to support the Windows Resource Compiler format.

This subpackage contains libraries and header files for developing
applications that want to make use of libwrc.

%package tools
Summary:        Utilities to inspect Windows Resource Compiler files
Group:          Productivity/File utilities

%description tools
This subpackage provides the utilities from libwrc, which allows for
reading Windows Resource Compiler files.

%prep
%setup -qn libwrc-%timestamp

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
%_libdir/libwrc.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libwrc*
%_libdir/libwrc.so
%_libdir/pkgconfig/libwrc.pc
%_mandir/man3/libwrc.3*

%files tools
%defattr(-,root,root)
%_bindir/wrcinfo
%_mandir/man1/wrcinfo.1*

%changelog
