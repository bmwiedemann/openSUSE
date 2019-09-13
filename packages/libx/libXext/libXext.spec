#
# spec file for package libXext
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libXext
%define lname	libXext6
Version:        1.3.4
Release:        0
Summary:        Common extensions to the X11 protocol
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXext
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXext/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11) >= 1.1.99.1
BuildRequires:  pkgconfig(xextproto) >= 7.1.99
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto) >= 7.0.13

%description
The Xext library contains a handful of X11 extensions:
- Double Buffer extension (DBE/Xdbe)
- Display Power Management Signaling (DPMS) extension
- X11 Nonrectangular Window Shape extension (Xshape)
- The MIT Shared Memory extension (MIT-SHM/Xshm)
- TOG-CUP (colormap utilization policy) protocol extension (Xcup)
- X Extended Visual Information extension (XEvi)
- X11 Double-Buffering, Multi-Buffering, and Stereo extension (Xmbuf)

%package -n %lname
Summary:        Common extensions to the X11 protocol
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libXext = 7.6_%version-%release
Obsoletes:      xorg-x11-libXext < 7.6_%version-%release

%description -n %lname
The Xext library contains a handful of X11 extensions:
- Double Buffer extension (DBE/Xdbe)
- Display Power Management Signaling (DPMS) extension
- X11 Nonrectangular Window Shape extension (Xshape)
- The MIT Shared Memory extension (MIT-SHM/Xshm)
- TOG-CUP (colormap) protocol extension (Xcup)
- X Extended Visual Information extension (XEvi)
- X11 Double-Buffering, Multi-Buffering, and Stereo extension (Xmbuf)

%package devel
Summary:        Development files for the X11 Common Extensions library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXext-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXext-devel < 7.6_%version-%release

%description devel
The Xext library contains a handful of X11 extensions:
- Double Buffer extension (DBE/Xdbe)
- Display Power Management Signaling (DPMS) extension
- X11 Nonrectangular Window Shape extension (Xshape)
- The MIT Shared Memory extension (MIT-SHM/Xshm)
- TOG-CUP (colormap) protocol extension (Xcup)
- X Extended Visual Information extension (XEvi)
- X11 Double-Buffering, Multi-Buffering, and Stereo extension (Xmbuf)

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --docdir=%_docdir/%name --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXext.so.6*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXext.so
%_libdir/pkgconfig/xext.pc
%_mandir/man3/*
%_docdir/%name

%changelog
