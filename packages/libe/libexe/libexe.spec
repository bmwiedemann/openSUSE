#
# spec file for package libexe
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


%define lname	libexe1
Name:           libexe
Version:        20210424
Release:        0
Summary:        Library to access the executable (EXE) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libexe
Source:         %{name}-%{version}.tar.xz
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
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
libexe is a library and related tools to access the executable (EXE) format.

At the moment the goal of this project is to provide functionality to parse EXE (PE/COFF) and the resources stored in them using libwrc. This functionality is used in libevt and libevx to parse EventLog messages from PE/COFF message files.

Part of the libyal family of libraries.

%package -n %{lname}
Summary:        Library to access the executable (EXE) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libexe is a library and related tools to access the executable (EXE) format.

At the moment the goal of this project is to provide functionality to parse EXE (PE/COFF) and the resources stored in them using libwrc. This functionality is used in libevt and libevx to parse EventLog messages from PE/COFF message files.

Part of the libyal family of libraries.

%package tools
Summary:        Tools to access Microsoft executable (EXE) format files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools to access Microsoft executable (EXE) format files including PE/COFF formats.

%package devel
Summary:        Development files for libexe
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Microsoft EXE file support for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libexe.

%package -n python3-%name
Summary:        Python bindings for libexe
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
#python-%name was previously the name of this submodule.  It was python2 bindings.
Obsoletes:      python-%name <= 20181128

%description -n python3-%name
Python bindings for libexe.  Libexe is a part of the libyal family of libraries.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libexe.so.*

%files tools
%license COPYING*
%_bindir/exeinfo
%_mandir/man1/exeinfo.1*

%files devel
%license COPYING*
%{_includedir}/libexe.h
%{_includedir}/libexe/
%{_libdir}/libexe.so
%{_libdir}/pkgconfig/libexe.pc
%{_mandir}/man3/libexe.3*

%files -n python3-%name
%python3_sitearch/pyexe.so

%changelog
