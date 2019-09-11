#
# spec file for package liblnk
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


Name:           liblnk
%define lname	liblnk1
%define timestamp 	20181227
Version:        0~%timestamp
Release:        0
Summary:        Library and tools to access the Windows Shortcut File (LNK) format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/liblnk/wiki
Source:         https://github.com/libyal/liblnk/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
Source2:        Windows_Shortcut_File_LNK_format.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20130904
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20130609
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libfdatetime) >= 20130317
BuildRequires:  pkgconfig(libfguid) >= 20130904
BuildRequires:  pkgconfig(libuna) >= 20120425
#BuildRequires:  pkgconfig(libfwsi) >= 20120426 (not yet stable per upstream 9/2014)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
liblnk is a library and tools to access Windows Shortcut File (LNK) format files.

%package -n %lname
Summary:        Library to access the Windows Shortcut File (LNK) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
liblnk is a library to access Windows Shortcut File (LNK) files.

%package tools
Summary:        Tools to access the Windows Shortcut File (LNK) format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
liblnk is a library to access Windows Shortcut File (LNK) files.
 
%package devel
Summary:        Development files for liblnk, a library to access Windows Shortcut Links
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
liblnk is a library to access Windows Shortcut File (LNK) files.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-%name
Summary:        Python bindings for liblnk, a Windows Shortcut Link parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
Requires:       python
Provides:       pylnk = %version

%description -n python-%name
Python binding for liblnk, which can read Windows Shortcut Link files.

%prep
%setup -qn liblnk-%timestamp
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
%_libdir/liblnk.so.*

%files tools
%defattr(-,root,root)
%_bindir/lnk*
%_mandir/man1/lnkinfo.1*

%files devel
%defattr(-,root,root)
%doc Windows_Shortcut_File_*.pdf
%_includedir/liblnk.h
%_includedir/liblnk/
%_libdir/liblnk.so
%_libdir/pkgconfig/liblnk.pc
%_mandir/man3/liblnk.3*

%files -n python-%name
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING 
%python_sitearch/pylnk.so

%changelog
