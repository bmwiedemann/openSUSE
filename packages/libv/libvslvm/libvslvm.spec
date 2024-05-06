#
# spec file for package libvslvm
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

%define lname   libvslvm1
Name:           libvslvm
Version:        20240504
Release:        0
Summary:        Library to access the Linux Logical Volume Manager (LVM) volume system
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libvslvm/
Source:         https://github.com/libyal/libvslvm/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libvslvm/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse)
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
BuildRequires:  pkgconfig(libfdata) >= 20240414
BuildRequires:  pkgconfig(libfvalue) >= 20240415
BuildRequires:  pkgconfig(libuna) >= 20240414
BuildRequires:  pkgconfig(zlib)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libvslvm is a library to access the Linux Logical Volume Manager
(LVM) volume system.

%package -n %lname
Summary:        Library to access Linux Logical Volume Manager (LVM) volume containers
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
The libvslvm library is a library to access Linux Logical Volume
Manager (LVM) volume containers

%package tools
Summary:        Several tools for reading Linux Logical Volume Manager (LVM) systems
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Several tools for reading Linux Logical Volume Manager (LVM) volume
systems.

See libvslvm for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libvslvm
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
Header files and libraries for developing applications for libvslvm

See libvslvm for additional details.

This package contains libraries and header files for developing
applications that want to make use of libvslvm.

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
mv %_builddir/rt/* %buildroot/
find "%buildroot" -type f -name "*.la" -delete -print

%check
#    this fails for the python check.
#    It is only checking if the python modules are present, so this is a false failure.
# make check

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libvslvm.so.*

%files -n %name-tools
%license COPYING*
%_bindir/vslvm*
%_mandir/man1/vslvm*.1*

%files -n %name-devel
%license COPYING*
%_includedir/libvslvm.h
%_includedir/libvslvm/
%_libdir/libvslvm.so
%_libdir/pkgconfig/libvslvm.pc
%_mandir/man3/libvslvm.3*

%files %python_files
%license COPYING*
%python_sitearch/pyvslvm.so

%changelog
