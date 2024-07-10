#
# spec file for package libbde
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

%define lname	libbde1
Name:           libbde
Version:        20240502
Release:        0
Summary:        Library and tools to access Microsoft Bitlocker Disk Encrypted partitions
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libbde
Source:         https://github.com/libyal/libbde/releases/download/%version/%name-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libbde/releases/download/%version/%name-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source10:       BitLocker_Drive_Encryption_BDE_format.pdf
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse3) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcaes) >= 20240413
BuildRequires:  pkgconfig(libcdata) >= 2024041
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 20240414
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfcache) >= 20240414
BuildRequires:  pkgconfig(libfdatetime) >= 20240414
BuildRequires:  pkgconfig(libfguid) >= 20240414
BuildRequires:  pkgconfig(libfvalue) >= 20240415
BuildRequires:  pkgconfig(libhmac) >= 20240417
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libbde is a library to access the BitLocker Drive Encryption (BDE)
format. The BDE format is used by Windows, as of Vista, to encrypt
data on a storage media volume.

%package -n %lname
Summary:        Library to access Microsoft Bitlocker Drive Encrypted volumes
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libbde is a library to access the BitLocker Drive Encryption (BDE)
format. The BDE format is used by Windows, as of Vista, to encrypt
data on a storage media volume.

Supported BDE formats:

* BitLocker Windows Vista
* BitLocker Windows 7
* BitLocker Windows 8 (Consumer Preview)
* BitLocker To Go

Supported protection methods:

* clear key
* password
* recovery password
* start-up key
* FKEV and/or TWEAK key data

Additional features:

* support for partial encrypted volumes
* zeros out the BDE metadata, matches behavior seen on Windows

%package tools
Summary:        Tools to access Microsoft Bitlocker Drive Encrypted volumes
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Tools to access the BitLocker Drive Encryption (BDE) format. The BDE
format is used by Windows, as of Vista, to encrypt data on a storage
media volume.

%package devel
Summary:        Development files for libbde, used to access Bitlocker Drive Encrypted Volumes
License:        GFDL-1.1-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libbde is a library to access the BitLocker Drive Encryption (BDE)
format. The BDE format is used by Windows, as of Vista, to encrypt
data on a storage media volume.

This subpackage contains libraries and header files for developing
applications that want to make use of libbde.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type --enable-python \
	PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print
# we have static libs for some reason, trash them
find "%buildroot" -name "*.a" -print -delete

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libbde.so.*

%files -n %name-tools
%license COPYING*
%_bindir/bde*
%_mandir/man1/bde*.1*

%files -n %name-devel
%license COPYING*
%doc BitLocker_Drive_Encryption_*.pdf
%_includedir/libbde.h
%_includedir/libbde/
%_libdir/libbde.so
%_libdir/pkgconfig/libbde.pc
%_mandir/man3/libbde.3*

%files %python_files
%license COPYING*
%python_sitearch/pybde.so

%changelog
