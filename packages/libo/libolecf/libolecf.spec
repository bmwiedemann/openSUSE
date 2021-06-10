#
# spec file for package libolecf
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
%define lname	libolecf1
Name:           libolecf
Version:        20210512
Release:        0
Summary:        Library and tools to access the OLE 2 Compound File (OLECF) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libolecf
Source:         %name-%version.tar.xz
Source2:        OLE_Compound_File_format.pdf
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
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libfwps) >= 20191221
BuildRequires:  pkgconfig(libuna) >= 20201204

%description
Library and tools to access the OLE 2 Compound File (OLECF) format. The OLE 2 Compound File format is used to store certain versions of Microsoft Office files, thumbs.db and other file formats.

%package -n %lname
Summary:        Library to access the OLE 2 Compound File (OLECF) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
Library to access the OLE 2 Compound File (OLECF) format. The OLE 2 Compound File format is used to store certain versions of Microsoft Office files, thumbs.db and other file formats.

%package tools
Summary:        Tools to access the OLE 2 Compound File (OLECF) format
License:        LGPL-3.0-or-later
Group:          System/Filesystems
Requires:       %lname = %version

%description tools
Tools to access the OLE 2 Compound File (OLECF) format. The OLE 2 Compound File format is used to store certain versions of Microsoft Office files, thumbs.db and other file formats.

%package devel
Summary:        Development files for %name
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libolecf is a library to access the OLE 2 Compound File (OLECF) format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python2-%{name}
Summary:        Python bindings for libolecf
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
BuildRequires:  pkgconfig(python2)
Obsoletes:      pyolecf = 20191221
Obsoletes:      python-%{name} = 20191221

%description -n python2-%name
Python bindings for libolecf, which can read MS IE cache files.

%package -n python3-%{name}
Summary:        Python bindings for libolecf
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
BuildRequires:  pkgconfig(python3)

%description -n python3-%name
Python bindings for libolecf, which can read MS IE cache files.

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
%_libdir/libolecf.so.*

%files tools
%_bindir/olecf*
%_mandir/man1/olecf*.1*

%files devel
%doc OLE_Compound_File_format.pdf
%_includedir/libolecf.h
%_includedir/libolecf/
%_libdir/libolecf.so
%_libdir/pkgconfig/libolecf.pc
%_mandir/man3/libolecf.3*

%if %{with python2}
%files -n python2-%name
%license COPYING*
%python2_sitearch/pyolecf.so
%endif

%files -n python3-%name
%license COPYING*
%python3_sitearch/pyolecf.so

%changelog
