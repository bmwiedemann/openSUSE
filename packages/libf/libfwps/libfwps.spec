#
# spec file for package libfwps
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           libfwps
%define lname	libfwps1
Version:        20260522
Release:        0
Summary:        Library for Windows Property Store data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfwps
Source:         https://github.com/libyal/libfwps/releases/download/%version/libfwps-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfwps/releases/download/%version/libfwps-alpha-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcdata) >= 20260520
BuildRequires:  pkgconfig(libcerror) >= 20260513
BuildRequires:  pkgconfig(libclocale) >= 20260520
BuildRequires:  pkgconfig(libcnotify) >= 20260520
BuildRequires:  pkgconfig(libcthreads) >= 20260518
BuildRequires:  pkgconfig(libfdatetime) >= 20260521
BuildRequires:  pkgconfig(libfguid) >= 20260521
BuildRequires:  pkgconfig(libfole) >= 20260521
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libfwps is a library for Windows Property Store data types.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for Windows Property Store data types
Group:          System/Libraries

%description -n %lname
libfwps is a library for Windows Property Store data types.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfwps
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfwps is a library for Windows Property Store data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwps.

%prep
%autosetup -p1

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
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libfwps.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files %python_files
%python_sitearch/*.so

%changelog
