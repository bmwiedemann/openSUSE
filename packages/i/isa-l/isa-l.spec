#
# spec file for package isa-l
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


Name:           isa-l
Version:        2.31.0
Release:        0
Summary:        Intel Intelligent Storage Acceleration Library
Group:          Development/Libraries/C and C++
License:        BSD-3-Clause
URL:            https://github.com/intel/isa-l
Source:         https://github.com/intel/isa-l/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  nasm >= 2.13

%description
Optimized low-level functions targeting storage applications.

%package -n igzip
Summary:        gzip backed by the ISA-L deflate library
Group:          Productivity/Archiving/Compression

%description -n igzip
igzip compresses and decompresses files similar to gzip using the
ISA-L deflate library.

Output .gz files are compatible with gzip and RFC 1952.

%package devel
Summary:        Development files for the Intel Intelligent Storage Acceleration Library
Group:          Development/Libraries/C and C++
Requires:       libisal2 = %{version}

%description devel
ISA-L is a collection of optimized low-level functions targeting
storage applications.

This package contains the development headers for the library found
in libisal2.

%package -n libisal2
Summary:        Intel Intelligent Storage Acceleration Library
Group:          System/Libraries

%description -n libisal2
ISA-L is a collection of optimized low-level functions targeting
storage applications. ISA-L includes:

* Erasure codes: Block Reed-Solomon type erasure codes for any
  encode/decode matrix in GF(2^8).
* CRC Implementations of cyclic redundancy check. Six different
  polynomials supported: iscsi32, ieee32, t10dif, ecma64, iso64,
  jones64.
* RAID calculation and operation on XOR and P+Q parity found in
  common RAID implementations.
* Compression of deflate-compatible data compression.
* De-compression of inflate-compatible data compression.

This package contains the development headers for the library found
in libisal2.

%prep
%autosetup

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
./autogen.sh
%configure
%make_build

%install
%make_install

%ldconfig_scriptlets -n libisal2

%files -n igzip
%license LICENSE
%doc README.md
%{_bindir}/igzip
%{_mandir}/man1/igzip.1.gz

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_includedir}/%{name}/crc.h
%{_includedir}/%{name}/crc64.h
%{_includedir}/%{name}/erasure_code.h
%{_includedir}/%{name}/gf_vect_mul.h
%{_includedir}/%{name}/igzip_lib.h
%{_includedir}/%{name}/mem_routines.h
%{_includedir}/%{name}/raid.h
%{_includedir}/%{name}/test.h
%{_libdir}/libisal.a
%{_libdir}/libisal.la
%{_libdir}/libisal.so
%{_libdir}/pkgconfig/libisal.pc

%files -n libisal2
%{_libdir}/libisal.so.2
%{_libdir}/libisal.so.2.0.31

%changelog
