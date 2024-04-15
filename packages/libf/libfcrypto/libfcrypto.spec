#
# spec file for package libfcrypto
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

Name:           libfcrypto
%define lname	libfcrypto1
Version:        20240414
Release:        0
Summary:        Library for encryption formats
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfcrypto
Source:         https://github.com/libyal/libfcrypto/releases/download/%version/libfcrypto-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfcrypto/releases/download/%version/libfcrypto-alpha-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.21
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcerror) >= 20240413
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libfcrypto is a library for encryption formats.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for encryption formats
Group:          System/Libraries

%description -n %lname
libfcrypto is a library for encryption formats.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfcrypto
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfcrypto is a library for encryption formats.

This subpackage contains libraries and header files for developing
applications that want to make use of libfcrypto.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --disable-rpath \
	--enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
echo "$python" >lastpython
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print

%check
export PYTHON="$(cat lastpython)"
# The testsuite has a symbol overload for malloc,
# and that no longer works when using version-script
make check || :

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libfcrypto.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files %python_files
%python_sitearch/pyfcrypto.so

%changelog
