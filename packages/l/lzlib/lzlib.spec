#
# spec file for package lzlib
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define lname liblz1
Name:           lzlib
Version:        1.15
Release:        0
Summary:        LZMA Compression and Decompression Library
License:        BSD-2-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.nongnu.org/lzip/lzlib.html
Source:         https://download.savannah.gnu.org/releases/lzip/lzlib/%name-%version.tar.gz
Source2:        https://download.savannah.gnu.org/releases/lzip/lzlib/%name-%version.tar.gz.sig
Source3:        %name.keyring
PreReq:         %install_info_prereq

%description
The lzlib compression library provides in-memory LZMA compression and
decompression functions, including integrity checking of the
decompressed data. The compressed data format used by the library is
the lzip format.

%package -n %lname
Summary:        LZMA Compression and Decompression Library
Group:          System/Libraries

%description -n %lname
The lzlib compression library provides in-memory LZMA compression and
decompression functions, including integrity checking of the
decompressed data. The compressed data format used by the library is
the lzip format.

%package devel
Summary:        LZMA Compression and Decompression Library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Obsoletes:      lzlib-devel < %version-%release
Provides:       lzlib-devel = %version-%release

%description devel
The lzlib compression library provides in-memory LZMA compression and
decompression functions, including integrity checking of the
decompressed data. The compressed data format used by the library is
the lzip format.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%prep
%autosetup

%build
# not autoconf!
# don't use the configure macro here, as it will cause the configure script to
# skip parameters as soon as it encounters one that it doesn't understand
mkdir build
pushd build/
../configure --prefix="%_prefix" --bindir="%_bindir" --datadir="%_datadir" \
	--includedir="%_includedir" --infodir="%_infodir" --libdir="%_libdir" \
	--mandir="%_mandir" --sysconfdir="%_sysconfdir" --enable-shared \
	CC="%__cc" CFLAGS="%optflags" CXX="%__cxx" CXXFLAGS="%optflags"
%make_build
popd

%install
pushd build/
%make_install LDCONFIG=true
popd
# configure had no --disable-static
rm -f "%buildroot/%_libdir"/*.a

%check
pushd build/
%make_build check
popd

%ldconfig_scriptlets -n %lname

%post devel
%install_info --info-dir="%_infodir" "%_infodir/%name.info%ext_info"

%preun devel
%install_info_delete --info-dir="%_infodir" "%_infodir/%name.info%ext_info"

%files -n %lname
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%_libdir/liblz.so.*

%files devel
%_includedir/lzlib.h
%_libdir/liblz.so
%_infodir/lzlib.info*

%changelog
