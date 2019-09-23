#
# spec file for package lzham_codec
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           lzham_codec
Version:        1_0_stable1
Release:        0
Summary:        Lossless data compression codec
License:        MIT
Group:          Productivity/Archiving/Compression
URL:            https://github.com/richgel999/lzham_codec
Source0:        https://github.com/richgel999/lzham_codec/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM lzham-no_threading.patch
Patch0:         lzham-no_threading.patch
# PATCH-FEATURE-UPSTREAM lzham-undef_types.patch
Patch1:         lzham-undef_types.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Lossless data compression codec with LZMA-like ratios but optimized for decompression speed, C/C++.

%package devel
Summary:        Development libraries and headers for %{name}
Group:          Development/Languages/C and C++
Requires:       %{name}-libs = %{version}

%description devel
This package contains development libraries and headers for %{name}.

%package libs
Summary:        Lossless data compression codec
Group:          Productivity/Archiving/Compression

%description libs
Libraries for encoding/decoding lzham codec files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
rm example?/*.vcxproj
# avoid conflict with the actual zlib header
mv include/zlib.h include/lzham_zlib.h
sed -e 's/zlib/lzham_zlib/' -i CMakeLists.txt -i lzhamdecomp/CMakeLists.txt

%build
%cmake
%make_jobs

%install
%cmake_install

# creates support file for pkg-config
mkdir %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/lzham_codec.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: lzham_codec
Description: Lossless data compression codec
Version: %{version}
Libs: -L${libdir} -llzhamdll -llzhamcomp -llzhamdecomp
Cflags: -I${includedir}
EOF

%files devel
%license LICENSE
%doc README.md example?
%{_includedir}/lzham.h
%{_includedir}/lzham_dynamic_lib.h
%{_includedir}/lzham_exports.inc
%{_includedir}/lzham_static_lib.h
%{_includedir}/lzham_zlib.h
%{_libdir}/pkgconfig/lzham_codec.pc

%files libs
%license LICENSE
%doc README.md
%{_libdir}/liblzhamcomp.so
%{_libdir}/liblzhamdecomp.so
%{_libdir}/liblzhamdll.so

%changelog
