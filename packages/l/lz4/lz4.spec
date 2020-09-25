#
# spec file for package lz4
#
# Copyright (c) 2020 SUSE LLC
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


%define lname	liblz4-1
Name:           lz4
Version:        1.9.2
Release:        0
Summary:        Hash-based Predictive Lempel–Ziv compressor
License:        GPL-2.0-or-later AND BSD-2-Clause
Group:          Productivity/Archiving/Compression
URL:            https://lz4.github.io/lz4/

#Git-Clone:	https://github.com/lz4/lz4
Source:         https://github.com/lz4/lz4/archive/v%version.tar.gz#/%name-%version.tar.gz
Source99:       baselibs.conf
Patch2:         lz-export.diff
BuildRequires:  pkgconfig

%description
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(Lempel–Ziv) family of byte-oriented compression schemes. It is a
LZP2 fork and provides better compression ratio for text files.

This subpackage provides a GPL command-line utility to make use of
the LZ4 algorithm.

%package -n %lname
Summary:        Hash-based predictive Lempel-Ziv compressor
License:        BSD-2-Clause
Group:          System/Libraries

%description -n %lname
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(Lempel–Ziv) family of byte-oriented compression schemes. It is a

This subpackage contains the (de)compressor code as a shared library.

%package -n liblz4-devel
Summary:        Development files for the LZ4 compressor
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n liblz4-devel
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(Lempel–Ziv) family of byte-oriented compression schemes. It is a

This subpackage contains libraries and header files for developing
applications that want to make use of liblz4.

%prep
%setup -q
%patch -P 2 -p1

%build
V=1 make %{?_smp_mflags} CFLAGS="%optflags"

%install
%make_install PREFIX="%_prefix" LIBDIR="%_libdir"
rm -f "%buildroot/%_libdir"/*.a

%check
LD_LIBRARY_PATH="%buildroot/%_libdir" ldd -r "%buildroot/%_bindir/lz4"
make %{?_smp_mflags} check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/lz4*
%_bindir/unlz4
%_mandir/man1/*.1*

%files -n %lname
%_libdir/liblz4.so.1*

%files -n liblz4-devel
%_includedir/lz4*.h
%_libdir/liblz4.so
%_libdir/pkgconfig/*.pc

%changelog
