#
# spec file for package libvsgpt
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


Name:           libvsgpt
%define lname	libvsgpt1
Version:        20221029
Release:        0
Summary:        Library and tools to access the GUID Partition Table (GPT) volume system format
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libvsgpt
Source:         https://github.com/libyal/libvsgpt/releases/download/%version/libvsgpt-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libvsgpt/releases/download/%version/libvsgpt-experimental-%version.tar.gz.asc
Source3:        %name.keyring
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
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libuna) >= 20220611
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libvsgpt is a library to access the GUID Partition Table (GPT)
volume system.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing the GUID partition table format
Group:          System/Libraries

%description -n %lname
libvsgpt is a library to access the GUID Partition Table (GPT)
volume system.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libvsgpt
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libvsgpt is a library to access the GUID Partition Table (GPT)
volume system.

This subpackage contains libraries and header files for developing
applications that want to make use of libvsgpt.

%package tools
Summary:        Utilities for inspecting GUID partition tables
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libvsgpt to
inspect GUID partition tables.

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
%_libdir/libvsgpt.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n %name-tools
%_bindir/vsgpt*
%_mandir/man1/vsgpt*

%files %python_files
%python_sitearch/*.so

%changelog
