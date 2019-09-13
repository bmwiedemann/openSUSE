#
# spec file for package chromaprint
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname      1
%bcond_without ffmpeg
Name:           chromaprint
Version:        1.4.3
Release:        0
Summary:        Audio Fingerprinting Library
License:        MIT AND LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            https://acoustid.org/chromaprint
Source0:        https://github.com/acoustid/chromaprint/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  libtag-devel
BuildRequires:  pkgconfig
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
%endif

%description
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.

%package -n libchromaprint%{soname}
Summary:        Audio Fingerprinting Library
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libchromaprint%{soname}
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.

%package -n libchromaprint-devel
Summary:        Audio Fingerprinting Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       fftw3-devel
Requires:       libchromaprint%{soname} = %{version}
Requires:       libtag-devel

%description -n libchromaprint-devel
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.

%if %{with ffmpeg}
%package fpcalc
Summary:        Chromaprint Audio Fingerprinting Command Line Tool
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       libchromaprint%{soname} = %{version}
Provides:       fpcalc = %{version}

%description fpcalc
Chromaprint is the core component of the Acoustid project. It's a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.
This package contains fpcalc, a command-line tool to perform Chromaprint
fingerprinting.
%endif

%prep
%setup -qn %{name}-v%{version}

%build
%cmake \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
%if %{with ffmpeg}
    -DUSE_AVFFT=ON \
    -DBUILD_TOOLS=ON
%endif

make %{?_smp_mflags}

%install
%cmake_install

%post   -n libchromaprint%{soname} -p /sbin/ldconfig
%postun -n libchromaprint%{soname} -p /sbin/ldconfig

%files -n libchromaprint%{soname}
%doc LICENSE.md NEWS.txt README.md
%{_libdir}/libchromaprint.so.%{soname}
%{_libdir}/libchromaprint.so.%{soname}.*

%files -n libchromaprint-devel
%{_includedir}/chromaprint.h
%{_libdir}/libchromaprint.so
%{_libdir}/pkgconfig/libchromaprint.pc

%if %{with ffmpeg}
%files fpcalc
%{_bindir}/fpcalc
%endif

%changelog
