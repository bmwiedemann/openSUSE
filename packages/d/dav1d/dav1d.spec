#
# spec file for package dav1d
#
# Copyright (c) 2021 SUSE LLC
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


%define _lto_cflags %{nil}
%define sover   5
Name:           dav1d
Version:        0.8.2
Release:        0
Summary:        An AV1 decoder
License:        BSD-2-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://code.videolan.org/videolan/dav1d
Source0:        https://code.videolan.org/videolan/dav1d/-/archive/%{version}/dav1d-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  meson >= 0.49.0
BuildRequires:  nasm >= 2.14
BuildRequires:  pkgconfig
# necessary to meson
BuildRequires:  rpm >= 4.14

%description
dav1d is a SIMD-enhanced decoder for AV1 video. It features

 * Accelerated assembly using x86 AVX2.
 * Partial acceleration using x86 SSSE3 and ARM NEON.
 * Support for bitdepths 8, 10 and 12.
 * Support for chroma subsamplings 4:2:0, 4:2:2, 4:4:4 and grayscale.

AV1 is a royalty-free video codec by the Alliance for Open Media. It
has the potential to be up to 20%% better than the HEVC codec.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n lib%{name}%{sover}
Summary:        AV1 decoder library
Group:          System/Libraries

%description -n lib%{name}%{sover}
%{name} is an AV1 decoder library.

%prep
%autosetup -p1

%build
# disabling xxhash until it can be built properly
%meson -Dxxhash_muxer=disabled
%meson_build

%install
%meson_install

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%{_bindir}/%{name}

%files devel
%doc CONTRIBUTING.md doc/PATENTS NEWS README.md THANKS.md
%license COPYING
%{_includedir}/dav1d
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}%{sover}
%license COPYING
%{_libdir}/lib%{name}.so.%{sover}*

%changelog
