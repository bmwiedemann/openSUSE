#
# spec file for package libfmos
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libfmos
%define lname	libfmos1
Version:        20220811
Release:        0
Summary:        Library for MacOS data types
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfmos
Source:         https://github.com/libyal/libfmos/releases/download/%version/libfmos-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfmos/releases/download/%version/libfmos-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcthreads) >= 20220102
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libfmos is a library for MacOS data types.

%package -n %lname
Summary:        Library for MacOS data types
Group:          System/Libraries

%description -n %lname
libfmos is a library for MacOS data types.

%package devel
Summary:        Development files for libfmos
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfmos is a library for MacOS data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfmos.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym" \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %buildroot -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfmos.so.*

%files -n %name-devel
%_includedir/libfmos.h
%_includedir/libfmos/
%_libdir/libfmos.so
%_libdir/pkgconfig/libfmos.pc
%_mandir/man3/libfmos.3*

%files %python_files
%python_sitearch/pyfmos.so

%changelog
