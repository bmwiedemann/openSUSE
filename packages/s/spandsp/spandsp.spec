#
# spec file for package spandsp
#
# Copyright (c) 2020 SUSE LLC
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


Name:           spandsp
%define lname	libspandsp2
Summary:        A DSP library for Telephony and SoftFAX
License:        LGPL-2.1-only AND GPL-2.0-only
Group:          Development/Libraries/C and C++
Version:        0.0.6
Release:        0
URL:            http://soft-switch.org/

Source:         http://soft-switch.org/downloads/spandsp/%name-%version.tar.gz
Source2:        baselibs.conf
Patch1:         spandsp-autoconf.diff
Patch2:         spandsp-raise-traintime-tolerance.diff
Patch3:         spandsp-handle-international-dialstring-prefix.diff
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkg-config
%define tests 0
%if 0%{?tests}
BuildRequires:  fftw3-devel
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(xproto)
%endif

%description
SpanDSP is a library of DSP functions for telephony, in the 8000 sample
per second world of E1s, T1s, and higher order PCM channels. It
contains low level functions, such as basic filters. It also contains
higher level functions, such as cadenced supervisory tone detection,
and a complete software FAX machine.

%package devel
Summary:        Development files for the SpanDSP library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel
Requires:       libtiff-devel

%description devel
This package contains files that are needed for developing or compiling
software that uses the spandsp library.

%package -n %lname
Summary:        A DSP library for Telephony and SoftFAX
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n %lname
SpanDSP is a library of DSP functions for telephony, in the 8000 sample
per second world of E1s, T1s, and higher order PCM channels. It
contains low level functions, such as basic filters. It also contains
higher level functions, such as cadenced supervisory tone detection,
and a complete software FAX machine.

%package doc
Summary:        Documentation for the libspandsp API
License:        LGPL-2.1-only AND GPL-2.0-only
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains documentation for the libspandsp API.

%prep
%autosetup -n %name-0.0.6 -p1

%build
%define _lto_cflags %nil
autoreconf -fiv
# Enabling MMX could be safe.. I see cpuid calls in the source
%configure \
%ifarch i586 i686
	--enable-mmx \
%endif
%ifarch x86_64
	--enable-sse --enable-sse2 \
%endif
	--disable-static \
	--enable-doc
%make_build

%check
%if 0%{?tests}
%make_build check
%endif

%install
%make_install
mkdir -p "%buildroot%_docdir/%name"
cp -a NEWS README DueDiligence ChangeLog doc/api/html \
	"%buildroot/%_docdir/%name"
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files devel
%license COPYING
%_includedir/*
%_libdir/lib%name.so
%_libdir/pkgconfig/*.pc

%files -n %lname
%_libdir/lib%name.so.2*

%files doc
%_docdir/%name/

%changelog
