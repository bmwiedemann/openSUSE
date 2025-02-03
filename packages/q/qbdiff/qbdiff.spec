#
# spec file for package qbdiff
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 0
Name:           qbdiff
Version:        1.0.0
Release:        0
Summary:        Quick Binary Diff for generating and applying binary patches
License:        LGPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/kspalaiologos/qbdiff
Source:         https://github.com/kspalaiologos/qbdiff/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liblzma)
# fails with 32 bit pointer error
ExcludeArch:    %{ix86} %{arm}

%description
Quick Binary Diff (qbdiff) is a tool for generating and applying binary
patches. It builds on the general ideas of bsdiff.

It is designed to be faster than bsdiff by taking advantage of multiple CPU
cores. It is also designed to produce generally smaller patch files, and
supports only LZMA compression as it performs well on sparse binary data.
Further it aims to be frugal on memory usage and provides integrity checking
using BLAKE2B.

%package -n lib%{name}%{sover}
Summary:        Quick Binary Diff shared library

%description -n lib%{name}%{sover}
Quick Binary Diff (qbdiff) is a tool for generating and applying binary
patches. It builds on the general ideas of bsdiff.

It is designed to be faster than bsdiff by taking advantage of multiple CPU
cores. It is also designed to produce generally smaller patch files, and
supports only LZMA compression as it performs well on sparse binary data.
Further it aims to be frugal on memory usage and provides integrity checking
using BLAKE2B.

This package contains the shared library.

%package devel
Summary:        Development files for qbdiff
Requires:       lib%{name}%{sover} = %{version}

%description devel
Quick Binary Diff (qbdiff) is a tool for generating and applying binary
patches. It builds on the general ideas of bsdiff.

It is designed to be faster than bsdiff by taking advantage of multiple CPU
cores. It is also designed to produce generally smaller patch files, and
supports only LZMA compression as it performs well on sparse binary data.
Further it aims to be frugal on memory usage and provides integrity checking
using BLAKE2B.

This package contains the files required for building using bsdiff.

%prep
%autosetup -p1
# avoid "UNKNOWN"
echo "%{version}" > .tarball-version

%build
autoreconf -fiv
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license LICENSE 3rdparty/libsais-LICENSE
%doc README.md TODO
%{_bindir}/qbdiff
%{_bindir}/qbpatch
%{_mandir}/man1/qbdiff.1%{?ext_man}
%{_mandir}/man1/qbpatch.1%{?ext_man}

%files -n lib%{name}%{sover}
%license LICENSE 3rdparty/libsais-LICENSE
%{_libdir}/libqbdiff.so.%{sover}
%{_libdir}/libqbdiff.so.%{sover}.*

%files devel
%license LICENSE 3rdparty/libsais-LICENSE
%{_includedir}/libqbdiff.h
%{_libdir}/libqbdiff.so
%{_libdir}/pkgconfig/qbdiff.pc

%changelog
