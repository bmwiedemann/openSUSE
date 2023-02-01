#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%global psuffix -doc
%else
%global psuffix %{nil}
%endif

%define srcname xorgproto

Name:           %{srcname}%{psuffix}
Version:        2022.2
Release:        0
%if "%{flavor}" == "doc"
Summary:        The X11 Protocol collection (documentation)
%else
Summary:        The X11 Protocol collection
%endif
License:        MIT
Group:          Development/Libraries/X11
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/proto/xorgproto
#Git-Web:	http://cgit.freedesktop.org/xorg/proto/xorgproto/
Source0:        https://xorg.freedesktop.org/releases/individual/proto/%{srcname}-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/proto/%{srcname}-%{version}.tar.xz.sig
Source2:        xorgproto.keyring
BuildRequires:  fdupes
BuildRequires:  pkgconfig
%if "%{flavor}" == "doc"
BuildRequires:  fop
BuildRequires:  xmlto
BuildRequires:  xorg-sgml-doctools
BuildRequires:  xsltproc
%endif
BuildArch:      noarch

%if "%{flavor}" == "doc"
%description
Documentation for X11 protocol headers.
%else

%description
The X11 protocol headers for X11 development.
This package contains all previously split protocol packages:
applewmproto, bigreqsproto, compositeproto, damageproto, dmxproto, dri2proto,
dri3proto, fixesproto, fontsproto, glproto, inputproto, kbproto, presentproto,
randrproto, recordproto, renderproto, resourceproto, scrnsaverproto, trapproto,
videoproto, windowswmproto, xcmiscproto, xextproto, xf86bigfontproto,
xf86dgaproto, xf86driproto, xf86miscproto, xf86vidmodeproto, xineramaproto,
xproto and xproxymngproto.
%endif

%package devel
Summary:        The X11 Protocol collection
Group:          Development/Libraries/X11
Obsoletes:      xorgproto-devel < %{version}
# the next is for obsoleting applewmproto <= 1.4.2
Obsoletes:      bigreqsproto-devel <= 1.1.2
Provides:       bigreqsproto-devel = %{version}
Obsoletes:      compositeproto-devel <= 0.4.2
Provides:       compositeproto-devel = %{version}
Obsoletes:      damageproto-devel <= 1.2.1
Provides:       damageproto-devel = %{version}
Obsoletes:      dmxproto-devel <= 2.3.1
Provides:       dmxproto-devel = %{version}
Obsoletes:      dri2proto-devel <= 2.8
Provides:       dri2proto-devel = %{version}
Obsoletes:      dri3proto-devel <= 1.2
Provides:       dri3proto-devel = %{version}
Obsoletes:      fixesproto-devel <= 5.0
Provides:       fixesproto-devel = %{version}
Obsoletes:      fontsproto-devel <= 2.1.3
Provides:       fontsproto-devel = %{version}
Obsoletes:      glproto-devel <= 1.4.17
Provides:       glproto-devel = %{version}
Obsoletes:      inputproto-devel <= 2.3.2
Provides:       inputproto-devel = %{version}
Obsoletes:      kbproto-devel <= 1.0.7
Provides:       kbproto-devel = %{version}
Obsoletes:      presentproto-devel <= 1.2
Provides:       presentproto-devel = %{version}
Obsoletes:      randrproto-devel <= 1.6.0
Provides:       randrproto-devel = %{version}
Obsoletes:      recordproto-devel <= 1.14.2
Provides:       recordproto-devel = %{version}
Obsoletes:      renderproto-devel <= 0.11.1
Provides:       renderproto-devel = %{version}
Obsoletes:      resourceproto-devel <= 1.2.0
Provides:       resourceproto-devel = %{version}
Provides:       scrnsaverproto-devel = %{version}
Obsoletes:      scrnsaverproto-devel <= 1.2.2
Provides:       trapproto-devel = %{version}
Obsoletes:      trapproto-devel <= 3.4.3
Provides:       videoproto-devel = %{version}
Obsoletes:      videoproto-devel <= 2.3.3
Provides:       windowswmproto-devel = %{version}
Obsoletes:      windowswmproto-devel <= 1.0.4
Provides:       xcmiscproto-devel = %{version}
Obsoletes:      xcmiscproto-devel <= 1.2.2
Provides:       xextproto-devel = %{version}
Obsoletes:      xextproto-devel <= 7.3.0
Provides:       xf86bigfontproto-devel = %{version}
Obsoletes:      xf86bigfontproto-devel <= 1.2.0
Provides:       xf86dgaproto-devel = %{version}
Obsoletes:      xf86dgaproto-devel <= 2.1
Provides:       xf86driproto-devel = %{version}
Obsoletes:      xf86driproto-devel <= 2.1.1
Provides:       xf86miscproto-devel = %{version}
Obsoletes:      xf86miscproto-devel <= 0.9.3
Provides:       xf86vidmodeproto-devel = %{version}
Obsoletes:      xf86vidmodeproto-devel <= 2.3.1
Provides:       xineramaproto-devel = %{version}
Obsoletes:      xineramaproto-devel <= 1.2.1
Obsoletes:      xorg-x11-proto-devel < %{version}
Provides:       xorg-x11-proto-devel = %{version}
Obsoletes:      xproto-devel <= 7.0.32
Provides:       xproto-devel = %{version}
Obsoletes:      xproxymngproto-devel <= 1.0.3
Provides:       xproxymngproto-devel = %{version}

%description devel
The complete X11 protocol headers for X11 development.
This package contains all previously split protocol packages:
applewmproto, bigreqsproto, compositeproto, damageproto, dmxproto, dri2proto,
dri3proto, fixesproto, fontsproto, glproto, inputproto, kbproto, presentproto,
randrproto, recordproto, renderproto, resourceproto, scrnsaverproto, trapproto,
videoproto, windowswmproto, xcmiscproto, xextproto, xf86bigfontproto,
xf86dgaproto, xf86driproto, xf86miscproto, xf86vidmodeproto, xineramaproto,
xproto and xproxymngproto.

%prep
%setup -q -n %{srcname}-%{version}

%build
%if (0%{?suse_version} < 1550)
%configure --enable-legacy
%else
%configure
%endif
%make_build

%install
%make_install
%if (0%{?suse_version} < 1550)
%endif
%fdupes '%{buildroot}%{_datadir}'

%if "%{flavor}" == "doc"
%files
%doc %{_datadir}/doc/*
%{nil <URL: https://bugzilla.opensuse.org/show_bug.cgi?id=1207721#c15> }
%exclude %{_datadir}/doc/*/*.{pdf,xml,ps,db}
%exclude %{_includedir}
%exclude %{_datarootdir}/pkgconfig
%else

%files devel
%license COPYING-*
%exclude %{_datadir}/doc
%dir %{_includedir}/GL
%{_includedir}/GL/*.h
%{_includedir}/GL/internal
%{_includedir}/X11/{dri,extensions,fonts}
%{_includedir}/X11/*.h
%{_datarootdir}/pkgconfig/*.pc
# we seriously don't want to package that again ...
%exclude %{_mandir}/man7/Xprint.7
%endif

%changelog
