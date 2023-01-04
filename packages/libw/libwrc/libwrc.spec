#
# spec file for package libwrc
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libwrc
%define lname	libwrc1
Version:        20221009
Release:        0
Summary:        Library to support the Windows Resource Compiler format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libwrc
Source:         https://github.com/libyal/libwrc/releases/download/%version/libwrc-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libwrc/releases/download/%version/libwrc-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libexe) >= 20210424
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfvalue) >= 20220120
BuildRequires:  pkgconfig(libfwnt) >= 20220922
BuildRequires:  pkgconfig(libuna) >= 20220611
BuildRequires:  pkgconfig(python3)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libwrc is a library to support the Windows Resource Compiler format.

%package -n %lname
Summary:        Library to support the Windows Resource Compiler format
Group:          System/Libraries

%description -n %lname
libwrc is a library to support the Windows Resource Compiler format.

%package devel
Summary:        Development files for libwrc, a Windows Resouce Compiler format support library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libwrc is a library to support the Windows Resource Compiler format.

This subpackage contains libraries and header files for developing
applications that want to make use of libwrc.

%package tools
Summary:        Utilities to inspect Windows Resource Compiler files
Group:          Productivity/File utilities

%description tools
This subpackage provides the utilities from libwrc, which allows for
reading Windows Resource Compiler files.

%prep
%autosetup -p1

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
mv "%_builddir/rt"/* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libwrc.so.1*

%files -n %name-devel
%_includedir/libwrc*
%_libdir/libwrc.so
%_libdir/pkgconfig/libwrc.pc
%_mandir/man3/libwrc.3*

%files -n %name-tools
%_bindir/wrcinfo
%_mandir/man1/wrcinfo.1*

%files %python_files
%python_sitearch/*.so

%changelog
