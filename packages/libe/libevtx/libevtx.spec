#
# spec file for package libevtx
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


Name:           libevtx
%define lname	libevtx1
%define timestamp	20181227
Version:        0~%timestamp
Release:        0
Summary:        Library and tools to access the Windows XML Event Log (EVTX) format
License:        LGPL-3.0-or-later AND GFDL-1.3-only
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libevtx/wiki
Source:         https://github.com/libyal/libevtx/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
Source2:        Windows_XML_Event_Log_EVTX.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
#latest version of these in OBS as of Jan 28, 2016
BuildRequires:  pkgconfig(libbfio) >= 20160108
BuildRequires:  pkgconfig(libcdata) >= 20130407
BuildRequires:  pkgconfig(libcdirectory) >= 20120425
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20150101
BuildRequires:  pkgconfig(libcnotify) >= 20150101
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcsystem) >= 20150629
BuildRequires:  pkgconfig(libexe) >= 20120405
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libregf) >= 20140803
BuildRequires:  pkgconfig(libuna) >= 20130609
BuildRequires:  pkgconfig(libwrc) >= 20140803

#testing fails if the factory package is used, use the internal version
#verified 2/2/2016
#BuildRequires:  pkgconfig(libfvalue) > 20151226
#BuildRequires:  pkgconfig(libfguid) >= 20150104
#BuildRequires:  pkgconfig(libfdatetime) >= 20150507
#BuildRequires:  pkgconfig(libfwnt) >= 20151206
#BuildRequires:  pkgconfig(libfwevt) >= 20160103
#build fails if the factory package is used, use the internal version
#verified 1/28/2016
#BuildRequires:  pkgconfig(libcstring) > 20150101
#BuildRequires:  pkgconfig(libcerror) > 20150407
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library and tools to access the Windows XML Event Log (EVTX) format.
For the Windows pre-XML Event Log (EVT) format, see libevt.

%package -n %lname
Summary:        Library to access the Windows XML Event Log (EVTX) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
Library to access the Windows Event Log (EVT) format.
For the Windows pre-XML Event Log (EVT) format, see libevt.

%package tools
Summary:        Utilities to export events from Windows XML event files (EVTX)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools for parsing EVTX files. These include evtxinfo and evtxexport.

%package devel
Summary:        Development files for libevtx, a Windows XML Event file parser
License:        LGPL-3.0-or-later AND GFDL-1.3-only
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libevtx is a library to access the Windows XML Event log format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-%name
Summary:        Python bindings for libevtx
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
Requires:       python
Provides:       pyevtx = %version

%description -n python-%name
Python bindings for libevtx, which can read Windows XML Event files.

%prep
%setup -qn libevtx-%timestamp
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
%_libdir/libevtx.so.*

%files tools
%defattr(-,root,root)
%_bindir/evtx*
%_mandir/man1/evt*.1*

%files devel
%defattr(-,root,root)
%doc Windows_XML_Event_Log*.pdf
%_includedir/libevtx.h
%_includedir/libevtx/
%_libdir/libevtx.so
%_libdir/pkgconfig/libevtx.pc
%_mandir/man3/libevtx.3*

%files -n python-%name
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING 
%python_sitearch/pyevtx.so

%changelog
