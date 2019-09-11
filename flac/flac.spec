#
# spec file for package flac
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           flac
Version:        1.3.2
Release:        0
Summary:        Free Lossless Audio Codec
License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.2-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://xiph.org/flac/
#Git-Web:	https://git.xiph.org/?p=flac.git
#Git-Clone:	git://git.xiph.org/flac
Source:         http://downloads.xiph.org/releases/flac/%{name}-%{version}.tar.xz
Source2:        baselibs.conf
Patch0:         flac-cflags.patch
Patch1:         flac-CVE-2017-6888.patch
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake >= 1.11
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(ogg)
Obsoletes:      %{name}-doc
%ifarch %{ix86}
BuildRequires:  nasm
%endif

%description
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation. Digital audio compressed by FLAC's
algorithm can typically be reduced to between 50 and 70 percent of
its original size, and decompresses to an identical copy of the
original audio data.

%package -n libFLAC8
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries
Obsoletes:      libflac < %{version}
Provides:       libflac = %{version}

%description -n libFLAC8
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation.

This package contains the C API library for FLAC.

%package -n libFLAC++6
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries

%description -n libFLAC++6
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation.

This package contains the C++ API library for FLAC.

%package devel
Summary:        FLAC Library Development Package
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libFLAC++6 = %{version}
Requires:       libFLAC8 = %{version}
Requires:       libstdc++-devel

%description devel
This package contains the files needed to compile programs that use the
FLAC library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fvi
%configure \
	--disable-silent-rules \
	--disable-thorough-tests \
	--disable-xmms-plugin \
	--disable-static \
	--disable-rpath \
	--enable-sse
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# wrongy installed docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}/

%check
make check %{?_smp_mflags}

%post -n libFLAC8 -p /sbin/ldconfig
%postun -n libFLAC8 -p /sbin/ldconfig
%post -n libFLAC++6 -p /sbin/ldconfig
%postun -n libFLAC++6 -p /sbin/ldconfig

%files
%doc AUTHORS README
%{_bindir}/*
%{_mandir}/man*/*

%files -n libFLAC8
%license COPYING*
%{_libdir}/libFLAC.so.8*

%files -n libFLAC++6
%license COPYING*
%{_libdir}/libFLAC++.so.6*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
