#
# spec file for package libpff
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


Name:           libpff
%define lname	libpff1
Version:        20260926
Release:        0
Summary:        Library and tools to access Microsoft PFF/OFF/PST/OST/PAB files
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libpff
Source:         https://github.com/libyal/libpff/releases/download/%version/libpff-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libpff/releases/download/%version/libpff-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source12:       PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
Source13:       PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
Source14:       Personal_Folder_File_PFF_format.pdf
Source15:       MAPI_definitions.pdf
Source16:       libpff-libfdata.pdf
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20260623
BuildRequires:  pkgconfig(libcdata) >= 20260703
BuildRequires:  pkgconfig(libcerror) >= 20260703
BuildRequires:  pkgconfig(libcfile) >= 20260704
BuildRequires:  pkgconfig(libclocale) >= 20260703
BuildRequires:  pkgconfig(libcnotify) >= 20260703
BuildRequires:  pkgconfig(libcpath) >= 20260703
BuildRequires:  pkgconfig(libcsplit) >= 2026073
BuildRequires:  pkgconfig(libcthreads) >= 20260703
BuildRequires:  pkgconfig(libfcache) >= 20260520
BuildRequires:  pkgconfig(libfdata) >= 20260521
BuildRequires:  pkgconfig(libfdatetime) >= 20260521
BuildRequires:  pkgconfig(libfguid) >= 20260521
BuildRequires:  pkgconfig(libfmapi) >= 20260521
BuildRequires:  pkgconfig(libfvalue) >= 20260531
BuildRequires:  pkgconfig(libfwnt) >= 20260602
BuildRequires:  pkgconfig(libuna) >= 20260602
BuildRequires:  pkgconfig(zlib)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

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
Requires:       libbfio-devel

%description devel
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

%prep
%autosetup -p1
cp -av %_sourcedir/*.pdf .

%build
echo "V_%version { global: *; };" >sym.ver
%{python_expand #
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}"
grep ' '' ''local' config.log && exit 1
%make_build LDFLAGS="-Wl,--version-script=$PWD/sym.ver"
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libpff.so.*

%files -n %name-tools
%license COPYING*
%_bindir/pff*
%_mandir/man1/pff*.1*

%files -n %name-devel
%doc MAPI_definitions.pdf
%doc PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
%doc PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
%doc Personal_Folder_File_*.pdf
%_includedir/libpff.h
%_includedir/libpff/
%_libdir/libpff.so
%_libdir/pkgconfig/libpff.pc
%_mandir/man3/libpff.3*

%files %python_files
%python_sitearch/pypff*

%changelog
