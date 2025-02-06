#
# spec file for package chromaprint
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


%define rev aa67c95b9e486884a6d3ee8b0c91207d8c2b0551
%define soname      1
Name:           chromaprint
Version:        1.5.1+git.20221217
Release:        0
Summary:        Audio Fingerprinting Library
License:        LGPL-2.1-only AND MIT
URL:            https://acoustid.org/chromaprint
#https://github.com/acoustid/chromaprint/archive/refs/
Source0:        https://github.com/acoustid/chromaprint/archive/%{rev}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         0005-Fix-compatibility-with-ffmpeg-7.0.patch

BuildRequires:  cmake
BuildRequires:  ffmpeg-7-libavcodec-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)

%description
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.

%package -n libchromaprint%{soname}
Summary:        Audio Fingerprinting Library
License:        LGPL-2.1-or-later

%description -n libchromaprint%{soname}
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.

%package -n libchromaprint-devel
Summary:        Audio Fingerprinting Library
License:        LGPL-2.1-or-later
Requires:       libchromaprint%{soname} = %{version}

%description -n libchromaprint-devel
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.

%package fpcalc
Summary:        Chromaprint Audio Fingerprinting Command Line Tool
License:        GPL-2.0-or-later
Requires:       libchromaprint%{soname} = %{version}
Provides:       fpcalc = %{version}

%description fpcalc
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.
This package contains fpcalc, a command-line tool to perform Chromaprint
fingerprinting.

%prep
%autosetup -p1 -n %{name}-%{rev}

%build
%cmake \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
    -DUSE_AVFFT=ON -DFFT_LIB=kissfft \
    -DBUILD_TESTS=OFF -DBUILD_TOOLS=ON

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libchromaprint%{soname}

%files -n libchromaprint%{soname}
%license LICENSE.md
%doc NEWS.txt README.md
%{_libdir}/libchromaprint.so.%{soname}
%{_libdir}/libchromaprint.so.%{soname}.*

%files -n libchromaprint-devel
%{_includedir}/chromaprint.h
%{_libdir}/libchromaprint.so
%{_libdir}/pkgconfig/libchromaprint.pc

%files fpcalc
%{_bindir}/fpcalc

%changelog
