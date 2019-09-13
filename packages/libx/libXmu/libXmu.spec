#
# spec file for package libXmu
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


Name:           libXmu
Version:        1.1.3
Release:        0
Summary:        Miscellaneous utility routines for X
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXmu
#Git-Web:       http://cgit.freedesktop.org/xorg/lib/libXmu/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtrans)

%description
The Xmu Library is a collection of miscellaneous (some might say random)
utility functions that have been useful in building various applications
and widgets. This library is required by the Athena Widgets.

%package -n libXmu6
Summary:        Miscellaneous utility routines for X
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libXmu = 7.6_%version-%release
Obsoletes:      xorg-x11-libXmu < 7.6_%version-%release
Requires:       xbitmaps

%description -n libXmu6
The Xmu library is a collection of miscellaneous (some might say random)
utility functions that have been useful in building various applications
and widgets, specifically the Athena Widgets.

%package -n libXmuu1
Summary:        More miscellaneous utility routines for X
Group:          System/Libraries

%description -n libXmuu1
The Xmu/Xmuu libraries are a collection of miscellaneous (some might
say random) utility functions that have been useful in building
various applications and widgets.

%package devel
Summary:        Development files for the X Miscellaneous Utility Libraries
Group:          Development/Libraries/C and C++
Requires:       libXmu6 = %version
Requires:       libXmuu1 = %version
# O/P added for 12.2
Provides:       xorg-x11-libXmu-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXmu-devel < 7.6_%version-%release
Requires:       xbitmaps-devel

%description devel
The Xmu/Xmuu libraries are a collection of miscellaneous (some might
say random) utility functions that have been useful in building
various applications and widgets.

This package contains the development headers for the library found
in libXmu6 and libXmuu1.

%prep
%setup -q

%build
%configure --docdir=%_docdir/%name --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post   -n libXmu6 -p /sbin/ldconfig

%postun -n libXmu6 -p /sbin/ldconfig

%post   -n libXmuu1 -p /sbin/ldconfig

%postun -n libXmuu1 -p /sbin/ldconfig

%files -n libXmu6
%defattr(-,root,root)
%_libdir/libXmu.so.6*

%files -n libXmuu1
%defattr(-,root,root)
%_libdir/libXmuu.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXmu*.so
%_libdir/pkgconfig/xmu*.pc
%_docdir/%name

%changelog
