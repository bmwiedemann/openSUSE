#
# spec file for package libcaes
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


Name:           libcaes
%define lname	libcaes1
Version:        20221127
Release:        0
Summary:        Library for AES encryption
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcaes
Source:         https://github.com/libyal/libcaes/releases/download/%version/libcaes-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libcaes/releases/download/%version/libcaes-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(openssl) >= 1.0
%{python_subpackages}
# Various notes: https://en.opensuse.org/libyal

%description
libcaes is a library for AES encryption.

%package -n %lname
Summary:        Library for AES encryption
Group:          System/Libraries

%description -n %lname
libcaes is a library for AES encryption.

%package devel
Summary:        Development files for libcaes, a AES encryption library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libcaes is a library for AES encryption.

This subpackage contains libraries and header files for developing
applications that want to make use of libcaes.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-python PYTHON_VERSION="%{$python_bin_suffix}" LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log || exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find "%buildroot" -name "*.la" -print -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libcaes.so.1*

%files -n %name-devel
%_includedir/libcaes*
%_libdir/libcaes.so
%_libdir/pkgconfig/libcaes.pc
%_mandir/man3/libcaes.3*

%files %python_files
%python_sitearch/*

%changelog
