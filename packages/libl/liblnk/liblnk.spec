#
# spec file for package liblnk
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
%define lname	liblnk1
Name:           liblnk
Version:        20210417
Release:        0
Summary:        Library and tools to access the Windows Shortcut File (LNK) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File Utilities
URL:            https://github.com/libyal/liblnk
Source:         %name-%version.tar.xz
Source2:        Windows_Shortcut_File_LNK_format.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfole) >= 20170502
BuildRequires:  pkgconfig(libfwps) >= 20191221
BuildRequires:  pkgconfig(libfwsi) >= 20210419
BuildRequires:  pkgconfig(libuna) >= 20201204

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
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
liblnk is a library to access Windows Shortcut File (LNK) files.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python2-%name
Summary:        Python bindings for liblnk, a Windows Shortcut Link parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
BuildRequires:  pkgconfig(python2)
Obsoletes:      pylnk <= 20191221
Obsoletes:      python-%name <= 20191221

%description -n python2-%name
Python2 binding for liblnk, which can read Windows Shortcut Link files.

%package -n python3-%name
Summary:        Python bindings for liblnk, a Windows Shortcut Link parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
BuildRequires:  pkgconfig(python3)

%description -n python3-%name
Python3 binding for liblnk, which can read Windows Shortcut Link files.

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
%_libdir/liblnk.so.*

%files tools
%_bindir/lnk*
%_mandir/man1/lnkinfo.1*

%files devel
%doc Windows_Shortcut_File_*.pdf
%_includedir/liblnk.h
%_includedir/liblnk/
%_libdir/liblnk.so
%_libdir/pkgconfig/liblnk.pc
%_mandir/man3/liblnk.3*

%if %{with python2}
%files -n python2-%name
%license COPYING*
%python2_sitearch/pylnk.so
%endif

%files -n python3-%name
%license COPYING*
%python3_sitearch/pylnk.so

%changelog
