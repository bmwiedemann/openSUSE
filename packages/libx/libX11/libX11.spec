#
# spec file for package libX11
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


Name:           libX11
Version:        1.8.2
Release:        0
Summary:        Core X11 protocol client library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libX11
#Git-Web:       http://cgit.freedesktop.org/xorg/lib/libX11/
Source:         http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FEATURE-UPSTREAM p_xlib_skip_ext_env.diff fdo#48588 bnc#167317 -- Add support for disabling extensions through environment variables
Patch1:         p_xlib_skip_ext_env.diff
# PATCH-FIX-UPSTREAM en-locales.diff fdo#48596 bnc#388711 -- Add missing data for more en locales
Patch2:         en-locales.diff
Patch3:         u_no-longer-crash-in-XVisualIDFromVisual.patch
Patch4:         U_Fix-797755-Allow-X-IfEvent-to-reenter-libX11.patch
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(xcb) >= 1.1.92
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.11
BuildRequires:  pkgconfig(xproto) >= 7.0.13
BuildRequires:  pkgconfig(xtrans)

%description
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package -n libX11-6
Summary:        Core X11 protocol client library
Group:          System/Libraries
Requires:       %{name}-data >= %{version}
# O/P added for 12.2. Ideally remove before 12.2 release.
Provides:       xorg-x11-libX11 = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libX11 < 7.6_%{version}-%{release}

%description -n libX11-6
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package -n libX11-xcb1
Summary:        XCB X11 protocol client library
Group:          System/Libraries
Requires:       %{name}-data >= %{version}

%description -n libX11-xcb1
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package data
Summary:        Shared data for the Core X11 protocol library
Group:          System/Libraries
BuildArch:      noarch

%description data
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package devel
Summary:        Development files for the Core X11 protocol library
Group:          Development/Libraries/C and C++
Requires:       libX11-6 = %{version}
Requires:       libX11-xcb1 = %{version}
# O/P added for 12.2
Provides:       xorg-x11-libX11-devel = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libX11-devel < 7.6_%{version}-%{release}
Conflicts:      xorgproto-devel < 2019.2
Provides:       xorgproto-devel:%{_includedir}/X11/extensions/XKBgeom.h

%description devel
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

This package contains the development headers for the library found
in libX11-6 and libX11-xcb1.

%prep
%setup -q
# make legal department happy (Bug #153744)
test -f nls/ja.U90/XLC_LOCALE.pre && exit 1
test -f nls/ja.S90/XLC_LOCALE.pre && exit 1

%patch1
%patch2
%patch3 -p1
%patch4 -p1

%build
%configure \
    --disable-silent-rules \
    --docdir=%{_docdir}/%{name} \
    --disable-thread-safety-constructor \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# Some files are empty/missing for some UTF-8 locales
pushd "%{buildroot}%{_datadir}/X11/locale"
for i in *.UTF-8; do
	echo "$i"
	if [ "$i" == "en_US.UTF-8" ]; then
		continue
	fi
	touch "$i/Compose" "$i/XI18N_OBJS"
	test -s "$i/Compose"    || ln -fns ../en_US.UTF-8/Compose    "$i"
	test -s "$i/XI18N_OBJS" || ln -fns ../en_US.UTF-8/XI18N_OBJS "$i"
	test -s "$i/XLC_LOCALE" || ln -fns ../en_US.UTF-8/XLC_LOCALE "$i"
done
popd

%fdupes %{buildroot}/%{_mandir}

%post   -n libX11-6 -p /sbin/ldconfig
%postun -n libX11-6 -p /sbin/ldconfig
%post   -n libX11-xcb1 -p /sbin/ldconfig
%postun -n libX11-xcb1 -p /sbin/ldconfig

%files -n libX11-6
%{_libdir}/libX11.so.6*

%files -n libX11-xcb1
%{_libdir}/libX11-xcb.so.1*

%files data
%{_datadir}/X11

%files devel
%{_includedir}/X11/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_docdir}/%{name}
%{_mandir}/man?/*

%changelog
