#
# spec file for package grail
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname  libgrail
%define sover   6
Name:           grail
Version:        3.1.1
Release:        0
Summary:        Gesture recognition library
License:        LGPL-3.0 AND GPL-3.0
Group:          Hardware/Other
Url:            https://launchpad.net/grail
Source:         https://launchpad.net/grail/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
Source1:        https://launchpad.net/grail/trunk/%{version}/+download/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-server-sdk
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(evemu)
BuildRequires:  pkgconfig(frame-x11)
BuildRequires:  pkgconfig(inputproto) >= 2.1.99.6
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi) >= 1.5.99.1
Provides:       %{name}-tools = %{version}
Obsoletes:      %{name}-tools < %{version}

%description
This tree consists of an interface and tools for handling gesture
recognition and gesture instantiation.
The library handles tentative getures, i.e., buffering of events
for several alternative gestures until a match is confirmed.

%package -n %{soname}%{sover}
Summary:        Gesture recognition library
Group:          System/Libraries

%description -n %{soname}%{sover}
This tree consists of an interface and tools for handling gesture
recognition and gesture instantiation.

The library handles tentative getures, i.e., buffering of events
for several alternative gestures until a match is confirmed.

%package devel
Summary:        Development files for gesture recognition library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{soname}%{sover} = %{version}

%description devel
Development files for the gesture recognition library (grail).
The library handles tentative getures, i.e., buffering of events
for several alternative gestures until a match is confirmed.

%prep
%setup -q

%build
autoreconf -fi
%configure \
  --disable-static       \
  --disable-silent-rules
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%doc AUTHORS COPYING* README
%{_bindir}/%{name}-test-*
%{_mandir}/man?/%{name}-test-*.?%{?ext_man}

%files -n %{soname}%{sover}
%doc AUTHORS COPYING* README
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%dir %{_includedir}/oif/
%{_includedir}/oif/%{name}.h
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
