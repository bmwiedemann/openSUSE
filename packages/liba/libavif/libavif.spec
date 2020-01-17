#
# spec file for package libavif
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%bcond_with aom

%define lib_name libavif0

Name:           libavif
Version:        0.5.3
Release:        0
Summary:        Library for encoding and decoding .avif files
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/AOMediaCodec/libavif
Source:         https://github.com/AOMediaCodec/libavif/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          https://github.com/cryptomilk/libavif/commit/cbcf62c2200be83b85b48059c819ae708216ccec.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  pkgconfig(dav1d)
%if %{with aom}
BuildRequires:  pkgconfig(aom)
%endif
BuildRequires:  pkgconfig(rav1e)
%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%package tools
Group:          Productivity/Graphics/Convertors
#
Summary:        Tools for libavif
%description tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the commandline tools for libavif.

%package -n %{lib_name}
Group:          Development/Libraries/C and C++
#
Summary:        Shared library from libavif
%description -n %{lib_name}
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the shared library for libavif.

%package devel
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}-%{release}
#
Summary:        Development files for libavif
%description devel
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the development files for libavif.

%prep
%autosetup -p1

%build
%cmake \
 -DAVIF_CODEC_RAV1E:BOOL=ON \
 -DAVIF_CODEC_DAV1D:BOOL=ON \
 %if %{with aom}
 -DAVIF_CODEC_AOM:BOOL=ON \
 %endif
 -DAVIF_BUILD_APPS:BOOL=ON           \
 -DAVIF_BUILD_EXAMPLES:BOOL=ON
make %{?_smp_mflags}

%install
%cmake_install

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files tools
%doc *.md
%license LICENSE
%{_bindir}/avifdec
%{_bindir}/avifenc

%files -n %{lib_name}
%license LICENSE
%{_libdir}/libavif.so.*

%files devel
%license LICENSE
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/

%changelog
