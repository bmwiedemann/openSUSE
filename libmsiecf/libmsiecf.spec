#
# spec file for package libmsiecf
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


Name:           libmsiecf
%define lname	libmsiecf1
%define timestamp	20181227
Version:        0~%timestamp
Release:        0
Summary:        Library to parse MS Internet Explorer Cache Files
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libmsiecf/wiki
Source:         https://github.com/libyal/libmsiecf/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
Source2:        MSIE_Cache_File_index.dat_format.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio) >= 20120426
BuildRequires:  pkgconfig(libcdata) >= 20190112
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20120701
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcsystem) >= 20150101
BuildRequires:  pkgconfig(libfdatetime) >= 20120522
BuildRequires:  pkgconfig(libfguid) >= 20120426
BuildRequires:  pkgconfig(libfole) >= 20150104
BuildRequires:  pkgconfig(libfvalue) >= 20120428
BuildRequires:  pkgconfig(libuna) >= 20120425
# these packages fail if the factory version is used, verified 1/14/2015
#BuildRequires:  pkgconfig(libcerror) >= 20120425
#BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libmsiecf is a library to parse MS Internet Explorer Cache Files.

%package -n %lname
Summary:        Library to parse MS Internet Explorer Cache Files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libmsiecf is a library to parse MS Internet Explorer Cache Files.

%package tools
Summary:        Utilities to inspect MS Internet Explorer Cache Files
License:        LGPL-3.0-or-later
Group:          System/Filesystems

%description tools
Several tools for reading MS Internet Explorer Cache files.
 
%package devel
Summary:        Development files for %name
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libmsiecf is a library to parse MS Internet Explorer Cache Files.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-%name
Summary:        Python bindings for libmsiecf
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
Requires:       python
Provides:       pymsiecf = %version

%description -n python-%name
Python bindings for libmsiecf, which can read MS IE cache files.

%prep
%setup -qn libmsiecf-%timestamp
cp "%SOURCE2" .

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find %buildroot -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%_libdir/libmsiecf.so.*

%files tools
%defattr(-,root,root)
%_bindir/msiecf*
%_mandir/man1/msiecf*.1*

%files devel
%defattr(-,root,root)
%doc MSIE_Cache_File*.pdf
%_includedir/libmsiecf.h
%_includedir/libmsiecf/
%_libdir/libmsiecf.so
%_libdir/pkgconfig/libmsiecf.pc
%_mandir/man3/libmsiecf.3*

%files -n python-%name
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING 
%python_sitearch/pymsiecf.so

%changelog
