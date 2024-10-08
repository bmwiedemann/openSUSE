#
# spec file for package libolecf
#
# Copyright (c) 2024 SUSE LLC
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


%define lname	libolecf1
Name:           libolecf
Version:        20240427
Release:        0
Summary:        Library and tools to access the OLE 2 Compound File (OLECF) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libolecf
Source:         https://github.com/libyal/libolecf/releases/download/%version/%name-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libolecf/releases/download/%version/%name-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source11:       OLE_Compound_File_format.pdf
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 20240414
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfdatetime) >= 20240415
BuildRequires:  pkgconfig(libfguid) >= 20240415
BuildRequires:  pkgconfig(libfole) >= 20240415
BuildRequires:  pkgconfig(libfvalue) >= 20240415
BuildRequires:  pkgconfig(libfwps) >= 20240415
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library and tools to access the OLE 2 Compound File (OLECF) format.
The OLE 2 Compound File format is used to store certain versions of
Microsoft Office files, thumbs.db and other file formats.

%package -n %lname
Summary:        Library to access the OLE 2 Compound File (OLECF) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
Library to access the OLE 2 Compound File (OLECF) format. The OLE 2
Compound File format is used to store certain versions of Microsoft
Office files, thumbs.db and other file formats.

%package tools
Summary:        Tools to access the OLE 2 Compound File (OLECF) format
License:        LGPL-3.0-or-later
Group:          System/Filesystems
Requires:       %lname = %version

%description tools
Tools to access the OLE 2 Compound File (OLECF) format. The OLE 2
Compound File format is used to store certain versions of Microsoft
Office files, thumbs.db and other file formats.

%package devel
Summary:        Development files for %name
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libolecf is a library to access the OLE 2 Compound File (OLECF) format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type --enable-python \
	PYTHON_VERSION="%{$python_bin_suffix}" \
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
%_libdir/libolecf.so.*

%files -n %name-tools
%_bindir/olecf*
%_mandir/man1/olecf*.1*

%files -n %name-devel
%doc OLE_Compound_File_format.pdf
%_includedir/libolecf.h
%_includedir/libolecf/
%_libdir/libolecf.so
%_libdir/pkgconfig/libolecf.pc
%_mandir/man3/libolecf.3*

%files %python_files
%license COPYING*
%python_sitearch/pyolecf.so

%changelog
