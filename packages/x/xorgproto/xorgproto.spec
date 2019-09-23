#
# spec file for package xorgproto
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


Name:           xorgproto
Version:        2019.1
Release:        0
Url:            http://xorg.freedesktop.org/
Summary:        The X11 Protocol collection
License:        MIT
Group:          Development/Libraries/X11

#Git-Clone:	git://anongit.freedesktop.org/xorg/proto/xorgproto
#Git-Web:	http://cgit.freedesktop.org/xorg/proto/xorgproto/
Source:         http://xorg.freedesktop.org/releases/individual/proto/%name-%version.tar.bz2
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The X11 protocol headers for X11 development.
This package contains all previously split protocol packages:
applewmproto, bigreqsproto, compositeproto, damageproto, dmxproto, dri2proto,
dri3proto, fixesproto, fontsproto, glproto, inputproto, kbproto, presentproto, 
randrproto, recordproto, renderproto, resourceproto, scrnsaverproto, trapproto,
videoproto, windowswmproto, xcmiscproto, xextproto, xf86bigfontproto, 
xf86dgaproto, xf86driproto, xf86miscproto, xf86vidmodeproto, xineramaproto, 
xproto and xproxymngproto.

%package devel
Summary:        The X11 Protocol collection
Group:          Development/Libraries/X11

Obsoletes:      xorgproto-devel < %{version}
# the next is for obsoleting applewmproto <= 1.4.2
Obsoletes:      bigreqsproto-devel <= 1.1.2
Obsoletes:      compositeproto-devel <= 0.4.2
Obsoletes:      damageproto-devel <= 1.2.1
Obsoletes:      dmxproto-devel <= 2.3.1
Obsoletes:      dri2proto-devel <= 2.8
Obsoletes:      dri3proto-devel <= 1.2
Obsoletes:      fixesproto-devel <= 5.0
Obsoletes:      fontsproto-devel <= 2.1.3
Obsoletes:      glproto-devel <= 1.4.17
Obsoletes:      inputproto-devel <= 2.3.2
Obsoletes:      kbproto-devel <= 1.0.7
Obsoletes:      presentproto-devel <= 1.2
Obsoletes:      randrproto-devel <= 1.6.0
Obsoletes:      recordproto-devel <= 1.14.2
Obsoletes:      renderproto-devel <= 0.11.1
Obsoletes:      resourceproto-devel <= 1.2.0
Obsoletes:      scrnsaverproto-devel <= 1.2.2
Obsoletes:      trapproto-devel <= 3.4.3
Obsoletes:      videoproto-devel <= 2.3.3
Obsoletes:      windowswmproto-devel <= 1.0.4
Obsoletes:      xcmiscproto-devel <= 1.2.2
Obsoletes:      xextproto-devel <= 7.3.0
Obsoletes:      xf86bigfontproto-devel <= 1.2.0
Obsoletes:      xf86dgaproto-devel <= 2.1
Obsoletes:      xf86driproto-devel <= 2.1.1
Obsoletes:      xf86miscproto-devel <= 0.9.3
Obsoletes:      xf86vidmodeproto-devel <= 2.3.1
Obsoletes:      xineramaproto-devel <= 1.2.1
Obsoletes:      xorg-x11-proto-devel
Obsoletes:      xproto-devel <= 7.0.32
Obsoletes:      xproxymngproto-devel <= 1.0.3

%description devel
The compelte X11 protocol headers for X11 development.
This package contains all previously split protocol packages:
applewmproto, bigreqsproto, compositeproto, damageproto, dmxproto, dri2proto,
dri3proto, fixesproto, fontsproto, glproto, inputproto, kbproto, presentproto, 
randrproto, recordproto, renderproto, resourceproto, scrnsaverproto, trapproto,
videoproto, windowswmproto, xcmiscproto, xextproto, xf86bigfontproto, 
xf86dgaproto, xf86driproto, xf86miscproto, xf86vidmodeproto, xineramaproto, 
xproto and xproxymngproto.

%prep
%setup -q

%build
#autoreconf -fi
%if (0%{?suse_version} < 1550)
%configure --enable-legacy
%else
%configure
%endif
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
%if (0%{?suse_version} < 1550)
# we seriously don't want to package that again ...
rm %{buildroot}%{_mandir}/man7/Xprint.7
%endif

%files devel
%defattr(-,root,root)
%doc %_datadir/doc/*
%_includedir/X11/
%_includedir/GL/
%{_datarootdir}/pkgconfig/*.pc

%changelog
