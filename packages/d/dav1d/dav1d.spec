#
# spec file for package dav1d
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


%define sover   7

Name:           dav1d
Version:        1.4.3
Release:        0
Summary:        An AV1 decoder
License:        BSD-2-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://code.videolan.org/videolan/dav1d
Source:         %{url}/-/archive/%{version}/dav1d-%{version}.tar.gz
Source99:       baselibs.conf

BuildRequires:  meson >= 0.49.0
BuildRequires:  nasm >= 2.14
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxxhash)

%description
dav1d is a SIMD-enhanced decoder for AV1 video. It features

 * Accelerated assembly using x86 AVX2.
 * Partial acceleration using x86 SSSE3 and ARM NEON.
 * Support for bitdepths 8, 10 and 12.
 * Support for chroma subsamplings 4:2:0, 4:2:2, 4:4:4 and grayscale.

AV1 is a royalty-free video codec by the Alliance for Open Media. It
has the potential to be up to 20%% better than the HEVC codec.
dav1d outperforms gav1 by about 20%% on ARM and 50%% on x86,
and has better scaling properties for larger thread counts.

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
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%ldconfig_scriptlets -n lib%{name}%{sover}

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
