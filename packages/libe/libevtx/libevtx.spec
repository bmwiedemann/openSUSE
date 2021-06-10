#
# spec file for package libevtx
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


%bcond_without python2
%define lname	libevtx1
Name:           libevtx
Version:        20210504
Release:        0
Summary:        Library and tools to access the Windows XML Event Log (EVTX) format
License:        GFDL-1.3-only AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libevtx
Source:         %name-%version.tar.xz
Source2:        Windows_XML_Event_Log_EVTX.pdf
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
%if %{with python2}
BuildRequires:  pkgconfig(python2)
%endif
BuildRequires:  pkgconfig(python3)

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
License:        GFDL-1.3-only AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libevtx is a library to access the Windows XML Event log format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python2-%name
Summary:        Python2 bindings for libevtx
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Obsoletes:      pyevtx <= 20191221
Obsoletes:      python-%name <= 20191221

%description -n python2-%name
Python bindings for libevtx, which can read Windows XML Event files.

%package -n python3-%name
Summary:        Python bindings for libevtx
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python

%description -n python3-%name
Python bindings for libevtx, which can read Windows XML Event files.

%prep
%autosetup -p1
cp "%SOURCE2" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure \
    --disable-static \
    --enable-wide-character-type \
%if %{with python2}
    --enable-python2 \
%endif
    --enable-python3
%make_build

%install
%make_install
find %buildroot -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libevtx.so.*

%files tools
%_bindir/evtx*
%_mandir/man1/evt*.1*

%files devel
%doc Windows_XML_Event_Log*.pdf
%_includedir/libevtx.h
%_includedir/libevtx/
%_libdir/libevtx.so
%_libdir/pkgconfig/libevtx.pc
%_mandir/man3/libevtx.3*

%if %{with python2}
%files -n python2-%name
%license COPYING*
%python2_sitearch/pyevtx.so
%endif

%files -n python3-%name
%license COPYING*
%python3_sitearch/pyevtx.so

%changelog
