#
# spec file for package zvbi
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


%define         sover 0
%define         libname lib%{name}%{sover}
%define         libchains lib%{name}-chains%{sover}
Name:           zvbi
Version:        0.2.38
Release:        0
Summary:        Linux "VBI proxy"
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://github.com/zapping-vbi/zvbi/
Source:         https://github.com/zapping-vbi/zvbi/archive/refs/tags/v%{version}.tar.gz
Source2:        baselibs.conf
Patch10:        10_fix_private_libs.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  timezone
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang

%description
With "video4linux" drivers, only one application at a time can capture
VB data.  The 2nd generation "v4l2" API allows multiple clients to
open a device, but still only one client may read from the device.  If,
for example, the Nxtvepg daemon runs in the background, users will not be
able to start a Teletext application.  The VBI proxy was developed as a
solution to this problem.

%package -n %{libname}
Summary:        VBI Decoding Library
Group:          System/Libraries

%description -n %{libname}
VBI stands for Vertical Blanking Interval, a gap between the image data
transmitted in an analog video signal. This gap is used to transmit AM
modulated data for various data services like Teletext and Closed
Caption.

The zvbi library provides routines to read from raw VBI sampling
devices, to demodulate raw to sliced VBI data, and to interpret the
data of several popular services.

%package -n %{libchains}
Summary:        VBI Decoding Library
Group:          System/Libraries
Conflicts:      %{libname} < %{version}-%{release}

%description -n %{libchains}
VBI stands for Vertical Blanking Interval, a gap between the image data
transmitted in an analog video signal. This gap is used to transmit AM
modulated data for various data services like Teletext and Closed
Caption.

The zvbi library provides routines to read from raw VBI sampling
devices, to demodulate raw to sliced VBI data, and to interpret the
data of several popular services.

%package devel
Summary:        Development files for the VBI decoding library
Group:          Development/Libraries/C and C++
Requires:       %{libchains} = %{version}
Requires:       %{libname} = %{version}

%description devel
This package includes the development files for the zvbi library which
provides routines to read from raw VBI sampling devices, to demodulate raw to
sliced VBI data, and to interpret the data of several popular services.

%lang_package

%prep
%setup -q
%patch10 -p1

%build
ACLOCAL="aclocal -I m4" autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%check
# This requires timezone package to be installed
%make_build check

%post -n %{libname} -p /sbin/ldconfig
%post -n %{libchains} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%postun -n %{libchains} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS BUGS ChangeLog NEWS README.md TODO
%{_bindir}/zvbi-atsc-cc
%{_bindir}/zvbi-chains
%{_bindir}/zvbi-ntsc-cc
%{_sbindir}/zvbid
%{_mandir}/man1/zvbi-atsc-cc.1%{?ext_man}
%{_mandir}/man1/zvbi-chains.1%{?ext_man}
%{_mandir}/man1/zvbi-ntsc-cc.1%{?ext_man}
%{_mandir}/man1/zvbid.1%{?ext_man}

%files lang -f %{name}.lang

%files -n %{libname}
%{_libdir}/libzvbi.so.%{sover}*

%files -n %{libchains}
%{_libdir}/libzvbi-chains.so.%{sover}*

%files devel
%{_includedir}/libzvbi.h
%{_libdir}/libzvbi.so
%{_libdir}/libzvbi-chains.so
%{_libdir}/pkgconfig/zvbi-*.pc

%changelog
