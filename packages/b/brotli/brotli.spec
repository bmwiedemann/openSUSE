#
# spec file for package brotli
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2017 Buschmann <buschmann23@opensuse.org>
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


%define sover 1
Name:           brotli
Version:        1.2.0
Release:        0
Summary:        Lossless Compression Algorithm
License:        MIT
Group:          Productivity/Archiving/Compression
URL:            https://github.com/google/brotli
Source:         https://github.com/google/brotli/archive/v%version.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  pkg-config
%{?suse_build_hwcaps_libs}

%description
This package contains the brotli command line utility to compress and
decompress data with the brotli compression algorithm.

Brotli is a generic-purpose lossless compression algorithm that
compresses data using a combination of a modern variant of the LZ77
algorithm, Huffman coding and 2nd order context modeling, with a
compression ratio comparable to the best currently available
general-purpose compression methods. It is similar in speed with
deflate but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in
RFC 7932.

%package -n libbrotlicommon%sover
Summary:        Common Library for Brotli Compression
Group:          System/Libraries

%description -n libbrotlicommon%sover
Common library for the Brotli general purpose lossless data
compression algorithm.

%package -n libbrotlidec%sover
Summary:        Library for Brotli Decompression
Group:          System/Libraries

%description -n libbrotlidec%sover
Decompression library for the Brotli general purpose lossless data
compression algorithm.

The specification of the Brotli Compressed Data Format is defined in
RFC 7932.

%package -n libbrotlienc%sover
Summary:        Library for Brotli Compression
Group:          System/Libraries

%description -n libbrotlienc%sover
Compression library for the Brotli general purpose lossless data
compression algorithm.

The specification of the Brotli Compressed Data Format is defined in
RFC 7932.

%package -n libbrotli-devel
Summary:        Development and Header Files for Brotli Compression
Group:          Development/Libraries/C and C++
Requires:       libbrotlicommon%sover = %version-%release
Requires:       libbrotlidec%sover = %version-%release
Requires:       libbrotlienc%sover = %version-%release
Provides:       libbrotlicommon-devel = %version-%release
Provides:       libbrotlidec-devel = %version-%release
Provides:       libbrotlienc-devel = %version-%release
Obsoletes:      libbrotlicommon-devel < %version-%release
Obsoletes:      libbrotlidec-devel < %version-%release
Obsoletes:      libbrotlienc-devel < %version-%release

%description -n libbrotli-devel
Development and headers files for (de)compressing data using the
Brotli general purpose lossless compression algorithm.

The specification of the Brotli Compressed Data Format is defined in
RFC 7932.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -DBROTLI_ENCODER_CLEANUP_ON_OOM"
%cmake
%cmake_build

%install
%cmake_install
mkdir -p "%buildroot/%_mandir/man1" "%buildroot/%_mandir/man3"
install -pm0644 docs/*.1 "%buildroot/%_mandir/man1/"
install -pm0644 docs/*.3 "%buildroot/%_mandir/man3/"

%check
%ctest

%ldconfig_scriptlets -n libbrotlicommon%sover
%ldconfig_scriptlets -n libbrotlidec%sover
%ldconfig_scriptlets -n libbrotlienc%sover

%files
%license LICENSE
%_bindir/brotli
%_mandir/man1/brotli.1*

%files -n libbrotlicommon%sover
%_libdir/libbrotlicommon.so.*

%files -n libbrotlidec%sover
%_libdir/libbrotlidec.so.*

%files -n libbrotlienc%sover
%_libdir/libbrotlienc.so.*

%files -n libbrotli-devel
%_includedir/brotli/
%_libdir/libbrotlicommon.so
%_libdir/libbrotlidec.so
%_libdir/libbrotlienc.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%changelog
