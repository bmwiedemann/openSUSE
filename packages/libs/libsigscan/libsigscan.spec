#
# spec file for package libsigscan
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

%define lname	libsigscan1
Name:           libsigscan
Version:        20240505
Release:        0
Summary:        Library for binary signature scanning
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsigscan
Source:         https://github.com/libyal/libsigscan/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libsigscan/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source9:        %name.keyring
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
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libsigscan is a library for binary signature scanning

libsigscan is part of the libyal family of libraries

%package -n %lname
Summary:        Library for binary signature scanning
Group:          System/Libraries

%description -n %lname
libsigscan is a library for binary signature scanning

%package tools
Summary:        Tools to scan for binary signatures
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
Tools to scan binary files for signatures.

%package devel
Summary:        Development files for libigscan
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libsigscan is a library for binary signature scanning

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

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
mv "%_builddir/rt/"* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libsigscan.so.*

%files -n %name-tools
%license COPYING*
%_bindir/sigscan
%_mandir/man1/sigscan.1%{?ext_man}
%config %_sysconfdir/sigscan.conf

%files -n %name-devel
%license COPYING*
%_includedir/libsigscan.h
%_includedir/libsigscan/
%_libdir/libsigscan.so
%_libdir/pkgconfig/libsigscan.pc
%_mandir/man3/libsigscan.3%{?ext_man}

%files %python_files
%python_sitearch/pysigscan.so

%changelog
