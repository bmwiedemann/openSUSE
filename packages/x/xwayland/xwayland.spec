#
# spec file for package xwayland
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


%define have_wayland_eglstream 1

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           xwayland
Version:        22.1.5
Release:        0
URL:            http://xorg.freedesktop.org/
Summary:        X
License:        MIT
Group:          System/X11/Servers/XF86_4
Source0:        %{url}/archive/individual/xserver/%{name}-%{version}.tar.xz
Source1:        %{url}/archive/individual/xserver/%{name}-%{version}.tar.xz.sig
Source2:        xwayland.keyring
Patch1205874:   U_0001-Xtest-disallow-GenericEvents-in-XTestSwapFakeInput.patch
Patch1205875:   U_0002-Xi-return-an-error-from-XI-property-changes-if-verif.patch
Patch1205876:   U_0003-Xi-avoid-integer-truncation-in-length-check-of-ProcX.patch
Patch1205877:   U_0004-Xi-disallow-passive-grabs-with-a-detail-255.patch
Patch1205878:   U_0005-Xext-free-the-screen-saver-resource-when-replacing-i.patch
Patch1205879:   U_0006-Xext-free-the-XvRTVideoNotify-when-turning-off-from-.patch
Patch1206017:   U_0007-xkb-reset-the-radio_groups-pointer-to-NULL-after-fre.patch
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  rendercheck
BuildRequires:  pkgconfig(bigreqsproto)
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(dri3proto)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(inputproto) >= 2.3.99.1
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
%if 0%{?have_wayland_eglstream} == 1
BuildRequires:  pkgconfig(wayland-eglstream-protocols)
%endif
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcmiscproto)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbcomp)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtrans)

%ifnarch s390 s390x
Requires(pre):  %fillup_prereq
%endif
Requires:       pkgconfig
Requires:       xkbcomp
#Recommends:     xorg-x11-fonts-core
%ifnarch s390 s390x
Requires:       libpixman-1-0
%endif
Obsoletes:      xorg-x11-server-wayland < %{version}
Provides:       xorg-x11-server-wayland = %{version}

%description
This package contains the Xwayland Server.

%package %{name}
Summary:        Xwayland Xserver
Group:          System/X11/Servers/XF86_4
Requires:       xkbcomp
Requires:       xkeyboard-config
Recommends:     xorg-x11-fonts-core

%description %{name}
This package contains the Xserver running on the Wayland Display Server.

%package devel
Summary:        Development files for Xwayland
Group:          System/Libraries
Requires:       %{name}
Requires:       c_compiler
Requires:       meson
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(xau)
Requires:       pkgconfig(xdmcp)
Requires:       pkgconfig(xkbfile)
Requires:       pkgconfig(xtrans)
Requires:       pkgconfig(xv)

%description devel
This package contains the Xwayland Server development files.

%prep
%autosetup -p1

%build
%{meson} \
   -Dglamor=true \
%if 0%{?have_wayland_eglstream} == 1
   -Dxwayland_eglstream=true \
%endif
   -Dxvfb=true \
   -Dglx=true \
   -Dxdmcp=true \
   -Dxdm-auth-1=true \
   -Dsecure-rpc=true \
   -Dipv6=true \
   -Dinput_thread=true \
   -Dvendor_name="SUSE LINUX" \
   -Dvendor_name_short="openSUSE" \
   -Dvendor_web="https://www.opensuse.org" \
   -Dlisten_tcp=false \
   -Dlisten_unix=true \
   -Dlisten_local=true \
   -Ddpms=true \
   -Dxf86bigfont=true \
   -Dscreensaver=true \
   -Dxres=true \
   -Dxace=true \
   -Dxselinux=false \
   -Dxinerama=true \
   -Dxcsecurity=true \
   -Dxv=true \
   -Dmitshm=true \
   -Dsha1=libcrypto \
   -Ddri3=true \
   -Dxwayland-path="%{_bindir}" \
   -Ddtrace=false \
   -Dlibunwind=false \
   -Dxkb_dir="/usr/share/X11/xkb" \
   -Dxkb_output_dir="/var/lib/xkb/compiled" \
   -Ddefault_font_path="/usr/share/fonts/misc:unscaled,\
/usr/share/fonts/Type1/,/usr/share/fonts/100dpi:unscaled,\
/usr/share/fonts/75dpi:unscaled,/usr/share/fonts/ghostscript/,\
/usr/share/fonts/cyrillic:unscaled,\
/usr/share/fonts/misc/sgi:unscaled,\
/usr/share/fonts/truetype/,built-ins" \
   %{nil}

%{meson_build}

%install
%{meson_install}
# Let xorg-x11-server provide the Xserver manual
rm -f %{buildroot}%{_mandir}/man1/Xserver.1
# Provided by xorg-x11-server
rm -f %{buildroot}%{_libdir}/xorg/protocol.txt

%files
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1%{ext_man}

%files devel
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/xorg

%changelog
