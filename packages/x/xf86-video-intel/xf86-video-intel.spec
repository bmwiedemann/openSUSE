#
# spec file for package xf86-video-intel
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_with glamor
%bcond_with backlighthelper
%bcond_with valgrind
Name:           xf86-video-intel
Version:        2.99.917+git8674.25c9a2fcc
Release:        0
Summary:        Intel video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://x.org/wiki/IntelGraphicsDriver/
#Git-Clone:	git://anongit.freedesktop.org/xorg/driver/xf86-video-intel
#Git-Web:	http://cgit.freedesktop.org/xorg/driver/xf86-video-intel/
# http://xorg.freedesktop.org/releases/individual/driver/
#Git-Archive:   git archive --format=tar.gz --prefix %{name}-%{version}/ master
Source0:        %{name}-%{version}.tar.xz
Source99:       baselibs.conf
Patch0:         n_fix-build-on-i686.patch
Patch1:         U_i810-multidef-fix.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dri2proto) >= 2.6
BuildRequires:  pkgconfig(dri3proto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.24
BuildRequires:  pkgconfig(libdrm_intel) >= 2.4.29
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
%if %{with valgrind}
BuildRequires:  pkgconfig(valgrind)
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xfixes)
### TODO: Remove xfont after XServer 1.19 is available
BuildRequires:  pkgconfig(xfont)
%if 0%{?suse_version} > 1315 || 0%{?is_opensuse}
BuildRequires:  pkgconfig(xfont2)
%endif
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xvmc)
Recommends:     vaapi-intel-driver
%if 0%{?suse_version} <= 1315 && !0%{?is_opensuse}
Supplements:    modalias(xorg-x11-server:pci:v00008086d*sv*sd*bc03sc*i*)
%else
# Intel Gen <= 3 (i810/i1815, i830, 845, 855, 865, 915, 945, G33)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00007121sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00007123sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00007125sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001132sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003577sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00002562sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000358Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003582sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00002572sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00002582sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00002592sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000258Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00002772sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d000027A2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d000027AEsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000A011sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000A001sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d000029B2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d000029C2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d000029D2sv*sd*bc*sc*i*)
%endif
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
Provides:       intel-i810-xorg-x11 = %{version}
Obsoletes:      intel-i810-xorg-x11 < %{version}
Provides:       xorg-x11-driver-video-intel = %{version}
Obsoletes:      xorg-x11-driver-video-intel < %{version}
# No Provides, as we technically don't provide the binaries
Obsoletes:      855resolution
Obsoletes:      915resolution
ExclusiveArch:  %ix86 x86_64
%{x11_abi_videodrv_req}
%if %{with glamor}
Requires:       glamor
BuildRequires:  pkgconfig(glamor)
%endif

%description
intel is an Xorg driver for Intel integrated video cards.

The driver supports depths 8, 15, 16 and 24. All visual types are
supported in depth 8. For the i810/i815 other depths support the
TrueColor and DirectColor visuals. For the i830M and later, only the
TrueColor visual is supported for depths greater than 8. The driver
supports hardware accelerated 3D via the Direct Rendering Infrastructure
(DRI), but only in depth 16 for the i810/i815 and depths 16 and 24 for
the 830M and later.

%prep
%setup -q
%ifarch %{ix86}
# Applied only on 32bit architectures because only those need it to build with
# GCC8. It may slightly hurt performance, so lets not apply it where not needed.
%patch0 -p1
%patch1 -p1
%endif

%build
%define _lto_cflags %{nil}
autoreconf -fvi
%configure \
        --disable-silent-rules \
%if %{with backlighthelper}
	--enable-backlight-helper \
%else
	--disable-backlight-helper \
%endif
%ifnarch %ix86
	--enable-kms-only \
%endif
%if %{with glamor}
	--enable-glamor \
%endif
	--enable-dri3 \
	--enable-uxa \
%if %{with valgrind}
	--enable-valgrind \
%endif
	--with-default-dri=2

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%if %{with backlighthelper}
%defattr(-,polkitd,polkitd)
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%endif

%defattr(-,root,root)
%license COPYING
%doc AUTHORS NEWS README
%ifarch %ix86
%{_libdir}/libI810XvMC.so*
%endif
%{_libdir}/libIntelXvMC.so*
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/intel_drv.so
%{_bindir}/intel-virtual-output
%{_mandir}/man4/intel.4%{?ext_man}
%{_mandir}/man4/intel-virtual-output.4%{?ext_man}
%if %{with backlighthelper}
%{_libexecdir}/xf86-video-intel-backlight-helper
%{_datadir}/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy
%endif

%changelog
