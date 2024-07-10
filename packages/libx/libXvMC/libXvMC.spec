#
# spec file for package libXvMC
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


Name:           libXvMC
%define lname	libXvMC1
Version:        1.0.14
Release:        0
Summary:        X-Video Motion Compensation library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXvMC
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXvMC/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xv)

%description
X-Video Motion Compensation (XvMC), is an extension of the X video
extension (Xv) for the X Window System. The XvMC API allows video
programs to offload portions of the video decoding process to the GPU
video-hardware.

%package -n %lname
Summary:        X-Video Motion Compensation library
Group:          System/Libraries

%description -n %lname
X-Video Motion Compensation (XvMC), is an extension of the X video
extension (Xv) for the X Window System. The XvMC API allows video
programs to offload portions of the video decoding process to the GPU
video-hardware.

The supported portions to be offloaded by XvMC onto the GPU are
motion compensation (mo comp) and inverse discrete cosine transform
(iDCT) for MPEG-2 video. XvMC also supports offloading decoding of mo
comp, iDCT, and VLD (Variable-Length Decoding) for MPEG-2/MPEG-4-ASP.

%package devel
Summary:        Development files for the X-Video Motion Compensation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Conflicts:      xorgproto-devel < 2019.2
Provides:       xorgproto-devel:%{_includedir}/X11/extensions/vldXvMC.h

%description devel
X-Video Motion Compensation (XvMC), is an extension of the X video
extension (Xv) for the X Window System. The XvMC API allows video
programs to offload portions of the video decoding process to the GPU
video-hardware.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
rm -f "%buildroot/%_libdir"/*.a
mkdir -p %buildroot/%_docdir/%name
mv %buildroot/%{_datadir}/doc/%name \
   %buildroot/%{_docdir}/%name

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXvMC*.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXvMC*.so
%_libdir/pkgconfig/xvmc.pc
%_libdir/pkgconfig/xvmc-wrapper.pc
%_docdir/%name

%changelog
