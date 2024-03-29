#
# spec file for package libvsapm
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


%{?sle15_python_module_pythons}

Name:           libvsapm
%define lname	libvsapm1
Version:        20240226
Release:        0
Summary:        Library and tools to access the Apple Partition Map volume system format
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libvsapm
Source:         https://github.com/libyal/libvsapm/releases/download/%version/libvsapm-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libvsapm/releases/download/%version/libvsapm-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcdata) >= 20240103
BuildRequires:  pkgconfig(libcerror) >= 20240101
BuildRequires:  pkgconfig(libcfile) >= 20240106
BuildRequires:  pkgconfig(libclocale) >= 20240107
BuildRequires:  pkgconfig(libcnotify) >= 20240108
BuildRequires:  pkgconfig(libcpath) >= 20240109
BuildRequires:  pkgconfig(libcsplit) >= 20240110
BuildRequires:  pkgconfig(libcthreads) >= 20240102
BuildRequires:  pkgconfig(libfcache) >= 20240112
BuildRequires:  pkgconfig(libfdata) >= 20240114
BuildRequires:  pkgconfig(libfguid) >= 20240116
BuildRequires:  pkgconfig(libuna) >= 20240130
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libvsapm is a library to access the Apple Partition Map (APM) volume
system format.

Part of the libyal family of libraries.

The Apple Partition Map (APM) is used on Motorola based Macintosh computers. On Intel based Macintosh computers the GUID Partition Table (GPT) is used.

The APM is supported by:
  * Apple Unix (A/UX)
  * Mac OS
  * Mac OS X

The APM consists of:
  * the drive descriptor
  * partition map entry of type Apple_partition_map
  * zero partition map entries

%package -n %lname
Summary:        Library for accessing the GUID partition table format
Group:          System/Libraries

%description -n %lname
libvsapm is a library to access the Apple Partition Map (APM) volume
system format.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libvsapm
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libvsapm is a library to access the Apple Partition Map (APM) volume
system format.

This subpackage contains libraries and header files for developing
applications that want to make use of libvsapm.

%package tools
Summary:        Utilities for inspecting GUID partition tables
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libvsapm to
inspect Apple Partition Map partition tables.

%prep
%autosetup -p1

%build
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
find %{buildroot} -type f -name "*.la" -delete -print
%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libvsapm.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n %name-tools
%_bindir/vsapm*
%_mandir/man1/vsapm*

%files %python_files
%python_sitearch/*.so

%changelog
