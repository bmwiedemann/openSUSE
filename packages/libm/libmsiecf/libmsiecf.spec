#
# spec file for package libmsiecf
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


Name:           libmsiecf
%define lname	libmsiecf1
Version:        20210506
Release:        0
Summary:        Library to parse MS Internet Explorer Cache Files
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libmsiecf
Source:         %name-%version.tar.xz
Source2:        MSIE_Cache_File_index.dat_format.pdf
Patch1:         system-libs.patch
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
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
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libuna) >= 20201204
%python_subpackages

%description
libmsiecf is a library to parse MS Internet Explorer Cache Files.

%package -n %lname
Summary:        Library to parse MS Internet Explorer Cache Files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libmsiecf is a library to parse MS Internet Explorer Cache Files.

%package tools
Summary:        Utilities to inspect MS Internet Explorer Cache Files
License:        LGPL-3.0-or-later
Group:          System/Filesystems

%description tools
Several tools for reading MS Internet Explorer Cache files.

%package devel
Summary:        Development files for %name
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libmsiecf is a library to parse MS Internet Explorer Cache Files.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
autoreconf -fi
# OOT builds are presently broken, so we have to install
# within each python iteration now, not in %%install.
%{python_expand #
%configure --disable-static --enable-wide-character-type --enable-python PYTHON_VERSION="%{$python_bin_suffix}"
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
%_libdir/libmsiecf.so.*

%files -n %name-tools
%_bindir/msiecf*
%_mandir/man1/msiecf*.1*

%files -n %name-devel
%doc MSIE_Cache_File*.pdf
%_includedir/libmsiecf.h
%_includedir/libmsiecf/
%_libdir/libmsiecf.so
%_libdir/pkgconfig/libmsiecf.pc
%_mandir/man3/libmsiecf.3*

%files %python_files
%license COPYING*
%python_sitearch/pymsiecf.so

%changelog
