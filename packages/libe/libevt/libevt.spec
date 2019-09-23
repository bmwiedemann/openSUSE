#
# spec file for package libevt
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


Name:           libevt
%define lname	libevt1
%define timestamp	20181227
Version:        0~%timestamp
Release:        0
Summary:        Library and tools to access the Windows Event Log (EVT) format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libevt/wiki
Source:         https://github.com/libyal/libevt/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
Source2:        Windows_Event_Log_EVT.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio) >= 20120426
BuildRequires:  pkgconfig(libcdata) >= 20120425
BuildRequires:  pkgconfig(libcdirectory) >= 20120423
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20120701
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libexe) >= 20120405
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfdatetime) >= 20120522
BuildRequires:  pkgconfig(libfguid) >= 20120426
BuildRequires:  pkgconfig(libfwevt) >= 20160103
BuildRequires:  pkgconfig(libregf) >= 20120405
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRequires:  pkgconfig(libwrc) >= 20120405

#plaso/run_tests.py fails with this external package
#verified 2.1.2016
#BuildRequires:  pkgconfig(libfvalue) >= 20151226
#BuildRequires:  pkgconfig(libfwnt) >= 20151206
# build fails with version in factory, use internal version
#verified 2.1.2016
#BuildRequires:  pkgconfig(libcstring) >= 20150101
#BuildRequires:  pkgconfig(libcerror) >= 20150407
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libevt is a library and tools to access the Windows Event Log
(EVT) format.
For the Windows XML Event Log (EVTX) format, see libevtx.

%package -n %lname
Summary:        Library to access the Windows Event Log (EVT) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libevt is a library and tools to access the Windows Event Log
(EVT) format.
For the Windows XML Event Log (EVTX) format, see libevtx.

%package tools
Summary:        Utilities to export events from Windows Event Log files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools for reading Windows Event Log (EVT) files. These include
evtinfo and evtexport. See evtxtools for Windows XML Event Log (EVTX)
programs.
 
%package devel
Summary:        Development files for libevt, a Windows event file parser
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libevt is a library to access the Windows Event Log (EVT) format.  

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-%name
Summary:        Python bindings for libevt, a Windows event file parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
Requires:       python
Provides:       pyevt = %version

%description -n python-%name
Python bindings for libevt, which can read Windows event files.

%prep
%setup -qn libevt-%timestamp
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
%doc AUTHORS ChangeLog README
%license COPYING 
%_libdir/libevt.so.*

%files tools
%defattr(-,root,root)
%_bindir/evt*
%_mandir/man1/evt*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README Windows_Event_Log*.pdf
%license COPYING 
%_includedir/libevt.h
%_includedir/libevt/
%_libdir/libevt.so
%_libdir/pkgconfig/libevt.pc
%_mandir/man3/libevt.3*

%files -n python-%name
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING 
%python_sitearch/pyevt.so

%changelog
