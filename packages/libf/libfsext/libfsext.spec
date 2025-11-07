#
# spec file for package libfsext
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define lname	libfsext1
Name:           libfsext
Version:        20251107
Release:        0
Summary:        Library and tools to access the Extended File System
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfsext
Source:         https://github.com/libyal/libfsext/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfsext/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source3:        %name.keyring
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
BuildRequires:  pkgconfig(libfcache) >= 20240414
BuildRequires:  pkgconfig(libfdata) >= 20240415
BuildRequires:  pkgconfig(libfdatetime) >= 20240415
BuildRequires:  pkgconfig(libfguid) >= 20240415
BuildRequires:  pkgconfig(libhmac) >= 20240417
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libfsext is a library to access the Extended File System (ext).

Read-only supported ext formats:

* ext2 (version 2)
* ext3 (version 3)
* ext4 (version 4)

Supported ext format features:

* ext4 inline data

Unsupported ext format features:

* ext (version 1)
* compression
* encryption

%package -n %lname
Summary:        Library to access the Extended File System (ext)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libfsext is a library to access the Extended File System (ext).

Read-only supported ext formats:

* ext2 (version 2)
* ext3 (version 3)
* ext4 (version 4)

Supported ext format features:

* ext4 inline data

Unsupported ext format features:

* ext (version 1)
* compression
* encryption

%package tools
Summary:        Tools to access the Extended File System (ext)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
Tools to access the Extended File System.  See libfsext for additional details.

%package devel
Summary:        Development files for libfsext, Extended File System (ext) library
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libfsext is a library to access the extended file system (ext) format.  see libfsext for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libfsext.

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
mv "%_builddir/rt"/* %buildroot/
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libfsext.so.*

%files -n %name-tools
%license COPYING*
%_bindir/fsext*
%_mandir/man1/fsext*.1*

%files -n %name-devel
%license COPYING*
%_includedir/libfsext.h
%_includedir/libfsext/
%_libdir/libfsext.so
%_libdir/pkgconfig/libfsext.pc
%_mandir/man3/libfsext.3*

%files %python_files
%license COPYING*
%python_sitearch/pyfsext.so

%changelog
