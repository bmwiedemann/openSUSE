#
# spec file for package libevt
#
# Copyright (c) 2022 SUSE LLC
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
Version:        20221022
Release:        0
Summary:        Library and tools to access the Windows Event Log (EVT) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libevt
Source:         https://github.com/libyal/libevt/releases/download/%version/libevt-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libevt/releases/download/%version/libevt-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source8:        Windows_Event_Log_EVT.pdf
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20220120
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcdirectory) >= 20220105
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libexe) >= 20210424
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20211023
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfvalue) >= 20220120
BuildRequires:  pkgconfig(libfwevt) >= 20220723
BuildRequires:  pkgconfig(libfwnt) >= 20210906
BuildRequires:  pkgconfig(libregf) >= 20220131
BuildRequires:  pkgconfig(libuna) >= 20220611
BuildRequires:  pkgconfig(libwrc) >= 20220720
BuildRequires:  pkgconfig(python3)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

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
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libevt.so.*

%files -n %name-tools
%_bindir/evt*
%_mandir/man1/evt*.1*

%files -n %name-devel
%doc Windows_Event_Log*.pdf
%license COPYING*
%_includedir/libevt.h
%_includedir/libevt/
%_libdir/libevt.so
%_libdir/pkgconfig/libevt.pc
%_mandir/man3/libevt.3*

%files %python_files
%license COPYING*
%python_sitearch/pyevt.so

%changelog
