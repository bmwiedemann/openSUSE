#
# spec file for package libexe
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


%define lname	libexe1
Name:           libexe
Version:        20260524
Release:        0
Summary:        Library to access the executable (EXE) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libexe
Source:         https://github.com/libyal/libexe/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libexe/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcdata) >= 20260520
BuildRequires:  pkgconfig(libcerror) >= 20260513
BuildRequires:  pkgconfig(libcfile) >= 20260520
BuildRequires:  pkgconfig(libclocale) >= 20260520
BuildRequires:  pkgconfig(libcnotify) >= 20260520
BuildRequires:  pkgconfig(libcpath) >= 20260520
BuildRequires:  pkgconfig(libcsplit) >= 20260520
BuildRequires:  pkgconfig(libcthreads) >= 20260518
BuildRequires:  pkgconfig(libfcache) >= 20260520
BuildRequires:  pkgconfig(libfdata) >= 20240415
BuildRequires:  pkgconfig(libfdatetime) >= 20260521
BuildRequires:  pkgconfig(libuna) >= 20260522
%python_subpackages

%description
libexe is a library and related tools to parse .exe files
(specifically PE/COFF) and the resources stored in them using
libwrc. This functionality is used in libevt and libevx to parse
EventLog messages from PE/COFF message files.

%package -n %lname
Summary:        Library to access the executable (EXE) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libexe is a library and related tools to parse .exe files
(specifically PE/COFF) and the resources stored in them using
libwrc. This functionality is used in libevt and libevx to parse
EventLog messages from PE/COFF message files.

%package tools
Summary:        Tools to access Microsoft executable (EXE) format files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools to access Microsoft executable (.exe) format files
including PE/COFF formats.

%package devel
Summary:        Development files for libexe
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
Library to provide Microsoft EXE file support for the libyal family
of libraries. libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libexe.

%prep
%autosetup -p1

%build
autoreconf -fi
%{python_expand #
# see libcdata for version-sc
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %buildroot -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libexe.so.*

%files -n %name-tools
%license COPYING*
%_bindir/exeinfo
%_mandir/man1/exeinfo.1*

%files -n %name-devel
%license COPYING*
%_includedir/libexe.h
%_includedir/libexe/
%_libdir/libexe.so
%_libdir/pkgconfig/libexe.pc
%_mandir/man3/libexe.3*

%files %python_files
%python_sitearch/pyexe.so

%changelog
