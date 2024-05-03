#
# spec file for package libluksde
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

%define lname	libluksde1
Name:           libluksde
Version:        20240503
Release:        0
Summary:        Library and tools to access LUKS Disk Encryption encrypted files
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libluksde
Source:         https://github.com/libyal/libluksde/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libluksde/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcaes) >= 20240413
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 20240414
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfcache) >= 20240414
BuildRequires:  pkgconfig(libfcrypto) >= 20240414
BuildRequires:  pkgconfig(libfdatetime) >= 20240414
BuildRequires:  pkgconfig(libfguid) >= 20240414
BuildRequires:  pkgconfig(libhmac) >= 20240417
BuildRequires:  pkgconfig(libuna) >= 20240414
BuildRequires:  pkgconfig(python3)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library and tools to access the New Technology File System (NTFS).

Note that this project currently only focuses on the analysis of the format.

%package -n %lname
Summary:        Library to access the New Technology File System (NTFS)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libluksde is a library to access LUKS Disk Encrypted volumes.

%package tools
Summary:        Tools to access the New Technology File System (NTFS)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
libluksde-tools is a project to access LUKS Disk Encrypted volumes.

%package devel
Summary:        Development files for libluksde
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
%name is a library to access the New Technology File System (NTFS).

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%autosetup -p1

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
%_libdir/libluksde.so.*

%files -n %name-tools
%_bindir/luksde*
%_mandir/man1/luksdeinfo.1*
%_mandir/man1/luksdemount.1*

%files -n %name-devel
%_includedir/libluksde.h
%_includedir/libluksde/
%_libdir/libluksde.so
%_libdir/pkgconfig/libluksde.pc
%_mandir/man3/libluksde.3*

%files %python_files
%license COPYING*
%python_sitearch/pyluksde.so

%changelog
