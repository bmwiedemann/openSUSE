#
# spec file for package libevt
#
# Copyright (c) 2021 SUSE LLC
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


%define lname	libevt1
Name:           libevt
Version:        20210503
Release:        0
Summary:        Library and tools to access the Windows Event Log (EVT) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libevt
Source:         %name-%version.tar.xz
Source2:        Windows_Event_Log_EVT.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcdirectory) >= 20200702
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libexe) >= 20210424
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libfwevt) >= 20210508
BuildRequires:  pkgconfig(libfwnt) >= 20210421
BuildRequires:  pkgconfig(libregf) >= 20210419
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(libwrc) >= 20210425
BuildRequires:  pkgconfig(python3)

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
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libevt is a library to access the Windows Event Log (EVT) format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python3-%name
Summary:        Python bindings for libevt, a Windows event file parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python

%description -n python3-%name
Python bindings for libevt, which can read Windows event files.

%prep
%autosetup -p1
cp "%SOURCE2" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure \
    --disable-static \
    --enable-wide-character-type \
    --enable-python3
%make_build

%install
%make_install
find %buildroot -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libevt.so.*

%files tools
%_bindir/evt*
%_mandir/man1/evt*.1*

%files devel
%doc Windows_Event_Log*.pdf
%license COPYING*
%_includedir/libevt.h
%_includedir/libevt/
%_libdir/libevt.so
%_libdir/pkgconfig/libevt.pc
%_mandir/man3/libevt.3*

%files -n python3-%name
%license COPYING*
%python3_sitearch/pyevt.so

%changelog
