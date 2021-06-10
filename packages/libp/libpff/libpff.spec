#
# spec file for package libpff
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


Name:           libpff
%define lname	libpff1
Version:        20210508
Release:        0
Summary:        Library and tools to access Microsoft PFF and OFF format files
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libpff
Source:         %name-%version.tar.xz
Source2:        PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
Source3:        PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
Source4:        Personal_Folder_File_PFF_format.pdf
Source5:        MAPI_definitions.pdf
Source6:        libpff-libfdata.pdf
Patch1:         system-libs.patch
Patch2:         pkgconfig.diff
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
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libfmapi) >= 20180714
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libfwnt) >= 20210421
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)

%description
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

%package -n %lname
Summary:        Library to access Microsoft PFF and OFF format files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

%package tools
Summary:        Tools to access Microsoft PST and OST files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
Tools to access the Personal Folder File (PFF) and the Offline Folder
File (OFF) format. These are used in several file types: PAB
(Personal Address Book), PST (Personal Storage Table) and OST
(Offline Storage Table).

%package devel
Summary:        Development files for libpff, a PFF/OFF file format library
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

%package -n python3-%name
Summary:        Python bindings for libpff, a PFF/OFF file format parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
#python-%name was previously the name of this submodule.  It was python2 bindings.
Obsoletes:      python-%name <= 20180714

%description -n python3-%name
Python bindings for libpff, which can read Personal Folder File (PFF)
and Offline Folder File (OFF) formats.

%prep
%autosetup -p1
cp "%{S:2}" "%{S:3}" "%{S:4}" "%{S:5}" "%{S:6}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
# Package has a history of not bumping on ABI breaks (e.g. 59bcd7a46e)
echo "V_%version { global: *; };" >sym.ver
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build LDFLAGS="-Wl,--version-script=$PWD/sym.ver"

%install
%make_install
find "%buildroot" -name "*.la" -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libpff.so.*

%files tools
%license COPYING*
%_bindir/pff*
%_mandir/man1/pff*.1*

%files devel
%doc MAPI_definitions.pdf
%doc PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
%doc PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
%doc Personal_Folder_File_*.pdf
%_includedir/libpff.h
%_includedir/libpff/
%_libdir/libpff.so
%_libdir/pkgconfig/libpff.pc
%_mandir/man3/libpff.3*

%files -n python3-%name
%python3_sitearch/pypff.so

%changelog
