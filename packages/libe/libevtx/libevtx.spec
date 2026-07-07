#
# spec file for package libevtx
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname	libevtx1
Name:           libevtx
Version:        20260705
Release:        0
Summary:        Library and tools to access the Windows XML Event Log (EVTX) format
License:        GFDL-1.3-only AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libevtx
Source:         https://github.com/libyal/libevtx/releases/download/%version/%name-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libevtx/releases/download/%version/%name-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source10:       Windows_XML_Event_Log_EVTX.pdf
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20260623
BuildRequires:  pkgconfig(libcdata) >= 20260703
BuildRequires:  pkgconfig(libcdirectory) >= 20260703
BuildRequires:  pkgconfig(libcerror) >= 20260703
BuildRequires:  pkgconfig(libcfile) >= 20260704
BuildRequires:  pkgconfig(libclocale) >= 20260703
BuildRequires:  pkgconfig(libcnotify) >= 20260703
BuildRequires:  pkgconfig(libcpath) >= 20260703
BuildRequires:  pkgconfig(libcsplit) >= 20260703
BuildRequires:  pkgconfig(libcthreads) >= 20260703
BuildRequires:  pkgconfig(libexe) >= 20260705
BuildRequires:  pkgconfig(libfcache) >= 20260520
BuildRequires:  pkgconfig(libfdata) >= 20260521
BuildRequires:  pkgconfig(libfdatetime) >= 20260521
BuildRequires:  pkgconfig(libfguid) >= 20260521
BuildRequires:  pkgconfig(libfvalue) >= 20260531
BuildRequires:  pkgconfig(libfwevt) >= 20260702
BuildRequires:  pkgconfig(libfwnt) >= 20260602
BuildRequires:  pkgconfig(libregf) >= 20260526
BuildRequires:  pkgconfig(libuna) >= 20260602
BuildRequires:  pkgconfig(libwrc) >= 20260705
BuildRequires:  pkgconfig(python3)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

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
Requires:       libbfio-devel

%description devel
libevtx is a library to access the Windows XML Event log format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libevtx.so.*

%files -n %name-tools
%_bindir/evtx*
%_mandir/man1/evt*.1*

%files -n %name-devel
%doc Windows_XML_Event_Log*.pdf
%_includedir/libevtx.h
%_includedir/libevtx/
%_libdir/libevtx.so
%_libdir/pkgconfig/libevtx.pc
%_mandir/man3/libevtx.3*

%files %python_files
%license COPYING*
%python_sitearch/pyevtx*

%changelog
