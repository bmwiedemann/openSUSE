#
# spec file for package flac
#
# Copyright (c) 2022 SUSE LLC
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


%define sover      12
%define sover_plus 10

Name:           flac
Version:        1.4.2
Release:        0
Summary:        Free Lossless Audio Codec
License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.2-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://xiph.org/flac/
#Git-Web:       https://github.com/xiph/flac
#Git-Clone:     https://github.com/xiph/flac.git
#Changelog:     https://xiph.org/flac/changelog.html
Source:         https://downloads.xiph.org/releases/flac/%{name}-%{version}.tar.xz
Source2:        baselibs.conf

BuildRequires:  autoconf >= 2.60
BuildRequires:  automake >= 1.11
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(ogg)
Obsoletes:      %{name}-doc

%description
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation. Digital audio compressed by FLAC's
algorithm can typically be reduced to between 50 and 70 percent of
its original size, and decompresses to an identical copy of the
original audio data.

%package -n libFLAC%{sover}
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries
Obsoletes:      libflac < %{version}
Provides:       libflac = %{version}

%description -n libFLAC%{sover}
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation.

This package contains the C API library for FLAC.

%package -n libFLAC++%{sover_plus}
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries

%description -n libFLAC++%{sover_plus}
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation.

This package contains the C++ API library for FLAC.

%package devel
Summary:        FLAC Library Development Package
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libFLAC%{sover} = %{version}
Requires:       libFLAC++%{sover_plus} = %{version}
Requires:       libstdc++-devel

%description devel
This package contains the files needed to compile programs that use
the FLAC library.

%prep
%autosetup -p1

%build
autoreconf -fvi
%configure \
	--disable-silent-rules \
	--disable-thorough-tests \
	--disable-static \
	--disable-rpath
%make_build

%install
%make_install docdir="%{_docdir}/%{name}"
find %{buildroot} -type f -name "*.la" -delete -print
# wrongy installed docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}/

%check
make check %{?_smp_mflags}

%ldconfig_scriptlets -n libFLAC%{sover}
%ldconfig_scriptlets -n libFLAC++%{sover_plus}

%files
%doc README.md
%{_bindir}/*
%{_mandir}/man*/*

%files -n libFLAC%{sover}
%license COPYING*
%{_libdir}/libFLAC.so.%{sover}*

%files -n libFLAC++%{sover_plus}
%license COPYING*
%{_libdir}/libFLAC++.so.%{sover_plus}*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/README.md

%changelog
