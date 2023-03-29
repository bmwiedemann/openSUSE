#
# spec file for package spandsp
#
# Copyright (c) 2023 SUSE LLC
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
%define lname	libspandsp3
Version:        3.0.0.g15
Release:        0
Summary:        A DSP library for Telephony and SoftFAX
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/freeswitch/spandsp

Source:         %name-%version.tar.xz
Source2:        baselibs.conf
Patch1:         no-sse.diff
Patch2:         spandsp-raise-traintime-tolerance.diff
Patch3:         spandsp-handle-international-dialstring-prefix.diff
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libjpeg-devel
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
Requires:       libjpeg-devel
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
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains documentation for the libspandsp API.

%prep
%autosetup -p1
# The cpuid calls in the source code only apply to a test program.
# The library itself is (was) statically enabling -msse during configure, which
# is now removed.

%build
autoreconf -fiv
%configure \
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
ln -s ../spandsp.h "%buildroot/%_includedir/spandsp/spandsp.h"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files devel
%license COPYING
%_includedir/*
%_libdir/lib%name.so
%_libdir/pkgconfig/*.pc

%files -n %lname
%_libdir/lib%name.so.3*

%files doc
%_docdir/%name/

%changelog
