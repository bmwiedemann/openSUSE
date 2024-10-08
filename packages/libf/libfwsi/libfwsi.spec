#
# spec file for package libfwsi
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


%define lname	libfwsi1
Name:           libfwsi
Version:        20240423
Release:        0
Summary:        Library to access the Windows Shell Item format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfwsi
Source:         https://github.com/libyal/libfwsi/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfwsi/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source3:        %name.keyring
Source9:        Windows_Shell_Item_format.pdf
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfdatetime) >= 20240415
BuildRequires:  pkgconfig(libfguid) >= 20240415
BuildRequires:  pkgconfig(libfole) >= 20240415
BuildRequires:  pkgconfig(libfwps) >= 20240417
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library to access the Windows Shell Item format for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %lname
Summary:        Library to access the Windows Shell Item format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
Library to access the Windows Shell Item format for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwsi
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Library to access the Windows Shell Item format for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwsi.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* %buildroot/
find %buildroot -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libfwsi.so.*

%files -n %name-devel
%license COPYING*
%doc Windows_Shell_Item_format.pdf
%_includedir/libfwsi.h
%_includedir/libfwsi/
%_libdir/libfwsi.so
%_libdir/pkgconfig/libfwsi.pc
%_mandir/man3/libfwsi.3*

%files %python_files
%license COPYING*
%python_sitearch/pyfwsi.so

%changelog
