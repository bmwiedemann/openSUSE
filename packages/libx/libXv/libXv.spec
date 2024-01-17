#
# spec file for package libXv
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


Name:           libXv
%define lname	libXv1
Version:        1.0.12
Release:        0
Summary:        X Video extension library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXv
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXv/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The X Video Extension (Xv) extension provides support for video
adaptors attached to an X display. It takes the approach that a
display may have one or more video adaptors, each of which has one or
more ports through which independent video streams pass.

%package -n %lname
Summary:        X Video extension library
Group:          System/Libraries
# O/P added for 12.2
Provides:       xorg-x11-libXv = 7.6_%version-%release
Obsoletes:      xorg-x11-libXv < 7.6_%version-%release

%description -n %lname
The X Video Extension (Xv) extension provides support for video
adaptors attached to an X display. It takes the approach that a
display may have one or more video adaptors, each of which has one or
more ports through which independent video streams pass.

Its use is to rescale video playback, do colorspace conversions, and
change contrast, brightness and hue using video controller hardware
acceleration.

%package devel
Summary:        Development files for the X Video extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXv-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXv-devel < 7.6_%version-%release

%description devel
The X Video Extension (Xv) extension provides support for video
adaptors attached to an X display. It takes the approach that a
display may have one or more video adaptors, each of which has one or
more ports through which independent video streams pass.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXv.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXv.so
%_libdir/pkgconfig/xv.pc
%_mandir/man3/*

%changelog
