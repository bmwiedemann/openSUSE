#
# spec file for package libxcb
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


%define lname   libxcb1
%if 0%{?suse_version} >= 1500
%bcond_with python2
%else
%bcond_without python2
%endif
Name:           libxcb
Version:        1.15
Release:        0
Summary:        X11 core protocol C library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xcb.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xcb/libxcb
#Git-Web:	https://cgit.freedesktop.org/xcb/libxcb/
#DL-URL:	https://xcb.freedesktop.org/dist/
Source:         https://xcb.freedesktop.org/dist/libxcb-%{version}.tar.xz
Source1:        https://xcb.freedesktop.org/dist/libxcb-%{version}.tar.xz.sig
Source2:        baselibs.conf
Source3:        libxcb.keyring
Patch1:         bug-262309_xcb-xauthlocalhostname.diff
Patch2:         n_If-auth-with-credentials-for-hostname-fails-retry-with-XAUTHLOCALHOSTNAME.patch
BuildRequires:  autoconf >= 2.57
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(xau) >= 0.99.2
BuildRequires:  pkgconfig(xcb-proto) >= 1.15
BuildRequires:  pkgconfig(xorg-macros) >= 1.18
%if %{with python2}
BuildRequires:  python-base >= 2.6
BuildRequires:  python-xcb-proto-devel >= 7.6_1.12
BuildRequires:  python-xml
%else
BuildRequires:  python3-base
BuildRequires:  python3-xcb-proto-devel >= 7.6_1.12
BuildRequires:  python3-xml
%endif

%description
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb1
Summary:        X11 core protocol C library
Group:          System/Libraries
Provides:       xorg-x11-libxcb = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libxcb < 7.6_%{version}-%{release}

%description -n libxcb1
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-composite0
Summary:        X11 Composite Extension C library
Group:          System/Libraries

%description -n libxcb-composite0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The Composite extension causes a entire sub-tree of the window
hierarchy to be rendered to an off-screen buffer. Applications can
then take the contents of that buffer and do whatever they like. The
off-screen buffer can be automatically merged into the parent window
or merged by external programs, called compositing managers.

%package -n libxcb-damage0
Summary:        X11 Damage Extension C library
Group:          System/Libraries

%description -n libxcb-damage0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Damage Extension allows applications to track modified regions
of drawables.

%package -n libxcb-dpms0
Summary:        X11 DPMS Extension C library
Group:          System/Libraries

%description -n libxcb-dpms0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-dri2-0
Summary:        X11 DRI2 Extension C library
Group:          System/Libraries

%description -n libxcb-dri2-0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-dri3-0
Summary:        X11 DRI3 Extension C library
Group:          System/Libraries

%description -n libxcb-dri3-0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-glx0
Summary:        X11 GLX Extension C library
Group:          System/Libraries

%description -n libxcb-glx0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-randr0
Summary:        X11 RandR Extension C library
Group:          System/Libraries

%description -n libxcb-randr0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Resize, Rotate and Reflect Extension (RandR) allows clients to
dynamically change X screens, so as to resize, to change the
orientation and layout of the root window of a screen.

%package -n libxcb-record0
Summary:        X11 RECORD Extension C library
Group:          System/Libraries

%description -n libxcb-record0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The RECORD extension supports the recording and reporting of all core
X protocol and arbitrary X extension protocol.

%package -n libxcb-render0
Summary:        X11 Render Extension C library
Group:          System/Libraries

%description -n libxcb-render0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-res0
Summary:        X11 Resource Extension C library
Group:          System/Libraries

%description -n libxcb-res0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-screensaver0
Summary:        X11 ScreenSaver Extension C library
Group:          System/Libraries

%description -n libxcb-screensaver0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

%package -n libxcb-shape0
Summary:        X11 Shape Extension C library
Group:          System/Libraries

%description -n libxcb-shape0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

- X11 Nonrectangular Window Shape extension (Xshape)

%package -n libxcb-shm0
Summary:        X11 Shared Memory Extension C library
Group:          System/Libraries

%description -n libxcb-shm0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The MIT Shared Memory (MIT-SHM) Extension allows exchanging image
data between client and server using shared memory, so that it does
not need to be transferred over sockets.

%package -n libxcb-sync1
Summary:        X11 Sync Extension C library
Group:          System/Libraries

%description -n libxcb-sync1
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-present0
Summary:        X11 Present Extension C library
Group:          System/Libraries

%description -n libxcb-present0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-xf86dri0
Summary:        X11 XFree86-DRI Extension C library
Group:          System/Libraries

%description -n libxcb-xf86dri0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-xfixes0
Summary:        X11 Xfixes Extension C library
Group:          System/Libraries

%description -n libxcb-xfixes0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Fixes extension provides applications with work-arounds for
various limitations in the core protocol.

%package -n libxcb-xkb1
Summary:        X11 Keyboard Extension C library
Group:          System/Libraries

%description -n libxcb-xkb1
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

Xkb extends the ability to control the keyboard
over what is offered by the X Window System core protocol.

%package -n libxcb-xinerama0
Summary:        X11 Xinerama Extension C library
Group:          System/Libraries

%description -n libxcb-xinerama0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

Xinerama is an extension to the X Window System which enables
multi-headed X applications and window managers to use two or more
physical displays as one large virtual display.

%package -n libxcb-xinput0
Summary:        X11 XInput Extension C library
Group:          System/Libraries

%description -n libxcb-xinput0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

Xinput is an extension to the X Window System intended to replace
core input processing.

%package -n libxcb-xtest0
Summary:        X11 XTEST Extension C library
Group:          System/Libraries

%description -n libxcb-xtest0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

%package -n libxcb-xv0
Summary:        X11 video Extension C library
Group:          System/Libraries

%description -n libxcb-xv0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Video Extension (Xv) extension provides support for video
adaptors attached to an X display. It takes the approach that a
display may have one or more video adaptors, each of which has one or
more ports through which independent video streams pass.

%package -n libxcb-xvmc0
Summary:        X11 Video Motion Compensation Extension C library
Group:          System/Libraries

%description -n libxcb-xvmc0
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

X-Video Motion Compensation (XvMC), is an extension of the X video
extension (Xv) for the X Window System. The XvMC API allows video
programs to offload portions of the video decoding process to the GPU
video-hardware.

%package devel
Summary:        Development files for the X11 protocol C library
Group:          Development/Libraries/C and C++
Requires:       libxcb-composite0 = %{version}
Requires:       libxcb-damage0 = %{version}
Requires:       libxcb-dpms0 = %{version}
Requires:       libxcb-dri2-0 = %{version}
Requires:       libxcb-dri3-0 = %{version}
Requires:       libxcb-glx0 = %{version}
Requires:       libxcb-present0 = %{version}
Requires:       libxcb-randr0 = %{version}
Requires:       libxcb-record0 = %{version}
Requires:       libxcb-render0 = %{version}
Requires:       libxcb-res0 = %{version}
Requires:       libxcb-screensaver0 = %{version}
Requires:       libxcb-shape0 = %{version}
Requires:       libxcb-shm0 = %{version}
Requires:       libxcb-sync1 = %{version}
Requires:       libxcb-xf86dri0 = %{version}
Requires:       libxcb-xfixes0 = %{version}
Requires:       libxcb-xinerama0 = %{version}
Requires:       libxcb-xinput0 = %{version}
Requires:       libxcb-xkb1 = %{version}
Requires:       libxcb-xtest0 = %{version}
Requires:       libxcb-xv0 = %{version}
Requires:       libxcb-xvmc0 = %{version}
# O/P added for 12.2
Provides:       xorg-x11-libxcb-devel = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libxcb-devel < 7.6_%{version}-%{release}

%description devel
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

This package contains the development headers for the library found
in %{lname}.

%package devel-doc
Summary:        Documentation for libxcb
Group:          Documentation/Man
BuildArch:      noarch

%description devel-doc
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

This subpackage contains the manual pages and documentation for
libxcb.

%prep
%setup -q
%patch1
%patch2 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --docdir=%{_docdir}/%{name} \
           --disable-static \
           --enable-xinput \
           --enable-xkb \
           --enable-sendfds
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libxcb1 -p /sbin/ldconfig
%postun -n libxcb1 -p /sbin/ldconfig
%post   -n libxcb-composite0 -p /sbin/ldconfig
%postun -n libxcb-composite0 -p /sbin/ldconfig
%post   -n libxcb-damage0 -p /sbin/ldconfig
%postun -n libxcb-damage0 -p /sbin/ldconfig
%post   -n libxcb-dpms0 -p /sbin/ldconfig
%postun -n libxcb-dpms0 -p /sbin/ldconfig
%post   -n libxcb-dri2-0 -p /sbin/ldconfig
%postun -n libxcb-dri2-0 -p /sbin/ldconfig
%post   -n libxcb-dri3-0 -p /sbin/ldconfig
%postun -n libxcb-dri3-0 -p /sbin/ldconfig
%post   -n libxcb-glx0 -p /sbin/ldconfig
%postun -n libxcb-glx0 -p /sbin/ldconfig
%post   -n libxcb-randr0 -p /sbin/ldconfig
%postun -n libxcb-randr0 -p /sbin/ldconfig
%post   -n libxcb-record0 -p /sbin/ldconfig
%postun -n libxcb-record0 -p /sbin/ldconfig
%post   -n libxcb-render0 -p /sbin/ldconfig
%postun -n libxcb-render0 -p /sbin/ldconfig
%post   -n libxcb-res0 -p /sbin/ldconfig
%postun -n libxcb-res0 -p /sbin/ldconfig
%post   -n libxcb-screensaver0 -p /sbin/ldconfig
%postun -n libxcb-screensaver0 -p /sbin/ldconfig
%post   -n libxcb-shape0 -p /sbin/ldconfig
%postun -n libxcb-shape0 -p /sbin/ldconfig
%post   -n libxcb-shm0 -p /sbin/ldconfig
%postun -n libxcb-shm0 -p /sbin/ldconfig
%post   -n libxcb-sync1 -p /sbin/ldconfig
%postun -n libxcb-sync1 -p /sbin/ldconfig
%post   -n libxcb-present0 -p /sbin/ldconfig
%postun -n libxcb-present0 -p /sbin/ldconfig
%post   -n libxcb-xf86dri0 -p /sbin/ldconfig
%postun -n libxcb-xf86dri0 -p /sbin/ldconfig
%post   -n libxcb-xfixes0 -p /sbin/ldconfig
%postun -n libxcb-xfixes0 -p /sbin/ldconfig
%post   -n libxcb-xkb1 -p /sbin/ldconfig
%postun -n libxcb-xkb1 -p /sbin/ldconfig
%post   -n libxcb-xinerama0 -p /sbin/ldconfig
%postun -n libxcb-xinerama0 -p /sbin/ldconfig
%post   -n libxcb-xinput0 -p /sbin/ldconfig
%postun -n libxcb-xinput0 -p /sbin/ldconfig
%post   -n libxcb-xtest0 -p /sbin/ldconfig
%postun -n libxcb-xtest0 -p /sbin/ldconfig
%post   -n libxcb-xv0 -p /sbin/ldconfig
%postun -n libxcb-xv0 -p /sbin/ldconfig
%post   -n libxcb-xvmc0 -p /sbin/ldconfig
%postun -n libxcb-xvmc0 -p /sbin/ldconfig

%files -n libxcb1
%{_libdir}/libxcb.so.1*

%files -n libxcb-composite0
%{_libdir}/libxcb-composite.so.0*

%files -n libxcb-damage0
%{_libdir}/libxcb-damage.so.0*

%files -n libxcb-dpms0
%{_libdir}/libxcb-dpms.so.0*

%files -n libxcb-dri2-0
%{_libdir}/libxcb-dri2.so.0*

%files -n libxcb-dri3-0
%{_libdir}/libxcb-dri3.so.0*

%files -n libxcb-glx0
%{_libdir}/libxcb-glx.so.0*

%files -n libxcb-randr0
%{_libdir}/libxcb-randr.so.0*

%files -n libxcb-record0
%{_libdir}/libxcb-record.so.0*

%files -n libxcb-render0
%{_libdir}/libxcb-render.so.0*

%files -n libxcb-res0
%{_libdir}/libxcb-res.so.0*

%files -n libxcb-screensaver0
%{_libdir}/libxcb-screensaver.so.0*

%files -n libxcb-shape0
%{_libdir}/libxcb-shape.so.0*

%files -n libxcb-shm0
%{_libdir}/libxcb-shm.so.0*

%files -n libxcb-sync1
%{_libdir}/libxcb-sync.so.1*

%files -n libxcb-present0
%{_libdir}/libxcb-present.so.0*

%files -n libxcb-xf86dri0
%{_libdir}/libxcb-xf86dri.so.*

%files -n libxcb-xfixes0
%{_libdir}/libxcb-xfixes.so.*

%files -n libxcb-xkb1
%{_libdir}/libxcb-xkb.so.1*

%files -n libxcb-xinerama0
%{_libdir}/libxcb-xinerama.so.0*

%files -n libxcb-xinput0
%{_libdir}/libxcb-xinput.so.0*

%files -n libxcb-xtest0
%{_libdir}/libxcb-xtest.so.0*

%files -n libxcb-xv0
%{_libdir}/libxcb-xv.so.0*

%files -n libxcb-xvmc0
%{_libdir}/libxcb-xvmc.so.0*

%files devel
%{_includedir}/xcb
%{_libdir}/libxcb*.so
%{_libdir}/pkgconfig/xcb*.pc

%files devel-doc
%{_docdir}/%{name}
%{_mandir}/man3/xcb*

%changelog
